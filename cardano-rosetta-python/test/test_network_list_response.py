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
from openapi_client.models.network_list_response import NetworkListResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestNetworkListResponse(unittest.TestCase):
    """NetworkListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.network_list_response.NetworkListResponse()  # noqa: E501
        if include_optional :
            return NetworkListResponse(
                network_identifiers = [
                    openapi_client.models.network_identifier.NetworkIdentifier(
                        blockchain = 'bitcoin', 
                        network = 'mainnet', 
                        sub_network_identifier = openapi_client.models.sub_network_identifier.SubNetworkIdentifier(
                            network = 'shard 1', 
                            metadata = {"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"}, ), )
                    ]
            )
        else :
            return NetworkListResponse(
                network_identifiers = [
                    openapi_client.models.network_identifier.NetworkIdentifier(
                        blockchain = 'bitcoin', 
                        network = 'mainnet', 
                        sub_network_identifier = openapi_client.models.sub_network_identifier.SubNetworkIdentifier(
                            network = 'shard 1', 
                            metadata = {"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"}, ), )
                    ],
        )

    def testNetworkListResponse(self):
        """Test NetworkListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
