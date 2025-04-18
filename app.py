#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_trigger_lambda.s3_trigger_lambda_stack import S3TriggerLambdaStack

"""
    This CDK app is an example of using a composition pattern to create a stack
    that contains an S3 bucket and a Lambda function.
    The S3 bucket is used to trigger the Lambda function when an object is created.   
"""

# Set up environment variables
account = os.getenv("AWS_ACCOUNT_ID")
primary_region = os.getenv("AWS_PRIMARY_REGION")
domain_name = os.getenv("AWS_DOMAIN_NAME", "default-domain-name")

primary_environment = cdk.Environment(account=account, region=primary_region)

app = cdk.App()
S3TriggerLambdaStack(
    app, "S3TriggerLambdaStack", domain_name=domain_name, env=primary_environment
)
app.synth()
