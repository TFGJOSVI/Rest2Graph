from python.classes import OpenAPI


def load_servers(open_api: OpenAPI) -> str:

    """
    Load the servers from the OpenAPI specification.
    :param open_api:
        An OpenAPI instance where includes the servers, queries and mutations.
    :return:
        A string containing the servers.
    """

    servers = open_api.servers

    string_replace = ''

    for server in servers:
        string_replace += f'\t- {server}\n'

    return string_replace
