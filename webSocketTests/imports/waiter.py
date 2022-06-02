import logging
from websocket import create_connection
import requests
import allure
import time

def waitResponse(ws, id="", timeout=10):
    logging.info(f'Waiting websocket response...') 
    counter = 0
    msg = ""
    while counter <= timeout:
        try:
            msg = ws.recv()
            if msg != None or msg != '':
                if id in msg:
                    break
                else: pass
            else:
                time.sleep(1)
                counter +=1
        except:
            counter +=1
    return msg

def waitGetResponseToBeChanged(url, newResponseText , timeout=20, ssl = None):
    logging.info(f'Waiting rest response to be changed...') 
    counter = 0
    if ssl == None or ssl == True:
        while counter <= timeout:
            # logging.info(request.text)
            try:
                if newResponseText not in str(requests.get(url, verify=ssl).text):
                    time.sleep(1)
                    counter += 1
                else:
                    break
            except:
                counter += 1
        return requests.get(url).text
    if ssl == False:
        while counter <= timeout:
            # logging.info(request.text)
            try:
                if newResponseText not in str(requests.get(url, verify=ssl, cert=None).text):
                    time.sleep(1)
                    counter += 1
                else:
                    break
            except:
                counter += 1
        return requests.get(url, verify=ssl, cert=None).text