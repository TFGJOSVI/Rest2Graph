import os

from python.classes import Mutation
from python.oas_analysis.main_oas_analysis import load_parameters, load_oas
from python.oas_analysis.read_response import read_response
from python.oas_analysis.read_requetsBody import read_requestBody


def read_mutation(mutation, oas, url, method):
    description = mutation.get('description', None)
    if not description:
        description = mutation.get('summary', '')

    parameters = load_parameters(mutation, oas)

    response = read_response(mutation['responses'], oas) if 'responses' in mutation else None

    request_body = read_requestBody(mutation['requestBody'], oas) if 'requestBody' in mutation else None

    name = mutation.get('operationId', None)
    if name is None:
        urls = url.split('/')
        name = method
        for u in urls:
            if u != '':
                if u[0] == '{':
                    u = u[1:-1]
                    name += f'By{u[0].capitalize()}{u[1:]}'
                else:
                    name += f'{u[0].capitalize()}{u[1:]}'

    return Mutation(description=description, parameters=parameters, url=url, name=name, response=response, request=request_body)


def read_queries(oas):
    queries = []
    for path in oas['paths']:
        for method in oas['paths'][path]:
            if method in ['post', 'put', 'delete']:
                query = read_mutation(oas['paths'][path][method], oas, path, method)
                queries.append(query)
    return queries



if __name__ == '__main__':
    list_files = os.listdir('../tests_set')

    r = []

    for file in list_files:
        r.extend(read_queries(load_oas(f'../tests_set/{file}')))

    for r_ in r:
        print(r_)
