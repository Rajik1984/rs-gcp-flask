# terraform/variables.tf

variable "project_id" {
  type        = string
  description = "The ID of the GCP project"
}

variable "region" {
  type        = string
  description = "The GCP region"
  default     = "us-central1"
}

variable "repo_name" {
  type        = string
  description = "The name of the Artifact Registry repository"
}
