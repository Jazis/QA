import sys

import pytest
sys.path.append('../../imports/')
from debug import *
import requests

import requests
import logging
from getter import getFromConfig
from waiter import *
import allure
from connect import *

@allure.step('User view json response')
def _is_loggin_test(seal, host):
    requests.packages.urllib3.disable_warnings() 
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal}, verify=False, cert=None)
    return isLogginRequest.text

@allure.step('Group get user response')
def sealValidation(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        newSeal = authFromAnotherUser("login1", "password1")
        host = getFromConfig("host")
        username = getFromConfig("login1")
        message = _is_loggin_test(newSeal, host)
        assert f'"user":"{newSeal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + newSeal.split("|")[0])
        assert getFromConfig("login1") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Try to check users list")
        message = requests.get(f"http://{host}/rest/logger/user_logs", cookies={"seal" : newSeal}, verify=False, cert=None).text
        for elem in ['"user":"operator"', "Administrator"]:
            assert elem not in message, "Something wrong with json response"
        logging.info("Sucessflly checked json response with groups")
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Group get user response')
def test_sealTest(seal):
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    sealValidation(seal1)