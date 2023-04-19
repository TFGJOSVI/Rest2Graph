from build_schemas_resolvers.create_open_api import create_open_api
from oas_analysis.read_open_api import read_open_api

FILE_PATH = '../config_file/copies_templates/copy.txt'

if __name__ == '__main__':
    open_api = create_open_api(FILE_PATH)
    print(open_api)
    oas = read_open_api(f'../tests/tests_set/pet_clinic.yaml')
    for query in oas.queries:
        query.description = None

    for mutation in oas.mutations:
        mutation.description = None
        if mutation.type == 'POST':
            mutation.type = 'post'
        elif mutation.type == 'PUT':
            mutation.type = 'put'
        elif mutation.type == 'DELETE':
            mutation.type = 'delete'
    print(oas)

    print(oas==open_api)


