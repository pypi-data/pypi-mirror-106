"""Django middleware."""

import os
import json

from typing import Union, Callable

from loguru import logger
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import get_resolver, URLPattern, URLResolver  # type: ignore

from escape_cli.static.constants import METHODS_PATH, ENDPOINTS_PATH
from escape_cli.utils.custom_types import Endpoint, Parameter, Transaction
from escape_cli.utils.result import save_transaction
from escape_cli.utils.parse import find_params, get_identifier, parse_body, parse_parameters, format_lib_to_openapi_path, interpolate_openapi_path

HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']


class GetRequestAndResponseInformation():

    """Fetch usefull information from requests and responses Save it in the transactions file."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.result: Transaction = {}
        self.get_response = get_response
        save_endpoints()

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Fetch the response after the view is called."""

        response = self.get_response(request)

        # Normally, the line above ultimately calls `process_view()` in which we process the request to save it later.
        # However for some malformed requests this `process_view()` is never called.
        # We presume that `process_view()` is the only function where we can access the params in path, but maybe some other parsed information.
        # TODO: verify the assertion in the previous sentence.
        # That's why we skill catch a maximum of info in `process_view()` but if `process_view` is never called we catch it here.
        if 'req' not in self.result:
            self.result['req'] = {
                'openApiPath': '',  # computed later
                'protocol': request.scheme,
                'host': request.get_host(),
                'route': request.path,
                'method': request.method,
                'parameters': {},
                'query': dict(request.GET.items()),
                'originalUrl': request.path,
                'headers': dict(request.headers),
                'cookies': request.COOKIES,
                'httpVersion': request.META['SERVER_PROTOCOL'].split('/')[1],
                'body': parse_body(request.body, request.content_type)}

        match = request.resolver_match
        if match:
            self.result['req']['openApiPath'] = format_lib_to_openapi_path(match.route)
        else:
            # Ultimately try iterpolation when there is no other choice…
            logger.warning(f'Cannot resolve route of {request.path}, interpolate openApiPath.')
            self.result['req']['openApiPath'] = interpolate_openapi_path(self.result['req']['originalUrl'], self.result['req']['parameters'])

        self.result['_identifier'] = get_identifier(self.result['req']['method'], self.result['req']['openApiPath'])

        res_headers = dict(response.items())
        res_body = parse_body(response.getvalue(), res_headers.get('Content-Type', ''))

        self.result['res'] = {'statusCode': response.status_code, 'messageCode': response.reason_phrase, 'headers': dict(response.items()), 'body': res_body}

        save_transaction(self.result)

        return response

    def process_view(self, request: HttpRequest, _view_func: Callable, _view_args: list, view_kwargs: dict) -> None:
        """Fetch the request before the view is called."""

        req_headers = dict(request.headers)
        req_body = parse_body(request.body, request.content_type)
        req_parameters = parse_parameters(view_kwargs)

        self.result['req'] = {
            'openApiPath': '',  # computed later
            'protocol': request.scheme,
            'host': request.get_host(),
            'route': request.path,
            'method': request.method,
            'parameters': req_parameters,
            'query': dict(request.GET.items()),
            'originalUrl': request.path,
            'headers': req_headers,
            'cookies': request.COOKIES,
            'httpVersion': request.META['SERVER_PROTOCOL'].split('/')[1],
            'body': req_body}


def save_endpoints() -> None:
    """Save ground truth endpoints."""
    # Used to ensure this code is ran only once
    if os.environ['ESCAPE_ENDPOINTS_MAPPED'] == 'False':
        os.environ['ESCAPE_ENDPOINTS_MAPPED'] = 'True'

        endpoints: list[Endpoint] = []

        endpoints = recurse_endpoints(endpoints, [get_resolver()])
        with open(ENDPOINTS_PATH, 'w') as f:
            json.dump(endpoints, f)


def recurse_endpoints(endpoints: list[Endpoint], resolvers: list[Union[URLPattern, URLResolver]], endpoint_start: str = '', parameters: list[Parameter] = None,
                      existing_routes: list[str] = None) -> list[Endpoint]:
    """Recursive function.

    Look throw the urls and save the endpoints.
    """

    existing_routes = existing_routes or []
    parameters = parameters or []

    with open(METHODS_PATH) as f:
        methods_dict = json.load(f)

    for url in resolvers:
        new_parameters = parameters + find_params(str(url.pattern), url.pattern.regex.pattern)
        lib_path = f'{endpoint_start}{url.pattern}'.lstrip('^')
        if isinstance(url, URLResolver):
            endpoints = recurse_endpoints(endpoints, url.url_patterns, lib_path, new_parameters, existing_routes)
        elif isinstance(url, URLPattern):
            openapi_path = format_lib_to_openapi_path(lib_path)

            if openapi_path not in existing_routes:  # Avoid duplicate endpoints
                existing_routes.append(openapi_path)

                handler = f'{url.callback.__module__}.{url.callback.__name__}'
                allowed_methods = HTTP_METHODS  # By default, all methods are allowed on every route in Django
                django_decorated = False
                if handler in methods_dict:  # But allowed methods can (very recommended) be restricted by @django.views.decorators.http.require_X decorator
                    allowed_methods = methods_dict[handler]
                    django_decorated = True

                for method in allowed_methods:
                    endpoints.append({
                        'openApiPath': openapi_path,
                        'libPath': lib_path,
                        'method': method,
                        'parameters': new_parameters,
                        'handler': handler,
                        'djangoDecorated': django_decorated,
                        '_identifier': get_identifier(method, openapi_path)})

    return endpoints
