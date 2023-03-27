import os

from oas_analysis.main_oas_analysis import load_oas
from python.oas_analysis.read_OpenAPI import read_OpenAPI

if __name__ == '__main__':
    paths = os.listdir('./tests_set')
    for path in paths:
        oas = load_oas(f'./tests_set/{path}')
        paths = oas['paths']
        OpenAPI = read_OpenAPI(oas)
        print(OpenAPI.queries)
        print(OpenAPI.mutations)
        print(OpenAPI.servers)






