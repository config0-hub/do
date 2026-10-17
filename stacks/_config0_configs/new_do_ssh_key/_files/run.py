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
    stack.parse.add_optional(key="name", types="str", tags="upload")
    stack.parse.add_optional(key="ssh_key_name", types="str")

    # The key pair's region. AWS keeps the private half in SSM there.
    stack.parse.add_optional(key="aws_default_region",
                             default="ap-northeast-1",
                             tags="tfvar,db,resource,tf_exec_env",
                             types="str")

    stack.parse.add_optional(key="cloud_tags_hash",
                             types="str",
                             tags="upload")

    # Declare execution groups
    stack.add_execgroup("config0-hub:::aws::ssh_key_pair", "tf_execgroup")
    stack.add_substack("config0-hub:::config0_core::tf_executor")
    stack.add_substack("config0-hub:::do::do_ssh_upload")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    # Use ssh_key_name as name if name is not provided
    if not stack.get_attr("name") and stack.get_attr("ssh_key_name"):
        stack.set_variable("name",
                          stack.ssh_key_name,
                          tags="upload",
                          types="str")

    if not stack.get_attr("name"):
        raise Exception("either name or ssh_key_name required")

    # The key pair takes the name as its key_name
    stack.set_variable("key_name",
                       stack.name,
                       tags="tfvar,db",
                       types="str")

    stack.verify_variables()

    # Create the key pair. EC2 generates it and keeps the private half in
    # SSM; the ssh_key_pair row names that parameter, never the key.
    tf = TFConstructor(stack=stack,
                       provider="aws",
                       execgroup_name=stack.tf_execgroup.name,
                       tf_runtime="tofu:1.11.14",
                       resource_name=stack.key_name,
                       resource_type="ssh_key_pair")

    tf.include(keys=["key_name",
                     "key_pair_id",
                     "public_key",
                     "private_key_ssm_path"])

    stack.tf_executor.insert(display=True, **tf.get())

    # Upload the public half to DigitalOcean. do_ssh_upload reads it from the
    # ssh_key_pair row.
    arguments = stack.get_tagged_vars(tag="upload", output="dict")
    human_description = f"upload ssh_public_key {stack.name} to DO"
    inputargs = {
        "arguments": arguments,
        "automation_phase": "infrastructure",
        "human_description": human_description
    }
    stack.do_ssh_upload.insert(display=True, **inputargs)

    return stack.get_results()
