# Builder image to install dependencies from pyproject and lock file
FROM quay.io/fedora/python-311:311 as builder
USER root
ENV POETRY_HOME=/opt/poetry \
    POETRY_VERSION=1.8.2
RUN wget -P /tmp/ https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem && \
    curl -sSL https://install.python-poetry.org | python - && \
    ${POETRY_HOME}/bin/poetry config virtualenvs.in-project true && \
    ${POETRY_HOME}/bin/poetry config certificates.de-cop-nexus.cert /tmp/Current-IT-Root-CAs.pem
COPY . /opt/app-root/src/
RUN ${POETRY_HOME}/bin/poetry install --only main

# ----------------------------------------------------------
FROM quay.io/fedora/python-311:311
LABEL maintainer="gfa-de@redhat.com" \
    io.k8s.description="Plan to Podcast" \
    io.k8s.display-name="plan_to_podcast" \
    io.openshift.tags="gfa"

USER root

# Update OS
RUN dnf -y update && \
    dnf -y install java-17-openjdk && \
    dnf -y autoremove && \
    dnf -y clean all && \
    wget -P /etc/pki/ca-trust/source/anchors https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem && \
    wget -P /tmp/ https://oss.sonatype.org/service/local/repositories/releases/content/org/teiid/teiid/16.0.0/teiid-16.0.0-jdbc.jar && \
    keytool -import -noprompt -keystore /etc/pki/java/cacerts -file /etc/pki/ca-trust/source/anchors/Current-IT-Root-CAs.pem -alias RH-IT-Root-CA -storepass changeit && \
    update-ca-trust enable && \
    update-ca-trust extract

COPY . /opt/app-root/src/
# (1) Fix file permissions. (2) Removes the activation script 
RUN fix-permissions /opt/app-root/src -P && \
    echo "" > /opt/app-root/bin/activate
COPY --from=builder --chown=1001:0 /opt/app-root/src/.venv /opt/app-root/src/.venv
USER 1001
CMD ["echo", "Image is live"]