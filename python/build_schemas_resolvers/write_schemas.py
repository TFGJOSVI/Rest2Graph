from config_file.utils import parse_type_oas_graphql
from python.classes import Schema

def write_schemas_string_build(schemas_list: list[Schema], all=False) -> str:

    schemas = ''

    for schema in schemas_list:
        schemas += '\ttype ' + schema.component.name + ' {\n'

        for attribute in schema.component.attributes:

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

    if all:

        for schema in schemas_list:
            schemas += '\tinput ' + 'Input' + schema.component.name + ' {\n'

            for attribute in schema.component.attributes:

                if attribute.type == 'array':
                    if attribute.required:
                        schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(
                            attribute.items_type, True) + ']!\n'
                    else:
                        schemas += '\t\t' + attribute.name + ': [' + parse_type_oas_graphql(
                            attribute.items_type, True) + ']\n'
                else:
                    if attribute.required:
                        schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type, True) + '!\n'
                    else:
                        schemas += '\t\t' + attribute.name + ': ' + parse_type_oas_graphql(attribute.type, True) + '\n'

            schemas += '\t}\n\n'

    return schemas