import sys
sys.path.append('../../imports/')

from connect import *
from waiter import *
import pytest
import logging
import allure

class temp():
    testSignalName = "TEST_SIGNAL_BY_TEST"
    testSubSignalName = "TEST_SUBSIGNAL_BY_TEST"

@allure.step('Create | Delete | Substep')
def alertsCheck(ws, authId, seal, host):
    ws.send('[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    logging.info("Authorized in api.konfigd.auth")
    waitResponse(ws)
    ws.send('[48,5145741861936976,{"receive_progress":false},"api.konfigd.get",["65a340af-be4b-f42e-0e57-5dab13321d46","exec alertsedit.pl --list --json"],{}]')
    message = ws.recv()
    assert temp.testSignalName not in message, "Something went wrong! Signal for test not deleted"
    logging.info( temp.testSignalName + " not founded in signals list")
    ws.send(r'[48,7064751568892062,{"receive_progress":false},"api.konfigd.set",["adcbf872-fa44-89d8-3a33-37016c3b0b58","exec alertsedit.pl ' + temp.testSignalName + r' create /Tree/'+ host + '/cpu --json"],{}]')
    waitResponse(ws)
    ws.send('[48,5710816997664542,{"receive_progress":false},"api.konfigd.set",["fa030abd-c0fc-d5e4-7381-08921bd90951","exec alertsedit.pl ' + temp.testSignalName + ' setup display-name=\''+ temp.testSignalName + '\' --json"],{}]')
    waitResponse(ws)
    ws.send(r'[48,2777448116771864,{"receive_progress":false},"api.konfigd.get",["1eaf514e-c08e-16f8-a75e-12f2c829cd5f","exec alertsedit.pl --list --json"],{}]')
    message = ws.recv()
    assert temp.testSignalName not in message, "Not found signal name in public list"
    ws.send(r'[48,6335085802664888,{"receive_progress":false},"api.konfigd.get",["2c7d5d45-c6b8-d5d3-13b6-c7f2cc35b632","exec alertsedit.pl ' + temp.testSignalName + r' dump --json"],{}]')
    message = ws.recv()
    assert temp.testSignalName in message, "Something went wrong! Signal for test not created"
    ws.send(r'[48,3749666729131486,{"receive_progress":false},"api.konfigd.set",["133f7348-5c6b-a4bc-0c59-ba86236230e6","exec alertsedit.pl ' + temp.testSignalName + r' add \"'+ temp.testSubSignalName+ r'\" Gauge linuxGenericCpuUtil --json"],{}]')
    waitResponse(ws)
    logging.info("Subsignal are connected")
    ws.send('[48,293563726994826,{"receive_progress":false},"api.konfigd.set",["c40d795c-9c28-a6d7-78f8-b241f6057625","exec alertsedit.pl ' + temp.testSignalName + ' remove --json"],{}]')
    waitResponse(ws)
    logging.info("Trying to remove test signal")
    ws.send('[48,4326942052087000,{"receive_progress":false},"api.konfigd.get",["aa1a64a8-c8f7-08d5-3617-62a983044efb","exec alertsedit.pl --list --json"],{}]')
    message = ws.recv()
    assert temp.testSignalName not in message, "Something went wrong! Signal for test not deleted"
    logging.info("Signal removed")

@allure.title('Alerts testing | Create | Delete | Subsignal')
@allure.description("The test tests the functions of creating, deleting and binding a sub-signal")
def test_alerts(seal):
    seal1 = seal.replace("qweDelimqwe", "|")
    data = auth(seal1)
    ws = data[0]
    seal0 = data[1]
    authId = data[2]
    newtestmachine = data[3]
    host = data[4]
    alertsCheck(ws, authId, seal0, host)