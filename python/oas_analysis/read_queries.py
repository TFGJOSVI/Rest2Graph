from python.classes import Query
from python.oas_analysis.main_oas_analysis import load_parameters
from python.oas_analysis.read_response import read_response


def read_query(query, oas, url):
    description = query.get('description', None)
    if description is None:
        description = query.get('summary', '')

    parameters = load_parameters(query, oas)

    response = read_response(query['responses'], oas)

    name = query.get('operationId', None)
    if name is None:
        urls = url.split('/')
        name = 'get'
        for u in urls:
            if u != '':
                if u[0] == '{':
                    u = u[1:-1]
                    name += f'By{u[0].capitalize()}{u[1:]}'
                else:
                    name += f'{u[0].capitalize()}{u[1:]}'

    return Query(description=description, parameters=parameters, url=url, name=name, response=response)



def read_queries(oas):
    queries = []
    for path in oas['paths']:
        for method in oas['paths'][path]:
            if method == 'get':
                query = read_query(oas['paths'][path][method], oas, path)
                queries.append(query)
    return queries