from build_schemas_resolvers.read_schemas_config_file import search_schema
from build_schemas_resolvers.utils import parse_type
from classes import Parameter, Response, Mutation, RequestBody


def read_mutations_config_file(file_path: str) -> list[Mutation]:
    mutations = []
    with open(file_path, 'r') as file:

        lines = file.read()

        posicion_inicio = lines.find('mutations:')
        posicion_fin = lines.find('types:')

        contenido_deseado = lines[posicion_inicio + len('mutations'):posicion_fin]

        for query in contenido_deseado.split('\n\n\t-')[1:]:
            parameters = []
            first_line = query.splitlines()[0]
            if first_line.__contains__('('):
                name = query.splitlines()[0].split('(')[0].strip()

            else:
                name = query.splitlines()[0].split(':')[0].strip()

            if first_line.__contains__('('):
                component_name = first_line.split('):')[1].strip()
                parameters_path = first_line.split('(')[1].split(')')[0].strip()
                if parameters_path:
                    for parameter in parameters_path.split(','):
                        required = False
                        in_query = False
                        if parameter.split(':')[1].strip().__contains__('!'):
                            required = True
                            type_parameter = parse_type(parameter.split(':')[1].replace('!', '').strip())
                        else:
                            type_parameter = parse_type(parameter.split(':')[1].strip())

                        name_parameter = parameter.split(':')[0].strip()

                        parameters.append(
                            Parameter(name=name_parameter, type=type_parameter, required=required, query=in_query))

            else:
                component_name = first_line.split(': ')[1].strip()


            schema_response = search_schema(file_path, component_name)

            if schema_response:
                response = Response(schema=schema_response)
            else:
                response = None

            if 'url:' in query:
                for line in query.splitlines():
                    if line.startswith('\t\t- url:'):
                        url = line.split('url: ')[1].split(' ')[1]
                        type = line.split('url: ')[1].split(' ')[0]

            if 'query_parameters:' in query:
                for line in query.splitlines():
                    if line.startswith('\t\t\t-'):
                        name_parameter = line.split(':')[0].split('-')[1].strip()
                        type_parameter = line.split(':')[1].strip()
                        required = False
                        in_query = True
                        if type_parameter.__contains__('!'):
                            required = True

                        parameters.append(
                            Parameter(name=name_parameter, type=type_parameter, required=required, query=in_query))

            request_body = None
            if 'request_body:' in query:
                for line in query.splitlines():
                    if line.startswith('\t\t- request_body:'):
                        required = False
                        request_body = line.split('request_body:')[1].split(' ')[1]
                        if request_body.__contains__('!'):
                            required = True
                            request_body = request_body.replace('!', '')
                        if request_body.__contains__('Input'):
                            request_body = request_body.replace('Input', '')
                        schema_request = search_schema(file_path, request_body)
                        if schema_request:
                            request_body = RequestBody(schema=schema_request, required=required)



            mutations.append(Mutation(name=name, url=url, type=type, parameters=parameters, response=response,
                                      request=request_body, description=None))

    return mutations