import boto3
from botocore.exceptions import ClientError
import json
import base64


AWS_AccountId = '651543716756'
Role_Name = 'ec2-ssm'

session = boto3.Session()
sts = session.client("sts")
response = sts.assume_role(
    RoleArn = "arn:aws:iam::651543716756:role/ec2-ssm",
    RoleSessionName="ec2-ssm"
)

def get_secret():

    secret_name = "anilkarnam/weather/key"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
            return secret 
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret
