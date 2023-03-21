from oas_analysis.main_oas_analysis import load_oas
from oas_analysis.read_requetsBody import read_requestBody

if __name__ == '__main__':
    path = 'tests_set/configuration_API.yaml'
    oas = load_oas(path)
    paths = oas['paths']

    for url in paths:
        print(f'\n################## {url} ##################')
        for method in paths[url]:
            print(f'\n\t{method}')
            requestBody = paths[url][method].get('requestBody', None)
            if requestBody:
                print(f'\t\t{read_requestBody(requestBody, oas)}')
            else:
                print(f'\t\tNo request body')







