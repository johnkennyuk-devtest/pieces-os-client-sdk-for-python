# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from pieces_os_client.models.searched_assets import SearchedAssets
from pieces_os_client.models.seeded_asset_tags import SeededAssetTags

from pieces_os_client.api_client import ApiClient
from pieces_os_client.api_response import ApiResponse
from pieces_os_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SearchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def full_text_search(self, query : Annotated[Optional[StrictStr], Field(description="This is a string that you can use to search your assets.")] = None, pseudo : Annotated[Optional[StrictBool], Field(description="This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.")] = None, **kwargs) -> SearchedAssets:  # noqa: E501
        """/search/full_text [GET]  # noqa: E501

        This will run FTS for exact search, and will NOT run fuzzy matching. This will only search the content within the   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.full_text_search(query, pseudo, async_req=True)
        >>> result = thread.get()

        :param query: This is a string that you can use to search your assets.
        :type query: str
        :param pseudo: This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.
        :type pseudo: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SearchedAssets
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the full_text_search_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.full_text_search_with_http_info(query, pseudo, **kwargs)  # noqa: E501

    @validate_arguments
    def full_text_search_with_http_info(self, query : Annotated[Optional[StrictStr], Field(description="This is a string that you can use to search your assets.")] = None, pseudo : Annotated[Optional[StrictBool], Field(description="This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/search/full_text [GET]  # noqa: E501

        This will run FTS for exact search, and will NOT run fuzzy matching. This will only search the content within the   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.full_text_search_with_http_info(query, pseudo, async_req=True)
        >>> result = thread.get()

        :param query: This is a string that you can use to search your assets.
        :type query: str
        :param pseudo: This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.
        :type pseudo: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SearchedAssets, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'pseudo'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method full_text_search" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('pseudo') is not None:  # noqa: E501
            _query_params.append(('pseudo', _params['pseudo']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {
            '200': "SearchedAssets",
            '500': "str",
        }

        return self.api_client.call_api(
            '/search/full_text', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def neural_code_search(self, query : Annotated[Optional[StrictStr], Field(description="This is a string that you can use to search your assets.")] = None, pseudo : Annotated[Optional[StrictBool], Field(description="This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.")] = None, **kwargs) -> SearchedAssets:  # noqa: E501
        """/search/neural_code [GET]  # noqa: E501

        This will run ncs on your assets. This will simply return FlattenedAssets, but will just be the assetuuids that match.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.neural_code_search(query, pseudo, async_req=True)
        >>> result = thread.get()

        :param query: This is a string that you can use to search your assets.
        :type query: str
        :param pseudo: This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.
        :type pseudo: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SearchedAssets
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the neural_code_search_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.neural_code_search_with_http_info(query, pseudo, **kwargs)  # noqa: E501

    @validate_arguments
    def neural_code_search_with_http_info(self, query : Annotated[Optional[StrictStr], Field(description="This is a string that you can use to search your assets.")] = None, pseudo : Annotated[Optional[StrictBool], Field(description="This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/search/neural_code [GET]  # noqa: E501

        This will run ncs on your assets. This will simply return FlattenedAssets, but will just be the assetuuids that match.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.neural_code_search_with_http_info(query, pseudo, async_req=True)
        >>> result = thread.get()

        :param query: This is a string that you can use to search your assets.
        :type query: str
        :param pseudo: This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.
        :type pseudo: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SearchedAssets, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query',
            'pseudo'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method neural_code_search" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('pseudo') is not None:  # noqa: E501
            _query_params.append(('pseudo', _params['pseudo']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {
            '200': "SearchedAssets",
            '500': "str",
        }

        return self.api_client.call_api(
            '/search/neural_code', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def tag_based_search(self, pseudo : Annotated[Optional[StrictBool], Field(description="This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.")] = None, seeded_asset_tags : Optional[SeededAssetTags] = None, **kwargs) -> SearchedAssets:  # noqa: E501
        """/search/tag_based [POST]  # noqa: E501

        This will run our tag based search, and return the assets that best match your passed in tags. This will simply return FlattenedAssets, but will just be the assetuuids that match.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.tag_based_search(pseudo, seeded_asset_tags, async_req=True)
        >>> result = thread.get()

        :param pseudo: This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.
        :type pseudo: bool
        :param seeded_asset_tags:
        :type seeded_asset_tags: SeededAssetTags
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SearchedAssets
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the tag_based_search_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.tag_based_search_with_http_info(pseudo, seeded_asset_tags, **kwargs)  # noqa: E501

    @validate_arguments
    def tag_based_search_with_http_info(self, pseudo : Annotated[Optional[StrictBool], Field(description="This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.")] = None, seeded_asset_tags : Optional[SeededAssetTags] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/search/tag_based [POST]  # noqa: E501

        This will run our tag based search, and return the assets that best match your passed in tags. This will simply return FlattenedAssets, but will just be the assetuuids that match.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.tag_based_search_with_http_info(pseudo, seeded_asset_tags, async_req=True)
        >>> result = thread.get()

        :param pseudo: This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false.
        :type pseudo: bool
        :param seeded_asset_tags:
        :type seeded_asset_tags: SeededAssetTags
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SearchedAssets, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pseudo',
            'seeded_asset_tags'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_based_search" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('pseudo') is not None:  # noqa: E501
            _query_params.append(('pseudo', _params['pseudo']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['seeded_asset_tags'] is not None:
            _body_params = _params['seeded_asset_tags']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['application']  # noqa: E501

        _response_types_map = {
            '200': "SearchedAssets",
            '500': "str",
        }

        return self.api_client.call_api(
            '/search/tag_based', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
