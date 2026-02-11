# DigitalOcean Droplet

## Description
This stack creates a DigitalOcean Droplet virtual machine with configurable options for networking, monitoring, and backups.

## Variables

### Required Variables

| Name | Description | Default |
|------|-------------|---------|
| ssh_key_id | SSH key ID for resource access | &nbsp; |
| hostname | Server hostname | _random |

### Optional Variables

| Name | Description | Default |
|------|-------------|---------|
| do_region | DigitalOcean deployment region | NYC1 |
| size | Droplet size/plan specification | s-1vcpu-1gb |
| with_backups | Enable automatic backups | &nbsp; |
| with_monitoring | Enable DigitalOcean monitoring | &nbsp; |
| with_ipv6 | Enable IPv6 networking | &nbsp; |
| with_private_networking | Enable private networking between Droplets | &nbsp; |
| with_resize_disk | Allow disk resizing | &nbsp; |
| timeout | Execution timeout in seconds | 600 |

## Dependencies

### Substacks
- [config0-publish:::tf_executor](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-publish/tf_executor/default)

### Execgroups
- [config0-publish:::do::droplet](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/exec/groups/config0-publish/do/droplet/default)

### Shelloutconfigs
- [config0-publish:::terraform::resource_wrapper](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/shelloutconfigs/config0-publish/terraform/resource_wrapper/default)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>