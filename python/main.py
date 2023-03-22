
from oas_analysis.read_requetsBody import read_requestBody, get_requestBody
from oas_analysis.main_oas_analysis import load_oas, load_parameters


if __name__ == '__main__':
    path = 'tests_set/tocha.yaml'
    oas = load_oas(path)
    paths = oas['paths']


