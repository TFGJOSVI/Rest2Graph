from build_schemas_resolvers.create_open_api import create_open_api
from build_schemas_resolvers.read_schemas_config_file import read_schemas
from oas_analysis.read_open_api import read_open_api
from build_schemas_resolvers.utils import copy_dir
from python.paths import *
from build_schemas_resolvers.build_resolvers import *
from build_schemas_resolvers.write_resolvers import write_resolvers
from python.build_schemas_resolvers.utils import zip_directory

FILE_PATH = '../tests/tests_set/pet_clinic.yaml'

if __name__ == '__main__':
    # copy_dir('./source_code_base/sourceCode', './source_code_return/sourceCode')

    # schemas = read_schemas(FILE_PATH)
    # for schema in schemas:
    #     print(schema)
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

    oas = create_open_api(FILE_PATH)

    resolver = build_resolvers(oas)

    write_resolvers(oas)

    zip_directory(SOURCE_CODE_BASE_PATH, SOURCE_CODE_RETURN_ZIP)