# Lambda Function
resource "aws_lambda_function" "ec2_restart" {
  filename         = "lambda_function.zip"
  function_name    = "ec2-restart-automation"
  role            = aws_iam_role.lambda_role.arn
  handler         = "lambda_function.lambda_handler"
  runtime         = "python3.9"
  timeout         = 30
  
  environment {
    variables = {
      INSTANCE_ID   = aws_instance.web_server.id
      SNS_TOPIC_ARN = aws_sns_topic.alerts.arn
    }
  }
}

# Lambda Function URL (for Sumo Logic webhook)
resource "aws_lambda_function_url" "webhook" {
  function_name      = aws_lambda_function.ec2_restart.function_name
  authorization_type = "NONE"
}