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
def rolesCheck(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        newSeal = authFromAnotherUser("operator_login", "operator_password").replace("%7C", "|")
        host = getFromConfig("host")
        username = getFromConfig("operator_login")
        message = _is_loggin_test(newSeal, host)
        assert f'"user":"{newSeal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + newSeal.split("|")[0])
        assert getFromConfig("operator_login") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Try to check roles list")
        cookies = {
            'root.user': '',
            'root.init_params.messages': '',
            'user': 'null',
            'user1.cfg-tree.sel_path': '',
            'user1.user': '',
            'user1.init_params.messages': '',
            'root.profile_display_name': 'Administrator',
            'user1.profile_display_path': '%2F',
            'user1.profile_display_name': '',
            'user1.profile_path': '',
            #'username': 'root',
            'seal': newSeal,
            'root.profile_path': '%2F',
            'root.profile_display_path': '%2F',
            'root.cfg-tree.sel_path': '%2F',
        }

        headers = {
            'Host': f'{host}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': f'http://{host}',
            'Referer': f'http://{host}/front/site/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close',
        }
        for i in range(100):
            response = requests.get(f'http://{host}/rest/auth/v1/apps/1/roles/' + str(i), cookies=cookies, headers=headers, verify=False)
            if "role" in response.text:
                logging.info(f"[{i}] " + response.text)
        data = '{"role":"boyz","description":"ee"}'
        response = requests.post(f'http://{host}/rest/auth/v1/apps/1/roles', cookies=cookies, headers=headers, data=data, verify=False)
        assert '{"detail":"Access denied"}' in response.text, "We create new role!!!! That's not good, miss much in rules"
        logging.info("Sucessflly checked checked roles!")
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Roles check')
def test_userRolescheck(seal):
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    rolesCheck(seal1)