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


class Main(newSchedStack):

    def __init__(self, stackargs):
        newSchedStack.__init__(self, stackargs)

        # Add required parameters
        self.parse.add_required(key="name", types="str")
        self.parse.add_required(key="do_region", tags="droplet", types="str", default="NYC1")
        self.parse.add_required(key="size", tags="droplet", types="str", default="s-1vcpu-2gb")

        # Add optional parameters
        self.parse.add_optional(key="with_monitoring", tags="droplet", types="bool")
        self.parse.add_optional(key="with_backups", tags="droplet", types="bool")
        self.parse.add_optional(key="with_ipv6", tags="droplet", types="bool")
        self.parse.add_optional(key="with_private_networking", tags="droplet", types="bool")
        self.parse.add_optional(key="with_resize_disk", tags="droplet", types="bool")
        self.parse.add_optional(key="cloud_tags_hash", tags="ssh_key,droplet", types="str")

        # Add required substacks
        self.stack.add_substack("config0-publish:::new_do_ssh_key")
        self.stack.add_substack("config0-publish:::droplet")
        self.stack.add_substack("config0-publish:::jenkins_on_docker")

        self.stack.init_substacks()

    def _set_hostname(self):
        self.stack.set_variable("hostname",
                                f"{self.stack.name}-vm",
                                tags="droplet,jenkins",
                                types="str")

    def _set_ssh_key_name(self):
        self.stack.set_variable("ssh_key_name",
                                f"{self.stack.name}-ssh-key",
                                tags="ssh_key,jenkins",
                                types="str")

    def run_ssh_key(self):
        self.stack.init_variables()
        self._set_ssh_key_name()
        self.stack.verify_variables()

        arguments = self.stack.get_tagged_vars(tag="ssh_key", output="dict")
        
        human_description = f"Create and upload ssh key name {self.stack.ssh_key_name}"
        inputargs = {
            "arguments": arguments,
            "automation_phase": "infrastructure",
            "human_description": human_description
        }

        return self.stack.new_do_ssh_key.insert(display=True, **inputargs)

    def run_droplet(self):
        # by default, it references a selector defined in the config0.yml
        self.parse.add_required(key="ssh_key_id",
                                tags="droplet",
                                types="str",
                                default="selector:::ssh_key_info::id")

        self.stack.init_variables()
        self._set_hostname()
        self.stack.verify_variables()

        arguments = self.stack.get_tagged_vars(tag="droplet", output="dict")

        human_description = f'Create droplet hostname {self.stack.hostname}'
        inputargs = {
            "arguments": arguments,
            "automation_phase": "infrastructure",
            "human_description": human_description
        }

        return self.stack.droplet.insert(display=True, **inputargs)

    def run_jenkins_ans(self):
        self.stack.init_variables()
        self._set_ssh_key_name()
        self._set_hostname()
        self.stack.verify_variables()

        arguments = self.stack.get_tagged_vars(tag="jenkins", output="dict")

        human_description = f"Install Jenkins on hostname {self.stack.hostname}"
        inputargs = {
            "arguments": arguments,
            "automation_phase": "infrastructure",
            "human_description": human_description
        }

        return self.stack.jenkins_on_docker.insert(display=True, **inputargs)

    def run(self):
        self.stack.unset_parallel(sched_init=True)
        self.add_job("ssh_key")
        self.add_job("droplet")
        self.add_job("jenkins_ans")

        return self.finalize_jobs()

    def schedule(self):
        # Create and upload SSH key
        sched = self.new_schedule()
        sched.job = "ssh_key"
        sched.archive.timeout = 1800
        sched.archive.timewait = 120
        sched.archive.cleanup.instance = "clear"
        sched.failure.keep_resources = True
        sched.conditions.retries = 1  # retries is always one for the first job
        sched.automation_phase = "infrastructure"
        sched.human_description = "Create and upload ssh-key to DO"
        sched.on_success = ["droplet"]
        self.add_schedule()

        # Create droplet
        sched = self.new_schedule()
        sched.job = "droplet"
        sched.archive.timeout = 1800
        sched.archive.timewait = 180
        sched.archive.cleanup.instance = "clear"
        sched.failure.keep_resources = True
        sched.automation_phase = "infrastructure"
        sched.human_description = "Create droplet on DO"
        sched.on_success = ["jenkins_ans"]
        self.add_schedule()

        # Install Jenkins
        sched = self.new_schedule()
        sched.job = "jenkins_ans"
        sched.archive.timeout = 1800
        sched.archive.timewait = 180
        sched.archive.cleanup.instance = "clear"
        sched.failure.keep_resources = True
        sched.automation_phase = "infrastructure"
        sched.human_description = "Install Jenkins on VM"
        self.add_schedule()

        return self.get_schedules()
