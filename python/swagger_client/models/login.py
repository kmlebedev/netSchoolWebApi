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

class Login(object):
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
        'at': 'str',
        'code': 'str',
        'time_out': 'int',
        'access_token': 'str',
        'refresh_token': 'str',
        'account_info': 'LoginAccountInfo',
        'token_type': 'str',
        'entry_point': 'str',
        'request_data': 'LoginRequestData',
        'error_message': 'str'
    }

    attribute_map = {
        'at': 'at',
        'code': 'code',
        'time_out': 'timeOut',
        'access_token': 'accessToken',
        'refresh_token': 'refreshToken',
        'account_info': 'accountInfo',
        'token_type': 'tokenType',
        'entry_point': 'entryPoint',
        'request_data': 'requestData',
        'error_message': 'errorMessage'
    }

    def __init__(self, at=None, code=None, time_out=None, access_token=None, refresh_token=None, account_info=None, token_type=None, entry_point=None, request_data=None, error_message=None):  # noqa: E501
        """Login - a model defined in Swagger"""  # noqa: E501
        self._at = None
        self._code = None
        self._time_out = None
        self._access_token = None
        self._refresh_token = None
        self._account_info = None
        self._token_type = None
        self._entry_point = None
        self._request_data = None
        self._error_message = None
        self.discriminator = None
        if at is not None:
            self.at = at
        if code is not None:
            self.code = code
        if time_out is not None:
            self.time_out = time_out
        if access_token is not None:
            self.access_token = access_token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if account_info is not None:
            self.account_info = account_info
        if token_type is not None:
            self.token_type = token_type
        if entry_point is not None:
            self.entry_point = entry_point
        if request_data is not None:
            self.request_data = request_data
        if error_message is not None:
            self.error_message = error_message

    @property
    def at(self):
        """Gets the at of this Login.  # noqa: E501


        :return: The at of this Login.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this Login.


        :param at: The at of this Login.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def code(self):
        """Gets the code of this Login.  # noqa: E501


        :return: The code of this Login.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Login.


        :param code: The code of this Login.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def time_out(self):
        """Gets the time_out of this Login.  # noqa: E501


        :return: The time_out of this Login.  # noqa: E501
        :rtype: int
        """
        return self._time_out

    @time_out.setter
    def time_out(self, time_out):
        """Sets the time_out of this Login.


        :param time_out: The time_out of this Login.  # noqa: E501
        :type: int
        """

        self._time_out = time_out

    @property
    def access_token(self):
        """Gets the access_token of this Login.  # noqa: E501


        :return: The access_token of this Login.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Login.


        :param access_token: The access_token of this Login.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this Login.  # noqa: E501


        :return: The refresh_token of this Login.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this Login.


        :param refresh_token: The refresh_token of this Login.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def account_info(self):
        """Gets the account_info of this Login.  # noqa: E501


        :return: The account_info of this Login.  # noqa: E501
        :rtype: LoginAccountInfo
        """
        return self._account_info

    @account_info.setter
    def account_info(self, account_info):
        """Sets the account_info of this Login.


        :param account_info: The account_info of this Login.  # noqa: E501
        :type: LoginAccountInfo
        """

        self._account_info = account_info

    @property
    def token_type(self):
        """Gets the token_type of this Login.  # noqa: E501


        :return: The token_type of this Login.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this Login.


        :param token_type: The token_type of this Login.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def entry_point(self):
        """Gets the entry_point of this Login.  # noqa: E501


        :return: The entry_point of this Login.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this Login.


        :param entry_point: The entry_point of this Login.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def request_data(self):
        """Gets the request_data of this Login.  # noqa: E501


        :return: The request_data of this Login.  # noqa: E501
        :rtype: LoginRequestData
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this Login.


        :param request_data: The request_data of this Login.  # noqa: E501
        :type: LoginRequestData
        """

        self._request_data = request_data

    @property
    def error_message(self):
        """Gets the error_message of this Login.  # noqa: E501


        :return: The error_message of this Login.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Login.


        :param error_message: The error_message of this Login.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(Login, dict):
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
        if not isinstance(other, Login):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
