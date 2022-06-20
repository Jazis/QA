import sys
sys.path.append('../../imports/')

from connect import *
from waiter import *
import pytest
import logging
import allure

@allure.step('Deleting machine from Tree')
def deleteDeviceFromTreeList(ws, seal,authId, newtestmachine, host):
    waitForResponse(ws, r'[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\"username\":\"'+ authId + r'\",\"seal\":\"'+ seal + r'\"}"],{}]')
    new_testmachine = str(newtestmachine).replace("-", "_")
    logging.info(f'Deleting {new_testmachine} from Tree') 
    message = waitForResponse(ws, '[48,3179904544707732,{"receive_progress":false},"api.konfigd.set",["0ca486f1-6888-f1cd-38ac-b0b981f667a3","exec konfne DEMOLISH /Tree/' + new_testmachine + ' --json"],{}]')
    checkAlreadyUsedNames(ws, seal,authId, newtestmachine, host, temp=0)


@allure.step('Checking Tree for name in list')
def checkAlreadyUsedNames(ws, seal, authId, newtestmachine, host, temp):
    getRequestForParseNames = requests.get(f"http://{host}/rest/tree/node?username={authId}&seal={seal}&path=/Tree").text
    logging.info(f'Checking Tree for name {newtestmachine} in list') 
    new_testmachine = str(newtestmachine).replace("-", "_")
    if temp == 0:
        if new_testmachine in getRequestForParseNames:
            deleteDeviceFromTreeList(ws, seal,authId, newtestmachine, host)   
    else:
        if new_testmachine in getRequestForParseNames:
            assert new_testmachine in getRequestForParseNames, "We found your new machine in list,"
            logging.info(f'Machine successfully deleted')

            
@allure.step('Adding new test machine to Tree')
def addingNewMachine(ws, seal, authId, host, machine):
    machineOs = machine[0].replace("device=", "")
    machineName = machine[1].replace("ip=", "")
    new_testmachine = str(machineName).replace("-", "_")
    waitForResponse(ws, '[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    waitForResponse(ws, '[48,6152715661537792,{"receive_progress":false},"api.konfigd.get",["08593f34-0d7c-39fd-7eae-cef72dd3cabc","exec konfne params --json ' + machine[0].replace("device=", "") + r'"],{}]')
    query = r'[48,2587343106998326,{"receive_progress":true},"api.konfigd.set",["3efe5182-0f28-ca6b-aa40-0737e8f1409b","exec konfne --device ' + machine[0].replace("device=", "") + r'  --tag \"ip=' + machine[1].replace("ip=", "") + r'\" '
    for elem in machine:
        if "device" not in elem and "ip" not in elem:
            query += r'--tag \"' +elem + r'\" '
            if "community=" in elem:
                query += " --fetchname "
    query+=r' add /Tree/' + new_testmachine + r' --json"],{}]'
    waitForResponse(ws, query)
    checkAlreadyUsedNames(ws, seal, authId, machineName, host, temp=1)

@allure.step('Connect all new signals from list to test machine')
def addingAllSignalForMachine(ws, machineName, host, seal, authId):
    machineName = machineName.replace("-", "_")
    waitForResponse(ws, '[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    waitForResponse(ws, '[48,8370770664346762,{"receive_progress":false},"api.konfigd.get",["862d7371-5bcb-edf3-e300-b07da12e9c33","exec alertsedit.pl --list-lic --json /Tree/' + machineName + r'"],{}]')
    waitForResponse(ws, '[48,3924402765767258,{"receive_progress":false},"api.konfigd.set",["600fe80c-6984-ae5b-9501-793919b47fca","exec alertsedit.pl --templates=\\"CiscoSanMDS,emc-dae,emc-disk,emc-dpe,emc-cpu,emc-lcc,emc-ps,esb-event,esb-process,diskIO,cim-health,cisco-router,hpux-cpu,hpux-memory,hpux-storage,gawain-gauge,generic-printer-toner,generic-printer-status,LinuxProcess,netflow,lancelot-alerts,lancelot-fifo,lancelot-fnmp,lancelot-kollector,lancelot-rest,linux-cpu-core-info,lnx-cpu,lnx-memory,lnx-storage,prisma-app-status,prisma-fan-status,prisma-enc-status,prisma-eth-status,prisma-temp-sensor,prisma-ser-status,process-run-table,traffic,traffic64,saa-router-rtt-icmp-ping,saa-router-rtt-http-get,saa-router-voip-jitter,sun-cpu,sun-memory,sun-storage,windows-cpu,windows-memory,windows-service,windows-storage,winnt-cpu,winnt-memory,winnt-storage\\" assign /Tree/' + machineName + r' --json"],{}]', True, 20, 10)
    getCheckingSignalsOnMachine = waitGetResponse(f'http://{host}/rest/tree/node?username={authId}&seal={seal}&with_alerts=1&filter_tags=0&path=/Tree/{machineName}')
    message = waitGetResponse(f'http://{host}/rest/tree/node?username={authId}&seal={seal}&with_alerts=1&filter_tags=0&path=/Tree/{machineName}')
    logging.info("Check signals on machine")
    logging.info("Signals connected!")


@allure.title('Signal add/delete check')
@allure.description("The test tests the functions of creating, deleting test PC")
def test_workWithSignals(seal):
    for machine in open('../../devices.ini', 'r').readlines():
        if sys.argv[1].replace("\n", "") in machine:
            machine = "[" + machine.split("][")[1]
            machine = machine.replace("[\"", "").replace("\"]", "").replace('", "', " ").replace('"', "").replace(",", "").replace("\n", "")
            machine = machine.split(" ")
            machineName = machine[1].replace("ip=", "")
            seal1 = seal.replace("qweDelimqwe", "|")
            data = auth(seal1)
            ws = data[0]
            seal = data[1]
            authId = data[2]
            newtestmachine = data[3]
            host = data[4]
            logging.info(f'Starting main functions') 
            checkAlreadyUsedNames(ws, seal, authId, machineName, host, temp=0)
            addingNewMachine(ws, seal, authId, host, machine)
            addingAllSignalForMachine(ws, machineName, host, seal, authId)
            deleteDeviceFromTreeList(ws, seal,authId, machineName, host)
            ws.close()