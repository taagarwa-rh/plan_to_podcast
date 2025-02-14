# Openshift Templates

In order to deploy resources into our OpenShift cluster(s), we will utilize a tool called [Kustomize](https://kustomize.io/) which is built right into `oc`/`kubectl`.

`Kustomize` is template and DSL free; allowing you to specify your resource YAML files as plain as possible with the addition of providing overrides for different configuration environments. The `Kustomize` terminology uses **overlays**, but we will use **environments**.

## Getting Started

### Prerequisites

The following tools are necessary: 

- `oc`

(Additionally, you might need to login via `oc login`)

### Next Steps

The folder structure is as follows:

```
oc-templates
├── base
│   ├── kustomization.yml
│   └── deployment.yml
├── preprod
│   ├── kustomization.yml
│   └── patch.yml
└── prod
    ├── kustomization.yml
    └── patch.yml
```

Common resources deployed into all environments are located in the [base](./base) folder. Environment specific resources should be located and placed into their respective folder (e.g [preprod](./preprod/) or [prod](./prod/)).

### Adding Resources

In order to add new resources (e.g `ConfigMap`), follow the following steps:

1. Determine if it is environment specific or not
    1. If **NOT**, add the resource (e.g _configmap.yml_) to the [base](./base/folder) folder and add the path to the [kustomization](./base/kustomization.yml) `resources` list
    1. If it is, repeat the instructions above, but for the environments folder.
1. Run `oc kustomize oc-templates/<environment>` to see the outputs.
    1. You can also run `oc kustomize base` to see which base objects will be created.
    1. _**Tip:** You can do the following to get nice color output: `oc kustomize oc-templates/preprod | bat -P -p -l yaml`_
1. Verify the `kustomization.yml` "extras" (e.g: `labels`, `namespace`) are doing what you want them to do.

### Validating and Deploying

After adding your files and environment specific configurations, you can run the following:

1. `oc diff -k oc-templates/<environment>` to view the difference between the state of the current cluster and those defined in these files.
1. **THIS SHOULD BE DONE VIA CI**
    1. Deploying is `oc apply -k oc-templates/<preprod>`.

## Notes

1. Deployment to the OpenShift cluster should be done via **CI/CD** and in certain special circumstances, can be done manually via a person with permissions (e.g. the Data Engineers.)

