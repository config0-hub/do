from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Section 1:
    # Add variables for the stack (many fetched from OpenTofu variables)
    stack.parse.add_required(key="doks_cluster_name",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_required(key="do_region",
                             tags="tfvar,db",
                             types="str",
                             default="lon1")

    stack.parse.add_optional(key="doks_cluster_version",
                             tags="tfvar,db",
                             types="str",
                             default="1.29.1-do.0")

    stack.parse.add_optional(key="doks_cluster_pool_size",
                             tags="tfvar",
                             types="str",
                             default="s-1vcpu-2gb-amd")

    stack.parse.add_optional(key="doks_cluster_pool_node_count",
                             tags="tfvar",
                             types="int",
                             default="1")

    stack.parse.add_optional(key="doks_cluster_autoscale_min",
                             tags="tfvar",
                             types="int",
                             default="1")

    stack.parse.add_optional(key="doks_cluster_autoscale_max",
                             tags="tfvar",
                             types="int",
                             default="3")

    stack.parse.add_optional(key="tf_runtime",
                             default="terraform:1.5.4",
                             types="str")

    # Section 2:
    # Declare execution groups - for simplicity we alias "tf_execgroup"
    # the execgroup must be fully qualified <repo_owner>:::<repo_name>::<execgroup_name>
    stack.add_execgroup("config0-publish:::do::doks",
                        "tf_execgroup")

    # Section 3:
    # Add substack - for OpenTofu it will almost always be config0-publish:::tf_executor
    stack.add_substack("config0-publish:::tf_executor")

    # Section 4:
    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    # Section 5:
    # For sensitive upload to ssm parameter store which will automatically expire/remove object
    ssm_obj = {
        "DIGITALOCEAN_TOKEN":stack.inputvars["DO_TOKEN"],
        "DIGITALOCEAN_ACCESS_TOKEN":stack.inputvars["DO_TOKEN"]
    }

    # Section 6:
    # if timeout exceeds 600, then it will use codebuild to execute tf
    # otherwise, if less than 600 seconds, it will use a lambda function
    # which is faster since lambda coldstarts is less than codebuild
    stack.set_variable("timeout",2700)

    # Section 7:
    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="do",
                       ssm_obj=ssm_obj,
                       resource_name=stack.doks_cluster_name,
                       resource_type="doks",
                       terraform_type="digitalocean_kubernetes_cluster")

    # Section 8:
    # keys to include in db fields
    # from the terraform resource type
    tf.include(keys=["name",
                     "service_subnet",
                     "id",
                     "urn",
                     "endpoint",
                     "kube_config",
                     "vpc_uuid"])

    # Section 9:
    # keys to map and include in db fields
    tf.include(maps={"cluster_id": "id",
                     "doks_version": "version"})

    # Section 10:
    # keys to publish and display in SaaS UI
    tf.output(keys=["doks_version",
                    "do_region",
                    "service_subnet",
                    "urn",
                    "vpc_uuid",
                    "endpoint"])

    # Section 11:
    # Finalize the tf_executor
    inputargs = tf.get()
    inputargs["overide_values"]["tf_runtime"] = stack.tf_runtime

    stack.tf_executor.insert(display=True,
                             **inputargs)

    # Section 12:
    # return results
    return stack.get_results()
