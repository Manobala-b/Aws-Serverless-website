# Aws-Serverless-website
Creating website using AWS Serverless technologies

# AWS Serverless Portfolio Website (Terraform Project)

This project is a "serverless three-tier architecture" deployed on "AWS using Terraform". It includes a static frontend hosted on "S3 + CloudFront", a backend built with "AWS Lambda", and data storage using "DynamoDB". API Gateway is used to expose the backend as a REST API.


## Architecture Overview

Frontend (S3 + CloudFront)
↓
API Gateway (HTTP API)
↓
AWS Lambda (handler.py)
↓
DynamoDB (Data storage)


## Technologies Used

- Terraform (Infrastructure as Code)
- Amazon S3 (Static website hosting)
- AWS CloudFront (Content Delivery)
- AWS Lambda (Serverless backend function)
- API Gateway (Trigger for Lambda)
- DynamoDB** (NoSQL database)
- Python (Lambda function code)

## 📂 Project Structure

.
├── main.tf # Terraform configuration
├── variables.tf # Input variables
├── outputs.tf # Output values
├── index.html # Frontend web page (hosted on S3)
├── handler.py # Lambda function backend
├── .gitignore # Git ignore rules
└── README.md # Project documentation


## 🚀 Features

- Fully serverless and scalable architecture
- Static hosting with global CDN using CloudFront
- API Gateway integrated with Lambda (Python)
- DynamoDB for persistent storage
- Entire infrastructure managed via Terraform

## 🧪 How to Deploy

### 1. Initialize Terraform
terraform init

2. Plan the infrastructure
terraform plan

4. Apply the configuration
terraform apply
Note: Ensure your AWS CLI is configured (aws configure) and IAM has sufficient permissions.

📌 Pre-requisites :

AWS CLI configured with IAM access

Terraform installed (v1.5+ recommended)

Python installed (for Lambda)

A bucket for remote state (if used)
