output "cloudfront_url" {
  description = "CloudFront distribution URL for the website"
  value       = "https://${aws_cloudfront_distribution.cdn.domain_name}"
}

output "api_gateway_endpoint" {
  description = "API Gateway endpoint to submit the form"
  value       = "${aws_apigatewayv2_api.api.api_endpoint}/submit"
}
