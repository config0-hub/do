from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="doks_cluster_name",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_required(key="do_region",
                             tags="tfvar,db",
                             types="str",
                             default='lon1')

    stack.parse.add_optional(key="doks_cluster_version",
                             tags="tfvar,db",
                             types="str",
                             default='1.26.3-do.0')

    stack.parse.add_optional(key="doks_cluster_pool_size",
                             tags="tfvar",
                             types="str",
                             default='s-1vcpu-2gb-amd')

    stack.parse.add_optional(key="doks_cluster_pool_node_count",
                             tags="tfvar",
                             types="int",
                             default='1')

    stack.parse.add_optional(key="doks_cluster_autoscale_min",
                             tags="tfvar",
                             types="int",
                             default='1')

    stack.parse.add_optional(key="doks_cluster_autoscale_max",
                             tags="tfvar",
                             types="int",
                             default='3')

    # declare execution groups
    stack.add_execgroup("config0-hub:::do::doks",
                        "tf_execgroup")

    # Add substack
    stack.add_substack('config0-hub:::tf_executor')

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    ssm_obj = { "DIGITALOCEAN_TOKEN":stack.inputvars["DO_TOKEN"],
                "DIGITALOCEAN_ACCESS_TOKEN":stack.inputvars["DO_TOKEN"] }

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="do",
                       ssm_obj=ssm_obj,
                       resource_name=stack.doks_cluster_name,
                       resource_type="doks",
                       terraform_type="digitalocean_kubernetes_cluster")

    tf.include(maps={"cluster_id": "id",
                     "doks_version": "version"})

    tf.include(keys=["name",
                     "service_subnet",
                     "id",
                     "urn",
                     "endpoint",
                     "kube_config",
                     "vpc_uuid"])

    # publish the info
    tf.output(keys=["doks_version",
                    "do_region",
                    "service_subnet",
                    "urn",
                    "vpc_uuid",
                    "endpoint"])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
