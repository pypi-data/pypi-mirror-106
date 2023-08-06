from datetime import datetime
import pytz
import pickle
import os
import boto3


def sts(role_arn: str, serial_no: str):
    try:
        with open('sts.pickle', 'rb') as handle:
            b = pickle.load(handle)
        is_expired = datetime.utcnow().replace(tzinfo=pytz.utc) < b['Credentials']['Expiration']
        if is_expired is True:
            os.environ["AWS_ACCESS_KEY_ID"] = b['Credentials']['AccessKeyId']
            os.environ["AWS_SECRET_ACCESS_KEY"] = b['Credentials']['SecretAccessKey']
            os.environ["AWS_SESSION_TOKEN"] = b['Credentials']['SessionToken']
            return
    except FileNotFoundError:
        pass
    sts_session = boto3.session.Session()
    mfa = input("MFA: ")
    client = sts_session.client('sts')
    r = client.assume_role(
        RoleArn=role_arn,
        RoleSessionName='marek',
        SerialNumber=serial_no,
        TokenCode=mfa)
    os.environ["AWS_ACCESS_KEY_ID"] = r['Credentials']['AccessKeyId']
    os.environ["AWS_SECRET_ACCESS_KEY"] = r['Credentials']['SecretAccessKey']
    os.environ["AWS_SESSION_TOKEN"] = r['Credentials']['SessionToken']

    with open('sts.pickle', 'wb') as handle:
        pickle.dump(r, handle, protocol=pickle.HIGHEST_PROTOCOL)
