# coding: utf-8

"""
    Instrument Quote Source API

    An ASP.NET Core Web API service for getting information about instrument quotes  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PeriodResponseDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'from_date': 'datetime',
        'untill_date': 'datetime'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'untill_date': 'untillDate'
    }

    def __init__(self, from_date=None, untill_date=None):  # noqa: E501
        """PeriodResponseDto - a model defined in Swagger"""  # noqa: E501
        self._from_date = None
        self._untill_date = None
        self.discriminator = None
        if from_date is not None:
            self.from_date = from_date
        if untill_date is not None:
            self.untill_date = untill_date

    @property
    def from_date(self):
        """Gets the from_date of this PeriodResponseDto.  # noqa: E501


        :return: The from_date of this PeriodResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this PeriodResponseDto.


        :param from_date: The from_date of this PeriodResponseDto.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def untill_date(self):
        """Gets the untill_date of this PeriodResponseDto.  # noqa: E501


        :return: The untill_date of this PeriodResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._untill_date

    @untill_date.setter
    def untill_date(self, untill_date):
        """Sets the untill_date of this PeriodResponseDto.


        :param untill_date: The untill_date of this PeriodResponseDto.  # noqa: E501
        :type: datetime
        """

        self._untill_date = untill_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PeriodResponseDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PeriodResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
