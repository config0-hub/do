"""
# Copyright (C) 2025 Gary Leong <gary@config0.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
    stack.add_execgroup("config0-publish:::do::droplet",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-publish:::tf_executor")

    # initialize variables
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    ssm_obj = {
        "DIGITALOCEAN_TOKEN": stack.inputvars["DO_TOKEN"],
        "DIGITALOCEAN_ACCESS_TOKEN": stack.inputvars["DO_TOKEN"]
    }

    stack.set_variable("timeout", 600)

    # use the terraform constructor (helper)
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       ssm_obj=ssm_obj,
                       provider="do",
                       resource_name=stack.hostname,
                       resource_type="server")

    tf.include(values={
        "do_region": stack.do_region,
        "name": stack.hostname,
        "hostname": stack.hostname
    })

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