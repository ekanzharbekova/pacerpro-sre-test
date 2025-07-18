
# SNS Topic
resource "aws_sns_topic" "alerts" {
  name = "ec2-restart-alerts"
}

# SNS Subscription (replace with your email)
resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = "projecttouse77@gmail.com"  # CHANGE THIS TO YOUR EMAIL
}