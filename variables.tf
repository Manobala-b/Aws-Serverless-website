variable "aws_region" {
  description = "The AWS region to deploy resources"
  default     = "ap-south-1" # Mumbai region
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket to host the static website"
  default     = "mano-frontend-site-bucket"
}
