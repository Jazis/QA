import sys
sys.path.append('../../imports/')
from debug import *

import logging
from getter import getFromConfig
from waiter import *
from messages import *
import allure

@allure.title("No login _api_bpm_camunda_engine_default_history_variable-instance method check")
def test_start(debugLevel):
    debugEnable(int(debugLevel))
    link = "/api/bpm/camunda/engine/default/history/variable-instance"
    host = getFromConfig("host")
    logging.info("Trying -> " + link)
    request0 = waitGetResponseToBeChanged("http://" + host + link, "data")
    try:
        request = waitGetResponseToBeChanged("http://" + host + link, "data").split('"message":"')[1].split('"')[0]
    except:
        request = waitGetResponseToBeChanged("http://" + host + link, "data").split('"message": "')[1].split('"')[0]
    assert request in messages.noLoginBadAnswers, "Something went wrong with this link ->" + link                
                                           