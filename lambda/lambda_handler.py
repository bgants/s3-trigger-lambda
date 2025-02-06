import json
import os
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    logger.info(event)
    msg = os.getenv("DOMAIN_NAME", "example.com")
    logger.info(f"Domain name: {msg}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda!"
        }),
    }


