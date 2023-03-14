from oas_analysis.main_oas_analysis import load_oas

if __name__ == '__main__':
    path = 'tests_set/pet_clinic.yaml'
    oas = load_oas(path)
    print(oas)
