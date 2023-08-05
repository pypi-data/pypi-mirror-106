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

class VersionedResourceListOfTransaction(object):
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
        'version': 'Version',
        'values': 'list[Transaction]',
        'href': 'str',
        'next_page': 'str',
        'previous_page': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'version': 'version',
        'values': 'values',
        'href': 'href',
        'next_page': 'nextPage',
        'previous_page': 'previousPage',
        'links': 'links'
    }

    required_map = {
        'version': 'required',
        'values': 'required',
        'href': 'optional',
        'next_page': 'optional',
        'previous_page': 'optional',
        'links': 'optional'
    }

    def __init__(self, version=None, values=None, href=None, next_page=None, previous_page=None, links=None):  # noqa: E501
        """
        VersionedResourceListOfTransaction - a model defined in OpenAPI

        :param version:  (required)
        :type version: lusid.Version
        :param values:  (required)
        :type values: list[lusid.Transaction]
        :param href: 
        :type href: str
        :param next_page: 
        :type next_page: str
        :param previous_page: 
        :type previous_page: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._version = None
        self._values = None
        self._href = None
        self._next_page = None
        self._previous_page = None
        self._links = None
        self.discriminator = None

        self.version = version
        self.values = values
        self.href = href
        self.next_page = next_page
        self.previous_page = previous_page
        self.links = links

    @property
    def version(self):
        """Gets the version of this VersionedResourceListOfTransaction.  # noqa: E501


        :return: The version of this VersionedResourceListOfTransaction.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionedResourceListOfTransaction.


        :param version: The version of this VersionedResourceListOfTransaction.  # noqa: E501
        :type: Version
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def values(self):
        """Gets the values of this VersionedResourceListOfTransaction.  # noqa: E501


        :return: The values of this VersionedResourceListOfTransaction.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this VersionedResourceListOfTransaction.


        :param values: The values of this VersionedResourceListOfTransaction.  # noqa: E501
        :type: list[Transaction]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def href(self):
        """Gets the href of this VersionedResourceListOfTransaction.  # noqa: E501


        :return: The href of this VersionedResourceListOfTransaction.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VersionedResourceListOfTransaction.


        :param href: The href of this VersionedResourceListOfTransaction.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def next_page(self):
        """Gets the next_page of this VersionedResourceListOfTransaction.  # noqa: E501


        :return: The next_page of this VersionedResourceListOfTransaction.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this VersionedResourceListOfTransaction.


        :param next_page: The next_page of this VersionedResourceListOfTransaction.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def previous_page(self):
        """Gets the previous_page of this VersionedResourceListOfTransaction.  # noqa: E501


        :return: The previous_page of this VersionedResourceListOfTransaction.  # noqa: E501
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """Sets the previous_page of this VersionedResourceListOfTransaction.


        :param previous_page: The previous_page of this VersionedResourceListOfTransaction.  # noqa: E501
        :type: str
        """

        self._previous_page = previous_page

    @property
    def links(self):
        """Gets the links of this VersionedResourceListOfTransaction.  # noqa: E501


        :return: The links of this VersionedResourceListOfTransaction.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionedResourceListOfTransaction.


        :param links: The links of this VersionedResourceListOfTransaction.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, VersionedResourceListOfTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
