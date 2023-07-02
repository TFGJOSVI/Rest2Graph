import os
import sys
import threading
import time

from selenium.webdriver.common.by import By

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from webapp.r2gweb.main import app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from python.paths import TESTS_SET_PATH

class TestWeb:

    def setup_class(cls):

        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        # Iniciar el servidor Flask en un hilo separado
        cls.server = threading.Thread(target=app.run)
        cls.server.start()
        time.sleep(1)  # Esperar un segundo para que el servidor se inicie

        cls.options = Options()

        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.implicitly_wait(3)  # Esperar hasta 3 segundos para encontrar elementos en la página

    def teardown_class(cls):
        # Detener el servidor Flask
        cls.server.join()

    def test_prueba(self):
        self.driver.get('http://localhost:5000/')

        button = self.driver.find_element(By.XPATH, '//*[@id="modal-btn"]')
        button.click()

        button_submit = self.driver.find_element(By.XPATH, '//*[@id="inputGroupFile04"]')
        button_submit.send_keys(os.path.join(TESTS_SET_PATH, 'pet_clinic.yaml'))
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/button').click()

        time.sleep(6)


        self.driver.execute_script('document.querySelector("#build-get > button").click()')

        time.sleep(90)

        # assert Location is '/'
        assert self.driver.current_url == 'http://localhost:5000/'






