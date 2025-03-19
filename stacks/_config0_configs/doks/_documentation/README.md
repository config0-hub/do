# DigitalOcean Kubernetes Service (DOKS) Stack

## Description
This stack creates and manages DigitalOcean Kubernetes Service (DOKS) clusters using Terraform/OpenTofu. It automates the provisioning and configuration of Kubernetes clusters in DigitalOcean cloud.

## Variables

### Required Variables

| Name              | Description                           | Default |
|-------------------|---------------------------------------|---------|
| doks_cluster_name | 99checkme99 Kubernetes cluster name   |         |

### Optional Variables

| Name                         | Description                                      | Default         |
|------------------------------|--------------------------------------------------|-----------------|
| do_region                    | DigitalOcean deployment region                   | lon1            |
| doks_cluster_version         | 99checkme99 Kubernetes version for DOKS          | 1.32            |
| doks_cluster_pool_size       | 99checkme99 Node pool size/instance type         | s-1vcpu-2gb-amd |
| doks_cluster_pool_node_count | 99checkme99 Initial node count in cluster        | 1               |
| doks_cluster_autoscale_min   | 99checkme99 Minimum node count for autoscaling   | 1               |
| doks_cluster_autoscale_max   | 99checkme99 Maximum node count for autoscaling   | 3               |
| tf_runtime                   | Terraform runtime version                         | tofu:1.8.8      |
| timeout                      | Configuration for timeout                         | 2700            |

## Features
- Automatic provisioning of DOKS clusters
- Configurable cluster version and region
- Autoscaling node pool configuration
- Integration with Config0 for automation
- Secure credential handling via SSM parameter store
- Automated execution via Lambda or CodeBuild based on timeout settings

## Dependencies

### Substacks
- [config0-publish:::tf_executor](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/tf_executor)

### Execgroups
- [config0-publish:::do::doks](https://api-app.config0.com/web_api/v1.0/exec/groups/config0-publish/do/doks)

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.