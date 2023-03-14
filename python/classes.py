from dataclasses import dataclass, field


# Validations
def validate_list(field, value):
    if not value:
        raise ValueError(f'{field.name}: the list cannot be empty')
    return value


# Dataclass
@dataclass
class Atribute:
    name: str = field(default='', metadata={'required': True})
    type: str = field(default='', metadata={'required': True})
    required: bool = field(default=False, metadata={'required': True})


@dataclass
class Component:
    atributes: list[Atribute] = field(default_factory=list, metadata={'validate': validate_list})
    name: str = field(default='', metadata={'required': True})


@dataclass
class Schema:
    type: str = field(default='', metadata={'required': True})
    component: Component = field(default=None, metadata={'required': True})


@dataclass
class Response:
    schema: Schema = field(default=None, metadata={'required': True})


@dataclass
class RequestBody:
    schema: Schema
    required: bool = field(default=False, metadata={'required': True})


@dataclass
class Parameter:
    name: str = field(default='', metadata={'required': True})
    type: str = field(default='', metadata={'required': True})
    query: bool = field(default=False, metadata={'required': True})
    required: bool = field(default=False, metadata={'required': True})


@dataclass
class Query:
    description: str
    parameters: list[Parameter]
    url: str = field(default='', metadata={'required': True})
    name: str = field(default='', metadata={'required': True})
    response: Response = field(default=None, metadata={'required': True})


@dataclass
class Mutation:
    description: str
    request: RequestBody
    parameters: list[Parameter]
    url: str = field(default='', metadata={'required': True})
    name: str = field(default='', metadata={'required': True})
    response: Response = field(default=None, metadata={'required': True})
