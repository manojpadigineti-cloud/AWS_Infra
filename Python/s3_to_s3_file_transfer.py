import boto3
# s3 = boto3.resource('s3')

# s3.meta.client.copy(copy_source, 'dest-bucket-s3-0102', 'dest-argo.jpg')

c = boto3.client('s3')
copy_source = {
    'Bucket': 'aws-bucket-90901',
    'Key': 'ArgoCD_Certificate.jpg'
}
c.copy_object(CopySource=copy_source, Bucket="dest-bucket-s3-0102", Key='test-argo.jpg')

