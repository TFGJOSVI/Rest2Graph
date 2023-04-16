from classes import OpenAPI
from config_file.utils import replace

FILE_PATH = 'templates/config_template_v1.txt'


def load_servers(open_api: OpenAPI) -> str:

    servers = open_api.servers

    string_replace = ''

    for server in servers:
        string_replace += f'\t- {server}\n'

    return string_replace
