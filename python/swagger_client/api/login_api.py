# coding: utf-8

"""
    NetSchool

    The API for the NetSchool irTech project  # noqa: E501

    OpenAPI spec version: 5.10.63221
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LoginApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def getauthdata(self, **kwargs):  # noqa: E501
        """getauthdata  # noqa: E501

        returns all login data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getauthdata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAuthData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getauthdata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getauthdata_with_http_info(**kwargs)  # noqa: E501
            return data

    def getauthdata_with_http_info(self, **kwargs):  # noqa: E501
        """getauthdata  # noqa: E501

        returns all login data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getauthdata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAuthData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getauthdata" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/getdata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAuthData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login(self, login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, **kwargs):  # noqa: E501
        """login  # noqa: E501

        returns all login data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int login_type: (required)
        :param int cid: (required)
        :param int sid: (required)
        :param int pid: (required)
        :param int cn: (required)
        :param int sft: (required)
        :param int scid: (required)
        :param str un: (required)
        :param str pw: (required)
        :param int lt: (required)
        :param str pw2: (required)
        :param int ver: (required)
        :return: Login
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_with_http_info(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, **kwargs)  # noqa: E501
        else:
            (data) = self.login_with_http_info(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, **kwargs)  # noqa: E501
            return data

    def login_with_http_info(self, login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, **kwargs):  # noqa: E501
        """login  # noqa: E501

        returns all login data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_with_http_info(login_type, cid, sid, pid, cn, sft, scid, un, pw, lt, pw2, ver, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int login_type: (required)
        :param int cid: (required)
        :param int sid: (required)
        :param int pid: (required)
        :param int cn: (required)
        :param int sft: (required)
        :param int scid: (required)
        :param str un: (required)
        :param str pw: (required)
        :param int lt: (required)
        :param str pw2: (required)
        :param int ver: (required)
        :return: Login
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login_type', 'cid', 'sid', 'pid', 'cn', 'sft', 'scid', 'un', 'pw', 'lt', 'pw2', 'ver']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'login_type' is set
        if ('login_type' not in params or
                params['login_type'] is None):
            raise ValueError("Missing the required parameter `login_type` when calling `login`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `login`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `login`")  # noqa: E501
        # verify the required parameter 'pid' is set
        if ('pid' not in params or
                params['pid'] is None):
            raise ValueError("Missing the required parameter `pid` when calling `login`")  # noqa: E501
        # verify the required parameter 'cn' is set
        if ('cn' not in params or
                params['cn'] is None):
            raise ValueError("Missing the required parameter `cn` when calling `login`")  # noqa: E501
        # verify the required parameter 'sft' is set
        if ('sft' not in params or
                params['sft'] is None):
            raise ValueError("Missing the required parameter `sft` when calling `login`")  # noqa: E501
        # verify the required parameter 'scid' is set
        if ('scid' not in params or
                params['scid'] is None):
            raise ValueError("Missing the required parameter `scid` when calling `login`")  # noqa: E501
        # verify the required parameter 'un' is set
        if ('un' not in params or
                params['un'] is None):
            raise ValueError("Missing the required parameter `un` when calling `login`")  # noqa: E501
        # verify the required parameter 'pw' is set
        if ('pw' not in params or
                params['pw'] is None):
            raise ValueError("Missing the required parameter `pw` when calling `login`")  # noqa: E501
        # verify the required parameter 'lt' is set
        if ('lt' not in params or
                params['lt'] is None):
            raise ValueError("Missing the required parameter `lt` when calling `login`")  # noqa: E501
        # verify the required parameter 'pw2' is set
        if ('pw2' not in params or
                params['pw2'] is None):
            raise ValueError("Missing the required parameter `pw2` when calling `login`")  # noqa: E501
        # verify the required parameter 'ver' is set
        if ('ver' not in params or
                params['ver'] is None):
            raise ValueError("Missing the required parameter `ver` when calling `login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'login_type' in params:
            form_params.append(('LoginType', params['login_type']))  # noqa: E501
        if 'cid' in params:
            form_params.append(('cid', params['cid']))  # noqa: E501
        if 'sid' in params:
            form_params.append(('sid', params['sid']))  # noqa: E501
        if 'pid' in params:
            form_params.append(('pid', params['pid']))  # noqa: E501
        if 'cn' in params:
            form_params.append(('cn', params['cn']))  # noqa: E501
        if 'sft' in params:
            form_params.append(('sft', params['sft']))  # noqa: E501
        if 'scid' in params:
            form_params.append(('scid', params['scid']))  # noqa: E501
        if 'un' in params:
            form_params.append(('UN', params['un']))  # noqa: E501
        if 'pw' in params:
            form_params.append(('PW', params['pw']))  # noqa: E501
        if 'lt' in params:
            form_params.append(('lt', params['lt']))  # noqa: E501
        if 'pw2' in params:
            form_params.append(('pw2', params['pw2']))  # noqa: E501
        if 'ver' in params:
            form_params.append(('ver', params['ver']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Login',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logindata(self, **kwargs):  # noqa: E501
        """logindata  # noqa: E501

        returns all login data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logindata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: LoginData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logindata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.logindata_with_http_info(**kwargs)  # noqa: E501
            return data

    def logindata_with_http_info(self, **kwargs):  # noqa: E501
        """logindata  # noqa: E501

        returns all login data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logindata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: LoginData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logindata" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logindata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def loginform(self, **kwargs):  # noqa: E501
        """loginform  # noqa: E501

        returns all loginform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.loginform(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int cid:
        :param int sid:
        :param int pid:
        :param int cn:
        :param int sft:
        :param str lastname:
        :param str cache_ver:
        :return: LoginForm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.loginform_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.loginform_with_http_info(**kwargs)  # noqa: E501
            return data

    def loginform_with_http_info(self, **kwargs):  # noqa: E501
        """loginform  # noqa: E501

        returns all loginform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.loginform_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int cid:
        :param int sid:
        :param int pid:
        :param int cn:
        :param int sft:
        :param str lastname:
        :param str cache_ver:
        :return: LoginForm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'sid', 'pid', 'cn', 'sft', 'lastname', 'cache_ver']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method loginform" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501
        if 'sid' in params:
            query_params.append(('sid', params['sid']))  # noqa: E501
        if 'pid' in params:
            query_params.append(('pid', params['pid']))  # noqa: E501
        if 'cn' in params:
            query_params.append(('cn', params['cn']))  # noqa: E501
        if 'sft' in params:
            query_params.append(('sft', params['sft']))  # noqa: E501
        if 'lastname' in params:
            query_params.append(('LASTNAME', params['lastname']))  # noqa: E501
        if 'cache_ver' in params:
            query_params.append(('cacheVer', params['cache_ver']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/loginform', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginForm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def prepareemloginform(self, **kwargs):  # noqa: E501
        """prepareemloginform  # noqa: E501

        returns all prepareemloginform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.prepareemloginform(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cache_ver:
        :return: PrepareEmLoginForm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.prepareemloginform_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.prepareemloginform_with_http_info(**kwargs)  # noqa: E501
            return data

    def prepareemloginform_with_http_info(self, **kwargs):  # noqa: E501
        """prepareemloginform  # noqa: E501

        returns all prepareemloginform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.prepareemloginform_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cache_ver:
        :return: PrepareEmLoginForm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cache_ver']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prepareemloginform" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cache_ver' in params:
            query_params.append(('cacheVer', params['cache_ver']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/prepareemloginform', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrepareEmLoginForm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def prepareloginform(self, **kwargs):  # noqa: E501
        """prepareloginform  # noqa: E501

        returns all prepareloginform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.prepareloginform(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int cid:
        :param int sid:
        :param int pid:
        :param int cn:
        :param int sft:
        :param str lastname:
        :param str cache_ver:
        :return: PrepareLoginForm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.prepareloginform_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.prepareloginform_with_http_info(**kwargs)  # noqa: E501
            return data

    def prepareloginform_with_http_info(self, **kwargs):  # noqa: E501
        """prepareloginform  # noqa: E501

        returns all prepareloginform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.prepareloginform_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int cid:
        :param int sid:
        :param int pid:
        :param int cn:
        :param int sft:
        :param str lastname:
        :param str cache_ver:
        :return: PrepareLoginForm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'sid', 'pid', 'cn', 'sft', 'lastname', 'cache_ver']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prepareloginform" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501
        if 'sid' in params:
            query_params.append(('sid', params['sid']))  # noqa: E501
        if 'pid' in params:
            query_params.append(('pid', params['pid']))  # noqa: E501
        if 'cn' in params:
            query_params.append(('cn', params['cn']))  # noqa: E501
        if 'sft' in params:
            query_params.append(('sft', params['sft']))  # noqa: E501
        if 'lastname' in params:
            query_params.append(('LASTNAME', params['lastname']))  # noqa: E501
        if 'cache_ver' in params:
            query_params.append(('cacheVer', params['cache_ver']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/prepareloginform', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrepareLoginForm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
