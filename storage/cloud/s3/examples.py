import boto3
from botocore.exceptions import ClientError
import config

DEFAULT_BUCKET = 'onesight-test'

s3 = boto3.client(
    's3',
    region_name='ap-northeast-2',
    aws_access_key_id=config.AWS_ACCESS_ID,
    aws_secret_access_key=config.AWS_ACCESS_KEY,
)

s3_resource = boto3.resource(
    's3',
    region_name='ap-northeast-2',
    aws_access_key_id=config.AWS_ACCESS_ID,
    aws_secret_access_key=config.AWS_ACCESS_KEY,
)


def get_all_buckets(client):
    """
    get current account's all buckets.
    :param client: the client
    :return:
    """
    res = client.list_buckets()
    buckets = [bucket['Name'] for bucket in res['Buckets']]
    return buckets


def list_objects(client, bucket=None):
    """
    get point bucket demo objects.
    :param client:
    :param bucket:
    :return:
    """
    if bucket is None:
        bucket = DEFAULT_BUCKET
    res = client.list_objects(
        Bucket=bucket,
        # Delimiter='string',
        EncodingType='url',
        # Marker='string',
        MaxKeys=5,
        # Prefix='string',
    )
    return res


def create_bucket(client, bucket_name):
    res = client.create_bucket(
        ACL='public-read',
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-northeast-2',
        },
    )
    return res


def upload_file(client, bucket, origin_file, target_name):
    res = client.upload_file(
        origin_file, bucket, target_name,
        ExtraArgs={
            'ACL': 'public-read',
            'ContentType': 'image/jpeg'
        }
    )
    return res


def put_object(client, bucket, origin_file, target_name):
    with open(origin_file, 'rb') as f:
        res = client.put_object(
            ACL='public-read',
            Body=f,
            Bucket=bucket,
            ContentType='image/jpeg',
            Key=target_name

        )
        return res


def list_acl(client, bucket):
    res = client.BucketAcl(bucket)
    return res


def head_object(client, bucket, target):
    try:
        res = client.head_object(
            Bucket=bucket,
            Key=target
        )
    except ClientError:
        return None
    else:
        return res


if __name__ == '__main__':
    test_bucket = 'onesight-test'
    # r = create_bucket(s3, 'onesight-test')
    # print(r)

    # r1 = get_all_buckets(s3)
    # print(r1)

    # r = upload_file(
    #     s3,
    #     test_bucket,
    #     'tt.jpg',
    #     'test1.png'
    # )
    # print(r)

    # r = list_objects(s3, bucket=test_bucket)
    # print(r)

    # r = list_acl(s3_resource, bucket=test_bucket)
    # print(r)

    # r = put_object(
    #     s3, bucket=test_bucket,
    #     origin_file='tt.jpg',
    #     target_name='test2.jpg'
    # )
    # print(r)

    # r = head_object(s3, test_bucket, 'test1.png')
    # print(r)
