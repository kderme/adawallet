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
from openapi_client.models.utxo import Utxo  # noqa: E501
from openapi_client.rest import ApiException

class TestUtxo(unittest.TestCase):
    """Utxo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Utxo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.utxo.Utxo()  # noqa: E501
        if include_optional :
            return Utxo(
                value = '0', 
                index = 1.337, 
                transaction_hash = '0'
            )
        else :
            return Utxo(
                value = '0',
                index = 1.337,
                transaction_hash = '0',
        )

    def testUtxo(self):
        """Test Utxo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
