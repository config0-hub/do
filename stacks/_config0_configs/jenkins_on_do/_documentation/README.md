**Description**

  - A single entry point for Jenkins on Docker end to end
  - This stack creates a schedule that runs three stacks as jobs:
    - config0-hub:::new_do_ssh_key
    - config0-hub:::droplet
    - config0-hub:::jenkins_on_docker

  - It provides a single opinionated endpoint that creates a simple Jenkins instance on Digital Ocean
  - The automation is end to end automation

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| name      | the name of the Jenkins instance  | string   | None         |
| do_region   | the DO region | string   | NYC1         |
| size   | the size of the droplet | string   | s-1vcpu-2gb         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| with_monitoring | the droplet with monitoring        | boolean   | true       |
| with_backups | the droplet with backups        | boolean   | None       |
| with_ipv6 | the droplet with ipv6        | boolean   | None       |
| with_private_networking | the droplet with private_networking        | boolean   | None       |
| with_resize_disk | the droplet with resize_disk        | boolean   | None       |

**Sample entry**
