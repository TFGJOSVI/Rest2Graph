import os
import shutil


def parse_type(response: str):
    if response.__contains__('['):
        type = 'array'
    elif response == 'Int':
        type = 'integer'
    elif response == 'Float':
        type = 'number'
    elif response == 'Boolean':
        type = 'boolean'
    elif response == 'String':
        type = 'string'
    else:
        type = response

    return type


def copy_dir(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
