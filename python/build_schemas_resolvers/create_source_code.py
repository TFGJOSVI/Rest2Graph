from build_schemas_resolvers.build_resolvers import build_resolvers
from build_schemas_resolvers.create_open_api import create_open_api


def create_source_code(oas_path: str) -> None:

    open_api = create_open_api(oas_path)
    build_resolvers(oas_path)