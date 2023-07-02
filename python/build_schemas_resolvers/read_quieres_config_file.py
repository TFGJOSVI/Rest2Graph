from python.build_schemas_resolvers.read_schemas_config_file import search_schema
from python.build_schemas_resolvers.utils import parse_type
from python.classes import Query, Parameter, Response


def read_queires_config_file(file_path: str) -> list[Query]:

    """
    Read the queries config file and return a list of queries.

    :param file_path:
        The path of the config file.
    :return:
        A list of queries.
    """

    queries = []
    with open(file_path, 'r') as file:

        lines = file.read()

        posicion_inicio = lines.find('queries:')
        posicion_fin = lines.find('mutations:')

        contenido_deseado = lines[posicion_inicio + len('queries'):posicion_fin]

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



            queries.append(Query(name=name, url=url, parameters=parameters, response=response, description=None))

    return queries
