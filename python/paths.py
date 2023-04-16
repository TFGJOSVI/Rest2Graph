import os
import sys

PYTHON_PATH = os.path.abspath(os.path.dirname(__file__)) + '{}'.format(os.path.sep)
ROOT_PATH = os.path.dirname(PYTHON_PATH)
TESTS_PATH = os.path.join(PYTHON_PATH, 'tests')
TESTS_SET_PATH = os.path.join(TESTS_PATH, 'tests_set')
OAS_ANALYSIS_PATH = os.path.join(PYTHON_PATH, 'oas_analysis')
CONFIG_FILE_PATH = os.path.join(PYTHON_PATH, 'config_file')
COPIES_TEMPLATE_PATH = os.path.join(CONFIG_FILE_PATH, 'copies_templates')
CONFIG_FILE_TEMPLATE = os.path.join(CONFIG_FILE_PATH, 'templates', 'config_template_v1.txt')
