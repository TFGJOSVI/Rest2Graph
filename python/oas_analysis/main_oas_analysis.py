import datetime
import yaml
import json
import os

from python.classes import Parameter


def custom_json_serializer(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))

def yaml2json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return json.dumps(data, default=custom_json_serializer)


def load_oas(path: str):
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


def load_parameters(method, oas):

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

def search_ref(oas, ref):
    rute = ref.split('/')
    for i in rute:
        if i != '#':
            oas = oas[i]
    return oas






