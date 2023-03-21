from oas_analysis.main_oas_analysis import load_oas, load_parameters

if __name__ == '__main__':
    path = 'tests_set/pet_clinic.yaml'
    oas = load_oas(path)
    path = oas['paths']

    for url in path:
        print(f'\n################## {url} ##################')
        for method in path[url]:
            print(load_parameters(oas['paths'][url][method], oas))
