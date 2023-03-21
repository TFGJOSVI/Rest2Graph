import datetime
import json
import os

import yaml

from python.classes import Parameter


def custom_json_serializer(obj):
    '''
    Custom json serializer
    :param obj:     object to serialize
    :return:        serialized object
    '''

    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def yaml2json(path: str):
    '''
    Convert a yaml file to json
    :param path:    path to the yaml file
    :return:        json file
    '''
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return json.dumps(data, default=custom_json_serializer)


def parse_ref(ref):
    # Check if ref is valid
    if not ref.startswith('#'):
        raise ValueError('Ref is not valid')

    # Remove #/ from ref
    ref = ref[2:]

    # Split ref
    ref = ref.split('/')

    return ref


def load_oas(path: str):
    '''
    Load an oas file
    :param path:    path to the oas file
    :return:        oas file
    '''
    # Check if path exists
    if not os.path.exists(path):
        raise ValueError('Path does not exist')

    if path.endswith('.json'):
        _file = json.load(open(path))
    elif path.endswith('.yaml'):
        _file = yaml2json(path)
        _file = json.loads(_file)
    else:
        raise ValueError('File format not supported')

    return _file


def load_parameters(method: dict, oas: dict):
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
