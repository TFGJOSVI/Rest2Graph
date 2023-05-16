import os

from config_file.load_mutations import load_mutations
from oas_analysis.utils import load_oas
from python.paths import TESTS_SET_PATH, COPIES_TEMPLATE_PATH
from python.oas_analysis.read_open_api import read_open_api as read_oas
from python.config_file.load_servers import load_servers
from python.config_file.load_schemas import load_schemas
from python.config_file.load_queries import load_queries
from python.config_file.create_config_file import create_config_file



class TestConfigFile:
    def setup_class(cls):

        oas_ady = {
            'name': 'adyen_developer_experience_team.yaml',
            'servers': '\t- https://cal-test.adyen.com/cal/services/Account/v6\n',
            'schemas': '\tinput InputGetUploadedDocumentsRequest {\n\t\taccountHolderCode: String!\n\t\tbankAccountUUID: String\n\t\tshareholderCode: String\n\t}',
            'queries': '',
            'mutations': '\t- post-checkAccountHolder: GenericResponse\n\t\t- url: POST /checkAccountHolder\n\t\t- request_body: InputPerformVerificationRequest'
        }

        oas_auth = {
            'name': 'authentiq_team.yaml',
            'servers': '\t- https://6-dot-authentiqio.appspot.com\n',
            'schemas': '\ttype JWT {\n\t\texp: Int\n\t\tfield: String\n\t\tsub: String\n\t}',
            'queries':  '\t- key_retrieve(PK: String!): JWT\n\t\t- url: GET /key/{PK}\n',
            'mutations': '\t- key_register: ObjectObject\n\t\t- url: POST /key\n\t\t- request_body: InputAuthentiqID'

        }

        oas_config = {
            'name': 'configuration_API.yaml',
            'servers': '\t- https://balanceplatform-api-test.adyen.com/bcl/v2\n',
            'schemas': '\ttype PaginatedBalanceAccountsResponse {\n\t\tbalanceAccounts: [BalanceAccount]!\n\t\thasNext: Boolean!\n\t\thasPrevious: Boolean!\n\t}',
            'queries': '\t- get-accountHolders-id(id: String!): AccountHolder\n\t\t- url: GET /accountHolders/{id}',
            'mutations': '\t- post-accountHolders: AccountHolder\n\t\t- url: POST /accountHolders\n\t\t- request_body: InputAccountHolderInfo'
        }

        oas_pel = {
            'name': 'peliculas.yaml',
            'servers': '\t- http://localhost:8000\n\t- http://127.0.0.0:8080\n',
            'schemas': '\ttype Pelicula {\n\t\tid: Int\n\t\tnombre: String\n\t\tdescripcion: String\n\t\tanyo: Int\n\t\tdirector: Int\n\t\tcategoria: Int\n\t}',
            'queries': '\t- getDirectores: [Director]\n\t\t- url: GET /directores',
            'mutations': '\t- postDirectores: Director\n\t\t- url: POST /directores\n\t\t- request_body: InputDirector'
        }

        oas_pet = {
            'name': 'pet_clinic.yaml',
            'servers': '\t- https://petstore3.swagger.io/api/v3\n',
            'schemas': '\ttype Pet {\n\t\tid: Int\n\t\tname: String!\n\t\tcategory: Category\n\t\tphotoUrls: [String]!\n\t\ttags: [Tag]\n\t\tstatus: String\n\t}',
            'queries': '\t- findPetsByStatus(): [Pet]\n\t\t- url: GET /pet/findByStatus\n\t\t- query_parameters:\n\t\t\t- status: string\n',
            'mutations': '\t- updatePet: Pet\n\t\t- url: PUT /pet\n\t\t- request_body: InputPet'
        }

        cls.oas_list = [oas_pet, oas_auth, oas_config, oas_pel, oas_ady]

    def test_load_servers(self):

        for i in self.oas_list:
            oas = os.path.join(TESTS_SET_PATH, i['name'])

            open_api = read_oas(oas)

            servers = load_servers(open_api)

            assert servers == i['servers']

    def test_load_schemas(self):

        for i in self.oas_list:
            oas = os.path.join(TESTS_SET_PATH, i['name'])

            open_api = read_oas(oas)

            schemas = load_schemas(open_api, load_oas(oas))

            assert i['schemas'] in schemas

    def test_load_queries(self):

        for i in self.oas_list:
            oas = os.path.join(TESTS_SET_PATH, i['name'])

            open_api = read_oas(oas)

            queries = load_queries(open_api)

            assert i['queries'] in queries

    def test_load_mutations(self):

        for i in self.oas_list:
            oas = os.path.join(TESTS_SET_PATH, i['name'])

            open_api = read_oas(oas)

            mutations = load_mutations(open_api)

            assert i['mutations'] in mutations

    def test_create_config_file(self):

            for i in self.oas_list:
                oas = os.path.join(TESTS_SET_PATH, i['name'])

                path_config = os.path.join(COPIES_TEMPLATE_PATH, f"copy-{i['name']}.txt")

                create_config_file(oas, path_config)

                assert os.path.exists(path_config)

                os.remove(path_config)

