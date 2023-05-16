import os

from build_schemas_resolvers.build_resolvers import build_resolvers
from python.build_schemas_resolvers.create_open_api import create_open_api
from python.build_schemas_resolvers.write_resolvers import write_resolvers
from python.build_schemas_resolvers.utils import zip_directory
from python.paths import TESTS_SET_PATH, SOURCE_CODE_BASE_PATH, SOURCE_CODE_RETURN_ZIP

FILE_PATH = os.path.join(TESTS_SET_PATH, 'pet_clinic.yaml')





