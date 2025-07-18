# SRE Monitoring & Automation
Monitors API response times and automatically restarts EC2 instances when performance degrades.


#!/bin/bash

zip lambda_function.zip lambda_function.py
mv lambda_function.zip terraform/

# 2. Deploy
cd terraform
terraform init
terraform apply -auto-approve

# 3. Get webhook URL for Sumo Logic

terraform output lambda_function_url


sumo_logic_query.txt - Query for slow API detection
lambda_function.py - EC2 restart automation
terraform/ - AWS infrastructure deployment

# Sumo Logic Setup

Use the query from sumo_logic_query.txt and set webhook to the Lambda URL output.

# Test

#!/bin/bash

curl -X POST "your-lambda-url" -d '{"test": true}'

# Cleanup
terraform destroy -auto-approve
