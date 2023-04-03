from python.config_file.load_servers import load_servers
from python.oas_analysis.read_open_api import read_open_api


if __name__ == '__main__':
    open_api = read_open_api('../tests_set/peliculas.yaml')

    load_servers(open_api, './copies_templates/copy.txt')