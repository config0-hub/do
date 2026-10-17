# Digital Ocean SSH Key Management

## Description
This stack creates a new SSH key pair and uploads the public key to DigitalOcean for use with DigitalOcean resources. EC2 generates the key pair in the `aws_default_region` of your AWS account and keeps the private half in SSM Parameter Store at `/ec2/keypair/<key_pair_id>`. The `ssh_key_pair` resource records `key_name`, `key_pair_id`, `public_key` and `private_key_ssm_path`, the name of that parameter. No Config0 state or record holds the private half. Removing the stack deletes the key pair, and AWS deletes the parameter with it.

## Variables

### Required
Either `name` or `ssh_key_name` must be provided. It is also the EC2 key pair name, unique per account and region.

### Optional
| Name | Description | Default |
|------|-------------|---------|
| name | Configuration for name | &nbsp; |
| ssh_key_name | Name label for SSH key | &nbsp; |
| aws_default_region | AWS region of the key pair and of its SSM parameter | ap-northeast-1 |
| cloud_tags_hash | Resource tags for cloud provider | &nbsp; |

## Dependencies

### Substacks
- [config0-hub:::config0_core::tf_executor](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-hub/tf_executor/default)
- [config0-hub:::do::do_ssh_upload](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/stacks/config0-hub/do_ssh_upload/default)

### Execgroups
- [config0-hub:::aws::ssh_key_pair](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/exec/groups/config0-hub/aws/ssh_key_pair/default)

### Scripts
- [config0-hub:::terraform::resource_wrapper](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/scripts/config0-hub/terraform/resource_wrapper/default)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>