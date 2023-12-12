**Description**

  - Creates a droplet/vm on digitalocean

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| ssh_key_id   | ssh key id for digital ocean            | string   | None         |
| hostname   | hostname/name for the droplet             | string   | None         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| do_region   | digital ocean region             | string   | NYC1         |
| size   | droplet size             | string   | s-1vcpu-1gb         |
| with_backups   | with_backups        | string   | false         |
| with_monitoring   | with_monitoring        | string   | false         |
| with_ipv6   | with_ipv6        | string   | false         |
| with_private_networking   | with_private_networking        | string   | false         |
| with_resize_disk   | with_resize_disk        | string   | false         |

**Sample entry:**
```
infrastructure:
  vm:
    stack_name: config0-hub:::droplet
    arguments:
      hostname: config0-demo
      ssh_key_id: 288907
