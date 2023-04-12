import os
from read_open_api import read_open_api

if __name__ == '__main__':

    list_of_files = os.listdir('../tests_set/')


    for file in list_of_files:
        oas = read_open_api(f'../tests_set/{file}')
        print(oas)
