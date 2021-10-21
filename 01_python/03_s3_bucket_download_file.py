##
## Author : Bhaskar Varadaraju
## A Python3 program to Download an existing file from AWS S3
##       
## ******  IMPORTANT : Set below before executing ******
##  export AWS_ACCESS_KEY_ID=<Your_Aws_KeyId>
##  export AWS_SECRET_ACCESS_KEY=<Your_Aws_Secret_Access_Key>
##
import boto3
import os

""" Input:
export S3_DOWNLOAD_FILENAME='01_shell.zip'
export S3_DOWNLOAD_LOCALNAME='/tmp/01_shell_local.zip'
export S3_BUCKET_NAME='<your_s3_bucket_name>'
"""

def download_from_aws_s3(bucket, remote_file, local_file):
    print("Downloading file : ", remote_file)
    s3_client = boto3.client('s3',
        region_name='ap-south-1',
    )
    s3_client.download_file(bucket, remote_file, local_file)

s3_file_name      = os.environ.get('S3_DOWNLOAD_FILENAME')
s3_local_filepath = os.environ.get('S3_DOWNLOAD_LOCALNAME')
s3_bucket_name    = os.environ.get('S3_BUCKET_NAME')

download_from_aws_s3( s3_bucket_name, s3_file_name, s3_local_filepath)

