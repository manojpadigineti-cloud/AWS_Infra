import boto3

s3 = boto3.client('s3')

bucket_name = input('Enter_the_source_bucket_name: ')
object_name = input(f"Enter_the_object_name_of: {bucket_name}: ")
local_file = input(f"Provide_the_local_file_name_of:{bucket_name} - {object_name}: ")
full_local_name = (f"{local_file}-{object_name}")
s3.download_file(bucket_name, object_name, full_local_name)
