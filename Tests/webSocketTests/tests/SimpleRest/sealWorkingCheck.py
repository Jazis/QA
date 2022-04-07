
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

class temp():
    customPayloads = ['f', '-', 'customWhat', '\'']

@allure.step('is_loggin_in get request')
def _is_loggin_test(seal, host):
    requests.packages.urllib3.disable_warnings() 
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal}, verify=False, cert=None)
    return isLogginRequest.text

def answerCheck(text):
    errorMsg = False
    for message in messages.noLoginBadAnswers:
        if message in text:
            errorMsg = True
    if "503 Service Unavailable" in text:
        logging.warning("503 Service Unavailable in response!!!")
    return errorMsg
    

@allure.step('Run seal checker')
def sealWorkingCheck(seal):
    try:
        requests.packages.urllib3.disable_warnings() 
        host = getFromConfig("host")
        message = _is_loggin_test(seal, host)
        assert f'"user":"{seal.split("|")[2]}"' in message, "Seal not loggin in"
        logging.info("Seal loggin in -> " + seal.split("|")[0])
        assert getFromConfig("login") in message, "User login not found on this page"
        logging.info("User login found on page")
        logging.info("Original seal -> " + seal.split("|")[0] + "|" + seal.split("|")[1] + "|" + seal.split("|")[2])
        for method in methods.restMethods:
            if "/rest/server/license" in method:
                continue
            time.sleep(1)
            sealCheck = waitGetResponseToBeChanged(f"http://{host}{method}?seal=" + seal.split("|")[0] + "|" + seal.split("|")[1] + "|" + seal.split("|")[2])
            assert sealCheck not in messages.noLoginBadAnswers, 'Something wrong with response!'
            logging.info(f"Sucessfully trying -> http://{host}{method}?seal=" + seal.split("|")[0] + "|" + seal.split("|")[1] + "|" + seal.split("|")[2])
            for payload in temp.customPayloads:
                url = f"http://{host}{method}?seal=" + seal.split("|")[0] + f"{payload}|" + seal.split("|")[1] + "|" + seal.split("|")[2]
                sealCheck = waitGetResponseToBeChanged(url)
                assert bool(answerCheck(sealCheck)) == True, 'Something wrong with response!\nUrl -> ' + url
                logging.info(f"Sucessfully trying -> {url}")
                url = f"http://{host}{method}?seal=" + seal.split("|")[0] + "|" + seal.split("|")[1] + f"{payload}|" + seal.split("|")[2]
                sealCheck = waitGetResponseToBeChanged(url)
                assert bool(answerCheck(sealCheck)) == True, 'Something wrong with response!\nUrl -> ' + url             
                logging.info(f"Sucessfully trying -> {url}")
                url = f"http://{host}{method}?seal=" + seal.split("|")[0] + "|" + seal.split("|")[1] + "|" + seal.split("|")[2] + f"{payload}"
                sealCheck = waitGetResponseToBeChanged(url)
                assert bool(answerCheck(sealCheck)) == True, 'Something wrong with response!\nUrl -> ' + url             
                logging.info(f"Sucessfully trying -> {url}")
        logging.info("Seal working correctly")
    except requests.exceptions.SSLError:
        pytest.fail("Plaese, try again without SSL check (--no-ssl) - requests.exceptions.SSLError")


@allure.title('Seal working check')
def test_sealWorkingTest(seal, debugLevel):
    debugEnable(int(debugLevel))
    requests.packages.urllib3.disable_warnings() 
    seal1 = seal.replace("qweDelimqwe", "|")
    sealWorkingCheck(seal1)