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


def _get_ssh_public_key(stack):

    _lookup = {"must_be_one": True,
               "resource_type": "ssh_key_pair",
               "name": stack.key_name}
    try:
        results = stack.get_resource(decrypt=True,
                                     **_lookup)[0]
    except:
        results = None

    if results:
        stack.logger.debug(f"found public key {_lookup}")

    if not results:
        _lookup = {"must_be_one": True,
                   "resource_type": "ssh_public_key",
                   "name": stack.key_name}
        try:
            results = stack.get_resource(decrypt=True,
                                         **_lookup)[0]
        except:
            results = None

        if results:
            stack.logger.debug(f"found public key {_lookup}")

    if not results:
        _lookup = {"must_be_one": True,
                   "resource_type": "inputvars",
                   "name": stack.key_name}
        try:
            results = stack.get_resource(decrypt=True,
                                         **_lookup)[0]
        except:
            results = None

        if results:
            stack.logger.debug(f"found public key {_lookup}")

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
    stack.add_execgroup("config0-publish:::do::ssh_key_upload",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-publish:::tf_executor")

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

    stack.set_variable("timeout", 600)

    ssm_obj = {"DIGITALOCEAN_TOKEN": stack.inputvars["DO_TOKEN"],
               "DIGITALOCEAN_ACCESS_TOKEN": stack.inputvars["DO_TOKEN"]}

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="do",
                       tf_runtime="tofu:1.8.8",
                       ssm_obj=ssm_obj,
                       resource_name=stack.ssh_key_name,
                       resource_type="ssh_public_key")

    tf.include(values={
                    "do_region": stack.do_region,
                    "name": stack.ssh_key_name,
                    "ssh_key_name": stack.ssh_key_name
                    })

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()