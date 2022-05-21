import json
import sys
import boto3

bucket = 'email-spam-dump'
key = 'spammers.json'
aws_access_key_id = ""
aws_secret_access_key = ""

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

def get_local_spammmers_json():
    with open(key, 'wb') as f:
        s3.download_fileobj(bucket, key, f)
l

def upload_to_aws(local_file, bucket, s3_file):

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False

def add_to_json():
    if len(sys.argv) == 1:
        print("no new email to add")
    else:
        print(f'Adding email address: {sys.argv[1]}')
        with open(key) as f:
            json_load = json.load(f)
            json_load['email_addresses'].append(sys.argv[1])
            json_dump = json.dumps(json_load)
            print(json_dump)
        with open(key, "w") as f:
            f.write(json_dump)
        upload_to_aws(key, bucket, key)


get_local_spammmers_json()
add_to_json()

