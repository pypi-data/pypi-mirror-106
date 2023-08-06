
from google.cloud import storage
import os

class Kraken_gstorage:
    """ Library to access google storage api. Requires key.json file. 

    LONG DESCRIPTION OF CLASS

    ATTRIBUTES:
    ATTRIBUTE1(type): Description
    ATTRIBUTE2(type): Description

    Reference from : https://cloud.google.com/storage/docs/listing-objects#storage-list-objects-python
    """

    def __init__(self, key_location = 'key.json', bucket_name = 'krkn'):
        # Initialize storage objecti with account key and bucket name

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_location

        self.bucket = bucket_name
        



    def get(self, source_blob_name):
        """Downloads a blob from the bucket."""
        # source_blob_name = the path and name to the file:
        # 'v1/test/test.json'


        storage_client = storage.Client()

        bucket = storage_client.bucket(self.bucket)
        blob = bucket.blob(source_blob_name)
        content = blob.download_as_text()

        return content




    def post(self, name, record):
        """Uploads a file to the bucket."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        
        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket)
        blob = bucket.blob(name)

        blob.upload_from_string(record)


        return 
        

    def delete(self, bucket_name, blob_name):
        """Deletes a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()

        return



    def create_bucket_class_location(self, bucket_name):
        """Create a new bucket in specific location with storage class"""
        # bucket_name = "your-new-bucket-name"

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)
        bucket.storage_class = "COLDLINE"
        new_bucket = storage_client.create_bucket(bucket, location="us")

        print(
            "Created bucket {} in {} with storage class {}".format(
                new_bucket.name, new_bucket.location, new_bucket.storage_class
            )
        )
        return new_bucket

        
    def list(self, directory = None):
        """Lists all the blobs in the given directory."""
        # bucket_name = "your-bucket-name"

        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(self.bucket, prefix = directory)

        for blob in blobs:
            print(blob.name)
