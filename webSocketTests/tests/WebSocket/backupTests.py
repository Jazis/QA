import re
import sys
sys.path.append('../../imports/')

from connect import *
from waiter import *
import pytest
import logging
import allure
import re
import requests

class temp():
    testBackupName = 'TEST_TEST_TEST_TEST'
    testBackupRestoreName = 'TEST_BACKUP_FOR_RESTORE'
    testMachine = ["device=Devices::Computers::Linux", "ip=qa-lnx-20", "community=public", "enable-disk-io=false", "enable-disks-changes=false", "split-cpu-by-units=false", "enable-hardware-changes=false",  "enable-process-changes=false",  "enable-software-changes=false",  "enable-arp-changes=false",  "enable-network-changes=false",  "enable-icmp-changes=false",  "enable-tcp-changes=false",  "enable-udp-changes=false",  "replicated=false"]

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
    waitForResponse(ws, r'[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\"username\":\"'+ authId + r'\",\"seal\":\"'+ seal + r'\"}"],{}]')
    waitForResponse(ws, r'[48,6152715661537792,{"receive_progress":false},"api.konfigd.get",["08593f34-0d7c-39fd-7eae-cef72dd3cabc","exec konfne params --json ' + machine[0].replace("device=", "") + r'"],{}]')
    query = r'[48,2587343106998326,{"receive_progress":true},"api.konfigd.set",["3efe5182-0f28-ca6b-aa40-0737e8f1409b","exec konfne --device ' + machine[0].replace("device=", "") + r'  --tag \"ip=' + machine[1].replace("ip=", "") + r'\" '
    for elem in machine:
        if "device" not in elem and "ip" not in elem and elem != "":
            query += r'--tag \"' +elem + r'\" '
            if "community=" in elem:
                query += " --fetchname "
    query+=r' add /Tree/' + new_testmachine + r' --json"],{}]'
    waitForResponse(ws, query)
    checkAlreadyUsedNames(ws, seal, authId, machineName, host, temp=1)

@allure.step('Make new backup')
def makeBackup(ws, authId, seal):
    logging.info("Making backup")
    waitForResponse(ws, '[48,5988383378038002,{"receive_progress":true},"api.konfigd.set",["b208e89b-4747-28c0-7af8-191f70d0569a","exec backup save ' + temp.testBackupRestoreName + ' --json"],{}]')
    logging.info("Searching new backup in list")
    message = waitForResponse(ws, '[48,6379282976853238,{"receive_progress":false},"api.konfigd.get",["16524f99-d3c6-e4df-d6fe-fa265cb6e8b3","exec backup list --json"],{}]')
    logging.info("New backup in list")

@allure.step('Restore backup')
def restoreBackup(ws, host, authId, seal, newtestmachine):
    waitForResponse(ws, '[48,93367551343864,{"receive_progress":true},"api.konfigd.set",["70fef11e-ae63-90a2-89da-82aec59101c4","exec backup restore ' + temp.testBackupRestoreName + ' --json"],{}]')
    logging.info("Restore backup")
    getRequestForParseNames = requests.get(f"http://{host}/rest/tree/node?username={authId}&seal={seal}&path=/Tree").text
    logging.info(f'Checking Tree for name {newtestmachine} in list') 
    new_testmachine = str(newtestmachine).replace("-", "_")
    if new_testmachine in getRequestForParseNames:
        assert new_testmachine in getRequestForParseNames, "We found your new machine in list"
        logging.info(f'Backup successfully restored')
        
@allure.step('Delete backup')
def deleteBackup(ws, authId, seal):
    logging.info("Deleting test backup")
    waitForResponse(ws, '[48,5502640661614768,{"receive_progress":true},"api.konfigd.set",["323d8e28-c88b-44f5-38f2-a384d34f6e46","exec backup delete [' + temp.testBackupRestoreName + '] --json"],{}]')
    message = waitForResponse(ws, '[48,5467022859114780,{"receive_progress":false},"api.konfigd.get",["eeee1943-9dc4-05de-fda5-db1dab384796","exec backup list --json"],{}]')
    assert temp.testBackupRestoreName not in message and temp.testBackupName not in message, "Something wrong with backups list file name, we found it"
    logging.info("Backup deleted!")
    

@allure.step('Main backup restore function')
def backupRestore(ws, authId, seal, host):
    machineName = temp.testMachine[1].replace("ip=", "")
    checkAlreadyUsedNames(ws, seal, authId, machineName, host, temp=0)
    makeBackup(ws, authId, seal)
    addingNewMachine(ws, seal, authId, host, temp.testMachine)
    restoreBackup(ws, host, authId, seal, machineName)
    deleteBackup(ws, authId, seal)

def unlockingWay(ws):
    message = waitForResponse(ws, '[48,6658596392440164,{"receive_progress":true},"api.konfigd.set",["f02fafd8-afca-bf9c-7953-f04de6de5060","exec backup unsafe ' + temp.testBackupName + ' --json"],{}]')
    logging.info("Making backup unsafe")
    message = waitForResponse(ws, '[48,5765208959444516,{"receive_progress":false},"api.konfigd.get",["f1616d55-e29c-2ba4-0bf8-21efe876a202","exec backup list --json"],{}]')
    # assert f'The backup {temp.testBackupName} marked as unsafe' in message, "Cannot check backup safe"
    logging.info("Deleting test backup")
    waitForResponse(ws, '[48,5502640661614768,{"receive_progress":true},"api.konfigd.set",["323d8e28-c88b-44f5-38f2-a384d34f6e46","exec backup delete [' + temp.testBackupName + '] --json"],{}]')
    message = waitForResponse(ws, '[48,5467022859114780,{"receive_progress":false},"api.konfigd.get",["eeee1943-9dc4-05de-fda5-db1dab384796","exec backup list --json"],{}]')
    assert temp.testBackupName in message, "Something wrong with backups list file name, we found it"
    logging.info("Backup deleted!")

@allure.step('Adding new test machine to Tree')
def workingWithBackup(ws, authId, seal):
    message = waitForResponse(ws, '[48,760721965037376,{"receive_progress":false},"api.konfigd.get",["629370ea-6661-88e9-e34c-d7cf7f2cbff4","exec backup list --json"],{}]')
    counter = 0
    if "Error another backup is running" in message:
        while counter == 20:
            time.sleep(1)
            message = ws.recv()
            counter += 1
    # assert 'name' in message and 'safe' in message
    logging.info("Making backup")
    waitForResponse(ws, '[48,5988383378038002,{"receive_progress":true},"api.konfigd.set",["b208e89b-4747-28c0-7af8-191f70d0569a","exec backup save ' + temp.testBackupName + ' --json"],{}]')
    logging.info("Searching new backup in list")
    message = waitForResponse(ws, '[48,6379282976853238,{"receive_progress":false},"api.konfigd.get",["16524f99-d3c6-e4df-d6fe-fa265cb6e8b3","exec backup list --json"],{}]')
    assert temp.testBackupName in message, "Something wrong with backups list filename"
    logging.info("Making safe backup")
    waitForResponse(ws, '[48,6181724810289738,{"receive_progress":true},"api.konfigd.set",["2c1b97fe-a7af-3859-8c4d-200ffe5667ab","exec backup safe ' + temp.testBackupName + ' --json"],{}]')
    message = waitForResponse(ws, '[48,5125273220617238,{"receive_progress":false},"api.konfigd.get",["cec8173e-3066-b6a2-baf3-30888d9c3e0e","exec backup list --json"],{}]')
    assert f'The backup {temp.testBackupName} marked as safe' in message or r'{\\"safe\\":1,\\"name\\":\\"'+ temp.testBackupName + r'\\"}', "Cannot check backup safe"
    logging.info("Making unsafe backup")
    waitForResponse(ws, '[48,6658596392440164,{"receive_progress":true},"api.konfigd.set",["f02fafd8-afca-bf9c-7953-f04de6de5060","exec backup unsafe ' + temp.testBackupName + ' --json"],{}]')
    message = waitForResponse(ws, '[48,5765208959444516,{"receive_progress":false},"api.konfigd.get",["f1616d55-e29c-2ba4-0bf8-21efe876a202","exec backup list --json"],{}]')
    logging.info("Deleting test backup")
    message = waitForResponse(ws, '[48,5502640661614768,{"receive_progress":true},"api.konfigd.set",["323d8e28-c88b-44f5-38f2-a384d34f6e46","exec backup delete [' + temp.testBackupName + '] --json"],{}]')
    # assert f'The backup {temp.testBackupName} marked as unsafe' in message, "Cannot check backup safe"
    message = waitResponse(ws, "deleted successfully")
    assert "deleted successfully" in message, "Cannot delete backup"
    message = waitForResponse(ws, '[48,5467022859114780,{"receive_progress":false},"api.konfigd.get",["eeee1943-9dc4-05de-fda5-db1dab384796","exec backup list --json"],{}]')
    pattern = re.compile(r'name\\":\\"[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{1,}\\"')
    logging.info("Backup deleted!")

@allure.title('Adding new device to Tree')
@allure.description("The test tests the functions of creating, deleting test PC")
def test_BackupCheck(seal):
    seal1 = seal.replace("qweDelimqwe", "|")
    data = auth(seal1)
    ws = data[0]
    seal = data[1]
    authId = data[2]
    newtestmachine = data[3]
    host = data[4]
    logging.info(f'Starting main functions')
    waitForResponse(ws, '[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    workingWithBackup(ws, authId, seal)
    backupRestore(ws, authId, seal, host)
    ws.close()
