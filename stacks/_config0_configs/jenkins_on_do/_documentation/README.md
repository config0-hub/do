# DigitalOcean Jenkins Deployment

## Description
This stack automates the deployment of a Jenkins instance on DigitalOcean. It creates an SSH key, provisions a DigitalOcean droplet, and installs Jenkins on the VM using Docker.

## Variables

### Required Variables

| Name | Description | Default |
|------|-------------|---------|
| name | Configuration for name | |
| do_region | DigitalOcean deployment region | NYC1 |
| size | Configuration for size | s-1vcpu-2gb |

### Optional Variables

| Name | Description | Default |
|------|-------------|---------|
| with_monitoring | Configuration for with monitoring | |
| with_backups | Configuration for with backups | |
| with_ipv6 | Configuration for with ipv6 | |
| with_private_networking | Configuration for with private networking | |
| with_resize_disk | Configuration for with resize disk | |
| cloud_tags_hash | Resource tags for cloud provider | |
| ssh_key_id | SSH key ID for resource access | selector:::ssh_key_info::id |

## Features
- Automated SSH key creation for secure access
- DigitalOcean droplet provisioning with configurable size and region
- Jenkins installation on the provisioned VM using Docker
- Scheduled workflow with proper dependencies between tasks

## Dependencies

### Substacks
- [config0-publish:::new_do_ssh_key](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/new_do_ssh_key)
- [config0-publish:::droplet](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/droplet)
- [config0-publish:::jenkins_on_docker](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/jenkins_on_docker)

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.