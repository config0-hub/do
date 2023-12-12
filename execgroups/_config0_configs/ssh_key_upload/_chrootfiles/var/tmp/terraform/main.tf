variable "ssh_key_name" {}
variable "ssh_public_key" {}

variable "cloud_tags" {
  description = "additional tags as a map"
  type        = map(string)
  default     = {}
}

resource "digitalocean_ssh_key" "default" {
  name       = var.ssh_key_name
  public_key = base64decode(var.ssh_public_key)
}
