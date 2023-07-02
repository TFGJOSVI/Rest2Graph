import os

from python.oas_analysis.read_open_api import read_open_api

if __name__ == '__main__':

    list_of_files = os.listdir('../tests/tests_set/')


    for file in list_of_files:
        oas = read_open_api(f'../tests/tests_set/{file}')
        print(f'\n\nFile: {file}#######################################')
        for query in oas.mutations:
            print(f'\n\nQuery: {query.name}#######################################')
            print(f'RequetBody: {query.request}')


