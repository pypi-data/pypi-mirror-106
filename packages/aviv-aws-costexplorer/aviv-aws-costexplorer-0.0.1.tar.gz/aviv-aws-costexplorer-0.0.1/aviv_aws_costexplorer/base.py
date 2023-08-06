import os
import botocore
import boto3

AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION', 'eu-west-1')

class AWSClient():
    __sts: botocore.client.BaseClient = None
    __client: botocore.client.BaseClient = None
    __account_id: str = None

    def __init__(self, account_id: str=None) -> None:
        if account_id:
            self.account_id = account_id

    @property
    def account_id(self) -> str:
        if not self.__account_id:
            self.account_id = self.sts.get_caller_identity().get('Account')
        return self.__account_id

    @account_id.setter
    def account_id(self, id: str):
        self.__account_id = id

    @property
    def sts(self) -> botocore.client.BaseClient:
        if not self.__sts:
            self.__sts = boto3.client('sts')
        return self.__sts

    @property
    def client(self) -> botocore.client.BaseClient:
        if not self.__client:
            self.client = boto3.client('ce')
        return self.__client

    @client.setter
    def client(self, val):
        self.__client = val

    def assume_role_client(self, role: str, account_id: str=None, client_type: str='ce'):
        if account_id:
            self.account_id = account_id
        stsrole = self.sts.assume_role(
            RoleArn=f"arn:aws:iam::{self.account_id}:role/{role}",
            RoleSessionName='CostReporter'
        )
        client = boto3.client(
            client_type,
            region_name=AWS_DEFAULT_REGION,
            aws_access_key_id=stsrole["Credentials"]["AccessKeyId"],
            aws_secret_access_key=stsrole["Credentials"]["SecretAccessKey"],
            aws_session_token=stsrole["Credentials"]["SessionToken"]
        )
        return client
