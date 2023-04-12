from oas_analysis.utils import load_oas
from paths import TESTS_SET_PATH
import os

class TestOasAnalysis:

    def setup_class(cls):
        cls.oas_1 = load_oas(os.path.join(TESTS_SET_PATH,'configuration_API.yaml'))
        cls.oas_2 = load_oas(os.path.join(TESTS_SET_PATH, 'adyen_developer_experience_team.yaml'))
        cls.oas_3 = load_oas(os.path.join(TESTS_SET_PATH, 'authentiq_team.yaml'))
        cls.oas_4 = load_oas(os.path.join(TESTS_SET_PATH, 'peliculas.yaml'))
        cls.oas_5 = load_oas(os.path.join(TESTS_SET_PATH, 'pet_clinic.yaml'))

    def test_prueba(self):
        print(self.oas_1)
        print(self.oas_2)
        print(self.oas_3)
        print(self.oas_4)
        print(self.oas_5)

        assert False
