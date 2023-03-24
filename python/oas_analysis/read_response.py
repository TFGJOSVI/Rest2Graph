import re

from python.classes import Response
from python.oas_analysis.read_schemas import read_schema


def read_response(method, oas):
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
