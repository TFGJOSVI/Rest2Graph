import re

from python.classes import OpenAPI
from python.config_file.utils import parse_type_oas_graphql


def build_resolvers(open_api: OpenAPI) -> dict:

    """
    Build resolvers.

    :param open_api:
        An OpenAPI instance where includes the servers, queries and mutations.
    :return:
        A dictionary with the resolvers.
    """

    queries, query_resolver = build_queries(open_api)
    mutations, mutation_resolver = build_mutations(open_api)

    result = {
        "query_resolvers": query_resolver,
        "mutation_resolvers": mutation_resolver,
        "queries": queries,
        "mutations": mutations
    }

    return result


def build_queries(open_api: OpenAPI) -> list[str]:

    """
    Build queries and resolvers queries.

    :param open_api:
        An OpenAPI instance where includes the servers, queries and mutations.
    :return:
        A list of queries  and a list of resolvers.
    """

    result_queries = []
    result_queries_resolvers = []

    for q in open_api.queries:
        s = ''
        s += f'\t {q.name}'

        q.url = q.url.replace("{", "${args.") if "$" not in q.url else q.url

        if len(q.parameters) > 0:
            s += '('
            for p in q.parameters:

                if "array" in p.type:
                    type = re.match(r"array\[(.*)\]", p.type).group(1)

                    p.type = f"[{parse_type_oas_graphql(type.replace('!', ''))}]"

                s += f'{p.name}: {parse_type_oas_graphql(p.type.replace("!",""))}{"!" if p.required else ""}, '
            s = s[:-2]
            s += ')'

        if q.response:
            s += f': {q.response.schema.component.name if q.response.schema.type != "array" else "[" + q.response.schema.component.name + "]"},\n'
        else:
            s += ': String,\n'

        result_queries.append(s)

        s2 = ''
        s2 += f'\t {q.name}: (root, args) => get(`{open_api.servers[0]}{q.url}?'

        for p_path in q.parameters:

            if q.parameters.index(p_path) != 0 and q.parameters.index(p_path) != len(q.parameters):
                s2 += " +'&'+"

            if p_path.query == True:
                s2 += "${" + "$$" + p_path.name + "=$$+" + f' args.{p_path.name} ? args.{p_path.name} : **' + "}"
                s2 = s2.replace("**", "''").replace("$$", "'").replace("_&_", "'&'")

        s2 += '`),\n'

        result_queries_resolvers.append(s2)

    return result_queries, result_queries_resolvers


def build_mutations(open_api: OpenAPI) -> list[str]:

    """
    Build mutations and resolvers mutations.

    :param open_api:
        An OpenAPI instance where includes the servers, queries and mutations.
    :return:
        A list of mutations and a list of resolvers.
    """

    result_mutations = []
    result_mutations_resolvers = []

    for q in open_api.mutations:
        s = ''
        s += f'\t {q.name}'

        q.url = q.url.replace("{", "${args.") if "$" not in q.url else q.url

        if len(q.parameters) > 0:
            s += '('
            for p in q.parameters:

                if "array" in p.type:
                    # array[string] -> [string]

                    type_ = re.match(r"array\[(.*)\]", p.type).group(1)

                    p.type = f"[{parse_type_oas_graphql(type_.replace('!', ''))}]"

                s += f'{p.name}: {parse_type_oas_graphql(p.type.replace("!",""))}{"!" if p.required else ""}, '
            s = s[:-2]

            if q.request:
                s += ', '

                if type(q.request)  == str:
                    s += f'input: {q.request}'
                else:
                    s += f'input: {"Input" + q.request.schema.component.name if q.request.schema.type != "array" else "[" + "Input" + q.request.schema.component.name + "]"}'

            s += ')'
        else:
            if q.request:
                s += '('

                if type(q.request)  == str:
                    s += f'input: {q.request}'
                else:
                    s += f'input: {"Input" + q.request.schema.component.name if q.request.schema.type != "array" else "[" + "Input" + q.request.schema.component.name + "]"}'

                s += ')'

        if q.response:
            s += f': {q.response.schema.component.name if q.response.schema.type != "array" else "[" + q.response.schema.component.name + "]"},\n'
        else:
            s += ': String,\n'

        result_mutations.append(s)

        s2 = ''
        s2 += f'\t {q.name}: (root, args) => {q.type.__str__().lower()}{"Data" if q.type == "DELETE" else ""}(`{open_api.servers[0]}{q.url}?'

        for p_path in q.parameters:

            if q.parameters.index(p_path) != 0 and q.parameters.index(p_path) != len(q.parameters):
                s2 += " +'&'+"

            if p_path.query == True:
                s2 += "${" + "$$" + p_path.name + "=$$+" + f' args.{p_path.name} ? args.{p_path.name} : **' + "}"
                s2 = s2.replace("**", "''").replace("$$", "'").replace("_&_", "'&'")

        s2 += '`,args),\n'

        result_mutations_resolvers.append(s2)

    return result_mutations, result_mutations_resolvers
