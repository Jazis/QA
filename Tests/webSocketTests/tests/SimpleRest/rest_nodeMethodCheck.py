import sys

import pytest
sys.path.append('../../imports/')
from debug import *
import requests
import logging
from getter import getFromConfig
from waiter import *
import allure
from connect import *
import time


@allure.step('User view json response')
def _is_loggin_test(seal, host):
    requests.packages.urllib3.disable_warnings() 
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal}, verify=False, cert=None)
    return isLogginRequest.text

@allure.step('Searching passwords in methods')
def nodeethodCheck(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        host = getFromConfig("host")
        username = getFromConfig("login")
        message = _is_loggin_test(seal, host)
        assert f'"user":"{seal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + seal.split("|")[0])
        assert getFromConfig("login") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Try to check method")
        message = requests.get(f"http://{host}/rest/tree/node?username={username}&seal={seal}&end_path=%2F&with_alerts=1&filter_tags=0&with_notifications=1&path=%2F", cookies={"seal" : seal}, verify=False, cert=None).text
        for elem in { "snmp-community", "permissions", "auto-target-path", "fnmp-collector-name", "auto-target-name-unlinked" }:
            assert elem in message, f"We cannot find this key -> {elem}"
            logging.info(f"We found {elem} in response")
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Searching passwords in methods')
def test_nodeethodCheck(seal):
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    nodeethodCheck(seal1)