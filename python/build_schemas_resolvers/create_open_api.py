from build_schemas_resolvers.read_mutations_config_file import read_mutations_config_file
from build_schemas_resolvers.read_quieres_config_file import read_queires_config_file
from build_schemas_resolvers.read_servers_config_file import read_servers_config_file
from classes import OpenAPI



def create_open_api(file_path: str) -> OpenAPI:
    mutations = read_mutations_config_file(file_path)
    queries = read_queires_config_file(file_path)
    servers = read_servers_config_file(file_path)

    return OpenAPI(mutations=mutations, queries=queries, servers=servers)