from python.classes import Parameter
from python.oas_analysis.main_oas_analysis import search_ref


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
