from build_schemas_resolvers.create_open_api import create_open_api
from build_schemas_resolvers.read_schemas_config_file import read_schemas
from oas_analysis.read_open_api import read_open_api

FILE_PATH = '../config_file/copies_templates/copy.txt'

if __name__ == '__main__':
    schemas = read_schemas(FILE_PATH)
    for schema in schemas:
        print(schema)
    # oas = read_open_api(f'../tests/tests_set/pet_clinic.yaml')
    # for query in oas.queries:
    #     query.description = None
    #
    # for mutation in oas.mutations:
    #     mutation.description = None
    #     if mutation.type == 'POST':
    #         mutation.type = 'post'
    #     elif mutation.type == 'PUT':
    #         mutation.type = 'put'
    #     elif mutation.type == 'DELETE':
    #         mutation.type = 'delete'
    # print(oas)

    # print(oas==open_api)


