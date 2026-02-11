# Terraform configuration block that specifies requirements
terraform {
  # Minimum required Terraform version
  required_version = ">= 1.1.0"
  
  # Required provider configurations
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"  # Provider source address
      version = "~> 2.0"                     # Acceptable provider versions
    }
  }
}

# DigitalOcean provider configuration
# Authentication is typically provided via environment variables:
# DIGITALOCEAN_TOKEN or DIGITALOCEAN_ACCESS_TOKEN
provider "digitalocean" {
}















