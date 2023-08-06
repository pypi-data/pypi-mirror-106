from miquido_sts import sts


def assume(role_arn: str, serial_no: str):
    sts.sts(role_arn, serial_no)
