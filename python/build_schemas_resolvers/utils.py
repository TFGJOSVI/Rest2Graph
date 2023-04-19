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
        type = 'object'
    return type