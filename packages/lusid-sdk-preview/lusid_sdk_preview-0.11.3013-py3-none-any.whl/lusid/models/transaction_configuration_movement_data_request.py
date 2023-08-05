# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3013
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TransactionConfigurationMovementDataRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'movement_types': 'str',
        'side': 'str',
        'direction': 'int',
        'properties': 'dict(str, PerpetualProperty)',
        'mappings': 'list[TransactionPropertyMappingRequest]',
        'name': 'str'
    }

    attribute_map = {
        'movement_types': 'movementTypes',
        'side': 'side',
        'direction': 'direction',
        'properties': 'properties',
        'mappings': 'mappings',
        'name': 'name'
    }

    required_map = {
        'movement_types': 'required',
        'side': 'required',
        'direction': 'required',
        'properties': 'optional',
        'mappings': 'optional',
        'name': 'optional'
    }

    def __init__(self, movement_types=None, side=None, direction=None, properties=None, mappings=None, name=None):  # noqa: E501
        """
        TransactionConfigurationMovementDataRequest - a model defined in OpenAPI

        :param movement_types:  . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes, Carry, CarryAsPnl (required)
        :type movement_types: str
        :param side:  The movement side (required)
        :type side: str
        :param direction:  The movement direction (required)
        :type direction: int
        :param properties: 
        :type properties: dict[str, lusid.PerpetualProperty]
        :param mappings: 
        :type mappings: list[lusid.TransactionPropertyMappingRequest]
        :param name:  The movement name (optional)
        :type name: str

        """  # noqa: E501

        self._movement_types = None
        self._side = None
        self._direction = None
        self._properties = None
        self._mappings = None
        self._name = None
        self.discriminator = None

        self.movement_types = movement_types
        self.side = side
        self.direction = direction
        self.properties = properties
        self.mappings = mappings
        self.name = name

    @property
    def movement_types(self):
        """Gets the movement_types of this TransactionConfigurationMovementDataRequest.  # noqa: E501

        . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes, Carry, CarryAsPnl  # noqa: E501

        :return: The movement_types of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._movement_types

    @movement_types.setter
    def movement_types(self, movement_types):
        """Sets the movement_types of this TransactionConfigurationMovementDataRequest.

        . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes, Carry, CarryAsPnl  # noqa: E501

        :param movement_types: The movement_types of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :type: str
        """
        if movement_types is None:
            raise ValueError("Invalid value for `movement_types`, must not be `None`")  # noqa: E501
        allowed_values = ["Settlement", "Traded", "StockMovement", "FutureCash", "Commitment", "Receivable", "CashSettlement", "CashForward", "CashCommitment", "CashReceivable", "Accrual", "CashAccrual", "ForwardFx", "CashFxForward", "UnsettledCashTypes", "Carry", "CarryAsPnl"]  # noqa: E501
        if movement_types not in allowed_values:
            raise ValueError(
                "Invalid value for `movement_types` ({0}), must be one of {1}"  # noqa: E501
                .format(movement_types, allowed_values)
            )

        self._movement_types = movement_types

    @property
    def side(self):
        """Gets the side of this TransactionConfigurationMovementDataRequest.  # noqa: E501

        The movement side  # noqa: E501

        :return: The side of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this TransactionConfigurationMovementDataRequest.

        The movement side  # noqa: E501

        :param side: The side of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def direction(self):
        """Gets the direction of this TransactionConfigurationMovementDataRequest.  # noqa: E501

        The movement direction  # noqa: E501

        :return: The direction of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TransactionConfigurationMovementDataRequest.

        The movement direction  # noqa: E501

        :param direction: The direction of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :type: int
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def properties(self):
        """Gets the properties of this TransactionConfigurationMovementDataRequest.  # noqa: E501


        :return: The properties of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TransactionConfigurationMovementDataRequest.


        :param properties: The properties of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

    @property
    def mappings(self):
        """Gets the mappings of this TransactionConfigurationMovementDataRequest.  # noqa: E501


        :return: The mappings of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :rtype: list[TransactionPropertyMappingRequest]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this TransactionConfigurationMovementDataRequest.


        :param mappings: The mappings of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :type: list[TransactionPropertyMappingRequest]
        """

        self._mappings = mappings

    @property
    def name(self):
        """Gets the name of this TransactionConfigurationMovementDataRequest.  # noqa: E501

        The movement name (optional)  # noqa: E501

        :return: The name of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransactionConfigurationMovementDataRequest.

        The movement name (optional)  # noqa: E501

        :param name: The name of this TransactionConfigurationMovementDataRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, TransactionConfigurationMovementDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
