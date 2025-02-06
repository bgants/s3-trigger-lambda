#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_trigger_lambda.s3_trigger_lambda_stack import S3TriggerLambda


account = os.getenv("AWS_ACCOUNT_ID")
primary_region = os.getenv("AWS_PRIMARY_REGION")
domain_name = os.getenv("AWS_DOMAIN_NAME")
primary_environment = cdk.Environment(account=account, region=primary_region)

app = cdk.App()
S3TriggerLambda(app, "S3TriggerLambda", env=primary_environment, domain_name=domain_name)
app.synth()
