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

class InstrumentResponseDto(object):
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
        'id': 'int',
        'name': 'str',
        'code': 'str',
        'type': 'str',
        'price_decimal_len': 'int',
        'volume_decimal_len': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'type': 'type',
        'price_decimal_len': 'priceDecimalLen',
        'volume_decimal_len': 'volumeDecimalLen'
    }

    def __init__(self, id=None, name=None, code=None, type=None, price_decimal_len=None, volume_decimal_len=None):  # noqa: E501
        """InstrumentResponseDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._code = None
        self._type = None
        self._price_decimal_len = None
        self._volume_decimal_len = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if type is not None:
            self.type = type
        if price_decimal_len is not None:
            self.price_decimal_len = price_decimal_len
        if volume_decimal_len is not None:
            self.volume_decimal_len = volume_decimal_len

    @property
    def id(self):
        """Gets the id of this InstrumentResponseDto.  # noqa: E501


        :return: The id of this InstrumentResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstrumentResponseDto.


        :param id: The id of this InstrumentResponseDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InstrumentResponseDto.  # noqa: E501


        :return: The name of this InstrumentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstrumentResponseDto.


        :param name: The name of this InstrumentResponseDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this InstrumentResponseDto.  # noqa: E501


        :return: The code of this InstrumentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InstrumentResponseDto.


        :param code: The code of this InstrumentResponseDto.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def type(self):
        """Gets the type of this InstrumentResponseDto.  # noqa: E501


        :return: The type of this InstrumentResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstrumentResponseDto.


        :param type: The type of this InstrumentResponseDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def price_decimal_len(self):
        """Gets the price_decimal_len of this InstrumentResponseDto.  # noqa: E501


        :return: The price_decimal_len of this InstrumentResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._price_decimal_len

    @price_decimal_len.setter
    def price_decimal_len(self, price_decimal_len):
        """Sets the price_decimal_len of this InstrumentResponseDto.


        :param price_decimal_len: The price_decimal_len of this InstrumentResponseDto.  # noqa: E501
        :type: int
        """

        self._price_decimal_len = price_decimal_len

    @property
    def volume_decimal_len(self):
        """Gets the volume_decimal_len of this InstrumentResponseDto.  # noqa: E501


        :return: The volume_decimal_len of this InstrumentResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._volume_decimal_len

    @volume_decimal_len.setter
    def volume_decimal_len(self, volume_decimal_len):
        """Sets the volume_decimal_len of this InstrumentResponseDto.


        :param volume_decimal_len: The volume_decimal_len of this InstrumentResponseDto.  # noqa: E501
        :type: int
        """

        self._volume_decimal_len = volume_decimal_len

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
        if issubclass(InstrumentResponseDto, dict):
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
        if not isinstance(other, InstrumentResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
