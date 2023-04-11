from dataclasses import dataclass, field


# Validations
def validate_list(key, value):
    if not value:
        raise ValueError(f'{key}: the list cannot be empty')
    return value


def validate_str(values):
    errors = []

    for key, value in values.items():

        if type(value) is str and not value:
            errors.append(key)

    if errors:
        raise ValueError(f'{", ".join(errors)}: the field cannot be empty')


# Dataclass
@dataclass
class Attribute:
    name: str = field(metadata={'required': True})
    type: str = field(metadata={'required': True})
    required: bool = field(metadata={'required': True})
    items_type: str = field(default=None)
    ref_schema: str = field(default=None)

    def __post_init__(self):
        validate_str(self.__dict__)

    def __eq__(self, other):
        return (
            isinstance(other, Attribute) and
            self.name == other.name and
            self.type == other.type and
            self.required == other.required
        )

    def __hash__(self):
        return hash((self.name, self.type, self.required))


@dataclass
class Component:
    name: str = field(metadata={'required': True})
    attributes: list[Attribute] = field(default_factory=list)

    def __eq__(self, other):
        return (
            isinstance(other, Component) and
            self.name == other.name and
            self.attributes == other.attributes
        )

    def __hash__(self):
        return hash((self.name, tuple(self.attributes)))


@dataclass
class Schema:
    type: str = field(metadata={'required': True})
    component: Component = field(metadata={'required': True})

    def __post_init__(self):
        validate_str(self.__dict__)

    def __eq__(self, other):
        return (
            isinstance(other, Schema) and
            self.type == other.type and
            self.component == other.component
        )

    def __hash__(self):
        return hash((self.type, self.component))

@dataclass
class Response:
    schema: Schema = field(metadata={'required': True})

    def __eq__(self, other):
        return (
            isinstance(other, Response) and
            self.schema == other.schema
        )

    def __hash__(self):
        return hash(self.schema)


@dataclass
class RequestBody:
    required: bool = field(metadata={'required': True})
    schema: Schema = field(default=None)

    def __eq__(self, other):
        return (
            isinstance(other, RequestBody) and
            self.required == other.required and
            self.schema == other.schema
        )

    def __hash__(self):
        return hash((self.required, self.schema))
@dataclass
class Parameter:
    name: str = field(metadata={'required': True})
    type: str = field(metadata={'required': True})
    query: bool = field(metadata={'required': True})
    required: bool = field(metadata={'required': True})

    def __post_init__(self):
        validate_str(self.__dict__)

    def __eq__(self, other):
        return (
            isinstance(other, Parameter) and
            self.name == other.name and
            self.type == other.type and
            self.query == other.query and
            self.required == other.required
        )

    def __hash__(self):
        return hash((self.name, self.type, self.query, self.required))


@dataclass
class Query:
    description: str
    parameters: list[Parameter]
    url: str = field(metadata={'required': True})
    name: str = field(metadata={'required': True})
    response: Response = field(metadata={'required': True})

    def __post_init__(self):
        validate_str(
            {
                'url': self.url,
                'name': self.name,
            }
        )

    def __eq__(self, other):
        return (
            isinstance(other, Query) and
            self.description == other.description and
            self.parameters == other.parameters and
            self.url == other.url and
            self.name == other.name and
            self.response == other.response
        )

    def __hash__(self):
        return hash((self.description, self.parameters, self.url, self.name, self.response))


@dataclass
class Mutation:
    description: str
    request: RequestBody
    parameters: list[Parameter]
    url: str = field(metadata={'required': True})
    name: str = field(metadata={'required': True})
    type: str = field(metadata={'required': True})
    response: Response = field(metadata={'required': True})

    def __post_init__(self):
        validate_str(
            {
                'url': self.url,
                'name': self.name,
            }
        )

    def __eq__(self, other):
        return (
            isinstance(other, Mutation) and
            self.description == other.description and
            self.request == other.request and
            self.parameters == other.parameters and
            self.url == other.url and
            self.name == other.name and
            self.type == other.type and
            self.response == other.response
        )

    def __hash__(self):
        return hash((self.description, self.request, self.parameters, self.url, self.name, self.type, self.response))

@dataclass
class OpenAPI:
    queries: list[Query]
    mutations: list[Mutation]
    servers: list[str]

    def __eq__(self, other):
        return (
            isinstance(other, OpenAPI) and
            self.queries == other.queries and
            self.mutations == other.mutations and
            self.servers == other.servers
        )

    def __hash__(self):
        return hash((self.queries, self.mutations, self.servers))



