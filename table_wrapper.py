"""
Manage tables
"""
import boto3
import logging
import os
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class Table():
    def __init__(self, name):
        #TODO
        pass

    def set(self, key, object):
        #TODO
        pass

    def get(self, key):
        #TODO
        pass

    def random_get(self):
        pass

# Yoinked from AWS sample
# use our local AWS config file instead
os.environ["AWS_CONFIG_FILE"] = os.path.join(os.path.curdir, "aws_test.conf")
logging.info("config file path: ", os.environ["AWS_CONFIG_FILE"])
s3_resource = boto3.resource('s3')

def get_s3():
    """Get a Boto 3 S3 resource with a default region"""
    global s3_resource
    return s3_resource

class S3EventTable(Table):

    def __init__(self, name):
        s3 = get_s3()
        self.bucket = None

        # test if bucket exists
        try:
            s3.meta.client.head_bucket(Bucket=name)
            logger.info(f"Bucket {name} exists")
            self.bucket = s3.Bucket(name)
        except ClientError:
            logger.info(f"Bucket: {name} does not exist yet... creating")
            # doesn't exist yet, create the bucket instead
            try:
                self.bucket = s3.create_bucket(Bucket=name)
                self.bucket.wait_until_exists()
                logger.info(f"Created new bucket: {name}")
            except ClientError as e:
                logger.exception(f"Exception creating new bucket: {name}")
                logger.exception(f"Exception: {e}")
                raise e

    def set(self, key, data):
        obj = self.bucket.Object(key)
        obj.put(Body=data)
        obj.wait_until_exists()
        logger.info(f"Put obj {key} to bucket")

    def get(self, key):
        try:
            data = self.bucket.Object(key).get()['Body'].read()
            logger.info(f"Got object {key} from bucket")
        except ClientError:
            logger.exception(f"Couldn't get object {key} from bucket")
            raise
        return data
    def random_get(self):
        pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(os.environ['AWS_CONFIG_FILE'])
    s3 = get_s3()
    # 1. test AWS credentials
    for bucket in s3.buckets.all():
        print(bucket.name)

    # 2. test set/get object
    t = S3EventTable("ericencountertable")
    t.set("t1", "This test event pops up")
    print(t.get("t1"))
