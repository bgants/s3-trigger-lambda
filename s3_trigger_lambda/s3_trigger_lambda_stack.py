from aws_cdk import (
    Stack,
)
from constructs import Construct

from s3_trigger_lambda.bucket_with_lambda import BucketWithLambda
import aws_cdk as cdk

"""
    This CDK stack creates an S3 bucket and a Lambda function that is triggered
    when an object is created in the bucket. The stack uses a custom construct
    to encapsulate the logic for creating the S3 bucket and the Lambda function.
    The stack also outputs the name of the S3 bucket.
"""


class S3TriggerLambdaStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        domain_name: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create custom construct for S3 bucket with Lambda trigger
        bucket_lambda = BucketWithLambda(
            self, "BucketWithLambda", domain_name
        )

        # Output the bucket name
        self.output_bucket_name = cdk.CfnOutput(
            self,
            "BucketName",
            value=bucket_lambda.bucket.bucket_name,
            description="The name of the S3 bucket",
        )
