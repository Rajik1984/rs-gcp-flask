variable "project_id" {
  description = "The GCP project ID"
}

variable "region" {
  description = "The GCP region"
}

variable "gcp_sa_key" {
  description = "The base64 encoded GCP service account key"
  type        = string
}
