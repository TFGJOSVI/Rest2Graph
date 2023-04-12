from config_file.load_schemas import load_schemas
from config_file.load_mutations import load_mutations
from config_file.load_queries import load_queries
from config_file.load_servers import load_servers
from config_file.utils import replace
from oas_analysis.read_open_api import read_open_api
from oas_analysis.utils import load_oas

FILE_PATH = './templates/config_template_v1.txt'


def create_config_file(oas_path: str, new_file_path: str) -> None:
    open_api = read_open_api(oas_path)
    oas = load_oas(oas_path)

    servers = load_servers(open_api, new_file_path)
    schemas = load_schemas(open_api, new_file_path, oas)
    queries = load_queries(open_api, new_file_path)
    mutations = load_mutations(open_api, new_file_path)

    replace(FILE_PATH, new_file_path, 'sub_servers', servers)
    replace(new_file_path, None, 'sub_types', schemas, False)
    replace(new_file_path, None, 'sub_queries', queries, False)
    replace(new_file_path, None, 'sub_mutations', mutations, False)

