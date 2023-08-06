import boto3


def from_settings(settings):
    return boto3.resource(
            'sqs',
            aws_access_key_id=settings['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=settings['AWS_SECRET_ACCESS_KEY'],
            endpoint_url=settings['AWS_ENDPOINT_URL'],
            region_name=settings['AWS_REGION_NAME'],
            use_ssl=settings['AWS_USE_SSL'],
            verify=settings['AWS_VERIFY'],
        )
