from python.classes import OpenAPI
from python.config_file.utils import parse_schema, parse_parameters, parse_parameters_query


def load_queries(open_api: OpenAPI) -> str:

    """
    Load the queries from the OpenAPI specification.

    :param open_api:
        An OpenAPI instance where includes the servers, queries and mutations.
    :return:
        A string containing the queries.
    """

    queries = open_api.queries

    string_replace = ''

    for query in queries:
        parameters_query = ''
        name = query.name
        response = parse_schema(query.response)
        if len(query.parameters) > 0:
            parameters_path = parse_parameters(query.parameters)
            parameters_query = parse_parameters_query(query.parameters)
            string_replace += f'\n\t- {name}({parameters_path}): {response}\n'
        else:
            string_replace += f'\n\t- {name}: {response}\n'

        url = f'\t\t- url: GET {query.url}\n'
        string_replace += url

        if parameters_query != '\t\t- query_parameters:':
            string_replace += f'{parameters_query}\n'

    return string_replace
