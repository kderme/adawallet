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
from openapi_client.models.construction_preprocess_request import ConstructionPreprocessRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestConstructionPreprocessRequest(unittest.TestCase):
    """ConstructionPreprocessRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConstructionPreprocessRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.construction_preprocess_request.ConstructionPreprocessRequest()  # noqa: E501
        if include_optional :
            return ConstructionPreprocessRequest(
                network_identifier = openapi_client.models.network_identifier.NetworkIdentifier(
                    blockchain = 'bitcoin', 
                    network = 'mainnet', 
                    sub_network_identifier = openapi_client.models.sub_network_identifier.SubNetworkIdentifier(
                        network = 'shard 1', 
                        metadata = {"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"}, ), ), 
                operations = [
                    openapi_client.models.operation.Operation(
                        operation_identifier = openapi_client.models.operation_identifier.OperationIdentifier(
                            index = 5, 
                            network_index = 0, ), 
                        related_operations = [{"index":1},{"index":2}], 
                        type = 'Transfer', 
                        status = 'Reverted', 
                        account = openapi_client.models.account_identifier.AccountIdentifier(
                            address = '0x3a065000ab4183c6bf581dc1e55a605455fc6d61', 
                            sub_account = openapi_client.models.sub_account_identifier.SubAccountIdentifier(
                                address = '0x6b175474e89094c44da98b954eedeac495271d0f', 
                                metadata = openapi_client.models.metadata.metadata(), ), 
                            metadata = openapi_client.models.metadata.metadata(), ), 
                        amount = openapi_client.models.amount.Amount(
                            value = '1238089899992', 
                            currency = openapi_client.models.currency.Currency(
                                symbol = 'BTC', 
                                decimals = 8, 
                                metadata = {"Issuer":"Satoshi"}, ), 
                            metadata = openapi_client.models.metadata.metadata(), ), 
                        coin_change = openapi_client.models.coin_change.CoinChange(
                            coin_identifier = openapi_client.models.coin_identifier.CoinIdentifier(
                                identifier = '0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1', ), 
                            coin_action = 'coin_created', ), 
                        metadata = openapi_client.models.operation_metadata.OperationMetadata(
                            withdrawal_amount = openapi_client.models.amount.Amount(
                                value = '1238089899992', 
                                currency = openapi_client.models.currency.Currency(
                                    symbol = 'BTC', 
                                    decimals = 8, ), ), 
                            deposit_amount = openapi_client.models.amount.Amount(
                                value = '1238089899992', 
                                currency = openapi_client.models.currency.Currency(
                                    symbol = 'BTC', 
                                    decimals = 8, ), ), 
                            staking_credential = openapi_client.models.public_key.PublicKey(
                                hex_bytes = '0', 
                                curve_type = 'secp256k1', ), 
                            pool_key_hash = '0', ), )
                    ], 
                metadata = openapi_client.models.construction_preprocess_request_metadata.ConstructionPreprocessRequest_metadata(
                    relative_ttl = 1.337, ), 
                max_fee = [
                    openapi_client.models.amount.Amount(
                        value = '1238089899992', 
                        currency = openapi_client.models.currency.Currency(
                            symbol = 'BTC', 
                            decimals = 8, 
                            metadata = {"Issuer":"Satoshi"}, ), 
                        metadata = openapi_client.models.metadata.metadata(), )
                    ], 
                suggested_fee_multiplier = 0
            )
        else :
            return ConstructionPreprocessRequest(
                network_identifier = openapi_client.models.network_identifier.NetworkIdentifier(
                    blockchain = 'bitcoin', 
                    network = 'mainnet', 
                    sub_network_identifier = openapi_client.models.sub_network_identifier.SubNetworkIdentifier(
                        network = 'shard 1', 
                        metadata = {"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"}, ), ),
                operations = [
                    openapi_client.models.operation.Operation(
                        operation_identifier = openapi_client.models.operation_identifier.OperationIdentifier(
                            index = 5, 
                            network_index = 0, ), 
                        related_operations = [{"index":1},{"index":2}], 
                        type = 'Transfer', 
                        status = 'Reverted', 
                        account = openapi_client.models.account_identifier.AccountIdentifier(
                            address = '0x3a065000ab4183c6bf581dc1e55a605455fc6d61', 
                            sub_account = openapi_client.models.sub_account_identifier.SubAccountIdentifier(
                                address = '0x6b175474e89094c44da98b954eedeac495271d0f', 
                                metadata = openapi_client.models.metadata.metadata(), ), 
                            metadata = openapi_client.models.metadata.metadata(), ), 
                        amount = openapi_client.models.amount.Amount(
                            value = '1238089899992', 
                            currency = openapi_client.models.currency.Currency(
                                symbol = 'BTC', 
                                decimals = 8, 
                                metadata = {"Issuer":"Satoshi"}, ), 
                            metadata = openapi_client.models.metadata.metadata(), ), 
                        coin_change = openapi_client.models.coin_change.CoinChange(
                            coin_identifier = openapi_client.models.coin_identifier.CoinIdentifier(
                                identifier = '0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1', ), 
                            coin_action = 'coin_created', ), 
                        metadata = openapi_client.models.operation_metadata.OperationMetadata(
                            withdrawal_amount = openapi_client.models.amount.Amount(
                                value = '1238089899992', 
                                currency = openapi_client.models.currency.Currency(
                                    symbol = 'BTC', 
                                    decimals = 8, ), ), 
                            deposit_amount = openapi_client.models.amount.Amount(
                                value = '1238089899992', 
                                currency = openapi_client.models.currency.Currency(
                                    symbol = 'BTC', 
                                    decimals = 8, ), ), 
                            staking_credential = openapi_client.models.public_key.PublicKey(
                                hex_bytes = '0', 
                                curve_type = 'secp256k1', ), 
                            pool_key_hash = '0', ), )
                    ],
        )

    def testConstructionPreprocessRequest(self):
        """Test ConstructionPreprocessRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
