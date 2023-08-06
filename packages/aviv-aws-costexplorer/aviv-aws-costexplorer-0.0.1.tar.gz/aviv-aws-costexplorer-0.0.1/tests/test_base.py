import pytest
import botocore
from aviv_aws_costexplorer import base


@pytest.fixture
def aacli():
    return base.AWSClient('42')


def test_awsclient(aacli):
    assert isinstance(aacli, base.AWSClient)
    assert isinstance(aacli.account_id, str)
    assert aacli.account_id == '42'

    assert isinstance(aacli.sts, botocore.client.BaseClient)
    assert isinstance(aacli.client, botocore.client.BaseClient)


# can ONLY test this with pre-defined AWS IAM Role deployed
# def test_assumerole():
#     aacli = base.AWSClient()
#     cecli = aacli.assume_role_client()
#     assert isinstance(cecli, botocore.client.BaseClient)
