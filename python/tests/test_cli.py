import os
import sys
import tempfile

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from click.testing import CliRunner
from python.main import build_graph
from python.paths import TESTS_SET_PATH

class TestCLI:

    def setup_class(cls):

        oas_ady = {
            'name': 'adyen_developer_experience_team.yaml',

        }
        oas_config = {
            'name': 'configuration_API.yaml',
        }
        oas_pel = {
            'name': 'peliculas.yaml',
        }
        oas_pet = {
            'name': 'pet_clinic.yaml',
        }

        cls.oas_list = [oas_pet, oas_pel, oas_ady, oas_config]

        cls.runner = CliRunner()

    def test_build_graph_help(self):

        result = self.runner.invoke(build_graph, ['--help',])

        assert '--oas-path' in result.output
        assert '--destination-path' in result.output
        assert '--config-file' in result.output
        assert '--help' in result.output

    def test_build_graph(self):

        for i in self.oas_list:
            self.runner.invoke(build_graph, ['--oas-path', os.path.join(TESTS_SET_PATH, i['name']), '--destination-path', tempfile.gettempdir()])

            assert os.path.exists(os.path.join(tempfile.gettempdir(),'sourceCode.zip'))
