import json
import boto3
import logging
import os
from datetime import datetime

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function to restart EC2 instance and send SNS notification
    Triggered by Sumo Logic alert for slow API responses
    """
    
    # Initialize AWS clients
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    
    # Get environment variables
    instance_id = os.environ.get('INSTANCE_ID')
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    
    try:
        # Log the incoming alert
        logger.info(f"Received Sumo Logic alert: {json.dumps(event)}")
        
        # Restart EC2 instance
        logger.info(f"Restarting EC2 instance: {instance_id}")
        ec2.reboot_instances(InstanceIds=[instance_id])
        
        # Prepare notification message
        message = {
            "timestamp": datetime.now().isoformat(),
            "alert": "Slow API response detected",
            "action": "EC2 instance restarted",
            "instance_id": instance_id,
            "status": "SUCCESS"
        }
        
        # Send SNS notification
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(message, indent=2),
            Subject="Automated EC2 Restart - Performance Issue"
        )
        
        logger.info("EC2 restart and notification completed successfully")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Instance restarted successfully',
                'instance_id': instance_id
            })
        }
        
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error: {error_msg}")
        
        # Send error notification
        try:
            error_message = {
                "timestamp": datetime.now().isoformat(),
                "alert": "Automation failure",
                "error": error_msg,
                "status": "FAILED"
            }
            
            sns.publish(
                TopicArn=sns_topic_arn,
                Message=json.dumps(error_message, indent=2),
                Subject="ERROR - Automated EC2 Restart Failed"
            )
        except:
            pass
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error restarting instance',
                'error': error_msg
            })
        }