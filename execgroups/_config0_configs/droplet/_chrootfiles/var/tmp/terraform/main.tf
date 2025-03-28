variable "ssh_key_id" {}

variable "image" {
  description = "The Droplet image id"
  default     = "ubuntu-20-04-x64"
}

variable "hostname" {
  description = "The hostname of the Droplet"
  default     = "config0-demo"
}

variable "do_region" {
  description = "The region of the Droplet"
  default     = "NYC1"
}

variable "size" {
  description = "The instance size"
  default     = "s-1vcpu-1gb"
}

variable "with_backups" {
  description = "Boolean controlling if backups are made"
  default     = false
}

variable "with_monitoring" {
  description = "Boolean controlling whether monitoring agent is installed"
  default     = false
}

variable "with_ipv6" {
  description = "Boolean controlling if IPv6 is enabled"
  default     = false
}

variable "with_resize_disk" {
  description = "Whether to increase the disk size when resizing a Droplet"
  default     = false
}

resource "digitalocean_droplet" "default" {
  image              = var.image
  name               = var.hostname
  region             = var.do_region
  size               = var.size
  backups            = var.with_backups
  monitoring         = var.with_monitoring
  ipv6               = var.with_ipv6
  private_networking = false
  resize_disk        = var.with_resize_disk
  ssh_keys           = [var.ssh_key_id]
}

output "ip" {
  value = digitalocean_droplet.default.ipv4_address
}

output "id" {
  value = digitalocean_droplet.default.id
}

output "image" {
  value = digitalocean_droplet.default.image
}

output "urn" {
  value = digitalocean_droplet.default.urn
}

output "private_ip" {
  value = digitalocean_droplet.default.ipv4_address_private
}

output "public_ip" {
  value = digitalocean_droplet.default.ipv4_address
}
