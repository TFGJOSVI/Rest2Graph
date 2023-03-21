from oas_analysis.read_requetsBody import read_requestBody, get_requestBody
from oas_analysis.main_oas_analysis import load_oas, load_parameters


if __name__ == '__main__':
    path = 'tests_set/tocha.yaml'
    oas = load_oas(path)
    paths = oas['paths']

    for url in paths:
        print(f'\n################## {url} ##################')
        for method in paths[url]:
            print(f'\n\t{method}')
            print(get_requestBody(paths[url][method], oas))
