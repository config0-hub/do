from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="ssh_key_id",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_required(key="hostname",
                             tags="tfvar,db",
                             default="_random",
                             types="str")

    stack.parse.add_optional(key="do_region",
                             tags="tfvar,db",
                             types="str",
                             default="NYC1")

    stack.parse.add_optional(key="size",
                             tags="tfvar,db",
                             types="str",
                             default="s-1vcpu-1gb")

    stack.parse.add_optional(key="with_backups",
                             tags="tfvar",
                             types="bool")

    stack.parse.add_optional(key="with_monitoring",
                             tags="tfvar",
                             types="bool")

    stack.parse.add_optional(key="with_ipv6",
                             tags="tfvar",
                             types="bool")

    stack.parse.add_optional(key="with_private_networking",
                             tags="tfvar",
                             types="bool")

    stack.parse.add_optional(key="with_resize_disk",
                             tags="tfvar",
                             types="bool")

    # declare execution groups
    stack.add_execgroup("config0-hub:::do::droplet",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-hub:::tf_executor")

    # initialize variables
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    ssm_obj = { "DIGITALOCEAN_TOKEN":stack.inputvars["DO_TOKEN"],
                "DIGITALOCEAN_ACCESS_TOKEN":stack.inputvars["DO_TOKEN"] }

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       ssm_obj=ssm_obj,
                       provider="do",
                       resource_name=stack.hostname,
                       resource_type="server",
                       terraform_type="digitalocean_droplet")

    tf.include(keys=["id",
                     "image",
                     "urn",
                     "ipv4_address_private",
                     "ipv4_address",
                     "do_region",
                     "name"])

    tf.include(maps={"hostname": "name",
                     "private_ip": "ipv4_address_private",
                     "public_ip": "ipv4_address"})

    # publish the info
    tf.output(keys=["id",
                    "hostname",
                    "image",
                    "private_ip",
                    "public_ip",
                    "do_region",
                    "urn"])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
