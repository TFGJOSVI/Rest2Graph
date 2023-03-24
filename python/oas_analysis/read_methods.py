import os

from python.classes import Query, Mutation
from python.oas_analysis.main_oas_analysis import load_oas
from python.oas_analysis.read_parameters import read_parameters
from python.oas_analysis.read_requets_body import read_request_body
from python.oas_analysis.read_response import read_response


def read_method(method, oas, url, type='get'):
    description = method.get('description', None)
    if description is None:
        description = method.get('summary', '')

    parameters = read_parameters(method, oas)

    response = read_response(method, oas)

    if type != 'get':
        request_body = read_request_body(method, oas) if 'requestBody' in method else None
    else:
        request_body = None

    name = method.get('operationId', None)
    if name is None:
        urls = url.split('/')
        name = type
        for u in urls:
            if u != '':
                if u[0] == '{':
                    u = u[1:-1]
                    name += f'By{u[0].capitalize()}{u[1:]}'
                else:
                    name += f'{u[0].capitalize()}{u[1:]}'

    if type == 'get':
        return Query(description=description, parameters=parameters, url=url, name=name, response=response)
    else:
        return Mutation(description=description, parameters=parameters, url=url, name=name, response=response,
                        request=request_body)


def read_methods(oas):
    methods = {
        'Query': [],
        'Mutation': []
    }
    for path in oas['paths']:
        for method in oas['paths'][path]:
            if method == 'get':
                query = read_method(oas['paths'][path][method], oas, path)
                methods['Query'].append(query)
            elif method in ['post', 'put', 'delete']:
                query = read_method(oas['paths'][path][method], oas, path, method)
                methods['Mutation'].append(query)
    return methods


if __name__ == '__main__':
    if __name__ == '__main__':
        list_files = os.listdir('../tests_set')

        r = {
            'Query': [],
            'Mutation': []
        }

        for file in list_files:
            r_ = read_methods(load_oas(f'../tests_set/{file}'))
            r['Query'].extend(r_['Query'])
            r['Mutation'].extend(r_['Mutation'])

        for r_ in r['Query']:
            print(r_)
