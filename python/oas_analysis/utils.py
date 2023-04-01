import datetime
import json
import os

import yaml


def custom_json_serializer(obj):
    """
    Custom json serializer.
    :param obj:
        Object to serialize.
    :return:
        Serialized object.
    """

    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def yaml2json(path: str):
    """
    Convert a yaml file to json.
    :param path:
        Path to the yaml file.
    :return:
        JSON file.
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return json.dumps(data, default=custom_json_serializer)


def load_oas(path: str):
    """
    Load an oas file.
    :param path:
        Path to the oas file.
    :return:
         OAS file.
    """
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


def search_ref(oas: dict, ref: str):
    """
    Search a reference in an oas file.
    :param oas:
        OAS file
    :param ref:
        Reference to search.
    :return:
        Reference.
    """

    if not ref.startswith('#'):
        raise ValueError('Ref is not valid')

    rute = ref.split('/')
    for i in rute:
        if i != '#':
            oas = oas[i]
    return oas


def parse_ref(ref: str):
    """
    Parse a ref.
    :param ref:
        Ref to parse.
    :return:
        Parsed ref.
    """

    # Check if ref is valid
    if not ref.startswith('#'):
        raise ValueError('Ref is not valid')

    # Remove #/ from ref
    ref = ref[2:]

    # Split ref
    ref = ref.split('/')

    return ref
