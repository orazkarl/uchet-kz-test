import logging

from aiobotocore.session import get_session


class S3Service(object):

    def __init__(self, aws_access_key_id, aws_secret_access_key, region, *args, **kwargs):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region = region

    async def upload_file(self, fileobject, bucket, key):
        session = get_session()
        async with session.create_client(
                's3',
                region_name=self.region,
                aws_secret_access_key=self.aws_secret_access_key,
                aws_access_key_id=self.aws_access_key_id
        ) as client:
            file_upload_response = await client.put_object(ACL="", Bucket=bucket, Key=key, Body=fileobject)
            if file_upload_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                logging.info(f"File uploaded path : https://{bucket}.s3.{self.region}.amazonaws.com/{key}")
                return True
        return False
