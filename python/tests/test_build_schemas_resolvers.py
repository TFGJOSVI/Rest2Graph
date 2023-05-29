import os

from build_schemas_resolvers.read_mutations_config_file import read_mutations_config_file
from build_schemas_resolvers.read_quieres_config_file import read_queires_config_file
from build_schemas_resolvers.read_schemas_config_file import read_schemas
from build_schemas_resolvers.read_servers_config_file import read_servers_config_file
from config_file.create_config_file import create_config_file
from oas_analysis.read_open_api import read_open_api
from oas_analysis.read_schemas import read_schema
from paths import TESTS_SET_PATH, COPIES_TEMPLATE_PATH


class TestBuildSchemasResolvers:

    def setup_class(cls):

        oas_ady = {
            'name': 'adyen_developer_experience_team.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'adyen_developer_experience_team.yaml')),
        }
        oas_config = {
            'name': 'configuration_API.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'configuration_API.yaml')),
        }
        oas_pel = {
            'name': 'peliculas.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'peliculas.yaml')),
        }
        oas_pet = {
            'name': 'pet_clinic.yaml',
            'oas': read_open_api(os.path.join(TESTS_SET_PATH, 'pet_clinic.yaml')),
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