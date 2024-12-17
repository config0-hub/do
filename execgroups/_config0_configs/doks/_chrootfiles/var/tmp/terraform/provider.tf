terraform {
  required_version = ">= 1.1.0"
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.26.0"
    }
  }
}

provider "digitalocean" {
}
