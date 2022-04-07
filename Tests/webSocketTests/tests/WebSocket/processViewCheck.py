import sys

sys.path.append("../../imports/")
from connect import *
from waiter import *
import time
import re
import pytest
import logging
import allure


@allure.step("Checking project processes")
def processCheck(ws, seal, authId):
    waitForResponse(ws,'[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"' + authId + '\\",\\"seal\\":\\"' + seal +'\\"}"],{}]',True,10,2)
    logging.info("api.konfigd.auth going successfully")
    message = waitForResponse(ws,'[48,4525279033177098,{"receive_progress":false},"api.konfigd.get",["2bb76118-6ef9-a6d6-cb97-bd1dce2ad2d6","exec overlord.pl ping --json"],{}]',True,10,2)
    return message


# @allure.feature(' The name of the function ')
# @allure.story(' Subfunction name ')
@allure.title("Checking project processes")
# @allure.description(' Test case description ')
def test_processCheck(seal):
    seal1 = seal.replace("qweDelimqwe", "|")
    data = auth(seal1)
    ws = data[0]
    seal = data[1]
    authId = data[2]
    dataFormat(processCheck(ws, seal, authId))
    ws.close()


@allure.step("Searching processes in response body")
def dataFormat(data):
    newData = str(data).replace("},\"data\":[", "")
    if len(newData.split("},{")) == 48:
        logging.info("Success! All 48 processes are visible")
