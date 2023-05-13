resource "multipass_instance" "dev" {
  name  = "timestep"
  cpus  = 1
  image = "ros2-humble"
}

provider "multipass" {}

terraform {
  required_providers {
    multipass = {
      source  = "larstobi/multipass"
      version = "~> 1.4.1"
    }
  }
}
