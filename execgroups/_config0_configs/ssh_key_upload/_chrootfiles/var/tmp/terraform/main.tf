variable "ssh_key_name" {}
variable "ssh_public_key" {}

resource "digitalocean_ssh_key" "default" {
  name       = var.ssh_key_name
  public_key = base64decode(var.ssh_public_key)
}

output "ssh_key_id" {
  value = digitalocean_ssh_key.default.id
}
