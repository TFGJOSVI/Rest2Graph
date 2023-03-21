from python.classes import RequestBody
from python.oas_analysis.main_oas_analysis import parse_ref
from python.oas_analysis.read_parameters import search_ref
from python.oas_analysis.read_schemas import read_schema


def read_requestBody(requestBody, oas):

    if 'content' in requestBody:
        content = requestBody['content']
        first_key = list(content.keys())[0]
        print(content[first_key]['schema'])
        schema = read_schema(content[first_key]['schema'], oas)
        required = requestBody.get('required', False)
        return RequestBody(required, schema)
    elif '$ref' in requestBody:
        print(requestBody)
        ref = requestBody['$ref']
        ref = search_ref(oas, ref)
        print(ref)
        return read_requestBody(ref, oas)