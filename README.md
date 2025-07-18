# pacerpro-sre-test
# SRE Assessment - Automated Performance Monitoring

# Automated solution that monitors API response times and restarts EC2 instances when performance degrades.
# Flow: Sumo Logic detects slow responses → Lambda function restarts EC2 → SNS sends notification

# Step-by-Step Deployment

# Step 1: Prepare Lambda Function
bashzip lambda_function.zip lambda_function.py

mv lambda_function.zip terraform/

# Step 2: Update Email Address
Edit terraform/sns.tf:
hclendpoint = "projecttouse77@gmail.com"  # Replace with your email

# Step 3: Deploy Infrastructure

bashcd terraform
terraform init
terraform plan
terraform apply -auto-approve

# Step 4: Note Important Outputs
# After deployment, save these values:

# lambda_function_url - Use this for Sumo Logic webhook

# instance_id - EC2 instance that will be restarted
# sns_topic_arn - Notification topic

# Step 5: Configure Sumo Logic Alert

# Use the query from sumo_logic_query.txt
# Set webhook URL to the lambda_function_url from Step 4
# Configure alert to trigger on more than 5 slow responses in 10 minutes

# Step 6: Confirm Email Subscription
# Check your email and confirm the SNS subscription to receive notifications.
# Testing the Solution
# Manual Test
# bash# Get Lambda URL from terraform output

terraform output lambda_function_url

# Test the function
curl -X POST "<your-lambda-url>" \
  -H "Content-Type: application/json" \
  -d '{"test": "manual trigger"}'


# Cleanup
terraform destroy -auto-approve

