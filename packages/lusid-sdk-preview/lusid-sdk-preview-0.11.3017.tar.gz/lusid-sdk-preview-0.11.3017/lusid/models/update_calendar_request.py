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

class UpdateCalendarRequest(object):
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
        'weekend_mask': 'WeekendMask',
        'source_provider': 'str',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'weekend_mask': 'weekendMask',
        'source_provider': 'sourceProvider',
        'properties': 'properties'
    }

    required_map = {
        'weekend_mask': 'required',
        'source_provider': 'required',
        'properties': 'required'
    }

    def __init__(self, weekend_mask=None, source_provider=None, properties=None):  # noqa: E501
        """
        UpdateCalendarRequest - a model defined in OpenAPI

        :param weekend_mask:  (required)
        :type weekend_mask: lusid.WeekendMask
        :param source_provider:  (required)
        :type source_provider: str
        :param properties:  (required)
        :type properties: list[lusid.ModelProperty]

        """  # noqa: E501

        self._weekend_mask = None
        self._source_provider = None
        self._properties = None
        self.discriminator = None

        self.weekend_mask = weekend_mask
        self.source_provider = source_provider
        self.properties = properties

    @property
    def weekend_mask(self):
        """Gets the weekend_mask of this UpdateCalendarRequest.  # noqa: E501


        :return: The weekend_mask of this UpdateCalendarRequest.  # noqa: E501
        :rtype: WeekendMask
        """
        return self._weekend_mask

    @weekend_mask.setter
    def weekend_mask(self, weekend_mask):
        """Sets the weekend_mask of this UpdateCalendarRequest.


        :param weekend_mask: The weekend_mask of this UpdateCalendarRequest.  # noqa: E501
        :type: WeekendMask
        """
        if weekend_mask is None:
            raise ValueError("Invalid value for `weekend_mask`, must not be `None`")  # noqa: E501

        self._weekend_mask = weekend_mask

    @property
    def source_provider(self):
        """Gets the source_provider of this UpdateCalendarRequest.  # noqa: E501


        :return: The source_provider of this UpdateCalendarRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_provider

    @source_provider.setter
    def source_provider(self, source_provider):
        """Sets the source_provider of this UpdateCalendarRequest.


        :param source_provider: The source_provider of this UpdateCalendarRequest.  # noqa: E501
        :type: str
        """
        if source_provider is None:
            raise ValueError("Invalid value for `source_provider`, must not be `None`")  # noqa: E501
        if source_provider is not None and len(source_provider) > 256:
            raise ValueError("Invalid value for `source_provider`, length must be less than or equal to `256`")  # noqa: E501
        if source_provider is not None and len(source_provider) < 1:
            raise ValueError("Invalid value for `source_provider`, length must be greater than or equal to `1`")  # noqa: E501
        if (source_provider is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', source_provider)):  # noqa: E501
            raise ValueError(r"Invalid value for `source_provider`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._source_provider = source_provider

    @property
    def properties(self):
        """Gets the properties of this UpdateCalendarRequest.  # noqa: E501


        :return: The properties of this UpdateCalendarRequest.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateCalendarRequest.


        :param properties: The properties of this UpdateCalendarRequest.  # noqa: E501
        :type: list[ModelProperty]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, UpdateCalendarRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
