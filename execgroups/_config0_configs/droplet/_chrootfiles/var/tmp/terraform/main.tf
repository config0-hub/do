resource "digitalocean_droplet" "default" {
  image              = var.image
  name               = var.hostname
  region             = var.do_region
  size               = var.size
  backups            = var.with_backups
  monitoring         = var.with_monitoring
  ipv6               = var.with_ipv6
  private_networking = false # Note: This attribute is deprecated but maintained for compatibility
  resize_disk        = var.with_resize_disk
  ssh_keys           = [var.ssh_key_id]
}

