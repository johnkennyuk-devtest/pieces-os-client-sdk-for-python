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

from pieces_client.models.analysis import Analysis
from pieces_client.models.format import Format
from pieces_client.models.format_reclassification import FormatReclassification
from pieces_client.models.seeded_tracked_format_event import SeededTrackedFormatEvent
from pieces_client.models.tracked_format_event import TrackedFormatEvent

from pieces_client.api_client import ApiClient
from pieces_client.api_response import ApiResponse
from pieces_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FormatApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def format_analysis(self, format : Annotated[StrictStr, Field(..., description="The id (uuid) for a specific format.")], **kwargs) -> Analysis:  # noqa: E501
        """/format/{format}/analysis [GET]  # noqa: E501

        This will get an analysis from a format's id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_analysis(format, async_req=True)
        >>> result = thread.get()

        :param format: The id (uuid) for a specific format. (required)
        :type format: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Analysis
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the format_analysis_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.format_analysis_with_http_info(format, **kwargs)  # noqa: E501

    @validate_arguments
    def format_analysis_with_http_info(self, format : Annotated[StrictStr, Field(..., description="The id (uuid) for a specific format.")], **kwargs) -> ApiResponse:  # noqa: E501
        """/format/{format}/analysis [GET]  # noqa: E501

        This will get an analysis from a format's id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_analysis_with_http_info(format, async_req=True)
        >>> result = thread.get()

        :param format: The id (uuid) for a specific format. (required)
        :type format: str
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
        :rtype: tuple(Analysis, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'format'
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
                    " to method format_analysis" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['format']:
            _path_params['format'] = _params['format']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Analysis",
            '500': "str",
        }

        return self.api_client.call_api(
            '/format/{format}/analysis', 'GET',
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
    def format_reclassify(self, transferable : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, format_reclassification : Optional[FormatReclassification] = None, **kwargs) -> Format:  # noqa: E501
        """/format/reclassify [POST]  # noqa: E501

        This endpoint will be used to reclassify a single Format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_reclassify(transferable, format_reclassification, async_req=True)
        >>> result = thread.get()

        :param transferable: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferable: bool
        :param format_reclassification:
        :type format_reclassification: FormatReclassification
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Format
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the format_reclassify_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.format_reclassify_with_http_info(transferable, format_reclassification, **kwargs)  # noqa: E501

    @validate_arguments
    def format_reclassify_with_http_info(self, transferable : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, format_reclassification : Optional[FormatReclassification] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/format/reclassify [POST]  # noqa: E501

        This endpoint will be used to reclassify a single Format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_reclassify_with_http_info(transferable, format_reclassification, async_req=True)
        >>> result = thread.get()

        :param transferable: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferable: bool
        :param format_reclassification:
        :type format_reclassification: FormatReclassification
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
        :rtype: tuple(Format, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferable',
            'format_reclassification'
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
                    " to method format_reclassify" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferable') is not None:  # noqa: E501
            _query_params.append(('transferable', _params['transferable']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['format_reclassification'] is not None:
            _body_params = _params['format_reclassification']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Format",
        }

        return self.api_client.call_api(
            '/format/reclassify', 'POST',
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
    def format_snapshot(self, format : Annotated[StrictStr, Field(..., description="The id (uuid) for a specific format.")], transferable : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, **kwargs) -> Format:  # noqa: E501
        """/format/{format} [GET] Scoped to Format  # noqa: E501

        Get a snapshot of a specific format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_snapshot(format, transferable, async_req=True)
        >>> result = thread.get()

        :param format: The id (uuid) for a specific format. (required)
        :type format: str
        :param transferable: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferable: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Format
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the format_snapshot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.format_snapshot_with_http_info(format, transferable, **kwargs)  # noqa: E501

    @validate_arguments
    def format_snapshot_with_http_info(self, format : Annotated[StrictStr, Field(..., description="The id (uuid) for a specific format.")], transferable : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/format/{format} [GET] Scoped to Format  # noqa: E501

        Get a snapshot of a specific format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_snapshot_with_http_info(format, transferable, async_req=True)
        >>> result = thread.get()

        :param format: The id (uuid) for a specific format. (required)
        :type format: str
        :param transferable: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferable: bool
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
        :rtype: tuple(Format, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'format',
            'transferable'
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
                    " to method format_snapshot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['format']:
            _path_params['format'] = _params['format']


        # process the query parameters
        _query_params = []
        if _params.get('transferable') is not None:  # noqa: E501
            _query_params.append(('transferable', _params['transferable']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Format",
        }

        return self.api_client.call_api(
            '/format/{format}', 'GET',
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
    def format_update_value(self, transferable : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, format : Annotated[Optional[Format], Field(description="This is the format that you want to update.")] = None, **kwargs) -> Format:  # noqa: E501
        """[POST] /format/update/value  # noqa: E501

        This will update a format's value, ie, a formats fragment or file depending on what is provided.  code/text fragment behavior: If this format is an asset.preview.base we will update the asset.original's value. if this format is an asset.preview.original we will update the asset.preview.base's value.  code/text file behavior: If the the format that is update is the asset.preview.base is a fragment and the asset.original is file then we will update the asset.original's value to be bytes or string respectively. This goes the same for orignal to preview but will be go the reverse order so if the original is a file we will update the preview base's fragment string.  image fragment/file: We will not modify preview -> orignal or original -> preview here. so there are zero side effects in this case, and will update as normal. (this will be the case for all other value updates.)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_update_value(transferable, format, async_req=True)
        >>> result = thread.get()

        :param transferable: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferable: bool
        :param format: This is the format that you want to update.
        :type format: Format
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Format
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the format_update_value_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.format_update_value_with_http_info(transferable, format, **kwargs)  # noqa: E501

    @validate_arguments
    def format_update_value_with_http_info(self, transferable : Annotated[Optional[StrictBool], Field(description="This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)")] = None, format : Annotated[Optional[Format], Field(description="This is the format that you want to update.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[POST] /format/update/value  # noqa: E501

        This will update a format's value, ie, a formats fragment or file depending on what is provided.  code/text fragment behavior: If this format is an asset.preview.base we will update the asset.original's value. if this format is an asset.preview.original we will update the asset.preview.base's value.  code/text file behavior: If the the format that is update is the asset.preview.base is a fragment and the asset.original is file then we will update the asset.original's value to be bytes or string respectively. This goes the same for orignal to preview but will be go the reverse order so if the original is a file we will update the preview base's fragment string.  image fragment/file: We will not modify preview -> orignal or original -> preview here. so there are zero side effects in this case, and will update as normal. (this will be the case for all other value updates.)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_update_value_with_http_info(transferable, format, async_req=True)
        >>> result = thread.get()

        :param transferable: This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement)
        :type transferable: bool
        :param format: This is the format that you want to update.
        :type format: Format
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
        :rtype: tuple(Format, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'transferable',
            'format'
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
                    " to method format_update_value" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('transferable') is not None:  # noqa: E501
            _query_params.append(('transferable', _params['transferable']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['format'] is not None:
            _body_params = _params['format']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Format",
            '500': "str",
        }

        return self.api_client.call_api(
            '/format/update/value', 'POST',
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
    def format_usage_event(self, seeded_tracked_format_event : Annotated[Optional[SeededTrackedFormatEvent], Field(description="This is a SeededTrackedFormatEvent, per tracked event:)")] = None, **kwargs) -> TrackedFormatEvent:  # noqa: E501
        """/format/usage/event [POST] Scoped to Format  # noqa: E501

        This is an analytics endpoint that will enable us to know when a user has copied/downloaded/beamed/viewed a format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_usage_event(seeded_tracked_format_event, async_req=True)
        >>> result = thread.get()

        :param seeded_tracked_format_event: This is a SeededTrackedFormatEvent, per tracked event:)
        :type seeded_tracked_format_event: SeededTrackedFormatEvent
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TrackedFormatEvent
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the format_usage_event_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.format_usage_event_with_http_info(seeded_tracked_format_event, **kwargs)  # noqa: E501

    @validate_arguments
    def format_usage_event_with_http_info(self, seeded_tracked_format_event : Annotated[Optional[SeededTrackedFormatEvent], Field(description="This is a SeededTrackedFormatEvent, per tracked event:)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/format/usage/event [POST] Scoped to Format  # noqa: E501

        This is an analytics endpoint that will enable us to know when a user has copied/downloaded/beamed/viewed a format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.format_usage_event_with_http_info(seeded_tracked_format_event, async_req=True)
        >>> result = thread.get()

        :param seeded_tracked_format_event: This is a SeededTrackedFormatEvent, per tracked event:)
        :type seeded_tracked_format_event: SeededTrackedFormatEvent
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
        :rtype: tuple(TrackedFormatEvent, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'seeded_tracked_format_event'
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
                    " to method format_usage_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['seeded_tracked_format_event'] is not None:
            _body_params = _params['seeded_tracked_format_event']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "TrackedFormatEvent",
        }

        return self.api_client.call_api(
            '/format/usage/event', 'POST',
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