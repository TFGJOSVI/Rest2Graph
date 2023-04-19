import os

from python.oas_analysis.read_open_api import read_open_api

if __name__ == '__main__':

    list_of_files = os.listdir('../tests/tests_set/')


    for file in list_of_files:
        oas = read_open_api(f'../tests/tests_set/{file}')
        print(f'\n\nFile: {file}#######################################')
        for query in oas.queries:
            print(f'\n\nQuery: {query.name}#######################################')
            print(f'Url: {query.url}')
            print(f'Description: {query.description}')
            print(f'Parameters: {query.parameters}')
            print(f'Response: {query.response}')


