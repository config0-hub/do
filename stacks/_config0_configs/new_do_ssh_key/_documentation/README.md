**Description**

  - This stack generates an SSH key and uploads it to DigitalOcean.

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| name   | name of the ssh key                 | string   | None         |

**Sample entry**

```
infrastructure:
   ssh_upload:
       stack_name: config0-hub:::do_ssh_upload
       arguments:
          name: config0-test-do-key
       credentials:
           - reference: do
             orchestration: true
```
