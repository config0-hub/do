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

    # Instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="key_name", types="str")
    stack.parse.add_optional(key="public_key", types="str")

    # Declare execution groups
    stack.add_execgroup("config0-publish:::do::ssh_key_upload", "tf_execgroup")

    # Add substack
    stack.add_substack("config0-publish:::tf_executor")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    if not stack.get_attr("public_key") and stack.inputvars.get("public_key"):
        stack.set_variable("public_key", stack.inputvars["public_key"])

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

    stack.set_variable("timeout", 600)

    ssm_obj = {
        "DIGITALOCEAN_TOKEN": stack.inputvars["DO_TOKEN"],
        "DIGITALOCEAN_ACCESS_TOKEN": stack.inputvars["DO_TOKEN"]
    }

    # Use the terraform constructor (helper)
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="do",
                       tf_runtime="tofu:1.9.1",
                       ssm_obj=ssm_obj,
                       resource_name=stack.ssh_key_name,
                       resource_type="ssh_public_key")

    tf.include(values={
        "do_region": stack.do_region,
        "name": stack.ssh_key_name,
        "ssh_key_name": stack.ssh_key_name
    })

    tf.include(maps={"id": "ssh_key_id"})

    # Publish the info
    tf.output(keys=["id", "name", "ssh_key_id"])

    # Finalize the tf_executor
    stack.tf_executor.insert(display=True, **tf.get())

    return stack.get_results()