from python.classes import Schema, Attribute, Component
from .main_oas_analysis import parse_ref


def read_schemas(schemas, oas):

    return [read_schema(schema, oas) for schema in schemas]


def read_object_schema(schema, required):
    atributes = []

    if 'properties' in schema:
        for name, parameter in schema['properties'].items():

            if '$ref' in parameter:
                parameter = Attribute(name, 'Object', name in required if required else False)
            else:
                parameter = Attribute(name, parameter['type'], name in required if required else False)

            atributes.append(parameter)

    component = Component(schema['title'], atributes)

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
            return read_object_schema(schema, required)
        elif schema['type'] == 'array':
            return read_array_schema(schema, oas)
