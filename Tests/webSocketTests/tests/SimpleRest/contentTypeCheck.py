
import sys

import pytest
sys.path.append('../../imports/')
from debug import *
import requests
import time

import requests
import logging
from getter import getFromConfig
from waiter import *
import allure
from methods import *
from messages import *

@allure.step('Content-Type check')
def contentTypeChecker(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        host = getFromConfig("host")
        for method in methods.restMethods:
            time.sleep(1)
            logging.info(f"Trying -> http://{host}{method}?seal=" + seal)
            request = waitGetResponseToBeChanged(f"http://{host}{method}?seal=" + seal, content = "headers")
            assert "application/json" in  request["Content-Type"] or "text/plain" in request["Content-Type"], f'Wrong content type!!!\nContent-Type: {request["Content-Type"]}\nUrl: http://{host}{method}?seal={seal}'
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Content-Type checking')
@allure.link('https://jira.link-to.ru/browse/ZS-12898')
def test_contentTypeChecker(seal, debugLevel):
    debugEnable(int(debugLevel))
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    contentTypeChecker(seal1)