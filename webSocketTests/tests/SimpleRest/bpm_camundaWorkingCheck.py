
import sys
sys.path.append('../../imports/')
from debug import *

import requests
import logging
from getter import getFromConfig
from waiter import *
import allure

@allure.step('Try to connect')
def camundaTest(seal):
    host = getFromConfig("host")
    login = getFromConfig("login")
    logging.info("Try connect to camunda")
    camundaTestRequest = requests.get(f"http://{host}/api/bpm/camunda/engine?login={login}&seal={seal}")
    assert '[{"name": "default"}]' in camundaTestRequest.text, "Camunda not work"
    logging.info("Successfully connected")

@allure.title('Seal update test')
def test_CamundaTest(seal, debugLevel):
    debugEnable(int(debugLevel))
    seal1 = seal.replace("qweDelimqwe", "|")
    camundaTest(seal1)