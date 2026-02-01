variable "ssh_key_id" {
  description = "The DigitalOcean SSH key ID to use for Droplet access"
  type        = string
}

variable "image" {
  description = "The Droplet image slug or ID to use for creation"
  type        = string
  default     = "ubuntu-20-04-x64"
}

variable "hostname" {
  description = "The hostname of the Droplet that will be created"
  type        = string
  default     = "config0-demo"
}

variable "do_region" {
  description = "The DigitalOcean region where the Droplet will be provisioned"
  type        = string
  default     = "NYC1"
}

variable "size" {
  description = "The Droplet size/plan to use (determines CPU, RAM, and disk)"
  type        = string
  default     = "s-1vcpu-1gb"
}

variable "with_backups" {
  description = "Boolean controlling if automated backups are enabled"
  type        = bool
  default     = false
}

variable "with_monitoring" {
  description = "Boolean controlling whether DigitalOcean monitoring agent is installed"
  type        = bool
  default     = false
}

variable "with_ipv6" {
  description = "Boolean controlling if IPv6 networking is enabled"
  type        = bool
  default     = false
}

variable "with_resize_disk" {
  description = "Whether to increase the disk size when resizing a Droplet"
  type        = bool
  default     = false
}

