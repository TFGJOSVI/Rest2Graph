import re
from typing import Union

from python.classes import Response
from python.oas_analysis.read_schemas import read_schema


def read_response(method: dict, oas: dict) -> Union[Response, None]:
    """
    Reads the definition of a response and converts it into a `Response` instance.

    :param method:
        A dictionary that should contain responses, parameters ... and other fields that are part of the OpenAPI.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        An instance of the `Response` class, or None if response does not contain 20X code.
    """

    response = method.get('responses', {})

    status_codes = list(response.keys())

    if len(status_codes) > 1:
        positive_status_codes = list(filter(lambda x: re.match(r'^20\d$', x), status_codes))
    else:
        positive_status_codes = status_codes

    for status_code in positive_status_codes:

        if 'content' in response[status_code]:
            contents = response[status_code]['content']
        else:
            return None

        json_content = list(filter(lambda x: x == 'application/json', contents.keys()))

        if len(json_content) > 0:
            schema = contents[json_content[0]]
            schema = read_schema(schema, oas)

            return Response(schema=schema)
        else:
            for c in contents:
                if 'schema' in contents[c]:
                    schema = contents[c]
                    schema = read_schema(schema, oas)

                    return Response(schema=schema)

    return None
