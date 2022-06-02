
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

@allure.step('is_loggin_in get request')
def _is_loggin_test(seal, host):
    requests.packages.urllib3.disable_warnings() 
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal}, verify=False, cert=None)
    return isLogginRequest.text

@allure.step('Run main seal validation test')
def sealValidation(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        host = getFromConfig("host")
        message = _is_loggin_test(seal, host)
        assert f'"user":"{seal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + seal.split("|")[0])
        assert getFromConfig("login") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Try to update seal")
        sealUpdate = requests.get(f"http://{host}/rest/account/update_seal", cookies={"seal" : seal}, verify=False, cert=None).cookies.get_dict()
        message = waitGetResponseToBeChanged(f"http://{host}/rest/account/is_logged_in", sealUpdate)
        assert seal.split("|")[0] not in message, "Seal not updated"
        logging.info("Seal successfully updated")
        logging.info(seal.split("|")[0] + " -> " + sealUpdate['seal'].split("%7C")[0])
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Seal update test')
def test_sealTest(seal):
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    sealValidation(seal1)