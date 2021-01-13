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


class NetworkStatusResponse(object):
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
        'current_block_identifier': 'BlockIdentifier',
        'current_block_timestamp': 'int',
        'genesis_block_identifier': 'BlockIdentifier',
        'oldest_block_identifier': 'BlockIdentifier',
        'sync_status': 'SyncStatus',
        'peers': 'list[Peer]'
    }

    attribute_map = {
        'current_block_identifier': 'current_block_identifier',
        'current_block_timestamp': 'current_block_timestamp',
        'genesis_block_identifier': 'genesis_block_identifier',
        'oldest_block_identifier': 'oldest_block_identifier',
        'sync_status': 'sync_status',
        'peers': 'peers'
    }

    def __init__(self, current_block_identifier=None, current_block_timestamp=None, genesis_block_identifier=None, oldest_block_identifier=None, sync_status=None, peers=None, local_vars_configuration=None):  # noqa: E501
        """NetworkStatusResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_block_identifier = None
        self._current_block_timestamp = None
        self._genesis_block_identifier = None
        self._oldest_block_identifier = None
        self._sync_status = None
        self._peers = None
        self.discriminator = None

        self.current_block_identifier = current_block_identifier
        self.current_block_timestamp = current_block_timestamp
        self.genesis_block_identifier = genesis_block_identifier
        if oldest_block_identifier is not None:
            self.oldest_block_identifier = oldest_block_identifier
        if sync_status is not None:
            self.sync_status = sync_status
        self.peers = peers

    @property
    def current_block_identifier(self):
        """Gets the current_block_identifier of this NetworkStatusResponse.  # noqa: E501


        :return: The current_block_identifier of this NetworkStatusResponse.  # noqa: E501
        :rtype: BlockIdentifier
        """
        return self._current_block_identifier

    @current_block_identifier.setter
    def current_block_identifier(self, current_block_identifier):
        """Sets the current_block_identifier of this NetworkStatusResponse.


        :param current_block_identifier: The current_block_identifier of this NetworkStatusResponse.  # noqa: E501
        :type: BlockIdentifier
        """
        if self.local_vars_configuration.client_side_validation and current_block_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `current_block_identifier`, must not be `None`")  # noqa: E501

        self._current_block_identifier = current_block_identifier

    @property
    def current_block_timestamp(self):
        """Gets the current_block_timestamp of this NetworkStatusResponse.  # noqa: E501

        The timestamp of the block in milliseconds since the Unix Epoch. The timestamp is stored in milliseconds because some blockchains produce blocks more often than once a second.  # noqa: E501

        :return: The current_block_timestamp of this NetworkStatusResponse.  # noqa: E501
        :rtype: int
        """
        return self._current_block_timestamp

    @current_block_timestamp.setter
    def current_block_timestamp(self, current_block_timestamp):
        """Sets the current_block_timestamp of this NetworkStatusResponse.

        The timestamp of the block in milliseconds since the Unix Epoch. The timestamp is stored in milliseconds because some blockchains produce blocks more often than once a second.  # noqa: E501

        :param current_block_timestamp: The current_block_timestamp of this NetworkStatusResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and current_block_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `current_block_timestamp`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                current_block_timestamp is not None and current_block_timestamp < 0):  # noqa: E501
            raise ValueError("Invalid value for `current_block_timestamp`, must be a value greater than or equal to `0`")  # noqa: E501

        self._current_block_timestamp = current_block_timestamp

    @property
    def genesis_block_identifier(self):
        """Gets the genesis_block_identifier of this NetworkStatusResponse.  # noqa: E501


        :return: The genesis_block_identifier of this NetworkStatusResponse.  # noqa: E501
        :rtype: BlockIdentifier
        """
        return self._genesis_block_identifier

    @genesis_block_identifier.setter
    def genesis_block_identifier(self, genesis_block_identifier):
        """Sets the genesis_block_identifier of this NetworkStatusResponse.


        :param genesis_block_identifier: The genesis_block_identifier of this NetworkStatusResponse.  # noqa: E501
        :type: BlockIdentifier
        """
        if self.local_vars_configuration.client_side_validation and genesis_block_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `genesis_block_identifier`, must not be `None`")  # noqa: E501

        self._genesis_block_identifier = genesis_block_identifier

    @property
    def oldest_block_identifier(self):
        """Gets the oldest_block_identifier of this NetworkStatusResponse.  # noqa: E501


        :return: The oldest_block_identifier of this NetworkStatusResponse.  # noqa: E501
        :rtype: BlockIdentifier
        """
        return self._oldest_block_identifier

    @oldest_block_identifier.setter
    def oldest_block_identifier(self, oldest_block_identifier):
        """Sets the oldest_block_identifier of this NetworkStatusResponse.


        :param oldest_block_identifier: The oldest_block_identifier of this NetworkStatusResponse.  # noqa: E501
        :type: BlockIdentifier
        """

        self._oldest_block_identifier = oldest_block_identifier

    @property
    def sync_status(self):
        """Gets the sync_status of this NetworkStatusResponse.  # noqa: E501


        :return: The sync_status of this NetworkStatusResponse.  # noqa: E501
        :rtype: SyncStatus
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this NetworkStatusResponse.


        :param sync_status: The sync_status of this NetworkStatusResponse.  # noqa: E501
        :type: SyncStatus
        """

        self._sync_status = sync_status

    @property
    def peers(self):
        """Gets the peers of this NetworkStatusResponse.  # noqa: E501


        :return: The peers of this NetworkStatusResponse.  # noqa: E501
        :rtype: list[Peer]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this NetworkStatusResponse.


        :param peers: The peers of this NetworkStatusResponse.  # noqa: E501
        :type: list[Peer]
        """
        if self.local_vars_configuration.client_side_validation and peers is None:  # noqa: E501
            raise ValueError("Invalid value for `peers`, must not be `None`")  # noqa: E501

        self._peers = peers

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
        if not isinstance(other, NetworkStatusResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkStatusResponse):
            return True

        return self.to_dict() != other.to_dict()
