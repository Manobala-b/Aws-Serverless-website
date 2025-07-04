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

🚀 Important Notes Before Deployment :

1. CORS Configuration Must Be Done Manually (Due to Terraform Limitation)
Terraform currently does not support cors_configuration block in aws_apigatewayv2_stage.
➤ After deployment, go to AWS Console → API Gateway → Routes → POST /submit → Enable CORS manually.
Set:

Allowed Origins: *

Allowed Methods: OPTIONS, POST

Allowed Headers: *


2. Update the API Gateway URL in contact.html Manually
After running terraform apply, Terraform will create a new API Gateway endpoint.
➤ You must copy that URL (e.g., https://xyz123.execute-api.ap-south-1.amazonaws.com/submit) and paste it inside website/contact.html as the fetch URL in the form submission code.


3. Re-upload the Updated contact.html After Editing the API URL
Once you've updated the API Gateway URL inside the file, re-upload contact.html to the website/ folder.
➤ Either commit and push it to GitHub or re-apply using Terraform.


4. Zip the Lambda Code Before Terraform Apply
If you update the Lambda Python code (handler.py), make sure to zip it before running Terraform:
Compress-Archive -Path lambda/handler.py -DestinationPath lambda.zip -Force


5. S3 Bucket Must Have Public Access Enabled
Terraform allows public read access to your S3 bucket via bucket policy and ACL settings, so that the static website can be accessed by anyone.


6. CloudFront May Take a Few Minutes to Reflect Changes
When you update HTML files and reapply Terraform, changes may take time due to CloudFront caching.
➤ You can invalidate the cache manually via AWS Console if needed.


7. DynamoDB Table Name and Lambda Environment Variable Must Match
Ensure that the TABLE_NAME environment variable in Lambda exactly matches the DynamoDB table name defined in Terraform (FormSubmissions in your case).


8. All Frontend Files Must Be Inside the website/ Folder
Terraform only uploads HTML files from the website/ directory. Make sure to place all .html files there (index.html, contact.html, etc.).
