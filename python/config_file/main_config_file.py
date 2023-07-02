from python.config_file.create_config_file import create_config_file
from python.oas_analysis.read_open_api import read_open_api


if __name__ == '__main__':
    # open_api = read_open_api('../tests_set/configuration_API.yaml')
    # oas = load_oas('../tests_set/configuration_API.yaml')
    #
    # load_schemas(open_api, './copies_templates/copy.txt', oas)
    # # load_servers(open_api, './copies_templates/copy.txt')
    # # load_queries(open_api, './copies_templates/copy.txt')
    # # load_mutations(open_api, './copies_templates/copy.txt')
    print(read_open_api('../tests/tests_set/pet_clinic.yaml').queries)
    for query in read_open_api('../tests/tests_set/pet_clinic.yaml').queries:
        print(query.parameters)

    create_config_file('../tests/tests_set/pet_clinic.yaml', './copies_templates/copy.txt')
