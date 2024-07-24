provider "google" {
  credentials = filebase64decode(var.gcp_sa_key)
  project     = var.project_id
  region      = var.region
}

variable "project_id" {}
variable "region" {}
variable "gcp_sa_key" {}

resource "google_storage_bucket" "default" {
  name     = "rs-gcp-flask"
  location = var.region
}



