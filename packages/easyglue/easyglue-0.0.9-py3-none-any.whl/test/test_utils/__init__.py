import boto3

s3_client = boto3.client('s3', region_name="eu-west-1")
ddb_client = boto3.client('dynamodb', region_name="eu-west-1")
glue_client = boto3.client('glue', region_name="eu-west-1")
secrets_client = boto3.client('secretsmanager', region_name="eu-west-1")


def delete_all_s3_objects(bucket: str, prefix: str):
    """
    Deletes all s3 objects in the given bucket and prefix
    :param bucket: S3 bucket
    :param prefix: S3 prefix
    :return: None
    """
    objects = list_all_objects(bucket, prefix)
    if objects:
        mapped_objects = list(map(lambda o: {'Key': o}, objects))
        s3_client.delete_objects(Bucket="bertolb", Delete={'Objects': mapped_objects})


def list_all_objects(bucket_name: str, prefix: str) -> list:
    """
    Lists all s3 objects in the given bucket and prefix
    :param bucket_name: S3 bucket
    :param prefix: S3 prefix
    :return: List of object keys
    """
    kwargs = {'Bucket': bucket_name, 'Prefix': prefix}
    object_list = []

    while True:
        resp = s3_client.list_objects_v2(**kwargs)
        object_list += list(map(lambda x: x.get('Key', ''), resp.get('Contents', [])))
        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break

    return object_list
