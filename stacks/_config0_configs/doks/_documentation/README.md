# DigitalOcean Kubernetes Service (DOKS) Stack

## Description
This stack creates and manages DigitalOcean Kubernetes Service (DOKS) clusters using Terraform/OpenTofu. It automates the provisioning and configuration of Kubernetes clusters in DigitalOcean cloud.

## Variables

### Required Variables

| Name              | Description                           | Default |
|-------------------|---------------------------------------|---------|
| doks_cluster_name | Kubernetes cluster name               | &nbsp;  |
| do_region         | DigitalOcean deployment region        | lon1    |

### Optional Variables

| Name                         | Description                              | Default         |
|------------------------------|------------------------------------------|-----------------|
| doks_cluster_version         | Kubernetes version for DOKS              | 1.32            |
| doks_cluster_pool_size       | Node pool size/instance type             | s-1vcpu-2gb-amd |
| doks_cluster_pool_node_count | Initial node count in cluster            | 1               |
| doks_cluster_autoscale_min   | Minimum node count for autoscaling       | 1               |
| doks_cluster_autoscale_max   | Maximum node count for autoscaling       | 3               |
| tf_runtime                   | Terraform runtime version                | tofu:1.9.1      |
| timeout                      | Configuration for timeout                | 2700            |

## Dependencies

### Substacks
- [config0-publish:::tf_executor](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-publish/tf_executor/default)

### Execgroups
- [config0-publish:::do::doks](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/exec/groups/config0-publish/do/doks/default)

### Shelloutconfigs
- [config0-publish:::terraform::resource_wrapper](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/shelloutconfigs/config0-publish/terraform/resource_wrapper/default)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>