import sys
sys.path.append('../../imports/')
from debug import *

import requests
import logging
from getter import getFromConfig
from waiter import *
import allure

@allure.step('is_loggin_in get request')
def _is_loggin_test(seal, host):
    isLogginRequest = requests.get(f"http://{host}/rest/account/is_logged_in", cookies={"seal" : seal})
    return isLogginRequest.text

@allure.step('Searching mp3 files in lancelot-data')
def soundSearching(seal):
    host = getFromConfig("host")
    username = getFromConfig("login")
    getMusicList = requests.get(f'http://{host}/rest/account/ls?dir=var/lancelot-data/_sounds&ext=mp3&seal={seal}&username={username}')
    message = getMusicList.text
    assert 'data' in message and 'var/lancelot-data/' in message, "Cannot find sounds"
    logging.info("Sounds in list!")

@allure.title('Sounds mp3 check')
def test_sound(seal, debugLevel):
    debugEnable(int(debugLevel))
    seal1 = seal.replace("qweDelimqwe", "|")
    soundSearching(seal1)