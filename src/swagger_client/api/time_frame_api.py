# coding: utf-8

"""
    Instrument Quote Source API (administrator)

    An ASP.NET Core Web API service for getting information about instrument quotes. Administrator tools to extend avaliable data  # noqa: E501

    OpenAPI spec version: v2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class TimeFrameApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_time_frame_get(self, **kwargs):  # noqa: E501
        """Get all timeframes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_time_frame_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TimeFrameResponseDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_time_frame_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_time_frame_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_time_frame_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all timeframes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_time_frame_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TimeFrameResponseDto]
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
                    " to method api_time_frame_get" % key
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
            '/api/TimeFrame', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TimeFrameResponseDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_time_frame_timeframe_str_get(self, timeframe_str, **kwargs):  # noqa: E501
        """Get TimeFrame by Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_time_frame_timeframe_str_get(timeframe_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str timeframe_str: (required)
        :return: TimeFrameResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_time_frame_timeframe_str_get_with_http_info(timeframe_str, **kwargs)  # noqa: E501
        else:
            (data) = self.api_time_frame_timeframe_str_get_with_http_info(timeframe_str, **kwargs)  # noqa: E501
            return data

    def api_time_frame_timeframe_str_get_with_http_info(self, timeframe_str, **kwargs):  # noqa: E501
        """Get TimeFrame by Code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_time_frame_timeframe_str_get_with_http_info(timeframe_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str timeframe_str: (required)
        :return: TimeFrameResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['timeframe_str']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_time_frame_timeframe_str_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'timeframe_str' is set
        if ('timeframe_str' not in params or
                params['timeframe_str'] is None):
            raise ValueError("Missing the required parameter `timeframe_str` when calling `api_time_frame_timeframe_str_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'timeframe_str' in params:
            path_params['timeframeStr'] = params['timeframe_str']  # noqa: E501

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
            '/api/TimeFrame/{timeframeStr}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimeFrameResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
