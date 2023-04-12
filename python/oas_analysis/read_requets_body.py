from typing import Union

from classes import RequestBody
from oas_analysis.read_schemas import read_schema
from oas_analysis.utils import search_ref


def read_request_body(request_body: dict, oas: dict) -> RequestBody:
    """
    Reads the definition of a request body and converts it into a `RequestBody` instance.

    :param request_body:
        A dictionary that should contain content, required ... and other fields that are part of the OpenAPI.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        An instance of the `RequestBody` class.
    """

    request_body = request_body.get('requestBody', request_body)

    if 'content' in request_body:
        content = request_body['content']
        first_key = list(content.keys())[0]
        schema = read_schema(content[first_key], oas)
        required = request_body.get('required', False)
        return RequestBody(required, schema)
    elif '$ref' in request_body:
        ref = request_body['$ref']
        ref = search_ref(oas, ref)
        return read_request_body(ref, oas)


def get_request_bodies(method: dict, oas: dict) -> Union[RequestBody, None]:
    """
    Reads all the definition of a request body and converts it into a `RequestBody` instance.

    :param method:
        A dictionary that should contain requestBody, response ... and other fields that are part of the OpenAPI
        specification.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        A list of instances of the RequestBody class, or None if it does not contain any instances.
    """

    requestBody = method.get('requestBody', None)
    if requestBody:
        return read_request_body(requestBody, oas)
    else:
        return None
