import sys
sys.path.append('../../imports/')

from connect import auth
from waiter import waitResponse
import pytest
import logging
import allure

@allure.step('Adding new test machine to Tree')
def addingNewMachine(ws, seal, authId, host, machine):
    machineOs = machine[0].replace("device=", "")
    machineName = machine[1].replace("ip=", "")
    new_testmachine = str(machineName).replace("-", "_")
    ws.send(r'[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\"username\":\"'+ authId + r'\",\"seal\":\"'+ seal + r'\"}"],{}]')
    message = waitResponse(ws)
    ws.send('[48,6152715661537792,{"receive_progress":false},"api.konfigd.get",["08593f34-0d7c-39fd-7eae-cef72dd3cabc","exec konfne params --json ' + machine[0].replace("device=", "") + r'"],{}]')
    message = waitResponse(ws)
    assert "08593f34-0d7c-39fd-7eae-cef72dd3cabc" in message, "qwe"
    query = r'[48,2587343106998326,{"receive_progress":true},"api.konfigd.set",["3efe5182-0f28-ca6b-aa40-0737e8f1409b","exec konfne --device ' + machine[0].replace("device=", "") + r'  --tag \"ip=' + machine[1].replace("ip=", "") + r'\" '
    for elem in machine:
        if "device" not in elem and "ip" not in elem and elem != "":
            query += r'--tag \"' +elem + r'\" '
            if "community=" in elem:
                query += " --fetchname "
    query+=r' add /Tree/' + new_testmachine + r' --json"],{}]'
    ws.send(query)
    message = waitResponse(ws, "3efe5182-0f28-ca6b-aa40-0737e8f1409b")
    
def test_workWithDevices(seal):
    for machine in open('../../devices.ini', 'r').readlines():
        machine = machine.replace("[\"", "").replace("\"]", "").replace('", "', " ").replace('"', "").replace(",", "").replace("\n", "")
        machine = machine.split(" ")
        machineName = machine[1].replace("ip=", "")
        seal1 = seal.replace("qweDelimqwe", "|")
        data = auth(seal1)
        ws = data[0]
        seal = data[1]
        authId = data[2]
        host = data[4]
        logging.info(f'Starting main functions') 
        addingNewMachine(ws, seal, authId, host, machine)
