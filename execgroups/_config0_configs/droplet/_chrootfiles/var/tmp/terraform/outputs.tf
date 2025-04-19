output "ip" {
  description = "The public IPv4 address of the Droplet"
  value       = digitalocean_droplet.default.ipv4_address
}

output "id" {
  description = "The ID of the Droplet"
  value       = digitalocean_droplet.default.id
}

output "image" {
  description = "The image of the Droplet"
  value       = digitalocean_droplet.default.image
}

output "urn" {
  description = "The uniform resource name of the Droplet"
  value       = digitalocean_droplet.default.urn
}

output "private_ip" {
  description = "The private IPv4 address of the Droplet"
  value       = digitalocean_droplet.default.ipv4_address_private
}

output "public_ip" {
  description = "The public IPv4 address of the Droplet"
  value       = digitalocean_droplet.default.ipv4_address
}