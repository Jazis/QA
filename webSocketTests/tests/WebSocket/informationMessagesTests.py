import sys
sys.path.append('../../imports/')

from connect import *
from waiter import *
import pytest
import logging
import allure

class temp():
    testMessageName = "TEST_MESSAGE_NAME"
    testMessageParameter = "TEST_PARAMETER"

@allure.step('Information messages test')
def addNewMEssage(ws, authId, seal, host):
    ws.send('[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    logging.info("Authorized in api.konfigd.auth")
    waitResponse(ws)
    checkList(ws, "name")
    ws.send(r'[48,2750552443725732,{"receive_progress":false},"api.info_msg.create_template",[],{"template":{"name":"' + temp.testMessageName + r'","content":"<span>{template}</span>"}}]')
    message = waitResponse(ws)
    assert r'data":{"success":true' in message, "Error with adding new message"
    checkList(ws, temp.testMessageName)
    setDescription(ws)
    addParam(ws)
    removeParam(ws)
    # checkList(ws, temp.testMessageParameter)
    removeMessage(ws)
    
def removeMessage(ws):
    logging.info("Removing message " + temp.testMessageParameter + " in " + temp.testMessageName)
    ws.send(r'[48,1621413467715036,{"receive_progress":false},"api.info_msg.delete_template",[],{"name":"' + temp.testMessageName + r'"}]')
    waitResponse(ws)
    ws.send(r'[48,8407576860288522,{"receive_progress":false},"api.info_msg.get_templates",[]]')
    message = waitResponse(ws)
    assert temp.testMessageName not in message, "The message was not deleted"

def removeParam(ws):
    logging.info("Removing parameter...")
    ws.send(r'[48,694249696132376,{"receive_progress":false},"api.info_msg.save_template",[],{"template":{"params":{"' + temp.testMessageParameter + r'":null},"name":"TEST_NAME_OF_MESSAGE"}}]')
    waitResponse(ws)
   
def addParam(ws):
    logging.info("Adding parameter " + temp.testMessageParameter + " in " + temp.testMessageName)
    ws.send(r'[48,784178240428412,{"receive_progress":false},"api.info_msg.save_template",[],{"template":{"params":{"' + temp.testMessageParameter + r'":""},"name":"' + temp.testMessageName + r'"}}]')
    message = waitResponse(ws)
    assert r'[{"data":{"success":true}}]]' in message, "Cannot add new parameter"
    
def checkList(ws, data = ""):
    logging.info("Checking list for " + data + "...")
    ws.send(r'[48,980082037499158,{"receive_progress":false},"api.info_msg.get_templates",[]]')
    message = waitResponse(ws, r'[{"data":[{"name":"')
    assert data in message, "Something wrong with get list of information messages"
    return message

def setDescription(ws):
    logging.info("Setting new description...")
    ws.send(r'[48,8927382072056122,{"receive_progress":false},"api.info_msg.save_template",[],{"template":{"params":{},"description":"test description","title":"Test title","groups":["administrators"],"users":["root"],"name":"'+ temp.testMessageName + r'"}}]')
    message = waitResponse(ws)
    assert r'[{"data":{"success":true}}]' in message, "Something wrong with update description information in information messages"

@allure.title('Information messages test')
def test_InformationMessages(seal):
    seal1 = seal.replace("qweDelimqwe", "|")
    data = auth(seal1)
    ws = data[0]
    seal0 = data[1]
    authId = data[2]
    newtestmachine = data[3]
    host = data[4]
    addNewMEssage(ws, authId, seal0, host)