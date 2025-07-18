
# Outputs
output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.web_server.id
}

output "lambda_function_url" {
  description = "Lambda Function URL for Sumo Logic webhook"
  value       = aws_lambda_function_url.webhook.function_url
}

output "sns_topic_arn" {
  description = "SNS Topic ARN"
  value       = aws_sns_topic.alerts.arn
}