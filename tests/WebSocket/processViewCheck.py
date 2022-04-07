import sys
sys.path.append('../../imports/')

from connect import *
from waiter import *
import time
import re
import pytest
import logging
import allure

@allure.step('Checking project processes')
def processCheck(ws, seal, authId):
    ws.send('[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    message = waitResponse(ws)
    assert 'f0369b56-ad01-e919-dfe6-9f0589d147f6' in message, "Something wrong with api.konfigd.auth."
    logging.info('api.konfigd.auth going successfully') 
    ws.send('[48,4525279033177098,{"receive_progress":false},"api.konfigd.get",["2bb76118-6ef9-a6d6-cb97-bd1dce2ad2d6","exec overlord.pl ping --json"],{}]')
    counter = 0
    while counter<=10: 
        messages = ws.recv()
        if ("2bb76118-6ef9-a6d6-cb97-bd1dce2ad2d6" in messages):
            break
        else:
            time.sleep(1)
            counter += 1
    assert "2bb76118-6ef9-a6d6-cb97-bd1dce2ad2d6" in messages, "Something wront with response message in websocket get process."
    ws.close()
    return messages

# @allure.feature(' The name of the function ')
# @allure.story(' Subfunction name ')
@allure.title('Checking project processes')
# @allure.description(' Test case description ')
def test_processCheck(seal):
    seal1 = seal.replace("qweDelimqwe", "|")
    data = auth(seal1)
    ws = data[0]
    seal = data[1]
    authId = data[2]
    dataFormat(processCheck(ws,seal,authId))

@allure.step('Searching processes in response body')
def dataFormat(data):
    newData = data.split("\"out\":\"")[1].split("}]}")[0] + "}]}"
    newData = newData.replace("\\\"", "")
    names = re.compile("name:[A-z-_]{1,}")
    if (len(names.findall(newData)) == 48):
        logging.info('Success! All 48 processes are visible') 