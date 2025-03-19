# DigitalOcean Droplet

## Description
This stack creates a DigitalOcean Droplet virtual machine with configurable options for networking, monitoring, and backups.

## Variables

### Required Variables

| Name | Description | Default |
|------|-------------|---------|
| ssh_key_id | SSH key ID for resource access | |
| hostname | Server hostname | _random |

### Optional Variables

| Name | Description | Default |
|------|-------------|---------|
| do_region | DigitalOcean deployment region | NYC1 |
| size | Configuration for size | s-1vcpu-1gb |
| with_backups | Configuration for with backups | |
| with_monitoring | Configuration for with monitoring | |
| with_ipv6 | Configuration for with ipv6 | |
| with_private_networking | Configuration for with private networking | |
| with_resize_disk | Configuration for with resize disk | |
| timeout | Configuration for timeout | 600 |

## Features
- Create a DigitalOcean Droplet with configurable specifications
- Support for private networking
- Optional IPv6 support
- Optional monitoring
- Optional automated backups
- Configurable disk resize settings

## Dependencies

### Substacks
- [config0-publish:::tf_executor](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/tf_executor)

### Execgroups
- [config0-publish:::do::droplet](https://api-app.config0.com/web_api/v1.0/exec/groups/config0-publish/do/droplet)

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.