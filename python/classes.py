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

    def __post_init__(self):
        validate_str(self.__dict__)


@dataclass
class Component:
    name: str = field(metadata={'required': True})
    attributes: list[Attribute] = field(default_factory=list)


@dataclass
class Schema:
    type: str = field(metadata={'required': True})
    component: Component = field(metadata={'required': True})

    def __post_init__(self):
        validate_str(self.__dict__)


@dataclass
class Response:
    schema: Schema = field(metadata={'required': True})


@dataclass
class RequestBody:
    required: bool = field(metadata={'required': True})
    schema: Schema = field(default=None)


@dataclass
class Parameter:
    name: str = field(metadata={'required': True})
    type: str = field(metadata={'required': True})
    query: bool = field(metadata={'required': True})
    required: bool = field(metadata={'required': True})

    def __post_init__(self):
        validate_str(self.__dict__)


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

@dataclass
class OpenAPI:
    queries: list[Query]
    mutations: list[Mutation]
    servers: list[str]



