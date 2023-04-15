from typing import Union

from python.classes import Query, Mutation
from python.oas_analysis.read_parameters import read_parameters
from python.oas_analysis.read_requets_body import read_request_body
from python.oas_analysis.read_response import read_response


def read_method(method: dict, oas: dict, url: str, method_type: str = 'get') -> Union[Query, Mutation]:
    """
    Reads the definition of an HTTP method and converts it into a `Query` or `Mutation` instance, depending on the type.
    of request.

    :param  method:
        A dictionary that should contain requestBody, response ... and other fields that are part of the OpenAPI
        specification.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :param url: str
        The URL of the API to which the method refers.
    :param method_type: str, optional
        The type of HTTP request to be made. Default is 'get', but can also be 'post', 'put', or 'delete'.
    :return:
        An instance of the `Query` or `Mutation` class, depending on the type of request.
    """

    description = method.get('description', None)
    if description is None:
        description = method.get('summary', '')

    parameters = read_parameters(method, oas)

    response = read_response(method, oas)

    if method_type != 'get':
        request_body = read_request_body(method, oas) if 'requestBody' in method else None
    else:
        request_body = None

    name = method.get('operationId', None)
    if name is None:
        urls = url.split('/')
        name = method_type
        for u in urls:
            if u != '':
                if u[0] == '{':
                    u = u[1:-1]
                    name += f'By{u[0].capitalize()}{u[1:]}'
                else:
                    name += f'{u[0].capitalize()}{u[1:]}'

    if method_type == 'get':
        return Query(description=description, parameters=parameters, url=url, name=name, response=response)
    else:
        return Mutation(description=description, parameters=parameters, url=url, name=name, response=response,
                        request=request_body, type=method_type)


def read_methods(oas: dict) -> dict[str, list[Union[Query, Mutation]]]:
    """
    Read all get, post, put and delete methods from an oas file.

    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        A list of Query and Mutation instances with the following structure:
        {
            'Query': [Query1, Query2, ...],
            'Mutation': [Mutation1, Mutation2, ...]
        }
    """

    methods = {
        'Query': [],
        'Mutation': []
    }
    for path in oas['paths']:
        for method in oas['paths'][path]:
            if method == 'get':
                query = read_method(oas['paths'][path][method], oas, path)
                methods['Query'].append(query)
            elif method in ['post', 'put', 'delete']:
                query = read_method(oas['paths'][path][method], oas, path, method)
                methods['Mutation'].append(query)
    return methods
