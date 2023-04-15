from classes import OpenAPI
from config_file.utils import replace, parse_schema, parse_parameters

FILE_PATH = 'templates/config_template_v1.txt'


def load_queries(open_api: OpenAPI, new_file_path: str) -> str:

    queries = open_api.queries

    string_replace = ''

    for query in queries:
        name = query.name
        response = parse_schema(query.response)
        if len(query.parameters) > 0:
            parameters = parse_parameters(query.parameters)
            string_replace += f'\t- {name}({parameters}) : {response}\n'
        else:
            string_replace += f'\t- {name}: {response}\n'

        url = f'\t\t- url: GET {query.url}\n'
        string_replace += url

    # replace(FILE_PATH, new_file_path, 'sub_queries', string_replace)

    return string_replace









