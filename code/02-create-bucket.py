""" 02 - Crear un bucket en S3 """

import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='iot-cloud-bucket-fa01')




