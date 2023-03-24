from oas_analysis.main_oas_analysis import load_oas

if __name__ == '__main__':
    path = 'tests_set/configuration_API.yaml'
    oas = load_oas(path)
    paths = oas['paths']
