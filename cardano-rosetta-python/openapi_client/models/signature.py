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


class Signature(object):
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
        'signing_payload': 'SigningPayload',
        'public_key': 'PublicKey',
        'signature_type': 'SignatureType',
        'hex_bytes': 'str'
    }

    attribute_map = {
        'signing_payload': 'signing_payload',
        'public_key': 'public_key',
        'signature_type': 'signature_type',
        'hex_bytes': 'hex_bytes'
    }

    def __init__(self, signing_payload=None, public_key=None, signature_type=None, hex_bytes=None, local_vars_configuration=None):  # noqa: E501
        """Signature - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signing_payload = None
        self._public_key = None
        self._signature_type = None
        self._hex_bytes = None
        self.discriminator = None

        self.signing_payload = signing_payload
        self.public_key = public_key
        self.signature_type = signature_type
        self.hex_bytes = hex_bytes

    @property
    def signing_payload(self):
        """Gets the signing_payload of this Signature.  # noqa: E501


        :return: The signing_payload of this Signature.  # noqa: E501
        :rtype: SigningPayload
        """
        return self._signing_payload

    @signing_payload.setter
    def signing_payload(self, signing_payload):
        """Sets the signing_payload of this Signature.


        :param signing_payload: The signing_payload of this Signature.  # noqa: E501
        :type: SigningPayload
        """
        if self.local_vars_configuration.client_side_validation and signing_payload is None:  # noqa: E501
            raise ValueError("Invalid value for `signing_payload`, must not be `None`")  # noqa: E501

        self._signing_payload = signing_payload

    @property
    def public_key(self):
        """Gets the public_key of this Signature.  # noqa: E501


        :return: The public_key of this Signature.  # noqa: E501
        :rtype: PublicKey
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Signature.


        :param public_key: The public_key of this Signature.  # noqa: E501
        :type: PublicKey
        """
        if self.local_vars_configuration.client_side_validation and public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def signature_type(self):
        """Gets the signature_type of this Signature.  # noqa: E501


        :return: The signature_type of this Signature.  # noqa: E501
        :rtype: SignatureType
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this Signature.


        :param signature_type: The signature_type of this Signature.  # noqa: E501
        :type: SignatureType
        """
        if self.local_vars_configuration.client_side_validation and signature_type is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_type`, must not be `None`")  # noqa: E501

        self._signature_type = signature_type

    @property
    def hex_bytes(self):
        """Gets the hex_bytes of this Signature.  # noqa: E501


        :return: The hex_bytes of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._hex_bytes

    @hex_bytes.setter
    def hex_bytes(self, hex_bytes):
        """Sets the hex_bytes of this Signature.


        :param hex_bytes: The hex_bytes of this Signature.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hex_bytes is None:  # noqa: E501
            raise ValueError("Invalid value for `hex_bytes`, must not be `None`")  # noqa: E501

        self._hex_bytes = hex_bytes

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
        if not isinstance(other, Signature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Signature):
            return True

        return self.to_dict() != other.to_dict()
