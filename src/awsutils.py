import boto3
import json
import base64
from botocore.exceptions import ProfileNotFound
from botocore.exceptions import ClientError

from config import REGION_NAME

REGION_NAME = REGION_NAME

class Secret(object):
    def __init__(self: str, secret: str, bucket: str, alias: str, profile: str, name: str) -> None:
        self.secret = secret
        self.bucket = bucket
        self.alias = alias
        self.profile = profile
        self.name = name


    def _set_profile(self) -> None:
        print(f'Attempting to set boto3 profile to: {self.profile}')
        try:
            boto3.setup_default_session(profile_name=self.profile)
            print('Success!') 
        except ProfileNotFound as error:
            print(error)


    def _encrypt_secret(self) -> bytes:
        ## can change this on the fly depending on requirements
        secret_list = self.secret.split(",")
        secret_dict = dict(id=secret_list[0], secret=secret_list[1])
        print(f'Encrypting secret with the KMS alias: {self.alias}')
        try:
            client = boto3.client('kms', region_name=REGION_NAME)
            cipher = client.encrypt(KeyId=f'alias/{self.alias}', Plaintext=json.dumps(secret_dict))[u'CiphertextBlob']
            return base64.b64encode(cipher)
        except ClientError as error:
            print(error)
        

    def upload_secret(self):
        self._set_profile()
        client = boto3.client('s3', region_name=REGION_NAME)
        print(f'Attempting to upload secret: <{self.secret}> to the <{self.bucket}> s3 bucket with name: <{self.name}>')
        try:
            client.put_object(Body=self._encrypt_secret(), Bucket=self.bucket, Key=self.name)
            print('Success!')
        except ClientError as error:
            print(error)

