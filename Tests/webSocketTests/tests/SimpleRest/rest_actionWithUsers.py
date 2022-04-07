import sys
import requests
sys.path.append('../../imports/')
from debug import *

import logging
from getter import getFromConfig
from waiter import *
from messages import *
import allure

class temp():
    displayName = "test_rest_user_creation"
    login = "test_rest_user_creation"
    password = "test_rest_user_creation"
    userId = ""
    

@allure.title("Create new account")     
def createAccount(seal, host, username):
    data = {
        "auth": "local",
        "profile-policy-current": "default",
        "password": temp.password,
        "displayName": temp.displayName,
        "login": temp.login,
        "groups": '["administrators"]',
        "username": username,
        "seal": seal
    }   
    logging.info("Try to create new test account")
    createAccountRequest = requests.post(f"http://{host}/rest/access/useradd", data = data, timeout=10).text
    try:
        assert 'data":[' in createAccountRequest and ']' in createAccountRequest, "Something wrong with create account"
        temp.userId = createAccountRequest.split('data":["')[1].split('"]')[0]
        logging.info("Account created and take id -> " + temp.userId)
    except:
        if 'Already exists' in createAccountRequest:
            assert 'Already exists' in createAccountRequest, "Someting went wrong with createAccountRequest output"
            logging.error("Username already exist")
def tryLoginNewAccount(host):
    data = {
        "login" : temp.login,
        "password" : temp.password
    }
    logging.info("Try to login on new test account")
    postReqForAuth = requests.post("http://" + host + "/rest/account/login", data = data, timeout=20).text
    if "Service Unavailable" in postReqForAuth:
        logging.error("Service Unavailable, please, try again later")
        exit()
    assert "displayName" in postReqForAuth, "DisplayName not in post response. Something wrong with auth post respose."
    logging.info("Login successfully")

                                           
def disableNewAcccount(seal, host, username):
    logging.info("Try to disable new test account")
    requestForDeleteNewAcc = requests.delete(f'http://{host}/rest/access/userdel?users=%5B%22{temp.userId}%22%5D&force=0', cookies={"seal":seal}).text
    #logging.info(requestForDeleteNewAcc)
    assert '"data":[{"user":"' + temp.userId + '"}]' in requestForDeleteNewAcc, "Something wrong with disable new account"
    logging.info("Disabled sucessfully")

def deleteNewAccount(seal, host, username):
    logging.info("Try to delete new test account")
    deleteNewAccountRequest = requests.delete(f'http://{host}/rest/access/userdel?users=%5B%22{temp.userId}%22%5D&force=1', cookies={"seal":seal}).text
    assert f'"data":["{temp.userId}","user=uid={temp.userId},ou=Users,dc=lanlot"]' in deleteNewAccountRequest, "Something went wrong with delete new account"
    logging.info("Delete sucessfully")

def simpleLoginToTakeNewSeal(host, username, password):
    data = {
        "login" : username,
        "password" : password
    }
    logging.info("Try to login back")
    postReqForAuth = requests.post("http://" + host + "/rest/account/login", data = data, timeout=20)
    if "Service Unavailable" in postReqForAuth.text:
        logging.error("Service Unavailable, please, try again later")
        exit()
    assert "displayName" in postReqForAuth.text, "DisplayName not in post response. Something wrong with auth post respose."
    seal = postReqForAuth.cookies["seal"]
    logging.info("Login back sucessfully, new seal -> " + seal.split("|")[0])
    return seal
    
@allure.title('Seal update test')
def test_sealTest(seal, debugLevel):
    debugEnable(int(debugLevel))
    seal1 = seal.replace("qweDelimqwe", "|")
    host = getFromConfig("host")
    username = getFromConfig("login")
    password = getFromConfig("password")
    createAccount(seal1, host, username)
    tryLoginNewAccount(host)
    seal1 = simpleLoginToTakeNewSeal(host, username, password)
    disableNewAcccount(seal1, host, username)
    deleteNewAccount(seal1, host, username)
