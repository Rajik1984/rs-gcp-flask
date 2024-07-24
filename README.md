# rs-gcp-flask

## Description

A basic CRUD app built with Flask, tested with pytest, continously deployed using Github Actions on Google Cloud Platform(GCP) built with Docker and Terraform.

## Architecture Diagram

![Architecture Diagram](/rs-gcp-flask.png)

## Features

- Create a person record
- Retrieve a person record
- Update a person record
- Delete a person record

## Prerequisites

- Python 3.9
- Docker
- GitHub account
- Google Cloud Platform account
- Terraform

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/rsgcp-flask-api.git
   cd rsgcp-flask-api
   ```

2. Build and run the Docker container locally:
    ```sh
    docker build -t rs-gcp-flask .
    docker run -p 8080:80 rs-gcp-flask
    ```
### Terraform Deployment

1. Initialize and apply Terraform configuration:
    ```sh
    terraform init
    terraform apply -var="project_id=your-gcp-project-id" -var="region of choice"
    ```

## CI/CD

GitHub Actions is used for CI/CD to automate the build and deployment process. Ensure the following secrets are set in your GitHub repository:
- `GCP_PROJECT_ID`
- `GCP_SA_KEY`
- `GCP_REGION`
