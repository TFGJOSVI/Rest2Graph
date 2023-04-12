from classes import OpenAPI
from config_file.utils import replace

FILE_PATH = './templates/config_template_v1.txt'


def load_servers(open_api: OpenAPI, new_file_path: str) -> str:

    servers = open_api.servers

    string_replace = ''

    for server in servers:
        string_replace += f'\t- {server}\n'

    # replace(FILE_PATH, new_file_path, 'sub_servers', string_replace)

    return string_replace
