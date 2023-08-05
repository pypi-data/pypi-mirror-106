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

class IsBusinessDayResponse(object):
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
        'requested_date_time': 'datetime',
        'is_business_day': 'bool'
    }

    attribute_map = {
        'requested_date_time': 'requestedDateTime',
        'is_business_day': 'isBusinessDay'
    }

    required_map = {
        'requested_date_time': 'required',
        'is_business_day': 'required'
    }

    def __init__(self, requested_date_time=None, is_business_day=None):  # noqa: E501
        """
        IsBusinessDayResponse - a model defined in OpenAPI

        :param requested_date_time:  (required)
        :type requested_date_time: datetime
        :param is_business_day:  (required)
        :type is_business_day: bool

        """  # noqa: E501

        self._requested_date_time = None
        self._is_business_day = None
        self.discriminator = None

        self.requested_date_time = requested_date_time
        self.is_business_day = is_business_day

    @property
    def requested_date_time(self):
        """Gets the requested_date_time of this IsBusinessDayResponse.  # noqa: E501


        :return: The requested_date_time of this IsBusinessDayResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_date_time

    @requested_date_time.setter
    def requested_date_time(self, requested_date_time):
        """Sets the requested_date_time of this IsBusinessDayResponse.


        :param requested_date_time: The requested_date_time of this IsBusinessDayResponse.  # noqa: E501
        :type: datetime
        """
        if requested_date_time is None:
            raise ValueError("Invalid value for `requested_date_time`, must not be `None`")  # noqa: E501

        self._requested_date_time = requested_date_time

    @property
    def is_business_day(self):
        """Gets the is_business_day of this IsBusinessDayResponse.  # noqa: E501


        :return: The is_business_day of this IsBusinessDayResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_business_day

    @is_business_day.setter
    def is_business_day(self, is_business_day):
        """Sets the is_business_day of this IsBusinessDayResponse.


        :param is_business_day: The is_business_day of this IsBusinessDayResponse.  # noqa: E501
        :type: bool
        """
        if is_business_day is None:
            raise ValueError("Invalid value for `is_business_day`, must not be `None`")  # noqa: E501

        self._is_business_day = is_business_day

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
        if not isinstance(other, IsBusinessDayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
