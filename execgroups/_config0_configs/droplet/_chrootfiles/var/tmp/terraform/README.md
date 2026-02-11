# DigitalOcean Droplet Terraform Module

This module creates a DigitalOcean Droplet with configurable settings for size, region, image, and various features.

## Usage

```hcl
module "do_droplet" {
  source     = "path/to/module"
  ssh_key_id = "your-ssh-key-id"
  
  # Optional configurations
  hostname   = "my-droplet"
  do_region  = "NYC3"
  size       = "s-2vcpu-2gb"
}
```

## Requirements

- OpenTofu >= 1.8.8
- DigitalOcean API token with write access

## Input Variables

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| ssh_key_id | The DigitalOcean SSH key ID to use for Droplet access | string | n/a | yes |
| image | The Droplet image slug or ID to use for creation | string | `"ubuntu-20-04-x64"` | no |
| hostname | The hostname of the Droplet that will be created | string | `"config0-demo"` | no |
| do_region | The DigitalOcean region where the Droplet will be provisioned | string | `"NYC1"` | no |
| size | The Droplet size/plan to use (determines CPU, RAM, and disk) | string | `"s-1vcpu-1gb"` | no |
| with_backups | Boolean controlling if automated backups are enabled | bool | `false` | no |
| with_monitoring | Boolean controlling whether DigitalOcean monitoring agent is installed | bool | `false` | no |
| with_ipv6 | Boolean controlling if IPv6 networking is enabled | bool | `false` | no |
| with_resize_disk | Whether to increase the disk size when resizing a Droplet | bool | `false` | no |

## Outputs

| Name | Description |
|------|-------------|
| ip | The public IPv4 address of the Droplet |
| id | The ID of the Droplet |
| image | The image of the Droplet |
| urn | The uniform resource name of the Droplet |
| private_ip | The private IPv4 address of the Droplet |
| public_ip | The public IPv4 address of the Droplet |

## Notes

- The `private_networking` parameter is deprecated in recent DigitalOcean provider versions but is maintained here for compatibility.
- This module creates a single Droplet with the specified configuration.

## License

Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.