# coding: utf-8

"""
    Rosetta

    Build Once. Integrate Your Blockchain Everywhere.  # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ConstructionCombineRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'network_identifier': 'NetworkIdentifier',
        'unsigned_transaction': 'str',
        'signatures': 'list[Signature]'
    }

    attribute_map = {
        'network_identifier': 'network_identifier',
        'unsigned_transaction': 'unsigned_transaction',
        'signatures': 'signatures'
    }

    def __init__(self, network_identifier=None, unsigned_transaction=None, signatures=None, local_vars_configuration=None):  # noqa: E501
        """ConstructionCombineRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network_identifier = None
        self._unsigned_transaction = None
        self._signatures = None
        self.discriminator = None

        self.network_identifier = network_identifier
        self.unsigned_transaction = unsigned_transaction
        self.signatures = signatures

    @property
    def network_identifier(self):
        """Gets the network_identifier of this ConstructionCombineRequest.  # noqa: E501


        :return: The network_identifier of this ConstructionCombineRequest.  # noqa: E501
        :rtype: NetworkIdentifier
        """
        return self._network_identifier

    @network_identifier.setter
    def network_identifier(self, network_identifier):
        """Sets the network_identifier of this ConstructionCombineRequest.


        :param network_identifier: The network_identifier of this ConstructionCombineRequest.  # noqa: E501
        :type: NetworkIdentifier
        """
        if self.local_vars_configuration.client_side_validation and network_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `network_identifier`, must not be `None`")  # noqa: E501

        self._network_identifier = network_identifier

    @property
    def unsigned_transaction(self):
        """Gets the unsigned_transaction of this ConstructionCombineRequest.  # noqa: E501


        :return: The unsigned_transaction of this ConstructionCombineRequest.  # noqa: E501
        :rtype: str
        """
        return self._unsigned_transaction

    @unsigned_transaction.setter
    def unsigned_transaction(self, unsigned_transaction):
        """Sets the unsigned_transaction of this ConstructionCombineRequest.


        :param unsigned_transaction: The unsigned_transaction of this ConstructionCombineRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unsigned_transaction is None:  # noqa: E501
            raise ValueError("Invalid value for `unsigned_transaction`, must not be `None`")  # noqa: E501

        self._unsigned_transaction = unsigned_transaction

    @property
    def signatures(self):
        """Gets the signatures of this ConstructionCombineRequest.  # noqa: E501


        :return: The signatures of this ConstructionCombineRequest.  # noqa: E501
        :rtype: list[Signature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this ConstructionCombineRequest.


        :param signatures: The signatures of this ConstructionCombineRequest.  # noqa: E501
        :type: list[Signature]
        """
        if self.local_vars_configuration.client_side_validation and signatures is None:  # noqa: E501
            raise ValueError("Invalid value for `signatures`, must not be `None`")  # noqa: E501

        self._signatures = signatures

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConstructionCombineRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstructionCombineRequest):
            return True

        return self.to_dict() != other.to_dict()
