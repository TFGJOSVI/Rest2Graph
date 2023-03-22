from python.classes import Parameter


def read_parameters(method: dict, oas: dict):

    '''
    Load parameters from a method
    :param method:  method to load parameters from
    :param oas:     oas file
    :return:        list of parameters
    '''

    parameters_list = method.get('parameters', [])
    res = []
    for parameter in parameters_list:
        if '$ref' in parameter:
            parameter = search_ref(oas, parameter['$ref'])
        name = parameter.get('name', '')
        query = parameter.get('in', '') == 'query'
        required = parameter.get('required', False)
        type = parameter['schema']['type']
        if type == 'array':
            type = f'{type}[{parameter["schema"]["items"]["type"]}]'
        res.append(Parameter(name, type, query, required))
    return res

def search_ref(oas: dict, ref: str):
    '''
    Search a reference in an oas file
    :param oas:     oas file
    :param ref:     reference to search
    :return:        reference
    '''
    rute = ref.split('/')
    for i in rute:
        if i != '#':
            oas = oas[i]
    return oas