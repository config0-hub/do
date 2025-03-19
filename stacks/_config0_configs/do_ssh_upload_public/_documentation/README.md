# DigitalOcean SSH Key Upload

## Description
This stack uploads an SSH public key to a DigitalOcean account and makes it available for use with DigitalOcean resources.

## Variables

### Required

| Name | Description | Default |
|------|-------------|---------|
| key_name | SSH key identifier for resource access |  |

### Optional

| Name | Description | Default |
|------|-------------|---------|
| public_key | SSH public key content |  |
| timeout | Configuration for timeout | 600 |

## Features
- Uploads SSH public key to DigitalOcean
- Returns the SSH key ID for use with other resources
- Manages SSH key with Terraform/OpenTofu

## Dependencies

### Substacks
- [config0-publish:::tf_executor](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/tf_executor)

### Execgroups
- [config0-publish:::do::ssh_key_upload](https://api-app.config0.com/web_api/v1.0/exec/groups/config0-publish/do/ssh_key_upload)

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.