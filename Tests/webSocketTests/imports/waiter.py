import logging
from websocket import create_connection
import requests
import allure
import time
import sys


def waitResponse(ws, id="", timeout=10):
    logging.info(f"Waiting websocket response...")
    counter = 0
    msg = ""
    while counter <= timeout:
        try:
            msg = ws.recv()
            if msg != None or msg != "":
                if id in msg:
                    break
                else:
                    pass
            else:
                time.sleep(1)
                counter += 1
        except:
            counter += 1
    return msg


def waitGetResponse(url, timeout=20, ssl=None):
    counter0 = 0
    logging.info(f"Waiting rest response to be changed...")
    firstMessage = requests.get(url).text
    while int(counter0) <= int(int(timeout)):
        newMessage = requests.get(url).text
        # print(newMessage)
        if len(firstMessage.split('"')) != len(newMessage.split('"')):
            # print (newMessage)
            return newMessage
        time.sleep(1)
        counter0 = counter0 + 1


def waitGetResponseToBeChanged(
    url, content="data", newResponseText="", timeout=20, ssl=None
):
    # print(f"\n\n\n{url}\n\n\n")
    logging.info(f"Waiting rest response to be changed...")
    counter = 0
    if ssl == None or ssl == True:
        while counter <= timeout:
            # logging.info(request.text)
            try:
                # print(requests.get(url, verify=ssl).text)
                if newResponseText not in str(requests.get(url, verify=ssl).text):
                    time.sleep(1)
                    counter += 1
                else:
                    # print(requests.get(url).text)
                    if content == "data":
                        return requests.get(url).text
                    if content == "headers":
                        return requests.get(url).headers
                    if content == "cookies":
                        return requests.get(url).cookies
            except:
                counter += 1
        if content == "data":
            return requests.get(url).text
        if content == "headers":
            return requests.get(url).headers
        if content == "cookies":
            return requests.get(url).cookies
    if ssl == False:
        while counter <= timeout:
            # logging.info(request.text)
            try:
                if newResponseText not in str(
                    requests.get(url, verify=ssl, cert=None).text
                ):
                    time.sleep(1)
                    counter += 1
                else:
                    break
            except:
                counter += 1
        if content == "data":
            return requests.get(url, verify=ssl, cert=None).text
        if content == "headers":
            return requests.get(url, verify=ssl, cert=None).headers
        if content == "cookies":
            return requests.get(url, verify=ssl, cert=None).cookies


def waitForResponse(ws, commandLine, _waitResponse=True, timeout=10, _retryTimes=2):
    counter0 = 0
    counter1 = 0
    commandLineId = None
    commandLineNumber = None
    for elem in commandLine.split('"'):
        if "-" in elem and len(elem.split("-")) == 5 and " " not in elem:
            commandLineId = elem
    for i in range(len(commandLine.split(","))):
        if (
            commandLine.split(",")[i].isdigit()
            and len(commandLine.split(",")[i]) >= 14
            and commandLine.split(",")[i - 1].split("[")[1].isdigit()
            and len(commandLine.split(",")[i - 1].split("[")[1]) < 3
        ):
            commandLineNumber = commandLine.split(",")[i]
    if commandLineId == None:
        commandLineId = commandLineNumber
    if commandLineNumber == None:
        commandLineNumber = commandLineId
    while counter0 < _retryTimes:
        time.sleep(0.5)
        ws.send(commandLine)
        if _waitResponse == False:
            return msg
        msg = ""
        while (
            counter1 <= timeout
            and commandLineId not in msg
            or commandLineNumber not in msg
        ):
            try:
                msg = ws.recv()
                if (
                    msg != None
                    or msg != ""
                    and commandLineId in msg
                    or commandLineNumber in msg
                ):
                    return msg
                else:
                    time.sleep(1)
                    counter1 += 1
            except:
                counter1 += 1
    assert (
        commandLineId in msg or commandLineNumber in msg
    ), "Something went wrong with WebSocket response"
    return msg
