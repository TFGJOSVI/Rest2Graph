import re

from python.classes import OpenAPI
from python.oas_analysis.read_schemas import SPECIAL_SCHEMAS
from python.config_file.utils import replace, parse_type_oas_graphql
from python.oas_analysis.utils import search_ref
from python.oas_analysis.read_schemas import read_schema


FILE_PATH = './templates/config_template_v1.txt'


def write_schemas_string(open_api: OpenAPI, oas: dict) -> str:
    queries = open_api.queries
    mutations = open_api.mutations

    queries_schemas = list(map(lambda query: query.response.schema, list(filter(lambda q: q.response, queries))))

    mutations_schemas = list(map(lambda mutation: mutation.response.schema, list(filter(lambda m: m.response, mutations))))
    mutations_schemas.extend(list(map(lambda mutation: mutation.request.schema, list(filter(lambda m: m.request, mutations)))))

    queries_schemas = list(filter(lambda schema: schema not in SPECIAL_SCHEMAS, queries_schemas))
    mutations_schemas = list(filter(lambda schema: schema not in SPECIAL_SCHEMAS, mutations_schemas))

    queries_schemas = list(set(queries_schemas))
    mutations_schemas = list(set(mutations_schemas))

    extra_schemas = []

    schemas = ''

    for schema in queries_schemas:
        schemas += '\ttype ' + schema.component.name + ' {\n'

        for attribute in schema.component.attributes:

            if attribute.ref_schema:
                schema = read_schema({'schema': {'$ref': attribute.ref_schema}}, oas)
                extra_schemas.append(schema)


            if attribute.type == 'array':
                if attribute.required:
                    schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(attribute.items_type) + ']!\n'
                else:
                    schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(attribute.items_type) + ']\n'
            else:
                if attribute.required:
                    schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type) + '!\n'
                else:
                    schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type) + '\n'

        schemas += '\t}\n\n'

    for schema in mutations_schemas:
        schemas += '\tinput ' + 'Input' + schema.component.name + ' {\n'

        for attribute in schema.component.attributes:

            if attribute.ref_schema:
                schema = read_schema({'schema':{'$ref': attribute.ref_schema}}, oas)
                extra_schemas.append(schema)

            if attribute.type == 'array':
                if attribute.required:
                    schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(attribute.items_type) + ']!\n'
                else:
                    schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(attribute.items_type) + ']\n'
            else:
                if attribute.required:
                    schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type) + '!\n'
                else:
                    schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type) + '\n'

        schemas += '\t}\n\n'


    extra_schemas = list(set(extra_schemas))

    for schema in extra_schemas:
        if schema not in queries_schemas or schema not in mutations_schemas:
            schemas += '\ttype ' + schema.component.name + ' {\n'

            for attribute in schema.component.attributes:

                if attribute.ref_schema:
                    schema = read_schema({'schema': {'$ref': attribute.ref_schema}}, oas)
                    extra_schemas.append(schema)

                if attribute.type == 'array':
                    if attribute.required:
                        schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(attribute.items_type) + ']!\n'
                    else:
                        schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(attribute.items_type) + ']\n'
                else:
                    if attribute.required:
                        schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type) + '!\n'
                    else:
                        schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type) + '\n'

            schemas += '\t}\n\n'

    return schemas


def load_schemas(open_api: OpenAPI, new_file_path: str, oas: dict) -> None:
    schemas_string = write_schemas_string(open_api, oas)

    replace(FILE_PATH, new_file_path, 'sub_types', schemas_string)
