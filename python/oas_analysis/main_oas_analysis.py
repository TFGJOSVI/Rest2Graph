import yaml
import json
import os


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

