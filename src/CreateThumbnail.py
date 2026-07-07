"""
This source code was provided as part of an official AWS Skill Builder hands-on lab.

The purpose of including this file in this repository is to document the complete implementation of the project and demonstrate the deployment and integration of the AWS services used during the lab.

Original business logic and implementation were created by Amazon Web Services (AWS).
"""

import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
import json

s3_client = boto3.client("s3")
s3 = boto3.resource("s3")


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((128, 128))
        image.save(resized_path)


def handler(event, context):
    for record in event["Records"]:
        #payload = record["body"]
        bucket = record['s3']['bucket']['name']
        print(bucket)
        key = record['s3']['object']['key']
        print(key)

        #download_path = "/tmp/{}{}".format(uuid.uuid4(), key.split("/")[-1])
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        print (download_path)
        #upload_path = "/tmp/resized-{}".format(key.split("/")[-1])
        #download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/resized-{}'.format(key)
        print (upload_path)
        s3_client.download_file(bucket, key, download_path)
        resize_image(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)

        #s3_client.download_file(bucket, key, download_path)
        #resize_image(download_path, upload_path)
        #s3.meta.client.upload_file(
        #    upload_path, bucket, "thumbnail/Thumbnail-" + key.split("/")[-1]
        #)
