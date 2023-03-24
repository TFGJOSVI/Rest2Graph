from python.classes import RequestBody
from python.oas_analysis.read_parameters import search_ref
from python.oas_analysis.read_schemas import read_schema


def read_request_body(request_body, oas):
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


def get_request_bodies(method, oas):
    requestBody = method.get('requestBody', None)
    if requestBody:
        return read_request_body(requestBody, oas)
    else:
        return None
