import datetime
import yaml
import json
import os

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









