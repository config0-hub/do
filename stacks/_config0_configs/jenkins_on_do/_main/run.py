class Main(newSchedStack):

    def __init__(self, stackargs):

        newSchedStack.__init__(self, stackargs)

        # ssh_key_name - name: config0-jenkins-key
        # hostname: config0-jenkins-master
        # region: NYC1
        # size: s-1vcpu-2gb

        # the name of the jenkins instance
        self.parse.add_required(key="name",
                                types="str")

        self.parse.add_required(key="do_region",
                                tags="droplet",
                                types="str",
                                default="NYC1")

        self.parse.add_required(key="size",
                                tags="droplet",
                                types="str",
                                default="s-1vcpu-2gb")

        self.parse.add_optional(key="with_monitoring",
                                tags="droplet",
                                types="bool")

        self.parse.add_optional(key="with_backups",
                                tags="droplet",
                                types="bool")

        self.parse.add_optional(key="with_ipv6",
                                tags="droplet",
                                types="bool")

        self.parse.add_optional(key="with_private_networking",
                                tags="droplet",
                                types="bool")

        self.parse.add_optional(key="with_resize_disk",
                                tags="droplet",
                                types="bool")

        self.parse.add_optional(key="cloud_tags_hash",
                                tags="ssh_key,droplet",
                                types="str")

        self.stack.add_substack("config0-hub:::new_do_ssh_key")
        self.stack.add_substack("config0-hub:::droplet")
        self.stack.add_substack("config0-hub:::jenkins_on_docker")

        self.stack.init_substacks()

    def _set_hostname(self):

        self.stack.set_variable("hostname",
                                "{}-vm".format(self.stack.name),
                                tags="droplet,jenkins",
                                types="str")

    def _set_ssh_key_name(self):

        self.stack.set_variable("ssh_key_name",
                                "{}-ssh-key".format(self.stack.name),
                                tags="ssh_key,jenkins",
                                types="str")

    def run_ssh_key(self):

        self.stack.init_variables()
        self._set_ssh_key_name()
        self.stack.verify_variables()

        arguments = self.stack.get_tagged_vars(tag="ssh_key",
                                               output="dict")
    
        human_description = "Create and upload ssh key name {}".format(self.stack.ssh_key_name)
        inputargs = {"arguments": arguments,
                    "automation_phase": "infrastructure",
                    "human_description": human_description}

        return self.stack.new_do_ssh_key.insert(display=True,
                                                **inputargs)

    def run_droplet(self):

        # by default, it references a selector defined in the config0.yml
        self.parse.add_required(key="ssh_key_id",
                                tags="droplet",
                                types="str",
                                default="selector:::ssh_key_info::id")

        self.stack.init_variables()
        self._set_hostname()
        self.stack.verify_variables()

        arguments = self.stack.get_tagged_vars(tag="droplet",
                                               output="dict")

        human_description = 'Create droplet hostname {}'.format(self.stack.hostname)
        inputargs = {"arguments": arguments,
                    "automation_phase": "infrastructure",
                    "human_description": human_description}


        return self.stack.droplet.insert(display=True, **inputargs)

    def run_jenkins_ans(self):

        self.stack.init_variables()
        self._set_ssh_key_name()
        self._set_hostname()
        self.stack.verify_variables()

        arguments = self.stack.get_tagged_vars(tag="jenkins",
                                               output="dict")

        human_description = "Install Jenkins on hostname {}".format(self.stack.hostname)
        inputargs = {"arguments": arguments,
                    "automation_phase": "infrastructure",
                    "human_description": human_description}


        return self.stack.jenkins_on_docker.insert(display=True,
                                                   **inputargs)

    def run(self):

        self.stack.unset_parallel()
        self.add_job("ssh_key")
        self.add_job("droplet")
        self.add_job("jenkins_ans")

        return self.finalize_jobs()

    def schedule(self):

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
