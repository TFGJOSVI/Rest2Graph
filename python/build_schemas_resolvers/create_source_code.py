from python.build_schemas_resolvers.build_resolvers import build_resolvers
from python.build_schemas_resolvers.create_open_api import create_open_api
from python.paths import SOURCE_CODE_RETURN_ZIP, SOURCE_CODE_RETURN_PATH
from python.build_schemas_resolvers.utils import zip_directory

def create_source_code(oas_path: str) -> None:

    open_api = create_open_api(oas_path)
    build_resolvers(open_api)
    zip_directory(SOURCE_CODE_RETURN_PATH, SOURCE_CODE_RETURN_ZIP)
