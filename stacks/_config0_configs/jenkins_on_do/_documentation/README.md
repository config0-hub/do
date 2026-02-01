# DigitalOcean Jenkins Deployment

## Description
This stack automates the deployment of a Jenkins instance on DigitalOcean. It creates an SSH key, provisions a DigitalOcean droplet, and installs Jenkins on the VM using Docker.

## Variables

### Required Variables

| Name | Description | Default |
|------|-------------|---------|
| name | The name of the Jenkins instance | &nbsp; |
| do_region | DigitalOcean deployment region | NYC1 |
| size | Size of the DigitalOcean droplet | s-1vcpu-2gb |

### Optional Variables

| Name | Description | Default |
|------|-------------|---------|
| with_monitoring | Enable monitoring for the droplet | &nbsp; |
| with_backups | Enable backups for the droplet | &nbsp; |
| with_ipv6 | Enable IPv6 for the droplet | &nbsp; |
| with_private_networking | Enable private networking for the droplet | &nbsp; |
| with_resize_disk | Enable disk resizing for the droplet | &nbsp; |
| cloud_tags_hash | Resource tags for cloud provider | &nbsp; |

## Dependencies

### Substacks
- [config0-publish:::new_do_ssh_key](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/new_do_ssh_key)
- [config0-publish:::droplet](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/droplet)
- [config0-publish:::jenkins_on_docker](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/jenkins_on_docker)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>