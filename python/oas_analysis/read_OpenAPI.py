from python.classes import OpenAPI
from python.oas_analysis.read_methods import read_methods


def read_servers(oas):
    servers = oas.get('servers', [])
    res = []
    if len(servers) > 0:
        for server in servers:
            res.append(server['url'])
    return res




def read_OpenAPI(oas):

    servers = read_servers(oas)
    methods = read_methods(oas)
    queries = methods['Query']
    mutations = methods['Mutation']
    return OpenAPI(servers=servers, queries=queries, mutations=mutations)