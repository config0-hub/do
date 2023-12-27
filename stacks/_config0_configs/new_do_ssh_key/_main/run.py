def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_optional(key="name",
                             typs="str")

    stack.parse.add_optional(key="ssh_key_name",
                             typs="str")

    stack.parse.add_optional(key="schedule_id",
                             typs="str",
                             tags="create,upload")

    stack.parse.add_optional(key="run_id",
                             typs="str",
                             tags="create,upload")

    stack.parse.add_optional(key="job_instance_id",
                             typs="str",
                             tags="create,upload")

    stack.parse.add_optional(key="job_id",
                             typs="str",
                             tags="create,upload")

    stack.parse.add_optional(key="cloud_tags_hash",
                             typs="str",
                             tags="upload")

    # declare execution groups
    stack.add_substack("config0-hub:::new_ssh_key")
    stack.add_substack("config0-hub:::do_ssh_upload")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_substacks()

    if not stack.get_attr("name") and stack.get_attr("ssh_key_name"):
        stack.set_variable("name",
                           stack.ssh_key_name,
                           tags="create,upload",
                           types="str")

    if not stack.get_attr("name"):
        raise Exception("either name or ssh_key_name required")

    stack.verify_variables()

    # create new ssh key pair
    arguments = stack.get_tagged_vars(tag="create",
                                      output="dict")

    human_description = "create ssh key name {}".format(stack.name)
    inputargs = {"arguments": arguments,
                "automation_phase": "infrastructure",
                "human_description": human_description}


    stack.new_ssh_key.insert(display=True, **inputargs)

    # upload ssh public pair
    arguments = stack.get_tagged_vars(tag="upload",
                                      output="dict")

    human_description = "upload ssh_public_key {} to DO".format(stack.name)
    inputargs = {"arguments": arguments,
                "automation_phase": "infrastructure",
                "human_description": human_description}


    stack.do_ssh_upload.insert(display=True, **inputargs)

    return stack.get_results()
