import os
import sys

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from python.build_schemas_resolvers.read_mutations_config_file import read_mutations_config_file
from python.build_schemas_resolvers.read_quieres_config_file import read_queires_config_file
from python.build_schemas_resolvers.read_schemas_config_file import read_schemas
from python.build_schemas_resolvers.read_servers_config_file import read_servers_config_file
from python.config_file.create_config_file import create_config_file
from python.oas_analysis.read_open_api import read_open_api
from python.oas_analysis.read_schemas import read_schema
from python.build_schemas_resolvers.build_resolvers import build_resolvers
from python.build_schemas_resolvers.create_open_api import create_open_api
from python.build_schemas_resolvers.write_resolvers import write_resolvers
from python.build_schemas_resolvers.write_schemas import write_schemas_string_build
from python.build_schemas_resolvers.create_source_code import create_source_code
from python.paths import TESTS_SET_PATH, COPIES_TEMPLATE_PATH, INDEX_JS, SOURCE_CODE_RETURN_ZIP


class TestBuildSchemasResolvers:

    def setup_class(cls):

        oas_ady = {
            'name': 'adyen_developer_experience_team.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'adyen_developer_experience_team.yaml')),
            'mutation_resolvers': '\t post-checkAccountHolder: (root, args) => post(`https://cal-test.adyen.com/cal/services/Account/v6/checkAccountHolder?`,args),\n',
            'mutations': '\t post-checkAccountHolder(input: InputPerformVerificationRequest): GenericResponse,\n',
            'schema': '\ttype DeletePayoutMethodRequest {\n\t\taccountHolderCode: String!\n\t\tpayoutMethodCodes: [String]!\n\t}'

        }
        oas_config = {
            'name': 'configuration_API.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'configuration_API.yaml')),
            'query_resolvers': '\t get-accountHolders-id: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders/${args.id}?`),\n',
            'mutation_resolvers':'\t post-accountHolders: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders?`,args),\n',
            'queries': '\t get-accountHolders-id(id: String!): AccountHolder,\n',
            'mutations': '\t post-accountHolders(input: InputAccountHolderInfo): AccountHolder,\n',
            'schema': '\ttype PaginatedAccountHoldersResponse {\n\t\taccountHolders: [AccountHolder]!\n\t\thasNext: Boolean!\n\t\thasPrevious: Boolean!\n\t}'
        }
        oas_pel = {
            'name': 'peliculas.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'peliculas.yaml')),
            'query_resolvers': '\t getDirectores: (root, args) => get(`http://localhost:8000/directores?`),\n',
            'mutation_resolvers': '\t postDirectores: (root, args) => post(`http://localhost:8000/directores?`,args),\n',
            'queries': '\t getDirectores: [Director],\n',
            'mutations': '\t postDirectores(input: InputDirector): Director,\n',
            'schema': '\ttype Pelicula {\n\t\tid: Int\n\t\tnombre: String\n\t\tdescripcion: String\n\t\tanyo: Int\n\t\tdirector: Int\n\t\tcategoria: Int\n\t}'
        }
        oas_pet = {
            'name': 'pet_clinic.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'pet_clinic.yaml')),
            'query_resolvers': "\t findPetsByStatus: (root, args) => get(`https://petstore3.swagger.io/api/v3/pet/findByStatus?${'status='+ args.status ? args.status : ''}`),\n",
            'mutation_resolvers': '\t updatePet: (root, args) => put(`https://petstore3.swagger.io/api/v3/pet?`,args),\n',
            'queries': '\t findPetsByStatus(status: String): [Pet],\n',
            'mutations': '\t updatePet(input: InputPet): Pet,\n',
            'schema': '\ttype ApiResponse {\n\t\tcode: Int\n\t\ttype: String\n\t\tmessage: String\n\t}'
        }

        cls.oas_list = [oas_pet, oas_pel, oas_ady, oas_config]


    def test_read_servers_config_file(self):

        for i in self.oas_list:
            create_config_file(os.path.join(TESTS_SET_PATH, i['name']), COPIES_TEMPLATE_PATH)

            servers = read_servers_config_file(COPIES_TEMPLATE_PATH)

            assert servers == i['oas'].servers


    def test_read_queries_config_file(self):

        for i in self.oas_list:
            create_config_file(os.path.join(TESTS_SET_PATH, i['name']), COPIES_TEMPLATE_PATH)

            queries = read_queires_config_file(COPIES_TEMPLATE_PATH)

            for query in i['oas'].queries:
                query.description = None
                if query.response:
                    attributes = query.response.schema.component.attributes
                    for attribute in attributes:
                        attribute.ref_schema = None

                    if query.response.schema.type == 'object':
                        query.response.schema.type = query.response.schema.component.name


            assert str(queries) in str(i['oas'].queries)


    def test_read_mutations_config_file(self):

        for i in self.oas_list:
            create_config_file(os.path.join(TESTS_SET_PATH, i['name']), COPIES_TEMPLATE_PATH)

            mutations = read_mutations_config_file(COPIES_TEMPLATE_PATH)

            for mutation in i['oas'].mutations:
                mutation.description = None

                if mutation.type == 'post':
                    mutation.type = 'POST'
                elif mutation.type == 'put':
                    mutation.type = 'PUT'
                elif mutation.type == 'delete':
                    mutation.type = 'DELETE'

                if mutation.response:
                    attributes = mutation.response.schema.component.attributes
                    for attribute in attributes:
                        attribute.ref_schema = None

                    if mutation.response.schema.type == 'object':
                        mutation.response.schema.type = mutation.response.schema.component.name


                if mutation.request:


                    if mutation.request.schema.type == '_OBJECT_STRING':
                        mutation.request.schema.type = '_OBJECT_STRING'
                    elif mutation.request.schema.type == '_OBJECT_INTEGER':
                        mutation.request.schema.type = '_OBJECT_INTEGER'
                    elif mutation.request.schema.type == '_OBJECT_BOOLEAN':
                        mutation.request.schema.type = '_OBJECT_BOOLEAN'
                    elif mutation.request.schema.type == '_OBJECT_NUMBER':
                        mutation.request.schema.type = '_OBJECT_NUMBER'
                    elif mutation.request.schema.type == 'array':
                        mutation.request.schema.type = 'array'
                    else:
                        mutation.request.schema.type = mutation.request.schema.component.name

                    attributes = mutation.request.schema.component.attributes
                    for attribute in attributes:
                        attribute.ref_schema = None
                        if attribute.type == 'object':
                            attribute.type = f'Input{attribute.type}'




                    if mutation.request.schema.type == 'object':
                        mutation.request.schema.type = f'Input{mutation.request.schema.component.name}'

            assert str(mutations).replace("Input","") == str(i['oas'].mutations).replace("Input","")

    def test_build_resolvers(self):

        for i in self.oas_list:
            open_api = create_open_api(os.path.join(TESTS_SET_PATH, i['name']))

            resolvers = build_resolvers(open_api)

            if 'query_resolvers' in i:
                assert i['query_resolvers'] in resolvers['query_resolvers']

            if 'mutation_resolvers' in i:
                assert i['mutation_resolvers'] in resolvers['mutation_resolvers']

            if 'queries' in i:
                assert i['queries'] in resolvers['queries']

            if 'mutations' in i:
                assert i['mutations'] in resolvers['mutations']

    def test_write_resolvers(self):

        for i in self.oas_list:
            open_api = create_open_api(os.path.join(TESTS_SET_PATH, i['name']))

            write_resolvers(open_api)

            with open(INDEX_JS, 'r') as f:
                index_js = f.read()

            if 'query_resolvers' in i:
                assert i['query_resolvers'] in index_js

            if 'mutation_resolvers' in i:
                assert i['mutation_resolvers'] in index_js

            if 'queries' in i:
                assert i['queries'] in index_js

            if 'mutations' in i:
                assert i['mutations'] in index_js

    def test_write_schemas(self):

        for i in self.oas_list:
            open_api = create_open_api(os.path.join(TESTS_SET_PATH, i['name']))

            schemas = set()

            for query in open_api.queries:
                if query.response:
                    schemas.add(query.response.schema)

            for mutation in open_api.mutations:
                if mutation.response:
                    schemas.add(mutation.response.schema)
                if mutation.request:
                    schemas.add(mutation.request.schema)

            schema = write_schemas_string_build(list(schemas))

            assert i['schema'] in schema

    def test_create_source_code(self):

        for i in self.oas_list:
            create_source_code(os.path.join(TESTS_SET_PATH, i['name']))

            assert os.path.exists(SOURCE_CODE_RETURN_ZIP)



