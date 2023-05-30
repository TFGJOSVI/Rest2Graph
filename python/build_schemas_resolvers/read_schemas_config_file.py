import re

from python.build_schemas_resolvers.utils import parse_type
from python.classes import Attribute, Component, Schema


STRING_COMPONENT_OBJECT = Component('String', [Attribute('value', 'string', True)])
STRING_SCHEMA = Schema('_OBJECT_STRING', STRING_COMPONENT_OBJECT)

NUMBER_COMPONENT_OBJECT = Component('Number', [Attribute('value', 'number', True)])
NUMBER_SCHEMA = Schema('_OBJECT_NUMBER', NUMBER_COMPONENT_OBJECT)

BOOLEAN_COMPONENT_OBJECT = Component('Boolean', [Attribute('value', 'boolean', True)])
BOOLEAN_SCHEMA = Schema('_OBJECT_BOOLEAN', BOOLEAN_COMPONENT_OBJECT)

INTEGER_COMPONENT_OBJECT = Component('Integer', [Attribute('value', 'integer', True)])
INTEGER_SCHEMA = Schema('_OBJECT_INTEGER', INTEGER_COMPONENT_OBJECT)

def read_schemas(file_path: str) -> list[str]:
    schemas = []
    with open(file_path, 'r') as file:
        lines = file.read()
        posicion_inicio = lines.find('types:')
        posicion_fin = lines.find('\t{\n\n\n')
        contenido_deseado = lines[posicion_inicio + len('schemas:'):posicion_fin]
        first_schema = contenido_deseado.split('\t}\n\n')[:-1][0]

        list_schemas = contenido_deseado.split('\t}\n\n')[:-1]

        list_schemas[0] = '\t' + list_schemas[0]



        for schema in list_schemas:
            first_line = schema.splitlines()[0]
            if schema.startswith('\ttype'):
                name_component = first_line.split('type')[1].strip().replace('{', '').strip()
                type_schema = parse_type(name_component)
                atributes = []
                for line in schema.splitlines():
                    if  line.startswith('\t\t'):
                        name = line.split(':')[0].strip()
                        type = line.split(':')[1].strip()
                        items_type = None
                        required = False

                        if type.__contains__('!'):
                            required = True
                            type = type.replace('!', '').strip()

                        if type.__contains__('['):
                                items_type = parse_type(type.split('[')[1].split(']')[0])
                                type = 'array'
                        else:
                            type = parse_type(type)

                        atributes.append(Attribute(name = name, type = type, items_type = items_type, required = required))

                component = Component(name = name_component, attributes = atributes)
                schema = Schema(type = type_schema, component = component)
                schemas.append(schema)
            elif schema.startswith('\tinput'):
                name_component = first_line.split('input')[1].strip().replace('{', '').strip()
                name_component = name_component.replace('Input', '')
                type_schema = parse_type(name_component)
                atributes = []
                for line in schema.splitlines():
                    if line.startswith('\t\t'):
                        name = line.split(':')[0].strip()

                        type = line.split(':')[1].strip()
                        items_type = None
                        required = False

                        if type.__contains__('!'):
                            required = True
                            type = type.replace('!', '').strip()

                        if type.__contains__('['):
                            items_type = parse_type(type.split('[')[1].split(']')[0])
                            type = 'array'
                        else:
                            type = parse_type(type)

                        atributes.append(Attribute(name=name, type=type, items_type=items_type, required=required))

                component = Component(name=name_component, attributes=atributes)
                schema = Schema(type=type_schema, component=component)
                schemas.append(schema)

    return schemas

def search_schema(file_path: str, component_name:str) -> Schema:
    if component_name == 'String':
        return STRING_SCHEMA
    elif component_name == 'Number':
        return NUMBER_SCHEMA
    elif component_name == 'Boolean':
        return BOOLEAN_SCHEMA
    elif component_name == 'Integer':
        return INTEGER_SCHEMA
    schemas = read_schemas(file_path)
    type_array = False
    if component_name.__contains__('['):
        component_name = component_name.replace('[', '').replace(']', '')
        type_array = True

    for schema in schemas:
        if schema.component.name == component_name.strip():
            if type_array:
                schema.type = 'array'
            return schema



