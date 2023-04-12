from typing import Union

from classes import Schema, Attribute, Component
from oas_analysis.utils import search_ref, parse_ref

STRING_COMPONENT_OBJECT = Component('String', [Attribute('value', 'string', True)])
STRING_SCHEMA = Schema('_OBJECT_STRING', STRING_COMPONENT_OBJECT)

NUMBER_COMPONENT_OBJECT = Component('Number', [Attribute('value', 'number', True)])
NUMBER_SCHEMA = Schema('_OBJECT_NUMBER', NUMBER_COMPONENT_OBJECT)

BOOLEAN_COMPONENT_OBJECT = Component('Boolean', [Attribute('value', 'boolean', True)])
BOOLEAN_SCHEMA = Schema('_OBJECT_BOOLEAN', BOOLEAN_COMPONENT_OBJECT)

INTEGER_COMPONENT_OBJECT = Component('Integer', [Attribute('value', 'integer', True)])
INTEGER_SCHEMA = Schema('_OBJECT_INTEGER', INTEGER_COMPONENT_OBJECT)

SPECIAL_SCHEMAS = [STRING_SCHEMA, NUMBER_SCHEMA, BOOLEAN_SCHEMA, INTEGER_SCHEMA]


def read_object_schema(schema: dict, required: Union[list[str], bool], oas: dict) -> Schema:
    """
    Reads the definition of an object schema and converts it into a `Schema` instance.

    :param schema:
        A dictionary that should contain type, properties ... and other fields that are part of the OpenAPI.
    :param required:
        A list of strings containing the names of the required attributes, or False if there are no required attributes.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        An instance of the `Schema` class.
    """

    attributes = []
    if 'properties' in schema:
        for name, parameter in schema['properties'].items():

            if '$ref' in parameter or 'properties' in parameter:

                ref_schema = parameter['$ref'] if '$ref' in parameter else None

                parameter = read_schema(parameter, oas)

                parameter = Attribute(name, parameter.type, name in required if required else False, ref_schema=ref_schema)

            elif 'type' in parameter and parameter['type'] == 'array':

                items_types = parameter['items']

                if '$ref' in items_types:
                    ref_schema = items_types['$ref']
                    items_types = parse_ref(items_types['$ref'])[-1]
                else:
                    items_types = items_types['type']
                    ref_schema = None

                parameter = Attribute(name, 'array', name in required if required else False, items_types, ref_schema)

            else:

                if 'oneOf' in parameter:
                    continue

                parameter = Attribute(name, parameter['type'], name in required if required else False)

            attributes.append(parameter)

    if 'additionalProperties' in schema:
        additional_properties = schema['additionalProperties']
        additional_properties = Attribute('additionalProperties', additional_properties['type'], False)
        attributes.append(additional_properties)

    if 'title' not in schema:
        schema['title'] = ''.join(i.title() for i in schema['type'].split('_')) + 'Object'

    component = Component(schema['title'], attributes)

    return Schema('object', component)


def read_array_schema(schema: dict, oas: dict) -> Schema:
    """
    Reads the definition of an array schema and converts it into a `Schema` instance.
    :param schema:
        A dictionary that should contain type, properties ... and other fields that are part of the OpenAPI.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        An instance of the `Schema` class.
    """

    schema = read_schema(schema['items'], oas)

    schema.type = 'array'

    return schema


def read_schema(schema: dict, oas: dict) -> Schema:
    """
    Reads the definition of a schema and converts it into a `Schema` instance.

    :param schema:
        A dictionary that should contain type, properties ... and other fields that are part of the OpenAPI.
    :param oas:
        A dictionary containing the complete API specification, following the OpenAPI format.
    :return:
        An instance of the `Schema` class.
    """

    schema = schema.get('schema', schema)

    required = schema.get('required', False)

    if 'required' in schema:
        required = schema['required']
        schema.pop('required')

    if '$ref' in schema:
        ref_ = schema['$ref']
        ref = parse_ref(ref_)
        schema_ref = search_ref(oas, ref_)
        schema.pop('$ref')
        schema.update(schema_ref)
        schema['title'] = ref[-1]
        return read_schema(schema, oas)

    if 'type' in schema:
        if schema['type'] == 'object':
            return read_object_schema(schema, required, oas)
        elif schema['type'] == 'array':
            return read_array_schema(schema, oas)
        elif schema['type'] == 'string':
            return STRING_SCHEMA
        elif schema['type'] == 'number':
            return NUMBER_SCHEMA
        elif schema['type'] == 'integer':
            return INTEGER_SCHEMA
        elif schema['type'] == 'boolean':
            return BOOLEAN_SCHEMA
    else:
        return read_object_schema(schema, required, oas)
