# terraform/main.tf

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "repository" {
  name     = var.repo_name
  format   = "DOCKER"
  location = var.region
}

output "artifact_registry_repository" {
  value = google_artifact_registry_repository.repository.name
}


