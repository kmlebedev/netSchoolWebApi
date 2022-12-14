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

class PrepareEmLoginForm(object):
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
        'countries': 'list[PrepareEmLoginFormCountries]',
        'states': 'list[PrepareEmLoginFormCountries]',
        'hlevels': 'list[PrepareEmLoginFormCountries]',
        'ems': 'list[PrepareEmLoginFormCountries]',
        'em_cid': 'int',
        'em_sid': 'int',
        'hlevel': 'int',
        'em_id': 'int'
    }

    attribute_map = {
        'countries': 'countries',
        'states': 'states',
        'hlevels': 'hlevels',
        'ems': 'ems',
        'em_cid': 'em_cid',
        'em_sid': 'em_sid',
        'hlevel': 'hlevel',
        'em_id': 'emId'
    }

    def __init__(self, countries=None, states=None, hlevels=None, ems=None, em_cid=None, em_sid=None, hlevel=None, em_id=None):  # noqa: E501
        """PrepareEmLoginForm - a model defined in Swagger"""  # noqa: E501
        self._countries = None
        self._states = None
        self._hlevels = None
        self._ems = None
        self._em_cid = None
        self._em_sid = None
        self._hlevel = None
        self._em_id = None
        self.discriminator = None
        if countries is not None:
            self.countries = countries
        if states is not None:
            self.states = states
        if hlevels is not None:
            self.hlevels = hlevels
        if ems is not None:
            self.ems = ems
        if em_cid is not None:
            self.em_cid = em_cid
        if em_sid is not None:
            self.em_sid = em_sid
        if hlevel is not None:
            self.hlevel = hlevel
        if em_id is not None:
            self.em_id = em_id

    @property
    def countries(self):
        """Gets the countries of this PrepareEmLoginForm.  # noqa: E501


        :return: The countries of this PrepareEmLoginForm.  # noqa: E501
        :rtype: list[PrepareEmLoginFormCountries]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this PrepareEmLoginForm.


        :param countries: The countries of this PrepareEmLoginForm.  # noqa: E501
        :type: list[PrepareEmLoginFormCountries]
        """

        self._countries = countries

    @property
    def states(self):
        """Gets the states of this PrepareEmLoginForm.  # noqa: E501


        :return: The states of this PrepareEmLoginForm.  # noqa: E501
        :rtype: list[PrepareEmLoginFormCountries]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this PrepareEmLoginForm.


        :param states: The states of this PrepareEmLoginForm.  # noqa: E501
        :type: list[PrepareEmLoginFormCountries]
        """

        self._states = states

    @property
    def hlevels(self):
        """Gets the hlevels of this PrepareEmLoginForm.  # noqa: E501


        :return: The hlevels of this PrepareEmLoginForm.  # noqa: E501
        :rtype: list[PrepareEmLoginFormCountries]
        """
        return self._hlevels

    @hlevels.setter
    def hlevels(self, hlevels):
        """Sets the hlevels of this PrepareEmLoginForm.


        :param hlevels: The hlevels of this PrepareEmLoginForm.  # noqa: E501
        :type: list[PrepareEmLoginFormCountries]
        """

        self._hlevels = hlevels

    @property
    def ems(self):
        """Gets the ems of this PrepareEmLoginForm.  # noqa: E501


        :return: The ems of this PrepareEmLoginForm.  # noqa: E501
        :rtype: list[PrepareEmLoginFormCountries]
        """
        return self._ems

    @ems.setter
    def ems(self, ems):
        """Sets the ems of this PrepareEmLoginForm.


        :param ems: The ems of this PrepareEmLoginForm.  # noqa: E501
        :type: list[PrepareEmLoginFormCountries]
        """

        self._ems = ems

    @property
    def em_cid(self):
        """Gets the em_cid of this PrepareEmLoginForm.  # noqa: E501


        :return: The em_cid of this PrepareEmLoginForm.  # noqa: E501
        :rtype: int
        """
        return self._em_cid

    @em_cid.setter
    def em_cid(self, em_cid):
        """Sets the em_cid of this PrepareEmLoginForm.


        :param em_cid: The em_cid of this PrepareEmLoginForm.  # noqa: E501
        :type: int
        """

        self._em_cid = em_cid

    @property
    def em_sid(self):
        """Gets the em_sid of this PrepareEmLoginForm.  # noqa: E501


        :return: The em_sid of this PrepareEmLoginForm.  # noqa: E501
        :rtype: int
        """
        return self._em_sid

    @em_sid.setter
    def em_sid(self, em_sid):
        """Sets the em_sid of this PrepareEmLoginForm.


        :param em_sid: The em_sid of this PrepareEmLoginForm.  # noqa: E501
        :type: int
        """

        self._em_sid = em_sid

    @property
    def hlevel(self):
        """Gets the hlevel of this PrepareEmLoginForm.  # noqa: E501


        :return: The hlevel of this PrepareEmLoginForm.  # noqa: E501
        :rtype: int
        """
        return self._hlevel

    @hlevel.setter
    def hlevel(self, hlevel):
        """Sets the hlevel of this PrepareEmLoginForm.


        :param hlevel: The hlevel of this PrepareEmLoginForm.  # noqa: E501
        :type: int
        """

        self._hlevel = hlevel

    @property
    def em_id(self):
        """Gets the em_id of this PrepareEmLoginForm.  # noqa: E501


        :return: The em_id of this PrepareEmLoginForm.  # noqa: E501
        :rtype: int
        """
        return self._em_id

    @em_id.setter
    def em_id(self, em_id):
        """Sets the em_id of this PrepareEmLoginForm.


        :param em_id: The em_id of this PrepareEmLoginForm.  # noqa: E501
        :type: int
        """

        self._em_id = em_id

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
        if issubclass(PrepareEmLoginForm, dict):
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
        if not isinstance(other, PrepareEmLoginForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
