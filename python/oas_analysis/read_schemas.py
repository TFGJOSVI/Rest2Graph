from python.classes import Schema, Attribute, Component
from python.oas_analysis.main_oas_analysis import parse_ref

STRING_COMPONENT_OBJECT = Component('String', [Attribute('value', 'string', True)])
STRING_SCHEMA = Schema('_OBJECT_STRING', STRING_COMPONENT_OBJECT)

NUMBER_COMPONENT_OBJECT = Component('Number', [Attribute('value', 'number', True)])
NUMBER_SCHEMA = Schema('_OBJECT_NUMBER', NUMBER_COMPONENT_OBJECT)

BOOLEAN_COMPONENT_OBJECT = Component('Boolean', [Attribute('value', 'boolean', True)])
BOOLEAN_SCHEMA = Schema('_OBJECT_BOOLEAN', BOOLEAN_COMPONENT_OBJECT)

INTEGER_COMPONENT_OBJECT = Component('Integer', [Attribute('value', 'integer', True)])
INTEGER_SCHEMA = Schema('_OBJECT_INTEGER', INTEGER_COMPONENT_OBJECT)


def read_object_schema(schema, required, oas):



    attributes = []

    if 'properties' in schema:
        for name, parameter in schema['properties'].items():

            if '$ref' in parameter:
                parameter = read_schema(parameter, oas)
                parameter = Attribute(name, parameter.type, name in required if required else False)
            elif type in parameter and parameter['type'] == 'array':
                parameter = read_schema(parameter, oas)
                parameter = Attribute(name, parameter.type, name in required if required else False)
            else:
                parameter = Attribute(name, parameter['type'], name in required if required else False)

            attributes.append(parameter)

    if 'additionalProperties' in schema:
        additional_properties = schema['additionalProperties']
        additional_properties = Attribute('additionalProperties', additional_properties['type'], False)
        attributes.append(additional_properties)

    if 'title' not in schema:
        schema['title'] = 'Object'

    component = Component(schema['title'], attributes)

    return Schema('object', component)


def read_array_schema(schema, oas):
    schema = read_schema(schema['items'], oas)

    schema.type = 'array'

    return schema


def read_schema(schema, oas):
    required = schema.get('required', False)

    if 'required' in schema:
        required = schema['required']
        schema.pop('required')

    if '$ref' in schema:
        ref = schema['$ref']
        ref = parse_ref(ref)
        schema_ref = eval('oas' + ''.join(f'["{i}"]' for i in ref))
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
