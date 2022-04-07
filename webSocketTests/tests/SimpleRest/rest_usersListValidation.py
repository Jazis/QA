
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

@allure.step('User view json response')
def _is_loggin_test(seal, host):
    requests.packages.urllib3.disable_warnings() 
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal}, verify=False, cert=None)
    return isLogginRequest.text

@allure.step('User list json view test')
def sealValidation(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        host = getFromConfig("host")
        username = getFromConfig("login")
        message = _is_loggin_test(seal, host)
        assert f'"user":"{seal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + seal.split("|")[0])
        assert getFromConfig("login") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Try to check users list")
        message = requests.get(f"http://{host}/rest/access/userget?&username={username}&seal={seal}&disabled=false&page=1&start=0", verify=False, cert=None).text
        for elem in ["displayName", "policies", "profile-policy-current", "auth", "user", "login", "path", "dpath", "permissions", "group" ]:
            assert elem  in message, "Something wrong with json response"
        logging.info("Sucessflly checked json response with users")
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('User list json view test')
def test_sealTest(seal):
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    sealValidation(seal1)