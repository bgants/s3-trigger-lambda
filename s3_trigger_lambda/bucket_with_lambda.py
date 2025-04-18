from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_s3_notifications as s3n,
)
from cdk_aws_lambda_powertools_layer import LambdaPowertoolsLayer
from constructs import Construct
import aws_cdk as cdk


"""
    This CDK stack creates an S3 bucket and a Lambda function that is triggered
"""


class BucketWithLambda(Construct):
    def __init__(
        self, scope: Construct, id: str, domain_name: str
    ) -> None:
        super().__init__(scope, id)

        # Get the account ID from the stack
        account_id = Stack.of(self).account

        # Create an S3 bucket
        self.bucket = s3.Bucket(
            self,
            "S3TriggerLambdaBucket",  # Provide a unique id for the bucket
            bucket_name=f"s3-trigger-lambda-{account_id}",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            # Could be dangerous in production, but useful for testing
            auto_delete_objects=True,
        )

        power_tools_layer = LambdaPowertoolsLayer(self, "PowerToolsLayer")

        # Create a Lambda function
        self.lambda_fn = _lambda.Function(
            self,
            f"s3_trigger_lambda-{account_id}",
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.from_asset("lambda"),
            handler="s3_trigger_lambda.handler",
            layers=[power_tools_layer],  # Add the Lambda Powertools layer
        )

        self.bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(self.lambda_fn)
        )
