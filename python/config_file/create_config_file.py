from python.config_file.load_schemas import load_schemas
from python.config_file.load_mutations import load_mutations
from python.config_file.load_queries import load_queries
from python.config_file.load_servers import load_servers
from python.config_file.utils import replace
from python.oas_analysis.read_open_api import read_open_api
from python.oas_analysis.utils import load_oas
from python.paths import CONFIG_FILE_TEMPLATE as FILE_PATH


def create_config_file(oas_path: str, new_file_path: str) -> None:
    open_api = read_open_api(oas_path)
    oas = load_oas(oas_path)

    servers = load_servers(open_api)
    schemas = load_schemas(open_api, oas)
    queries = load_queries(open_api)
    mutations = load_mutations(open_api)

    replace(FILE_PATH, new_file_path, 'sub_servers', servers)
    replace(new_file_path, None, 'sub_types', schemas, False)
    replace(new_file_path, None, 'sub_queries', queries, False)
    replace(new_file_path, None, 'sub_mutations', mutations, False)
