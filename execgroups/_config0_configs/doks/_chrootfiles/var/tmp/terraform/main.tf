###########################################
# variables
###########################################

variable "cloud_tags" {
  description = "additional tags as a map"
  type        = map(string)
  default     = {}
}

variable "do_region" {
  description = "Digital Ocean region"
  type        = string
}

variable "doks_cluster_name" {
  description = "DOKS cluster name"
  type        = string
}

variable "doks_cluster_version" {
  description = "Kubernetes version provided by DOKS"
  type        = string
  default     = "1.21.3-do.0" 
}

variable "doks_cluster_pool_size" {
  description = "DOKS cluster node pool size"
  type        = string
}

variable "doks_cluster_pool_node_count" {
  description = "DOKS cluster worker nodes count"
  type        = number
}

variable "doks_cluster_autoscale_min" {
  description = "DOKS mininum number of autoscale workers"
  type        = number
  default     = 1
}

variable "doks_cluster_autoscale_max" {
  description = "DOKS max number of autoscale workers"
  type        = number
  default     = 3
}

variable "auto_upgrade" {
  description = "DOKS auto_upgrade"
  default     = true
}

###########################################
# main
###########################################

resource "digitalocean_kubernetes_cluster" "primary" {
  name         = var.doks_cluster_name
  version      = var.doks_cluster_version
  region       = var.do_region
  auto_upgrade = var.auto_upgrade

  node_pool {
    name       = "${var.doks_cluster_name}-pool"
    size       = var.doks_cluster_pool_size
    node_count = var.doks_cluster_pool_node_count
    auto_scale = true
    min_nodes  = var.doks_cluster_autoscale_min
    max_nodes  = var.doks_cluster_autoscale_max

    tags       = [ var.do_region, 
                   var.doks_cluster_name ]

    labels     = { "region": var.do_region,
                   "cluster_name": var.doks_cluster_name }

  }

    tags       = [ var.do_region, 
                   var.doks_cluster_name ]


}
