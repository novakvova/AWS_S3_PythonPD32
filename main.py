import os
import boto3

#print("Сало - це смачно і дуже корисно!")
s3_client = boto3.client('s3') # S3 client
s3_resource = boto3.resource('s3') # S3 resource

response = s3_client.list_buckets() # List all buckets
for bucket in response['Buckets']:
    print(bucket)

response = s3_client.list_objects_v2(Bucket='my-girl-images') # List objects in a bucket
objects = response.get('Contents', [])
print(objects)

#s3_client.download_file("my-girl-images", "dog.jpg", "downloaded_dog.jpg") # Download a file from S3
s3_client.download_file("my-girl-images", "info.txt", "downloaded_info.txt")