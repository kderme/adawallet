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


class ConstructionMetadataRequest(object):
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
        'options': 'ConstructionMetadataRequestOptions',
        'public_keys': 'list[PublicKey]'
    }

    attribute_map = {
        'network_identifier': 'network_identifier',
        'options': 'options',
        'public_keys': 'public_keys'
    }

    def __init__(self, network_identifier=None, options=None, public_keys=None, local_vars_configuration=None):  # noqa: E501
        """ConstructionMetadataRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network_identifier = None
        self._options = None
        self._public_keys = None
        self.discriminator = None

        self.network_identifier = network_identifier
        self.options = options
        if public_keys is not None:
            self.public_keys = public_keys

    @property
    def network_identifier(self):
        """Gets the network_identifier of this ConstructionMetadataRequest.  # noqa: E501


        :return: The network_identifier of this ConstructionMetadataRequest.  # noqa: E501
        :rtype: NetworkIdentifier
        """
        return self._network_identifier

    @network_identifier.setter
    def network_identifier(self, network_identifier):
        """Sets the network_identifier of this ConstructionMetadataRequest.


        :param network_identifier: The network_identifier of this ConstructionMetadataRequest.  # noqa: E501
        :type: NetworkIdentifier
        """
        if self.local_vars_configuration.client_side_validation and network_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `network_identifier`, must not be `None`")  # noqa: E501

        self._network_identifier = network_identifier

    @property
    def options(self):
        """Gets the options of this ConstructionMetadataRequest.  # noqa: E501


        :return: The options of this ConstructionMetadataRequest.  # noqa: E501
        :rtype: ConstructionMetadataRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ConstructionMetadataRequest.


        :param options: The options of this ConstructionMetadataRequest.  # noqa: E501
        :type: ConstructionMetadataRequestOptions
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def public_keys(self):
        """Gets the public_keys of this ConstructionMetadataRequest.  # noqa: E501


        :return: The public_keys of this ConstructionMetadataRequest.  # noqa: E501
        :rtype: list[PublicKey]
        """
        return self._public_keys

    @public_keys.setter
    def public_keys(self, public_keys):
        """Sets the public_keys of this ConstructionMetadataRequest.


        :param public_keys: The public_keys of this ConstructionMetadataRequest.  # noqa: E501
        :type: list[PublicKey]
        """

        self._public_keys = public_keys

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
        if not isinstance(other, ConstructionMetadataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstructionMetadataRequest):
            return True

        return self.to_dict() != other.to_dict()
