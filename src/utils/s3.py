import os
import boto3
import uuid
import base64
from botocore.exceptions import ClientError


def put_item_s3(
    file: str,
    file_name: str,
    content_type: str,
    ticket_id: int,
    comentario_id: int | None
):
    print("put_item_s3")

    s3 = boto3.client('s3')
    bucket_name = os.getenv("BUCKET_NAME")
    keys = []

    binary_data = base64.b64decode(file)
    str_uuid = str(uuid.uuid4())

    key = f"{ticket_id}/"

    if comentario_id:
        key += f"{comentario_id}/"

    key += f"{str_uuid}-{file_name}"

    print(bucket_name, key, binary_data, content_type)

    s3.put_object(Bucket=bucket_name,
                  Key=key,
                  Body=binary_data,
                  ContentType=content_type,)

    return key


def create_presigned_url(bucket_name, object_name, expiration=3600):
    print('create_presigned_url')
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(e)
        return None
    return response
