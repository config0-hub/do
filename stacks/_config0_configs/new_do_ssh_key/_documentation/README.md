# Digital Ocean SSH Key Management

## Description
This stack creates a new SSH key pair and uploads the public key to DigitalOcean for use with DigitalOcean resources.

## Variables

### Required
None - Either `name` or `ssh_key_name` must be provided.

### Optional
| Name | Description | Default |
|------|-------------|---------|
| name | Configuration for name | |
| ssh_key_name | Name label for SSH key | |
| schedule_id | config0 builtin - id of schedule associated with a stack/workflow | |
| run_id | config0 builtin - id of a run for the instance of a stack/workflow | |
| job_instance_id | config0 builtin - id of a job instance of a job in a schedule | |
| job_id | config0 builtin - id of job in a schedule | |
| cloud_tags_hash | Resource tags for cloud provider | |

## Features
- Name of ssh key must be provided by either name or ssh_key_name
- Creates a new SSH key pair 
- Uploads the SSH public key to DigitalOcean
- Supports automatic key naming

## Dependencies

### Substacks
- [config0-publish:::new_ssh_key](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/new_ssh_key)
- [config0-publish:::do_ssh_upload](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/do_ssh_upload)

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.