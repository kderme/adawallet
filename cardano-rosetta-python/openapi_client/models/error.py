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


class Error(object):
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
        'code': 'int',
        'message': 'str',
        'retriable': 'bool',
        'details': 'ErrorDetails'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'retriable': 'retriable',
        'details': 'details'
    }

    def __init__(self, code=None, message=None, retriable=None, details=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._message = None
        self._retriable = None
        self._details = None
        self.discriminator = None

        self.code = code
        self.message = message
        self.retriable = retriable
        if details is not None:
            self.details = details

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501

        Code is a network-specific error code. If desired, this code can be equivalent to an HTTP status code.  # noqa: E501

        :return: The code of this Error.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.

        Code is a network-specific error code. If desired, this code can be equivalent to an HTTP status code.  # noqa: E501

        :param code: The code of this Error.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and code < 0):  # noqa: E501
            raise ValueError("Invalid value for `code`, must be a value greater than or equal to `0`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        Message is a network-specific error message. The message MUST NOT change for a given code. In particular, this means that any contextual information should be included in the details field.  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        Message is a network-specific error message. The message MUST NOT change for a given code. In particular, this means that any contextual information should be included in the details field.  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def retriable(self):
        """Gets the retriable of this Error.  # noqa: E501

        An error is retriable if the same request may succeed if submitted again.  # noqa: E501

        :return: The retriable of this Error.  # noqa: E501
        :rtype: bool
        """
        return self._retriable

    @retriable.setter
    def retriable(self, retriable):
        """Sets the retriable of this Error.

        An error is retriable if the same request may succeed if submitted again.  # noqa: E501

        :param retriable: The retriable of this Error.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and retriable is None:  # noqa: E501
            raise ValueError("Invalid value for `retriable`, must not be `None`")  # noqa: E501

        self._retriable = retriable

    @property
    def details(self):
        """Gets the details of this Error.  # noqa: E501


        :return: The details of this Error.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Error.


        :param details: The details of this Error.  # noqa: E501
        :type: ErrorDetails
        """

        self._details = details

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
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
