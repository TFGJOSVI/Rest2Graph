from python.config_file.create_config_file import create_config_file
from python.build_schemas_resolvers.read_mutations_config_file import read_mutations_config_file
from python.build_schemas_resolvers.read_quieres_config_file import read_queires_config_file
from python.build_schemas_resolvers.read_servers_config_file import read_servers_config_file
from python.build_schemas_resolvers.read_schemas_config_file import read_schemas
from classes import OpenAPI
from python.paths import COPIES_TEMPLATE_PATH as file_path



def create_open_api(oas_path:str) -> OpenAPI:

    create_config_file(oas_path, file_path)

    mutations = read_mutations_config_file(file_path)
    queries = read_queires_config_file(file_path)
    servers = read_servers_config_file(file_path)
    schemas = read_schemas(file_path)

    return OpenAPI(mutations=mutations, queries=queries, servers=servers, schemas=schemas)

def create_open_api_not_default_path(dst_path: str) -> OpenAPI:

    mutations = read_mutations_config_file(dst_path)
    queries = read_queires_config_file(dst_path)
    servers = read_servers_config_file(dst_path)
    schemas = read_schemas(dst_path)

    return OpenAPI(mutations=mutations, queries=queries, servers=servers, schemas=schemas)

