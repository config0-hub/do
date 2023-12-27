**Description**

  - This stack provisions a managed Kubernetes cluster on DigitalOcean.

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| do_region   | digital ocean region                 | string   | lon1         |
| doks_cluster_name            | digital ocean kubernetes name  | string |     | 
| doks_cluster_version         | digital ocean kubernetes version | string | 1.26.3-do.0
| doks_cluster_pool_size       | digital ocean kubernetes pool worker | string | s-1vcpu-2gb-amd
| doks_cluster_pool_node_count | digital ocean kubernetes node count  | number | 1
| doks_cluster_autoscale_max   | digital ocean kubernetes autoscale node max | number | 4
| doks_cluster_autoscale_min   | digital ocean kubernetes autoscale node min | number | 2


**Sample entry**

```
infrastructure:
   doks:
       stack_name: config0-hub:::doks
       arguments:
          doks_cluster_name: eval-config0-doks
       credentials:
           - reference: do
             orchestration: true
```
