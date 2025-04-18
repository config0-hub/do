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


def run(stackargs):

    # Instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_optional(key="name", types="str")
    stack.parse.add_optional(key="ssh_key_name", types="str")

    stack.parse.add_optional(key="schedule_id",
                             types="str",
                             tags="create,upload")

    stack.parse.add_optional(key="run_id",
                             types="str",
                             tags="create,upload")

    stack.parse.add_optional(key="job_instance_id",
                             types="str",
                             tags="create,upload")

    stack.parse.add_optional(key="job_id",
                             types="str",
                             tags="create,upload")

    stack.parse.add_optional(key="cloud_tags_hash",
                             types="str",
                             tags="upload")

    # Declare execution groups
    stack.add_substack("config0-publish:::new_ssh_key")
    stack.add_substack("config0-publish:::do_ssh_upload")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_substacks()

    # Use ssh_key_name as name if name is not provided
    if not stack.get_attr("name") and stack.get_attr("ssh_key_name"):
        stack.set_variable("name",
                          stack.ssh_key_name,
                          tags="create,upload",
                          types="str")

    if not stack.get_attr("name"):
        raise Exception("either name or ssh_key_name required")

    stack.verify_variables()

    # Create new ssh key pair
    arguments = stack.get_tagged_vars(tag="create", output="dict")
    human_description = f"create ssh key name {stack.name}"
    inputargs = {
        "arguments": arguments,
        "automation_phase": "infrastructure",
        "human_description": human_description
    }
    stack.new_ssh_key.insert(display=True, **inputargs)

    # Upload ssh public pair
    arguments = stack.get_tagged_vars(tag="upload", output="dict")
    human_description = f"upload ssh_public_key {stack.name} to DO"
    inputargs = {
        "arguments": arguments,
        "automation_phase": "infrastructure",
        "human_description": human_description
    }
    stack.do_ssh_upload.insert(display=True, **inputargs)

    return stack.get_results()