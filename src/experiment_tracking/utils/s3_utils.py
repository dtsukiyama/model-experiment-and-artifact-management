import boto3


def list_s3_objects(bucket_name, prefix=""):
    """
    Lists objects in an S3 bucket.
    :param bucket_name: Name of the S3 bucket.
    :param prefix: Prefix for filtering objects.
    """
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    return [obj["Key"] for obj in response.get("Contents", [])]
