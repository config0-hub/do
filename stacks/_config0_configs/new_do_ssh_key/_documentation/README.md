# Digital Ocean SSH Key Management

## Description
This stack creates a new SSH key pair and uploads the public key to DigitalOcean for use with DigitalOcean resources.

## Variables

### Required
Either `name` or `ssh_key_name` must be provided.

### Optional
| Name | Description | Default |
|------|-------------|---------|
| name | Configuration for name | &nbsp; |
| ssh_key_name | Name label for SSH key | &nbsp; |
| schedule_id | config0 builtin - id of schedule associated with a stack/workflow | &nbsp; |
| run_id | config0 builtin - id of a run for the instance of a stack/workflow | &nbsp; |
| job_instance_id | config0 builtin - id of a job instance of a job in a schedule | &nbsp; |
| job_id | config0 builtin - id of job in a schedule | &nbsp; |
| cloud_tags_hash | Resource tags for cloud provider | &nbsp; |

## Dependencies

### Substacks
- [config0-publish:::new_ssh_key](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-publish/new_ssh_key/default)
- [config0-publish:::do_ssh_upload](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-publish/do_ssh_upload/default)

### ShelloutConfigs
- [config0-publish:::terraform::resource_wrapper](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/shelloutconfigs/config0-publish/terraform/resource_wrapper/default)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>