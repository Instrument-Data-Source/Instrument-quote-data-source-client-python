# coding: utf-8

"""
    Instrument Quote Source API

    An ASP.NET Core Web API service for getting information about instrument quotes  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class InstrumentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_instrument_get(self, **kwargs):  # noqa: E501
        """api_instrument_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InstrumentResponseDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_instrument_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_instrument_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_instrument_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_instrument_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InstrumentResponseDto]
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
                    " to method api_instrument_get" % key
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
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Instrument', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InstrumentResponseDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_instrument_instrument_str_get(self, instrument_str, **kwargs):  # noqa: E501
        """api_instrument_instrument_str_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_instrument_str_get(instrument_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_str: (required)
        :return: dict(str, PeriodResponseDto)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_instrument_instrument_str_get_with_http_info(instrument_str, **kwargs)  # noqa: E501
        else:
            (data) = self.api_instrument_instrument_str_get_with_http_info(instrument_str, **kwargs)  # noqa: E501
            return data

    def api_instrument_instrument_str_get_with_http_info(self, instrument_str, **kwargs):  # noqa: E501
        """api_instrument_instrument_str_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_instrument_str_get_with_http_info(instrument_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_str: (required)
        :return: dict(str, PeriodResponseDto)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instrument_str']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_instrument_instrument_str_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instrument_str' is set
        if ('instrument_str' not in params or
                params['instrument_str'] is None):
            raise ValueError("Missing the required parameter `instrument_str` when calling `api_instrument_instrument_str_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrument_str' in params:
            path_params['instrumentStr'] = params['instrument_str']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Instrument/{instrumentStr}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, PeriodResponseDto)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_instrument_instrument_str_periods_get(self, instrument_str, **kwargs):  # noqa: E501
        """api_instrument_instrument_str_periods_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_instrument_str_periods_get(instrument_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_str: (required)
        :return: dict(str, PeriodResponseDto)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_instrument_instrument_str_periods_get_with_http_info(instrument_str, **kwargs)  # noqa: E501
        else:
            (data) = self.api_instrument_instrument_str_periods_get_with_http_info(instrument_str, **kwargs)  # noqa: E501
            return data

    def api_instrument_instrument_str_periods_get_with_http_info(self, instrument_str, **kwargs):  # noqa: E501
        """api_instrument_instrument_str_periods_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_instrument_str_periods_get_with_http_info(instrument_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_str: (required)
        :return: dict(str, PeriodResponseDto)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instrument_str']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_instrument_instrument_str_periods_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instrument_str' is set
        if ('instrument_str' not in params or
                params['instrument_str'] is None):
            raise ValueError("Missing the required parameter `instrument_str` when calling `api_instrument_instrument_str_periods_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrument_str' in params:
            path_params['instrumentStr'] = params['instrument_str']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Instrument/{instrumentStr}/periods', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, PeriodResponseDto)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_instrument_post(self, **kwargs):  # noqa: E501
        """api_instrument_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewInstrumentRequestDto body:
        :return: InstrumentResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_instrument_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_instrument_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_instrument_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_instrument_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_instrument_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewInstrumentRequestDto body:
        :return: InstrumentResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_instrument_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Instrument', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstrumentResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
