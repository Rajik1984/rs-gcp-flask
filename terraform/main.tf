provider "google" {
  credentials = filebase64decode(var.gcp_sa_key)
  project     = var.project_id
  region      = var.region
}

variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
}

variable "gcp_sa_key" {
  description = "The base64 encoded GCP service account key"
  type        = string
}

resource "google_storage_bucket" "default" {
  name     = "your-gcp-bucket-name"
  location = var.region
}

output "bucket_name" {
  value = google_storage_bucket.default.name
}



