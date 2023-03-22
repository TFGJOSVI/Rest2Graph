from oas_analysis.main_oas_analysis import load_oas, load_parameters
from python.oas_analysis.read_queries import read_queries
from python.oas_analysis.read_response import read_response

if __name__ == '__main__':
    path = 'tests_set/configuration_API.yaml'
    oas = load_oas(path)
    paths = oas['paths']




