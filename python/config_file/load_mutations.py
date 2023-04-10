from python.classes import OpenAPI
from python.config_file.utils import parse_schema, parse_parameters, replace

FILE_PATH = './templates/config_template_v1.txt'


def load_mutations(open_api: OpenAPI, new_file_path: str) -> None:

    mutations = open_api.mutations

    string_replace = ''

    for mutation in mutations:
        print(mutation)
        name = mutation.name
        response = parse_schema(mutation.response)
        if len(mutation.parameters) > 0:
            parameters = parse_parameters(mutation.parameters)
            string_replace += f'\t- {name}({parameters}) : {response}\n'
        else:
            string_replace += f'\t- {name}: {response}\n'

        url = f'\t\t- url: {mutation.type.upper()} {mutation.url}\n'
        string_replace += url

        request_body = parse_schema(mutation.request)
        if request_body:
            string_replace += f'\t\t- request_body: Input{request_body}\n'


    replace(FILE_PATH, new_file_path, 'sub_mutations', string_replace)