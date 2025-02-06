from aws_cdk import (
    Stack,    
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_notifications as s3_notifications
)
import aws_cdk as cdk
from constructs import Construct
from cdk_aws_lambda_powertools_layer import LambdaPowertoolsLayer


class S3TriggerLambda(Stack):

    def __init__(self, scope: Construct, construct_id: str, domain_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        domain_name = domain_name

        # S3 bucket
        trigger_bucket = s3.Bucket(
            self, "TriggerBucket",
            versioned=True,
            bucket_name=f'trigger-{self.account}-{self.region}',
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            enforce_ssl=True
        )

        powertoolsLayer = LambdaPowertoolsLayer(self, 'PowertoolsLayer')

        # Lambda function
        trigger_lambda = _lambda.Function(
            self, "TriggerLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset("lambda"),
            layers=[powertoolsLayer],
            environment={
                "DOMAIN_NAME": domain_name
            }
        )

        # add rule to bucket to trigger lambda
        trigger_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3_notifications.LambdaDestination(trigger_lambda)
        )


