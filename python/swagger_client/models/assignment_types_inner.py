# coding: utf-8

"""
    NetSchool

    The API for the NetSchool irTech project  # noqa: E501

    OpenAPI spec version: 5.10.63221
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AssignmentTypesInner(object):
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
        'abbr': 'str',
        'order': 'int',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'abbr': 'abbr',
        'order': 'order',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, abbr=None, order=None, id=None, name=None):  # noqa: E501
        """AssignmentTypesInner - a model defined in Swagger"""  # noqa: E501
        self._abbr = None
        self._order = None
        self._id = None
        self._name = None
        self.discriminator = None
        if abbr is not None:
            self.abbr = abbr
        if order is not None:
            self.order = order
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def abbr(self):
        """Gets the abbr of this AssignmentTypesInner.  # noqa: E501


        :return: The abbr of this AssignmentTypesInner.  # noqa: E501
        :rtype: str
        """
        return self._abbr

    @abbr.setter
    def abbr(self, abbr):
        """Sets the abbr of this AssignmentTypesInner.


        :param abbr: The abbr of this AssignmentTypesInner.  # noqa: E501
        :type: str
        """

        self._abbr = abbr

    @property
    def order(self):
        """Gets the order of this AssignmentTypesInner.  # noqa: E501


        :return: The order of this AssignmentTypesInner.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AssignmentTypesInner.


        :param order: The order of this AssignmentTypesInner.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def id(self):
        """Gets the id of this AssignmentTypesInner.  # noqa: E501


        :return: The id of this AssignmentTypesInner.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignmentTypesInner.


        :param id: The id of this AssignmentTypesInner.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssignmentTypesInner.  # noqa: E501


        :return: The name of this AssignmentTypesInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignmentTypesInner.


        :param name: The name of this AssignmentTypesInner.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(AssignmentTypesInner, dict):
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
        if not isinstance(other, AssignmentTypesInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
