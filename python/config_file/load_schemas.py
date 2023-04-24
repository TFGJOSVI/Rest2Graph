import re

from classes import OpenAPI
from oas_analysis.read_schemas import SPECIAL_SCHEMAS
from config_file.utils import replace, parse_type_oas_graphql
from oas_analysis.read_schemas import read_schema
from oas_analysis.utils import parse_ref


FILE_PATH = 'templates/config_template_v1.txt'


def write_schemas_string(open_api: OpenAPI, oas: dict) -> str:
    queries = open_api.queries
    mutations = open_api.mutations

    queries_schemas = list(map(lambda query: query.response.schema, list(filter(lambda q: q.response and q.response.schema.type!="array", queries))))

    queries_schemas.extend(list(map(lambda mutation: mutation.response.schema, list(filter(lambda m: m.response, mutations)))))
    mutations_schemas = (list(map(lambda mutation: mutation.request.schema, list(filter(lambda m: m.request, mutations)))))

    queries_schemas = list(filter(lambda schema: schema not in SPECIAL_SCHEMAS, queries_schemas))
    mutations_schemas = list(filter(lambda schema: schema not in SPECIAL_SCHEMAS, mutations_schemas))

    all_schemas = queries_schemas + mutations_schemas

    queries_schemas = list(set(queries_schemas))
    mutations_schemas = list(set(mutations_schemas))

    extra_schemas = []

    schemas = ''

    types_schemas = []

    for schema in queries_schemas:

        for attribute in schema.component.attributes:

            if attribute.ref_schema:
                schema_ = read_schema({'schema': {'$ref': attribute.ref_schema}}, oas)
                extra_schemas.append(schema_)

        if schema.component.name not in types_schemas:

            types_schemas.append(schema.component.name)

            schemas += '\ttype ' + schema.component.name + ' {\n'

            for attribute in schema.component.attributes:

                if attribute.ref_schema:
                    schema = read_schema({'schema': {'$ref': attribute.ref_schema}}, oas)
                    extra_schemas.append(schema)

                if attribute.type == 'array' or attribute.items_type:
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

    type_schemas_mutations = []

    for schema in mutations_schemas:

        for attribute in schema.component.attributes:

            if attribute.ref_schema:
                schema_ = read_schema({'schema': {'$ref': attribute.ref_schema}}, oas)
                extra_schemas.append(schema_)

        if schema.component.name not in type_schemas_mutations:
            type_schemas_mutations.append(schema.component.name)

            schemas += '\tinput ' + 'Input' + schema.component.name + ' {\n'

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


    for schema in all_schemas:
        for attribute in schema.component.attributes:

            if attribute.ref_schema:
                schema_ = read_schema({'schema': {'$ref': attribute.ref_schema}}, oas)
                extra_schemas.append(schema_)


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


def load_schemas(open_api: OpenAPI, oas: dict) -> str:
    return write_schemas_string(open_api, oas)

