import os
import sys

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from python.oas_analysis.read_open_api import read_open_api as read_api
from python.paths import TESTS_SET_PATH


class TestOasAnalysis:

    def setup_class(cls):

        oas_ady = {
            'name': 'adyen_developer_experience_team.yaml',
            'num_queries': 0,
            'num_posts': 20,
            'num_puts': 0,
            'num_deletes': 0,
            'num_servers': 1,
            'urls_queries': [],
            'urls_posts' : ['/checkAccountHolder', '/closeAccount', '/closeAccountHolder',
                            '/closeStores', '/createAccount', '/createAccountHolder',
                           '/deleteBankAccounts', '/deleteLegalArrangements',
                           '/deletePayoutMethods', '/deleteShareholders', '/deleteSignatories',
                           '/getAccountHolder', '/getTaxForm', '/getUploadedDocuments',
                           '/suspendAccountHolder', '/unSuspendAccountHolder', '/updateAccount',
                           '/updateAccountHolder', '/updateAccountHolderState', '/uploadDocument'],
            'urls_puts' : [],
            'urls_deletes' : [],
            'queries_parameters': [],
            'posts_parameters': [],
            'puts_parameters': [],
            'deletes_parameters': [],
            'responses_queries': []
        }

        oas_auth = {
            'name': 'authentiq_team.yaml',
            'num_queries': 2,
            'num_posts': 5,
            'num_puts': 2,
            'num_deletes': 3,
            'num_servers': 1,
            'urls_queries': ['/key/{PK}', '/scope/{job}'],
            'urls_posts': ['/key', '/key/{PK}', '/login', '/scope', '/scope/{job}'],
            'urls_puts' : ['/key/{PK}', '/scope/{job}'],
            'urls_deletes' : ['/key', '/key/{PK}', '/scope/{job}'],
            'queries_parameters': [[('PK', 'string', False, True)], [('job', 'string', False, True)]],
            'posts_parameters': [[],
                                 [('PK', 'string', False, True)],
                                 [('callback', 'string', True, True)],
                                 [('test', 'integer',True, False)],
                                [('job', 'string', False, True)]],
            'puts_parameters': [[('PK', 'string', False, True)], [('job', 'string', False, True)]],

            'deletes_parameters': [
                [('email', 'string', True, True), ('phone', 'string', True, True), ('code', 'string', True, False)],
                [('PK', 'string', False, True), ('secret', 'string', True, True)],
                [('job', 'string', False, True)]],
            'responses_queries':[
                {
                    'type': 'object',
                    'name': 'JWT'
                }
            ]

        }

        oas_config = {
            'name': 'configuration_API.yaml',
            'num_queries': 13,
            'num_posts': 6,
            'num_puts': 0,
            'num_deletes': 2,
            'num_servers': 1,
            'urls_queries': ["/accountHolders/{id}", "/accountHolders/{id}/balanceAccounts",
                             "/balanceAccounts/{balanceAccountId}/sweeps",
                             '/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}', "/balanceAccounts/{id}",
                             "/balanceAccounts/{id}/paymentInstruments", "/balancePlatforms/{id}",
                             "/balancePlatforms/{id}/accountHolders", "/paymentInstrumentGroups/{id}",
                             "/paymentInstrumentGroups/{id}/transactionRules", "/paymentInstruments/{id}",
                             "/paymentInstruments/{id}/transactionRules", '/transactionRules/{transactionRuleId}'],
            'urls_posts': ['/accountHolders', '/balanceAccounts',
                           '/balanceAccounts/{balanceAccountId}/sweeps', '/paymentInstrumentGroups',
                           '/paymentInstruments', '/transactionRules'],
            'urls_puts' : [],
            'urls_deletes' : ['/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}', '/transactionRules/{transactionRuleId}'],
            'queries_parameters': [[('id', 'string', False, True)],
                                   [('id', 'string', False, True), ('offset', 'integer', True, False), ('limit', 'integer', True, False)],
                                    [('balanceAccountId', 'string', False, True), ('offset', 'integer', True, False), ('limit', 'integer', True, False)],
                                    [('balanceAccountId', 'string', False, True), ('sweepId', 'string', False, True)],
                                    [('id', 'string', False, True)],
                                    [('id', 'string', False, True), ('offset', 'integer', True, False), ('limit', 'integer', True, False)],
                                    [('id', 'string', False, True)],
                                    [('id', 'string', False, True), ('offset', 'integer', True, False), ('limit', 'integer', True, False)],
                                    [('id', 'string', False, True)],
                                    [('id', 'string', False, True)],
                                    [('id', 'string', False, True)],
                                    [('id', 'string', False, True)],
                                    [('transactionRuleId', 'string', False, True)]],
            'posts_parameters': [[], [], [('balanceAccountId', 'string', False, True)], [], [], []],
            'puts_parameters': [],
            'deletes_parameters': [[('balanceAccountId', 'string', False, True), ('sweepId', 'string', False, True)],
                                   [('transactionRuleId', 'string', False, True)]],


            'responses_queries': [
                {
                    'type': 'object',
                    'name': 'BalancePlatform'
                },
                {
                    'type': 'object',
                    'name': 'PaginatedBalanceAccountsResponse'
                },
                {
                    'type': 'object',
                    'name': 'BalanceSweepConfigurationsResponse'
                },
                {
                    'type': 'object',
                    'name': 'BalanceAccount'
                },
                {
                    'type': 'object',
                    'name': 'PaginatedPaymentInstrumentsResponse'
                },
                {
                    'type': 'object',
                    'name': 'TransactionRulesResponse'
                },
                {
                    'type': 'object',
                    'name': 'PaginatedAccountHoldersResponse'
                },
                {
                    'type': 'object',
                    'name': 'SweepConfigurationV2'
                },
                {
                    'type': 'object',
                    'name': 'PaymentInstrumentGroup'
                },
                {
                    'type': 'object',
                    'name': 'PaymentInstrument'
                },
                {
                    'type': 'object',
                    'name': 'TransactionRuleResponse'
                },
                {
                    'type': 'object',
                    'name': 'AccountHolder'
                }
            ]
        }

        oas_pel = {
            'name': 'peliculas.yaml',
            'num_queries': 8,
            'num_posts': 3,
            'num_puts': 3,
            'num_deletes': 4,
            'num_servers': 2,
            'urls_queries': ["/directores", "/directores/{id}", "/categorias", "/categorias/{id}", "/peliculas",
                     "/peliculas/{id}", '/peliculas/categoria/{id}', '/peliculas/director/{id}'],
            'urls_posts': ['/directores', '/categorias', '/peliculas'],
            'urls_puts': ['/directores/{id}', '/categorias/{id}', '/peliculas/{id}'],
            'urls_deletes': ['/directores/{id}', '/categorias/{id}', '/peliculas/{id}', '/peliculas/{id}/categoria/{cat}'],
            'queries_parameters': [[],
                                   [('id', 'integer', False, True)],
                                   [],
                                   [('id', 'integer', False, True)],
                                   [],
                                   [('id', 'integer', False, True)],
                                   [('id', 'integer', False, True)], [('id', 'integer', False, True)]] ,
            'posts_parameters': [[], [], []],
            'puts_parameters': [[('id', 'integer', False, True)], [('id', 'integer', False, True)], [('id', 'integer', False, True)]],
            'deletes_parameters': [[('id', 'integer', False, True)],
                                   [('id', 'integer', False, True)],
                                   [('id', 'integer', False, True)],
                                   [('id', 'integer', False, True), ('cat', 'integer', False, True)]],
            'responses_queries': [
                {
                    'name': 'Pelicula',
                    'type': 'array'
                },
                {
                    'name': 'Categoria',
                    'type': 'array'
                },
                {
                    'name': 'Director',
                    'type': 'array'
                },
                {
                    'name': 'Categoria',
                    'type': 'object'
                },
                {
                    'name': 'Pelicula',
                    'type': 'object'
                },
                {
                    'name': 'Director',
                    'type': 'object'
                }
            ]
        }

        oas_pet = {
            'name': 'pet_clinic.yaml',
            'num_queries': 8,
            'num_posts': 6,
            'num_puts': 2,
            'num_deletes': 3,
            'num_servers': 1,
            'urls_queries': ["/pet/findByStatus", "/pet/findByTags", "/pet/{petId}", "/store/inventory",
                     "/store/order/{orderId}", "/user/login", "/user/logout", "/user/{username}"],
            'urls_posts': ['/pet', '/pet/{petId}', '/pet/{petId}/uploadImage', '/store/order', '/user', '/user/createWithList'],
            'urls_puts' : ['/pet', '/user/{username}'],
            'urls_deletes' : ['/pet/{petId}', '/store/order/{orderId}', '/user/{username}'],
            'queries_parameters': [[('status', 'string', True, False)],
                                   [('tags', 'array[string]', True, False)],
                                   [('petId', 'integer', False, True)],
                                   [],
                                   [('orderId', 'integer', False, True)],
                                   [('username', 'string', True, False), ('password', 'string', True, False)],
                                   [],
                                   [('username', 'string', False, True)]],
            'posts_parameters': [[], [('petId', 'integer', False, True), ('name', 'string', True, False), (('status', 'string',True, False))],
                                 [('petId', 'integer', False, True), ('additionalMetadata', 'string', True, False)],
                                 [], [], []],
            'puts_parameters': [[], [('username', 'string', False, True)]],
            'deletes_parameters':  [[('api_key', 'string', False, False), ('petId', 'integer', False, True)],
                                    [('orderId', 'integer', False, True)],
                                    [('username','string', False,True)]],
            'responses_queries': [
                {
                    'type': 'array',
                    'name': 'Pet',
                },
                {
                    'type': 'object',
                    'name': 'Order',
                },
                {
                    'type': 'object',
                    'name': 'ObjectObject'
                },
                {
                    'type': 'object',
                    'name': 'User',
                },
                None,
                {
                    'type': '_OBJECT_STRING',
                    'name': 'String',
                }
            ],

        }

        cls.oas_list = [oas_pet, oas_auth, oas_config, oas_pel, oas_ady]

    def test_count_queries(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            assert len(oas.queries) == i['num_queries']

    def test_count_mutations(self):

        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            posts = [method for method in oas.mutations if method.type == 'post']
            puts = [method for method in oas.mutations if method.type == 'put']
            deletes = [method for method in oas.mutations if method.type == 'delete']
            assert len(posts) == i['num_posts']
            assert len(puts) == i['num_puts']
            assert len(deletes) == i['num_deletes']

    def test_count_servers(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            assert len(oas.servers) == i['num_servers']

    def test_check_queries_urls(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            urls = [query.url for query in oas.queries]
            assert urls == i['urls_queries']

    def test_check_mutations_urls(self):

        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            posts = [method.url for method in oas.mutations if method.type == 'post']
            puts = [method.url for method in oas.mutations if method.type == 'put']
            deletes = [method.url for method in oas.mutations if method.type == 'delete']
            assert posts == i['urls_posts']
            assert puts == i['urls_puts']
            assert deletes == i['urls_deletes']

    def test_check_schemas(self):

        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            queries = oas.queries

            schemas = list(set(query.response for query in queries))

            schemas = list(map(lambda x:  {'type': x.schema.type, 'name': x.schema.component.name} if x else x, schemas))

            assert all([schema in schemas for schema in i['responses_queries']])

    def test_check_queries_parameters(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            index = 0
            for query in oas.queries:
                for j in range(len(query.parameters)):

                    p = (query.parameters[j].name, query.parameters[j].type, query.parameters[j].query, query.parameters[j].required)

                    assert p in i['queries_parameters'][index]
                index += 1

    def test_check_post_parameters(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            index = 0
            mutations_posts = [method for method in oas.mutations if method.type == 'post']
            for mutation in mutations_posts:
                for j in range(len(mutation.parameters)):
                    p = (mutation.parameters[j].name, mutation.parameters[j].type, mutation.parameters[j].query, mutation.parameters[j].required)
                    assert p in i['posts_parameters'][index]
                index += 1


    def test_check_put_parameters(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            index = 0
            mutations_puts = [method for method in oas.mutations if method.type == 'put']
            for mutation in mutations_puts:
                print(f'\nURL {mutation.url}')
                for j in range(len(mutation.parameters)):
                    p = (mutation.parameters[j].name, mutation.parameters[j].type, mutation.parameters[j].query, mutation.parameters[j].required)
                    assert p in i['puts_parameters'][index]
                index += 1



    def test_check_delete_parameters(self):
        for i in self.oas_list:
            oas = read_api(os.path.join(TESTS_SET_PATH, i['name']))
            index = 0
            mutations_deletes = [method for method in oas.mutations if method.type == 'delete']
            for mutation in mutations_deletes:
                    for j in range(len(mutation.parameters)):
                        p = (mutation.parameters[j].name, mutation.parameters[j].type, mutation.parameters[j].query, mutation.parameters[j].required)
                        assert p in i['deletes_parameters'][index]

                    index += 1









