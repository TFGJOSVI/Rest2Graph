import os

from python.oas_analysis.utils import load_oas
from python.oas_analysis.read_open_api import read_open_api

if __name__ == '__main__':
    paths = os.listdir('./tests_set')
    for path in paths:
        oas = load_oas(f'./tests_set/{path}')
        paths = oas['paths']
        OpenAPI = read_open_api(oas)
        print(OpenAPI.queries)
        print(OpenAPI.mutations)
        print(OpenAPI.servers)






