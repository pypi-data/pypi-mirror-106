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

class Tolerance(object):
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
        'value': 'float',
        'type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'type': 'type'
    }

    required_map = {
        'value': 'optional',
        'type': 'optional'
    }

    def __init__(self, value=None, type=None):  # noqa: E501
        """
        Tolerance - a model defined in OpenAPI

        :param value:  The numerical value of the property.
        :type value: float
        :param type:  The available values are: Absolute, Relative
        :type type: str

        """  # noqa: E501

        self._value = None
        self._type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if type is not None:
            self.type = type

    @property
    def value(self):
        """Gets the value of this Tolerance.  # noqa: E501

        The numerical value of the property.  # noqa: E501

        :return: The value of this Tolerance.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Tolerance.

        The numerical value of the property.  # noqa: E501

        :param value: The value of this Tolerance.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this Tolerance.  # noqa: E501

        The available values are: Absolute, Relative  # noqa: E501

        :return: The type of this Tolerance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Tolerance.

        The available values are: Absolute, Relative  # noqa: E501

        :param type: The type of this Tolerance.  # noqa: E501
        :type: str
        """
        allowed_values = ["Absolute", "Relative"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, Tolerance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
