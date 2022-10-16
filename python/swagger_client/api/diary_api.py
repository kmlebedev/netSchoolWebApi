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


class DiaryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def diary_assignn_details(self, assign_id, student_id, **kwargs):  # noqa: E501
        """diary_assignn_details  # noqa: E501

        returns assign information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.diary_assignn_details(assign_id, student_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assign_id: (required)
        :param int student_id: (required)
        :return: DiaryAssignDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.diary_assignn_details_with_http_info(assign_id, student_id, **kwargs)  # noqa: E501
        else:
            (data) = self.diary_assignn_details_with_http_info(assign_id, student_id, **kwargs)  # noqa: E501
            return data

    def diary_assignn_details_with_http_info(self, assign_id, student_id, **kwargs):  # noqa: E501
        """diary_assignn_details  # noqa: E501

        returns assign information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.diary_assignn_details_with_http_info(assign_id, student_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assign_id: (required)
        :param int student_id: (required)
        :return: DiaryAssignDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assign_id', 'student_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method diary_assignn_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assign_id' is set
        if ('assign_id' not in params or
                params['assign_id'] is None):
            raise ValueError("Missing the required parameter `assign_id` when calling `diary_assignn_details`")  # noqa: E501
        # verify the required parameter 'student_id' is set
        if ('student_id' not in params or
                params['student_id'] is None):
            raise ValueError("Missing the required parameter `student_id` when calling `diary_assignn_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assign_id' in params:
            path_params['assignId'] = params['assign_id']  # noqa: E501

        query_params = []
        if 'student_id' in params:
            query_params.append(('studentId', params['student_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/student/diary/assigns/{assignId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiaryAssignDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
