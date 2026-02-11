# DigitalOcean SSH Key Upload

## Description
This stack uploads an SSH public key to a DigitalOcean account and makes it available for use with DigitalOcean resources.

## Variables

### Required

| Name | Description | Default |
|------|-------------|---------|
| key_name | SSH key identifier for resource access | &nbsp; |
| public_key | SSH public key content | &nbsp; |

### Optional

| Name | Description | Default |
|------|-------------|---------|
| timeout | Configuration for timeout | 600 |

## Dependencies

### Substacks
- [config0-publish:::tf_executor](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-publish/tf_executor/default)

### Execgroups
- [config0-publish:::do::ssh_key_upload](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/exec/groups/config0-publish/do/ssh_key_upload/default)

### Shelloutconfigs
- [config0-publish:::terraform::resource_wrapper](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/shelloutconfigs/config0-publish/terraform/resource_wrapper/default)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>