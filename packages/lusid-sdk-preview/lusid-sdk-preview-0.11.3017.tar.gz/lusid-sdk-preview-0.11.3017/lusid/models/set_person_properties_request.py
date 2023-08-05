# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3017
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class SetPersonPropertiesRequest(object):
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
        'properties': 'dict(str, list[ModelProperty])'
    }

    attribute_map = {
        'properties': 'properties'
    }

    required_map = {
        'properties': 'optional'
    }

    def __init__(self, properties=None):  # noqa: E501
        """
        SetPersonPropertiesRequest - a model defined in OpenAPI

        :param properties:  Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended.
        :type properties: dict(str, list[ModelProperty])

        """  # noqa: E501

        self._properties = None
        self.discriminator = None

        self.properties = properties

    @property
    def properties(self):
        """Gets the properties of this SetPersonPropertiesRequest.  # noqa: E501

        Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended.  # noqa: E501

        :return: The properties of this SetPersonPropertiesRequest.  # noqa: E501
        :rtype: dict(str, list[ModelProperty])
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SetPersonPropertiesRequest.

        Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended.  # noqa: E501

        :param properties: The properties of this SetPersonPropertiesRequest.  # noqa: E501
        :type: dict(str, list[ModelProperty])
        """

        self._properties = properties

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
        if not isinstance(other, SetPersonPropertiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
