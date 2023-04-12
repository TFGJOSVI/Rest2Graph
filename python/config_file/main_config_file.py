from config_file.load_schemas import load_schemas
from oas_analysis.read_open_api import read_open_api
from oas_analysis.utils import load_oas
from config_file.create_config_file import create_config_file

if __name__ == '__main__':
    # open_api = read_open_api('../tests_set/configuration_API.yaml')
    # oas = load_oas('../tests_set/configuration_API.yaml')
    #
    # load_schemas(open_api, './copies_templates/copy.txt', oas)
    # # load_servers(open_api, './copies_templates/copy.txt')
    # # load_queries(open_api, './copies_templates/copy.txt')
    # # load_mutations(open_api, './copies_templates/copy.txt')

    create_config_file('../tests_set/configuration_API.yaml', './copies_templates/copy.txt')
