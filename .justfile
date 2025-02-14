default_version := `poetry version -s`
project_name := "plan_to_podcast"

_default:
    @ just --list

# Run recipes for MR approval
pre-mr: format lint

# Formats Code
format:
    poetry run ruff check --select I --fix plan_to_podcast 
    poetry run ruff format plan_to_podcast 

# Tests Code
test *options:
    poetry run pytest -s tests/ {{ options }}

# Lints Code
lint *options:
    poetry run ruff check plan_to_podcast  {{ options }}

# Increments the code version
bump type:
    poetry run bump2version --current-version={{ default_version }} {{ type }}

test-container: (build-image "testing-latest")
    - podman run --rm --name plan-to-podcast -it plan-to-podcast:testing-latest /bin/bash




# Deploy application to openshift - WILL BE DEPRECATED IN A FUTURE RELEASE
oc-deploy env:
    oc apply -k oc-templates/{{ env }}

# DEPRECATED - WILL BE REMOVED - Run the openshift build
oc-build-tag version=("v" + default_version):
    oc start-build -n sandbox-ssa-gfa -w plan-to-podcast
    oc tag -n sandbox-ssa-gfa plan-to-podcast:latest plan-to-podcast:{{ version }}

[private]
build-image tag:
    podman build -t plan-to-podcast:{{ tag }} .