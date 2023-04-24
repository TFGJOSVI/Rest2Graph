from classes import OpenAPI
from config_file.utils import parse_schema, parse_parameters, replace, parse_parameters_query

FILE_PATH = 'templates/config_template_v1.txt'





def load_mutations(open_api: OpenAPI) -> str:

    mutations = open_api.mutations

    string_replace = ''


    for mutation in mutations:
        parameters_query = ''
        name = mutation.name
        response = parse_schema(mutation.response)
        if len(mutation.parameters) > 0:
            parameters_path = parse_parameters(mutation.parameters)
            parameters_query = parse_parameters_query(mutation.parameters)
            string_replace += f'\n\t- {name}({parameters_path}): {response}\n'
        else:
            string_replace += f'\n\t- {name}: {response}\n'

        url = f'\t\t- url: {mutation.type.upper()} {mutation.url}\n'
        string_replace += url

        request_body = parse_schema(mutation.request)

        if request_body and mutation.request.schema.type == 'array':
            string_replace += f'\t\t- request_body: {request_body}'
        elif request_body == 'String' or request_body == 'Int' or request_body == 'Boolean' or request_body == 'Float':
            string_replace += f'\t\t- request_body: {request_body}'
        elif not request_body:
            pass
        else:
            string_replace += f'\t\t- request_body: Input{request_body}'

        if request_body and mutation.request.required:
            string_replace += '!\n'
        elif request_body:
            string_replace += '\n'


        if parameters_query != '\t\t- query_parameters:':
            string_replace += f'{parameters_query}\n'



    return string_replace