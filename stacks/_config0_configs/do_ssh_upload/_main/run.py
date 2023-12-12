from config0_publisher.terraform import TFConstructor


def _get_ssh_public_key(stack):

    try:
        _lookup = {"must_be_one": True}
        _lookup["resource_type"] = "ssh_key_pair"
        _lookup["name"] = stack.key_name
        results = stack.get_resource(decrypt=True,
                                     **_lookup)[0]
    except:
        results = None

    if not results:
       try:
            _lookup = {"must_be_one": True}
            _lookup["resource_type"] = "ssh_public_key"
            _lookup["name"] = stack.key_name
            results = stack.get_resource(decrypt=True, 
                                         **_lookup)[0]
       except:
           results = None

    if not results:
       try:
            _lookup = {"must_be_one": True}
            _lookup["resource_type"] = "inputvars"
            _lookup["name"] = stack.key_name
            results = stack.get_resource(decrypt=True, 
                                         **_lookup)[0]
       except:
           results = None

    public_key_hash = results.get("public_key_hash")
    
    if public_key_hash:
        return public_key_hash

    public_key = results.get("public_key")

    if public_key:
        return stack.b64_encode(public_key)

    raise Exception("could not retrieve public key/public key hash from query")

def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_optional(key="key_name")

    stack.parse.add_optional(key="name",
                             types="str")

    # declare execution groups
    stack.add_execgroup("config0-hub:::do::ssh_key_upload",
                        "tf_execgroup")

    # Add substack
    stack.add_substack('config0-hub:::tf_executor')

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    if not stack.get_attr("key_name") and stack.get_attr("name"):
        stack.set_variable("key_name",
                           stack.name,
                           types="str")

    if not stack.get_attr("key_name"):
        msg = "key_name or name variable has to be set"
        raise Exception(msg)

    stack.set_variable("ssh_key_name",
                       stack.key_name,
                       tags="tfvar,db",
                       types="str")

    stack.set_variable("ssh_public_key",
                       _get_ssh_public_key(stack),
                       tags="tfvar",
                       types="str")

    ssm_obj = { "DIGITALOCEAN_TOKEN":stack.inputvars["DO_TOKEN"],
                "DIGITALOCEAN_ACCESS_TOKEN":stack.inputvars["DO_TOKEN"] }

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="do",
                       ssm_obj=ssm_obj,
                       resource_name=stack.key_name,
                       resource_type="ssh_public_key",
                       terraform_type="digitalocean_ssh_key")

    tf.include(maps={"ssh_key_id": "id"})

    tf.include(keys=["id",
                     "name"])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
