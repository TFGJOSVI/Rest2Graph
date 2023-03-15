import yaml
import json
import os

from python.classes import Parameter


def yaml2json(path: str):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return json.dumps(data)


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


def load_parameters(file, url, method):
    path = file['paths'][url][method]
    parameters = path.get('parameters', [])
    res = []
    for parameter in parameters:
        name = parameter.get('name', '')
        query = parameter.get('in', '') == 'query'
        required = parameter.get('required', False)
        type = parameter['schema']['type']
        if type == 'array':
            type = f'{type}[{parameter["schema"]["items"]["type"]}]'
        res.append(Parameter(name, type, query, required))
    return res







