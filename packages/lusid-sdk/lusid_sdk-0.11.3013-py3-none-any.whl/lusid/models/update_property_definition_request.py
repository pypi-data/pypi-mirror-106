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

class UpdatePropertyDefinitionRequest(object):
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
        'display_name': 'str',
        'property_description': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'property_description': 'propertyDescription'
    }

    required_map = {
        'display_name': 'required',
        'property_description': 'optional'
    }

    def __init__(self, display_name=None, property_description=None):  # noqa: E501
        """
        UpdatePropertyDefinitionRequest - a model defined in OpenAPI

        :param display_name:  The display name of the property. (required)
        :type display_name: str
        :param property_description:  Describes the property
        :type property_description: str

        """  # noqa: E501

        self._display_name = None
        self._property_description = None
        self.discriminator = None

        self.display_name = display_name
        self.property_description = property_description

    @property
    def display_name(self):
        """Gets the display_name of this UpdatePropertyDefinitionRequest.  # noqa: E501

        The display name of the property.  # noqa: E501

        :return: The display_name of this UpdatePropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdatePropertyDefinitionRequest.

        The display name of the property.  # noqa: E501

        :param display_name: The display_name of this UpdatePropertyDefinitionRequest.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def property_description(self):
        """Gets the property_description of this UpdatePropertyDefinitionRequest.  # noqa: E501

        Describes the property  # noqa: E501

        :return: The property_description of this UpdatePropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._property_description

    @property_description.setter
    def property_description(self, property_description):
        """Sets the property_description of this UpdatePropertyDefinitionRequest.

        Describes the property  # noqa: E501

        :param property_description: The property_description of this UpdatePropertyDefinitionRequest.  # noqa: E501
        :type: str
        """
        if property_description is not None and len(property_description) > 512:
            raise ValueError("Invalid value for `property_description`, length must be less than or equal to `512`")  # noqa: E501

        self._property_description = property_description

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
        if not isinstance(other, UpdatePropertyDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
