import json
from aws_lambda_powertools import Logger

logger = Logger()


@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    # Log the event
    logger.info(f"Received event from S3 bucket: {json.dumps(event)}")

    try:
        record = event["Records"][0]
        s3_info = record["s3"]
        bucket_name = s3_info["bucket"]["name"]
        object_key = s3_info["object"]["key"]
        object_size = s3_info["object"]["size"]
        logger.info(f"Bucket: {bucket_name}, Key: {object_key}, Size: {object_size}")
    except KeyError as e:
        logger.error(f"KeyError: {e}")
        return {"statusCode": 400, "body": json.dumps("Invalid event format")}
