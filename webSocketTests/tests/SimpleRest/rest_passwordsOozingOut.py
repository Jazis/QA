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

class temp():
    methods = [
        "/rest/account/is_logged_in",
        "/rest/account/login",
        "/rest/account/logout",
        "/rest/account/update_seal",
        "/rest/server/about",
        "/rest/server/license",
        "/rest/server/refresh_license",
        "/rest/tree/node",
        "/rest/tree/nodes",
        "/rest/device/target",
        "/rest/device/target_views",
        "/rest/device/report_view",
        "/rest/device/targets",
        "/rest/server/locale",
        "/rest/alert/history",
        "/rest_long/alert/history",
        "/rest/alert/history",
        "/rest/alert/new_comment",
        "/rest_long/alert/comments",
        "/rest/inventory/device_descr",
        "/rest/inventory/targets",
        "/rest/access/userget",
        "/rest/access/useradd",
        "/rest/access/usermod",
        "/rest/access/userdel",
        "/rest/access/groupget",
        "/rest/access/groupadd",
        "/rest/access/groupmod",
        "/rest/access/groupdel",
        "/rest/access/group_addusers",
        "/rest/access/group_delusers",
        "/rest/access/get_group_paths",
        "/rest/access/group_delpaths",
        "/rest/access/permsmod",
        "/rest/access/ldap_sync_ad"
    ]

@allure.step('User view json response')
def _is_loggin_test(seal, host):
    requests.packages.urllib3.disable_warnings() 
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal}, verify=False, cert=None)
    return isLogginRequest.text

@allure.step('Searching passwords in methods')
def passwordsOozingOut(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        host = getFromConfig("host")
        username = getFromConfig("login")
        message = _is_loggin_test(seal, host)
        assert f'"user":"{seal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + seal.split("|")[0])
        assert getFromConfig("login") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Try to check methods")
        for method in temp.methods:
            message = requests.get(f"http://{host}{method}", cookies={"seal" : seal}, verify=False, cert=None).text
            for elem in ['"{SHA' + "}"]:
                assert elem not in message, "Something wrong with json response"
            logging.info(f"Sucessflly checked {method} for passwords in respose")
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Searching passwords in methods')
def test_passwordsOozingOut(seal):
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    passwordsOozingOut(seal1)