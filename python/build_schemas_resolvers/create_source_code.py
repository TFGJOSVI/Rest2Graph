from python.build_schemas_resolvers.write_resolvers import write_resolvers
from python.build_schemas_resolvers.build_resolvers import build_resolvers
from python.build_schemas_resolvers.create_open_api import create_open_api, create_open_api_not_default_path
from python.paths import SOURCE_CODE_RETURN_ZIP, SOURCE_CODE_RETURN_PATH, SOURCE_CODE_BASE_PATH
from python.build_schemas_resolvers.utils import zip_directory
from python.classes import OpenAPI


def create_source_code(oas_path: str, open_api:OpenAPI = None) -> None:

    """
    Create the source code of the project.

    :param open_api:
        The open api object.
    :param oas_path:
        The path of the open api file.
    :return:
        None
    """

    if open_api is None:
        open_api = create_open_api(oas_path)

    write_resolvers(open_api)
    zip_directory(SOURCE_CODE_RETURN_PATH, SOURCE_CODE_RETURN_ZIP)

def create_source_code_not_default_path(dst_path: str) -> None:

    """
    Create the source code of the project with a config file path.

    :param dst_path:
        The path of the config file.
    :return:
        None
    """

    open_api = create_open_api_not_default_path(dst_path)
    write_resolvers(open_api)
    zip_directory(SOURCE_CODE_RETURN_PATH, SOURCE_CODE_RETURN_ZIP)

def build_schemas_resolvers(oas_path: str) -> None:
    oas = create_open_api(oas_path)

    resolver = build_resolvers(oas)

    write_resolvers(oas)

    zip_directory(SOURCE_CODE_BASE_PATH, SOURCE_CODE_RETURN_ZIP)
