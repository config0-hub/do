from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="key_name",
                             types="str")

    stack.parse.add_optional(key="public_key",
                             types="str")

    # declare execution groups
    stack.add_execgroup("config0-hub:::do::ssh_key_upload",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-hub:::tf_executor")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    if not stack.get_attr("public_key") and stack.inputvars.get("public_key"):
        stack.set_variable("public_key", 
                           stack.inputvars["public_key"])

    if not stack.get_attr("public_key"):
        msg = "public_key is missing"
        raise Exception(msg)

    stack.set_variable("ssh_public_key", 
                       stack.public_key,
                       tags="tfvar",
                       types="str")

    stack.set_variable("ssh_key_name",
                       stack.key_name,
                       tags="tfvar,db",
                       types="str")

    ssm_obj = { "DIGITALOCEAN_TOKEN":stack.inputvars["DO_TOKEN"],
                "DIGITALOCEAN_ACCESS_TOKEN":stack.inputvars["DO_TOKEN"] }

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="do",
                       ssm_obj=ssm_obj,
                       resource_name=stack.ssh_key_name,
                       resource_type="ssh_public_key",
                       terraform_type="digitalocean_ssh_key")

    tf.include(maps={"ssh_key_id": "id"})

    tf.include(keys=["id",
                     "name"])

    # publish the info
    tf.output(keys=["id",
                    "name",
                    "ssh_key_id"])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
