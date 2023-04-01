from python.classes import OpenAPI
from python.oas_analysis.read_methods import read_methods

from utils import load_oas


def read_servers(oas: str) -> list[str]:
    """
    Read the servers from the OpenAPI specification.

    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        A list of servers.

    """

    servers = oas.get('servers', [])
    res = []
    if len(servers) > 0:
        for server in servers:
            res.append(server['url'])
    return res


def read_open_api(oas_path: str) -> OpenAPI:
    """
    Read the OpenAPI specification.

    :param oas_path:
        The path to the OpenAPI specification.
    :return:
        An OpenAPI instance where includes the servers, queries and mutations.
    """

    oas = load_oas(oas_path)

    servers = read_servers(oas)
    methods = read_methods(oas)
    queries = methods['Query']
    mutations = methods['Mutation']
    return OpenAPI(servers=servers, queries=queries, mutations=mutations)
