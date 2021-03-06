"""
Manage tables.
Hash table for testing + AWS table for use
"""
import random
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
        """
        :return: object at key
        """
        pass

    def keys(self):
        """
        :return: list of all valid keys
        """
        pass

    def random_get(self):
        """
        :return: key, value
        """
        pass


class TestingTable(Table):
    def __init__(self, name):
        self.t = {}

    def set(self, key, object):
        self.t[key] = object

    def get(self, key):
        return self.t.get(key)

    def keys(self):
        return self.t.keys()

    def random_get(self):
        k = random.choice(list(self.t.keys()))
        return k, self.get(k)

# Yoinked from AWS sample
# use our local AWS config file instead
os.environ["AWS_CONFIG_FILE"] = os.path.join(os.path.curdir, "aws.conf")
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
        self.bucket_name = name

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
            return None
        return data.decode("utf-8")

    def keys(self):
        """ latest 1000 keys, todo cache?"""
        s3 = get_s3()
        resp = s3.meta.client.list_objects(Bucket=self.bucket_name)
        keys = [k['Key'] for k in resp['Contents']]
        return keys

    def random_get(self):
        choice = random.choice(self.keys())
        logger.info(f"chose random object {choice} from bucket")
        return choice, self.get(choice)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(os.environ['AWS_CONFIG_FILE'])
    s3 = get_s3()
    # 1. test AWS credentials
    print("my buckets: ")
    for bucket in s3.buckets.all():
        print(bucket.name)
    print(" ")

    # 2. test set/get object
    t = S3EventTable("andyemptybucket")
    t.set("t1", "This test event pops up")
    t.set("t2", "This other test event")
    print(t.get("t1"))
    print(t.keys())
    print(t.random_get())

    # 3. test local table
    t2 = TestingTable('fa')
    t2.set("a", 1)
    t2.set("c", 2)
    t2.set("b", 3)

    print("get C: " , t2.get("c"))
    print("get rand: " , t2.random_get())
