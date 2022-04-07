import subprocess
import os
import sys
from imports.waiter import *
from imports.getter import *
from websocket import *
import time
import threading

def banner():
    banner = print(f"""
    -----------------------------------------------------------------
   | -s          --skip [filename].py        | Skip one test         |
   | -h          --help                      | This message          |
   | -ot         --only-this [filename].py   | Only one test         |
   | -ll         --log-level DEBUG|INFO|OFF  | Log level             |
   | -t          --timeout [default 0.2 sec] | Timeout between tests |
   | -th         --threads [default 4]       | Set threads           |
   | -db         --debug-level 1             | Turn on debug         |
   |                                                                 |
   | -wst        --webSocketTests            | Run only WS tests     |
   | -srt        --simpleRestTests           | Run only REST tests   |
   |                                                                 |
   | Scripts count : {temp.scriptsCount}       
   | Scripts start with : --log-cli-level=INFO (default)             |
    -----------------------------------------------------------------""")
    return banner

class temp():
    scriptsCount = 0
    host = ""
    subprotocols = ""
    authID = ""
    login = ""
    password = ""
    newtestmachine = ""
    seal = ""
    warningFiles = []
    
def exitFunc():
    while True:
        message = os.system("ps aux | grep pytest >/dev/null 2>&1")
        if "-m pytest" in str(message):
            time.sleep(1)
            pass
        else:
            time.sleep(3)
            print("All done!")
            break 
    sys.exit()

def restAuth(_is_this_websocket = 0):
    if _is_this_websocket == 0:
        folderPlace = "/tests/SimpleRest"
    else: 
        folderPlace = "/tests/WebSocket"
    with open(os.getcwd().replace(folderPlace, "/") + "config.ini", "r") as file:
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
    data = {
        "login" : temp.login,
        "password" : temp.password
    }
    postReqForAuth = requests.post("http://" + temp.host + "/rest/account/login", data = data, timeout=20).text
    if "Service Unavailable" in postReqForAuth:
        logging.error("Service Unavailable, please, try again later")
        exit()
    assert "displayName" in postReqForAuth, "DisplayName not in post response. Something wrong with auth post respose."
    for i in range(len(postReqForAuth.split('\"'))):
        if postReqForAuth.split('\"')[i] == "seal":
            temp.seal = postReqForAuth.split('\"')[i + 2]    

def webSocketAuth():
    ws = create_connection(f"ws://{temp.host}/ws", subprotocols=["wamp.2.json"],timeout=10000)
    ws.send('[1,"realm1",{"roles":{"caller":{"features":{"caller_identification":true,"progressive_call_results":true}},"callee":{"features":{"caller_identification":true,"pattern_based_registration":true,"shared_registration":true,"progressive_call_results":true,"registration_revocation":true}},"publisher":{"features":{"publisher_identification":true,"subscriber_blackwhite_listing":true,"publisher_exclusion":true}},"subscriber":{"features":{"publisher_identification":true,"pattern_based_subscription":true,"subscription_revocation":true}}},"authmethods":["ticket"],"authid":"' + str(temp.authID) + '"}]')
    assert '[4,"ticket",{}]' in ws.recv(), 'Something wrong with webSocket connection.'
    ws.send('[5,"' + temp.seal + '",{}]')
    message = waitResponse(ws)
    assert temp.host in message, "Your host machine not found."
    listOfData = [ws, temp.seal, temp.authID, temp.newtestmachine, temp.host]
    return listOfData

def interlayer():
    restData = restAuth(1)
    wsData = webSocketAuth()
    ws = wsData[0]
    seal = wsData[1]
    authId = wsData[2]
    ws.send('[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'+ authId +'\\",\\"seal\\":\\"'+ seal +'\\"}"],{}]')
    waitResponse(ws)
    ws.send('[48,4326942052087000,{"receive_progress":false},"api.konfigd.get",["aa1a64a8-c8f7-08d5-3617-62a983044efb","exec alertsedit.pl --list --json"],{}]')
    waitResponse(ws)
    return wsData

folderWithTests = os.listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split("/")[-1], "tests/WebSocket/"))
folderDir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split("/")[-1], "tests/WebSocket/")
restFolderWithTests = os.listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split("/")[-1], "tests/SimpleRest/"))
restFolderDir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split("/")[-1], "tests/SimpleRest/")

def testsConters():
    foldersWithTests = [folderWithTests, restFolderWithTests]
    for folder in foldersWithTests:
        for file in folder:
            if '.' in file and '.' not in file[0] and file not in temp.warningFiles:
                temp.scriptsCount+= 1

temp.warningFiles = getFromConfig("warningFiles", "config.ini").replace(" ", "").split(",")

testsConters()
print("Count of tests -> " + str(temp.scriptsCount))

def argumetsIndexSearch(values):
    for value in values:
        for i in range(len(sys.argv)):
            if value in str(sys.argv[i]):
                index0 = sys.argv[i]
    return str(index0)

debuglevelIndex = 0
debuglevel = 0
onlyIndex = 0
skipIndex = 0
logLevelIndex = 0
timeoutInSec = 0.2
threadsCount = 4 
argument = sys.argv
desicion = []
if "-h" in argument or "--help" in argument:
    banner()
    exit()
if "-s" in argument or "--skip" in argument:
    skipIndex = argument.index(argumetsIndexSearch(["-s", "--skip"]))
if "-ot" in argument or "--only-this" in argument:
    onlyIndex = argument.index(argumetsIndexSearch(["-ot", "--only-this"]))
if "-ll" in argument or "--log-level" in argument:
    logLevelIndex = argument.index(argumetsIndexSearch(["-ll", "--log-level"]))
if "-t" in argument or "--timeout" in argument:
    timeoutInSec = sys.argv[argument.index(argumetsIndexSearch(["-t", "--timeout"])) + 1] 
if "-wst" in argument or "--webSocketTests" in argument:
    desicion.append(argument.index(argumetsIndexSearch(["-wst", "--webSocketTests"])))
if "-srt" in argument or "--simpleRestTests" in argument:
    desicion.append(argument.index(argumetsIndexSearch(["-srt", "--simpleRestTests"])))
if "-th" in argument or "--threads" in argument:
    threadsCount = sys.argv[argument.index(argumetsIndexSearch(["-th", "--threads"])) + 1]
if "-db" in argument or "--debug-level" in argument:
    print(str(sys.argv))
    debuglevel = sys.argv[argument.index(argumetsIndexSearch(["-db", "--debug-level"])) + 1]
    debuglevelIndex = argument.index(argumetsIndexSearch(["-db", "--debug-level"]))
    
def makeTestsDebugMode(filename, folderWithTests):
    filePath = folderWithTests
    counter = 0
    while counter == 0:
        counter+= 1
        with open(filePath + "/" + filename, "r") as file:
            if "from debug import *" in file.read():
                file.close()
            else:
                data = ""
                fileText = open(filePath + "/" + filename, 'r').read()
                if "import sys" not in fileText:
                    data += "import sys\n"
                if "sys.path.append('../../imports/')" not in fileText:
                    data += "sys.path.append('../../imports/')\n"
                for i in range(len(fileText.split(" "))):
                    if "test_" in fileText.split(" ")[i] and ":" in fileText.split(" ")[i] and "def" in fileText.split(" ")[i-1]:
                        if "," in fileText.split(" ")[i]:
                            functionName = fileText.split(" ")[i].replace(")", ", debugLevel)")
                            oldFunctionName = fileText.split(" ")[i]
                        if "()" in fileText.split(" ")[i]:
                            functionName = fileText.split(" ")[i].replace("()", "(debugLevel)")
                            oldFunctionName = fileText.split(" ")[i]
                        else:
                            functionName = fileText.split(" ")[i].replace(")", ", debugLevel)")
                            oldFunctionName = fileText.split(" ")[i]
                        if "debugEnable(int(debugLevel))" not in functionName:
                            functionName += "\tdebugEnable(int(debugLevel))\n"
                data += fileText.replace(oldFunctionName, functionName).replace("\t", "    ")
                if "from debug import *" not in fileText:
                    ndata = data.replace("sys.path.append('../../imports/')", "sys.path.append('../../imports/')\nfrom debug import *")
                else: 
                    ndata = data
                fileTextAdd = open(filePath + "/" + filename, 'w').write(ndata)        
    
def workWithFiles(file, processName, _dir_with_tests):
    counter = 0
    while counter == 0:
        counter+=1
        if '.' in file and '.' not in file[0] and file not in temp.warningFiles:
            if "-ll" in sys.argv[logLevelIndex] or "--log-level" in sys.argv[logLevelIndex]:
                if sys.argv[logLevelIndex + 1] == "off":
                    commandLineLog = ""
                else:
                    commandLineLog = "--log-cli-level=" + sys.argv[logLevelIndex + 1]
            else:
                commandLineLog = "--log-cli-level=" + "INFO"
            if "-ot" in sys.argv[onlyIndex] or "--only-this" in sys.argv[onlyIndex]:
                if file in argument[onlyIndex + 1]:
                    if "-db" in argument[debuglevelIndex] or "--debug-level" in argument[debuglevelIndex]:
                        makeTestsDebugMode(file, _dir_with_tests)
                    else: pass
                    filename = "../logs/tests_logs/" + file.replace(".py", "") + ".log"
                    if processName == "wsr":
                        os.system("python3 -m pytest " + file + " --seal=" + temp.seal.replace("|", "qweDelimqwe") + " " + commandLineLog + " -s -q --alluredir=../logs/result/ | tee ../logs/tests_logs/" + file.replace(".py", "") + ".log && sed 's/\\\\r\\\\n/\\n/g' " + filename + " > " + filename + "O && mv " + filename + "O "+ filename +" &")
                    else:
                        os.system("python3 -m pytest " + file + " --seal=" + temp.seal.replace("|", "qweDelimqwe") + " --debugLevel=" + str(debuglevel) + " " + commandLineLog + " -s -q --alluredir=../logs/result/ | tee ../logs/tests_logs/" + file.replace(".py", "") + ".log && sed 's/\\\\r\\\\n/\\n/g' " + filename + " > " + filename + "O && mv " + filename + "O "+ filename +" &")
                    exitFunc()
            else:
                if "-db" in argument[debuglevelIndex] or "--debug-level" in argument[debuglevelIndex]:
                        makeTestsDebugMode(file, _dir_with_tests)
                if "-s" in argument[skipIndex] or "--skip" in argument[skipIndex]:
                    if file in argument[skipIndex + 1]:
                        logging.warning("Skip this test" + file)
                        continue
                filename = "../logs/tests_logs/" + file.replace(".py", "") + ".log"
                if processName == "wsr":
                    os.system("python3 -m pytest " + file + " --seal=" + temp.seal.replace("|", "qweDelimqwe") + " " + commandLineLog + " -s -q --alluredir=../logs/result/ | tee ../logs/tests_logs/" + file.replace(".py", "") + ".log && sed 's/\\\\r\\\\n/\\n/g' " + filename + " > " + filename + "O && mv " + filename + "O "+ filename +" &")
                else:
                    process = subprocess.Popen("python3 -m pytest " + file + " --seal=" + temp.seal.replace("|", "qweDelimqwe") + " --debugLevel=" + str(debuglevel) + " " + commandLineLog + " -s -q --alluredir=../logs/result/ | tee ../logs/tests_logs/" + file.replace(".py", "") + ".log && sed 's/\\\\r\\\\n/\\n/g' " + filename + " > " + filename + "O && mv " + filename + "O "+ filename +" &", shell=True).wait()
        else: pass
        threads.remove(processName)
            
threads = []
def runTests(_dir_with_tests, folderWT, _is_socket_open = 0):
    processCounter = 0
    os.chdir(_dir_with_tests)
    if _is_socket_open == 1:
        interlayer()
        for file in folderWT:
            threads.append("wsr")
            workWithFiles(file, "wsr", _dir_with_tests)
    else:
        restAuth()
        for file in folderWT:
            while True:
                if len(threads) >= 4:
                    time.sleep(0.1)
                    pass
                else:
                    processCounter += 1
                    threads.append(f"Thread {processCounter}")
                    threading.Thread(workWithFiles(file, f"Thread {processCounter}", _dir_with_tests), name=f"Thread {processCounter}")
                    time.sleep(int(timeoutInSec))
                    break

if len(desicion) == 0:
    runTests(folderDir, folderWithTests, 1)
    runTests(restFolderDir, restFolderWithTests, 0)
else:
    for i in range(len(desicion)):
        if sys.argv[desicion[i]] == "-wst" or sys.argv[desicion[i]] == "--webSocketTests":
            runTests(folderDir, folderWithTests, 1)
        if sys.argv[desicion[i]] == "-srt" or sys.argv[desicion[i]] == "--simpleRestTests":
            runTests(restFolderDir, restFolderWithTests, 0)
        
exitFunc()
