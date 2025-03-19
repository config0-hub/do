# DigitalOcean SSH Key Upload

## Description
This stack uploads an SSH public key to DigitalOcean, allowing it to be used for resource access with DigitalOcean services.

## Variables

### Required
None - Either `key_name` or `ssh_key_name` must be provided.

### Optional
| Name | Description | Default |
|------|-------------|---------|
| key_name | SSH key identifier for resource access | |
| name | Configuration for name | |
| do_region | DigitalOcean deployment region | |
| ssh_key_name | Name label for SSH key | |
| timeout | Configuration for timeout | 600 |

## Features
- Name of ssh key must be provided by either key_name or ssh_key_name
- Retrieves SSH public keys from different resource types (ssh_key_pair, ssh_public_key, inputvars) from Config0 resource database
- Automatically uploads the SSH key to DigitalOcean
- Associates the SSH key with your DigitalOcean account
- Base64 encodes public keys when required

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