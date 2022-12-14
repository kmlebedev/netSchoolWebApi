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

class LoginData(object):
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
        'product_name': 'str',
        'version': 'str',
        'school_login': 'bool',
        'em_login': 'bool',
        'esia_login': 'bool',
        'esia_login_page': 'str',
        'esia_main_auth': 'bool',
        'esia_button': 'bool',
        'signature_login': 'bool',
        'cache_ver': 'str',
        'windows_auth': 'bool',
        'enable_sms': 'bool',
        'esa_login': 'bool',
        'esa_login_page': 'str'
    }

    attribute_map = {
        'product_name': 'productName',
        'version': 'version',
        'school_login': 'schoolLogin',
        'em_login': 'emLogin',
        'esia_login': 'esiaLogin',
        'esia_login_page': 'esiaLoginPage',
        'esia_main_auth': 'esiaMainAuth',
        'esia_button': 'esiaButton',
        'signature_login': 'signatureLogin',
        'cache_ver': 'cacheVer',
        'windows_auth': 'windowsAuth',
        'enable_sms': 'enableSms',
        'esa_login': 'esaLogin',
        'esa_login_page': 'esaLoginPage'
    }

    def __init__(self, product_name=None, version=None, school_login=None, em_login=None, esia_login=None, esia_login_page=None, esia_main_auth=None, esia_button=None, signature_login=None, cache_ver=None, windows_auth=None, enable_sms=None, esa_login=None, esa_login_page=None):  # noqa: E501
        """LoginData - a model defined in Swagger"""  # noqa: E501
        self._product_name = None
        self._version = None
        self._school_login = None
        self._em_login = None
        self._esia_login = None
        self._esia_login_page = None
        self._esia_main_auth = None
        self._esia_button = None
        self._signature_login = None
        self._cache_ver = None
        self._windows_auth = None
        self._enable_sms = None
        self._esa_login = None
        self._esa_login_page = None
        self.discriminator = None
        if product_name is not None:
            self.product_name = product_name
        if version is not None:
            self.version = version
        if school_login is not None:
            self.school_login = school_login
        if em_login is not None:
            self.em_login = em_login
        if esia_login is not None:
            self.esia_login = esia_login
        if esia_login_page is not None:
            self.esia_login_page = esia_login_page
        if esia_main_auth is not None:
            self.esia_main_auth = esia_main_auth
        if esia_button is not None:
            self.esia_button = esia_button
        if signature_login is not None:
            self.signature_login = signature_login
        if cache_ver is not None:
            self.cache_ver = cache_ver
        if windows_auth is not None:
            self.windows_auth = windows_auth
        if enable_sms is not None:
            self.enable_sms = enable_sms
        if esa_login is not None:
            self.esa_login = esa_login
        if esa_login_page is not None:
            self.esa_login_page = esa_login_page

    @property
    def product_name(self):
        """Gets the product_name of this LoginData.  # noqa: E501


        :return: The product_name of this LoginData.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this LoginData.


        :param product_name: The product_name of this LoginData.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def version(self):
        """Gets the version of this LoginData.  # noqa: E501


        :return: The version of this LoginData.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LoginData.


        :param version: The version of this LoginData.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def school_login(self):
        """Gets the school_login of this LoginData.  # noqa: E501


        :return: The school_login of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._school_login

    @school_login.setter
    def school_login(self, school_login):
        """Sets the school_login of this LoginData.


        :param school_login: The school_login of this LoginData.  # noqa: E501
        :type: bool
        """

        self._school_login = school_login

    @property
    def em_login(self):
        """Gets the em_login of this LoginData.  # noqa: E501


        :return: The em_login of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._em_login

    @em_login.setter
    def em_login(self, em_login):
        """Sets the em_login of this LoginData.


        :param em_login: The em_login of this LoginData.  # noqa: E501
        :type: bool
        """

        self._em_login = em_login

    @property
    def esia_login(self):
        """Gets the esia_login of this LoginData.  # noqa: E501


        :return: The esia_login of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._esia_login

    @esia_login.setter
    def esia_login(self, esia_login):
        """Sets the esia_login of this LoginData.


        :param esia_login: The esia_login of this LoginData.  # noqa: E501
        :type: bool
        """

        self._esia_login = esia_login

    @property
    def esia_login_page(self):
        """Gets the esia_login_page of this LoginData.  # noqa: E501


        :return: The esia_login_page of this LoginData.  # noqa: E501
        :rtype: str
        """
        return self._esia_login_page

    @esia_login_page.setter
    def esia_login_page(self, esia_login_page):
        """Sets the esia_login_page of this LoginData.


        :param esia_login_page: The esia_login_page of this LoginData.  # noqa: E501
        :type: str
        """

        self._esia_login_page = esia_login_page

    @property
    def esia_main_auth(self):
        """Gets the esia_main_auth of this LoginData.  # noqa: E501


        :return: The esia_main_auth of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._esia_main_auth

    @esia_main_auth.setter
    def esia_main_auth(self, esia_main_auth):
        """Sets the esia_main_auth of this LoginData.


        :param esia_main_auth: The esia_main_auth of this LoginData.  # noqa: E501
        :type: bool
        """

        self._esia_main_auth = esia_main_auth

    @property
    def esia_button(self):
        """Gets the esia_button of this LoginData.  # noqa: E501


        :return: The esia_button of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._esia_button

    @esia_button.setter
    def esia_button(self, esia_button):
        """Sets the esia_button of this LoginData.


        :param esia_button: The esia_button of this LoginData.  # noqa: E501
        :type: bool
        """

        self._esia_button = esia_button

    @property
    def signature_login(self):
        """Gets the signature_login of this LoginData.  # noqa: E501


        :return: The signature_login of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._signature_login

    @signature_login.setter
    def signature_login(self, signature_login):
        """Sets the signature_login of this LoginData.


        :param signature_login: The signature_login of this LoginData.  # noqa: E501
        :type: bool
        """

        self._signature_login = signature_login

    @property
    def cache_ver(self):
        """Gets the cache_ver of this LoginData.  # noqa: E501


        :return: The cache_ver of this LoginData.  # noqa: E501
        :rtype: str
        """
        return self._cache_ver

    @cache_ver.setter
    def cache_ver(self, cache_ver):
        """Sets the cache_ver of this LoginData.


        :param cache_ver: The cache_ver of this LoginData.  # noqa: E501
        :type: str
        """

        self._cache_ver = cache_ver

    @property
    def windows_auth(self):
        """Gets the windows_auth of this LoginData.  # noqa: E501


        :return: The windows_auth of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._windows_auth

    @windows_auth.setter
    def windows_auth(self, windows_auth):
        """Sets the windows_auth of this LoginData.


        :param windows_auth: The windows_auth of this LoginData.  # noqa: E501
        :type: bool
        """

        self._windows_auth = windows_auth

    @property
    def enable_sms(self):
        """Gets the enable_sms of this LoginData.  # noqa: E501


        :return: The enable_sms of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        """Sets the enable_sms of this LoginData.


        :param enable_sms: The enable_sms of this LoginData.  # noqa: E501
        :type: bool
        """

        self._enable_sms = enable_sms

    @property
    def esa_login(self):
        """Gets the esa_login of this LoginData.  # noqa: E501


        :return: The esa_login of this LoginData.  # noqa: E501
        :rtype: bool
        """
        return self._esa_login

    @esa_login.setter
    def esa_login(self, esa_login):
        """Sets the esa_login of this LoginData.


        :param esa_login: The esa_login of this LoginData.  # noqa: E501
        :type: bool
        """

        self._esa_login = esa_login

    @property
    def esa_login_page(self):
        """Gets the esa_login_page of this LoginData.  # noqa: E501


        :return: The esa_login_page of this LoginData.  # noqa: E501
        :rtype: str
        """
        return self._esa_login_page

    @esa_login_page.setter
    def esa_login_page(self, esa_login_page):
        """Sets the esa_login_page of this LoginData.


        :param esa_login_page: The esa_login_page of this LoginData.  # noqa: E501
        :type: str
        """

        self._esa_login_page = esa_login_page

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
        if issubclass(LoginData, dict):
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
        if not isinstance(other, LoginData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
