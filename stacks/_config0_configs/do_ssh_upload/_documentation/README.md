**Description**

  - This stack uploads an existing SSH key to DigitalOcean.

**Infrastructure**

  - This stack assumes that the public key of the SSH key is located in the Config0 resources database, which will be uploaded to DigitalOcean.

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
