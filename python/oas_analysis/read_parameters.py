from python.classes import Parameter
from python.oas_analysis.utils import search_ref


def read_parameters(method: dict, oas: dict) -> list[Parameter]:
    """
    Load parameters from a method.

    :param method:
        A dictionary that should contain requestBody, response ... and other fields that are part of the OpenAPI
        specification.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        A list of parameters.
    """

    parameters_list = method.get('parameters', [])
    res = []
    for parameter in parameters_list:
        if '$ref' in parameter:
            parameter = search_ref(oas, parameter['$ref'])
        name = parameter.get('name', '')
        query = parameter.get('in', '') == 'query'
        required = parameter.get('required', False)
        _type = parameter['schema']['type']
        if _type == 'array':
            _type = f'{_type}[{parameter["schema"]["items"]["type"]}]'
        res.append(Parameter(name, _type, query, required))
    return res
