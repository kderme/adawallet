# coding: utf-8

"""
    Rosetta

    Build Once. Integrate Your Blockchain Everywhere.  # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.account_identifier import AccountIdentifier  # noqa: E501
from openapi_client.rest import ApiException

class TestAccountIdentifier(unittest.TestCase):
    """AccountIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountIdentifier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.account_identifier.AccountIdentifier()  # noqa: E501
        if include_optional :
            return AccountIdentifier(
                address = '0x3a065000ab4183c6bf581dc1e55a605455fc6d61', 
                sub_account = openapi_client.models.sub_account_identifier.SubAccountIdentifier(
                    address = '0x6b175474e89094c44da98b954eedeac495271d0f', 
                    metadata = openapi_client.models.metadata.metadata(), ), 
                metadata = None
            )
        else :
            return AccountIdentifier(
                address = '0x3a065000ab4183c6bf581dc1e55a605455fc6d61',
        )

    def testAccountIdentifier(self):
        """Test AccountIdentifier"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
