import logging
from websocket import create_connection
import requests
import allure
from waiter import *

class temp():
    host = ""
    subprotocols = ""
    authID = ""
    seal = ""
    login = ""
    password = ""
    newtestmachine = ""

@allure.step('Authorize')
def auth(seal):
    with open("../../config.ini", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            if "[host]" in line:
                temp.host = line.split(" = ")[1]
            if "[subprotocols]" in line:
                temp.subprotocols = line.split(" = ")[1]    
            if "[authId]" in line:
                temp.authID = line.split(" = ")[1]
            if "[login]" in line:
                temp.login = line.split(" = ")[1] 
            if "[password]" in line:
                temp.password = line.split(" = ")[1] 
            if "[newTestMachine]" in line:
                temp.newtestmachine = line.split(" = ")[1]  
    ws = create_connection(f"ws://{temp.host}/ws", subprotocols=["wamp.2.json"],timeout=10000)
    ws.send('[1,"realm1",{"roles":{"caller":{"features":{"caller_identification":true,"progressive_call_results":true}},"callee":{"features":{"caller_identification":true,"pattern_based_registration":true,"shared_registration":true,"progressive_call_results":true,"registration_revocation":true}},"publisher":{"features":{"publisher_identification":true,"subscriber_blackwhite_listing":true,"publisher_exclusion":true}},"subscriber":{"features":{"publisher_identification":true,"pattern_based_subscription":true,"subscription_revocation":true}}},"authmethods":["ticket"],"authid":"' + str(temp.authID) + '"}]')
    message = waitResponse(ws)
    assert '[4,"ticket",{}]' in message, 'Something wrong with webSocket connection.'
    ws.send('[5,"' + seal + '",{}]')
    message = waitResponse(ws)
    assert temp.host in message, "Your host machine not found."
    listOfData = [ws, seal, temp.authID, temp.newtestmachine, temp.host]
    logging.info("Authorization was successful")
    return listOfData