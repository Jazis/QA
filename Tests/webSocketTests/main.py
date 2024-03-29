try:
    import subprocess
    import os
    import sys
    from imports.waiter import *
    from imports.getter import *
    from imports.waiter import waitResponse
    from websocket import *
    import time
    import threading
    import urllib3
    import random
    import requests
    import logging
except ModuleNotFoundError:
    print("Please, install requerements requirements.txt\nCommand: python -m pip install -r requirements.txt")
    sys.exit()


class temp:
    scriptsCount = 0
    host = ""
    subprotocols = ""
    authID = ""
    login = ""
    password = ""
    newtestmachine = ""
    seal = ""
    warningFiles = []
    buildHash0 = ""


logsFolderPath = os.path.abspath(__file__).replace(
    os.path.abspath(__file__).split("/")[-1], "tests/logs/tests_logs/"
)
if os.path.isdir("tests/logs/tests_logs/") == False:
    os.mkdir("tests")
    os.mkdir("tests/WebSocket/0")
    os.mkdir("tests/SimpleRest/0")
    os.mkdir("tests/logs/")
    os.mkdir("tests/logs/tests_logs/")
    os.mkdir("tests/logs/result/")

allureLogsFolderPath = os.path.abspath(__file__).replace(
    os.path.abspath(__file__).split("/")[-1], "tests/logs/result/"
)
logsFolderWithTests = os.listdir(logsFolderPath)
folderWithTests = os.listdir(
    os.path.abspath(__file__).replace(
        os.path.abspath(__file__).split("/")[-1], "tests/WebSocket/"
    )
)
folderDir = os.path.abspath(__file__).replace(
    os.path.abspath(__file__).split("/")[-1], "tests/WebSocket/"
)
restFolderWithTests = os.listdir(
    os.path.abspath(__file__).replace(
        os.path.abspath(__file__).split("/")[-1], "tests/SimpleRest/"
    )
)
restFolderDir = os.path.abspath(__file__).replace(
    os.path.abspath(__file__).split("/")[-1], "tests/SimpleRest/"
)

arrayForFailedTests = []


def testsConters():
    foldersWithTests = [folderWithTests, restFolderWithTests]
    for folder in foldersWithTests:
        for file in folder:
            if "." in file and "." not in file[0] and file not in temp.warningFiles:
                temp.scriptsCount += 1
    return temp.scriptsCount


def banner():
    testsConters()
    banner = print(
        f"""
    -----------------------------------------------------------------------------------------------------------------------------
   | -s          --skip [filename].py or bpm,dms               | Skip tests by group or single name test                         |
   | -h          --help                                        | This message                                                    |
   | -ot         --only-this [filename].py or bpm,dms          | Starting selected group of tests or single name tests           |
   | -ll         --log-level DEBUG|INFO|OFF                    | Log level                                                       |
   | -t          --timeout [default 0.2 sec]                   | Timeout between tests                                           |
   | -r          --repeat [times]                              | Failed tests repeater                                           |
   | -th         --threads [default 4]                         | Set threads                                                     |
   | -db         --debug-level 1                               | Turn on debug                                                   |
   | -pk         --process-killing [time] - 180sec default     | Timer for process killing (Use `off` for disable this function) |
   | -sr         --start-reconnect-times [times] - 20 default  | Open new session reconnection times (taking seal)               |
   | -sr-time    --start-reconnect-timeout [secs] - 1 default  | Timer open new session recconect                                |
   | --no-ssl    (demo)                                        | Turn off ssl                                                    |
   | --ssl       (demo)                                        | Turn on ssl                                                     |
   | -gen        --generate                                    | (device.ini) Data generation                                    |
   |             --hash                                        | Build hash for saving results                                   |
   |             --allure-output-dir [dir]                     | Set allure output directory                                     |
   |             --simple-logs-output-dir [dir]                | Set simple output directory                                     |
   |             --delete-logs                                 | Delete all logs                                                 |
   |             --waiting-for-response - 40 default           | Main responses timeout                                          |
   
   | -wst        --webSocketTests                              | Run only WS tests                                               |
   | -srt        --simpleRestTests                             | Run only REST tests                                             |
   |                                                                                                                             |
   | Scripts count : {temp.scriptsCount}                                                            
   | Scripts start with : --log-cli-level=INFO (default)                                                                         |
    -----------------------------------------------------------------------------------------------------------------------------"""
    )
    return banner


def reRunTests(failedTestsRunLoop):
    print(
        f"({str(failedTestsRunLoop)})Failed tests array -> {str(arrayForFailedTests)}"
    )
    for file in arrayForFailedTests:
        arrayForFailedTests.remove(file)
        processCounter = 0
        while True:
            processCounter += 1
            threads.append(f"Thread replay {processCounter}")
            if os.path.isfile(folderDir + file):
                threading.Thread(
                    workWithFiles(file, f"Thread replay {processCounter}", folderDir),
                    name=f"Thread {processCounter}",
                ).start()
                time.sleep(int(timeoutInSec))
            if os.path.isfile(restFolderDir + file):
                threading.Thread(
                    workWithFiles(
                        file, f"Thread replay {processCounter}", restFolderDir
                    ),
                    name=f"Thread {processCounter}",
                ).start()
                time.sleep(int(timeoutInSec))
            break


def endfunc(force=0):
    while True:
        ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE).communicate()[0]
        new_ps = str(ps).replace("\n", "")
        if "-m pytest" in str(new_ps):
            time.sleep(1)
            pass
        else:
            time.sleep(1)
            print("All done!")
            break
    if force == 0:
        sys.exit()
    else:
        pass


def exitFunc():
    i = 1
    failedTestsRunLoop = 0
    while True:
        ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE).communicate()[0]
        new_ps = str(ps).replace("\n", "")
        if "-m pytest" in str(new_ps):
            time.sleep(1)
            pass
        else:
            time.sleep(1)
            while i <= int(repeatIndex):
                failedTestsRunLoop += 1
                if len(arrayForFailedTests) != 0:
                    reRunTests(failedTestsRunLoop)
                    endfunc(1)
                    i += 1
                else:
                    break
            break
    sys.exit()


def argumetsIndexSearch(values):
    for value in values:
        for i in range(len(sys.argv)):
            if value == str(sys.argv[i]):
                index0 = sys.argv[i]
    return str(index0)


def makingIpFromRange(ip):
    ips = []
    ipInput = ip
    fromWhere = ipInput.split("-")[0]
    toWhere = ipInput.split("-")[1]
    for i in range(int(fromWhere.split(".")[0]), int(toWhere.split(".")[0]) + 1):
        firstDigit = i
        for j in range(int(fromWhere.split(".")[1]), int(toWhere.split(".")[1]) + 1):
            secondDigit = j
            print(str(firstDigit) + "." + str(secondDigit))
            for k in range(
                int(fromWhere.split(".")[2]), int(toWhere.split(".")[2]) + 1
            ):
                thirdDigit = k
                for l in range(
                    int(fromWhere.split(".")[3]), int(toWhere.split(".")[3]) + 1
                ):
                    fourthDigit = l
                    newIpFromRange = (
                        str(firstDigit)
                        + "."
                        + str(secondDigit)
                        + "."
                        + str(thirdDigit)
                        + "."
                        + str(fourthDigit)
                    )
                    ips.append(newIpFromRange)
    return ips


def workingModeLinesGenerator(mainLine, testName, ipInput, isIp, request):
    ipInput0 = ipInput
    if (
        "." not in ipInput0
        and "-" not in ipInput0
        and "," not in ipInput0
        or isIp == False
        and "," not in ipInput0
    ):
        for i in range(len(mainLine.split("position"))):
            newMainLine = mainLine.replace("<ipInput>", ipInput)
            for i in range(len(newMainLine.split("position"))):
                if request == "random":
                    newMeaning = bool(random.randint(0, 1))
                    if newMeaning == 0:
                        newMainLine = newMainLine.replace(f"<position{i}>", f"false")
                    if newMeaning == 1:
                        newMainLine = newMainLine.replace(f"<position{i}>", f"true")
                else:
                    newMainLine = mainLine.replace(f"<position{i}>", f"{request}")
        open("new_device.ini", "a+").write(f"[{testName}]{newMainLine}")
    if "," in ipInput0 and isIp == False:
        ips = ipInput0.split(",")
        for ip in ips:
            for i in range(len(mainLine.split("position"))):
                newMainLine = mainLine.replace("<ipInput>", ip)
                for i in range(len(newMainLine.split("position"))):
                    if request == "random":
                        newMeaning = bool(random.randint(0, 1))
                        if newMeaning == 0:
                            newMainLine = newMainLine.replace(
                                f"<position{i}>", f"false"
                            )
                        if newMeaning == 1:
                            newMainLine = newMainLine.replace(f"<position{i}>", f"true")
                    else:
                        newMainLine = mainLine.replace(f"<position{i}>", f"{request}")
            open("new_device.ini", "a+").write(f"[{testName}]{newMainLine}\n")
    if isIp == True and "," not in ipInput0 and "-" in ipInput0 or "." in ipInput0:
        ips = makingIpFromRange(ipInput)
        for ip in ips:
            for i in range(len(mainLine.split("position"))):
                newMainLine = mainLine.replace("<ipInput>", ip)
                for i in range(len(newMainLine.split("position"))):
                    if request == "random":
                        newMeaning = bool(random.randint(0, 1))
                        if newMeaning == 0:
                            newMainLine = newMainLine.replace(
                                f"<position{i}>", f"false"
                            )
                        if newMeaning == 1:
                            newMainLine = newMainLine.replace(f"<position{i}>", f"true")
                    else:
                        newMainLine = mainLine.replace(f"<position{i}>", f"{request}")
            open("new_device.ini", "a+").write(f"[{testName}]{newMainLine}")


def makeDeviceIniGreateAgain():
    open("new_device.ini", "w")
    testName = ""
    ipInput = ""
    workingMode = ""
    while testName == "":
        testName = input("Please, input test name here -> ")
    while ipInput == "":
        ipInput = input(
            "Please, input single IP or IPs range (0.0.0.0-1.1.1.1) here -> "
        )
    isIp = None
    try:
        newIpInput = ipInput.replace(".", "").replace("-", "")
        if int(newIpInput):
            isIp = True
    except:
        isIp = False
    osName = input(
        "Please, input devices os here\n (ex. Devices::Computers::Linux), type Enter for use example -> "
    )
    if osName == "":
        osName = "Devices::Computers::Linux"
        print("Selected os ->  Devices::Computers::Linux")
    print("Os name that you selected -> " + osName)
    for line in open("blanks.settings", "r").readlines():
        if osName in line:
            mainLine = line.split("]=")[1]
    communityLine = input(
        "Please, input community line\n(ex. public), type Enter for use example ->"
    )
    if communityLine == "":
        communityLine = "public"
        print("Community line ->  public")
    while workingMode not in {
        "no",
        "nothing",
        "a",
        "all",
        "r",
        "random",
        "s",
        "specific",
    }:
        workingMode = input(
            "Which mode do you prefer to use? [no]thing | [a]ll | [r]andom | [s]pecific-> "
        )
    try:
        mainLine = mainLine.replace("<osName>", osName)
    except UnboundLocalError:
        print(f"blanks.settings dont have this OS name -> {osName}")
        exit()
    mainLine = mainLine.replace("<communityLine>", communityLine)
    if workingMode == "no" or workingMode == "nothing":
        workingModeLinesGenerator(mainLine, testName, ipInput, isIp, "false")
    if workingMode == "a" or workingMode == "all":
        workingModeLinesGenerator(mainLine, testName, ipInput, isIp, "true")
    if workingMode == "r" or workingMode == "random":
        workingModeLinesGenerator(mainLine, testName, ipInput, isIp, "random")
    if workingMode == "s" or workingMode == "specific":
        if "." not in ipInput and "-" not in ipInput or isIp == False:
            print(
                f"Test name -> {testName}\ndevice={osName}\nip={ipInput}\ncommunity={communityLine}"
            )
            line = f'[{testName}]["device={osName}", "ip={ipInput}", "community={communityLine}",'
            for elem in [
                "enable-disk-io",
                "enable-disks-changes",
                "split-cpu-by-units",
                "enable-hardware-changes",
                "enable-process-changes",
                "enable-software-changes",
                "enable-arp-changes",
                "enable-network-changes",
                "enable-icmp-changes",
                "enable-tcp-changes",
                "enable-udp-changes",
                "replicated",
            ]:
                line0 = ""
                line0 = '"' + elem + "="
                while True:
                    choose = input(f"{elem}=")
                    if choose not in {"true", "false", "t", "f"}:
                        print("Choose from these answers -> [t]rue | [f]alse")
                    else:
                        if "t" in choose or "true" in choose:
                            line0 += "true"
                        if "f" in choose or "false" in choose:
                            line0 += "false"
                        break
                line0 += '", '
                line += line0
            nline = line[: len(line) - 2]
            open("new_device.ini", "a+").write(nline + "]\n")


def logsDeleting():
    counter0 = 0
    counter1 = 0
    for file in os.listdir(allureLogsFolderPath):
        print("[DELETED] " + allureLogsFolderPath + file)
        os.system("yes | rm -r " + allureLogsFolderPath + file + " > /dev/null 2>&1")
        counter0 += 1
    for file in os.listdir(logsFolderPath):
        print("[DELETED] " + logsFolderPath + file)
        os.system("yes | rm -r " + logsFolderPath + file)
        counter1 += 1
    print(
        f"Deleted files -> [{counter0 + counter1}]; Allure logs ->[{counter0}]; Simple logs -> [{counter1}]"
    )


skippedFiles = []
skipWays = []
onlyWayFiles = []
onlyThisWays = []
repeatIndex = 0
debuglevelIndex = 0
debuglevel = 0
startReconTimes = 40
startReconTimesTimeout = 1
onlyIndex = 0
skipIndex = 0
noSslIndex = 0
processKillingTime = 30
logLevelIndex = 0
timeoutInSec = 0.2
waitForResponseTimeout = 40
threadsCount = 4

argument = sys.argv
desicion = []
if "-h" in argument or "--help" in argument:
    banner()
    sys.exit()
if "-s" in argument or "--skip" in argument:
    skipIndex = argument.index(argumetsIndexSearch(["-s", "--skip"]))
    if "," in argument[skipIndex + 1]:
        for i in range(len(argument[skipIndex + 1].split(","))):
            skipWays.append(argument[skipIndex + 1].split(",")[i])
    if "." not in argument[skipIndex + 1]:
        skipWays.append(argument[skipIndex + 1])
if "-ot" in argument or "--only-this" in argument:
    onlyIndex = argument.index(argumetsIndexSearch(["-ot", "--only-this"]))
    if "," in argument[onlyIndex + 1]:
        for i in range(len(argument[onlyIndex + 1].split(","))):
            onlyThisWays.append(argument[onlyIndex + 1].split(",")[i])
    if "." not in argument[onlyIndex + 1]:
        onlyThisWays.append(argument[onlyIndex + 1])
if "-ll" in argument or "--log-level" in argument:
    logLevelIndex = argument.index(argumetsIndexSearch(["-ll", "--log-level"]))
if "-t" in argument or "--timeout" in argument:
    timeoutInSec = sys.argv[
        argument.index(argumetsIndexSearch(["-t", "--timeout"])) + 1
    ]
if "--waiting-for-response" in argument:
    waitForResponseTimeout = sys.argv[
        argument.index(argumetsIndexSearch(["--waiting-for-response"])) + 1
    ]
if "-sr" in argument or "--start-reconnect-times" in argument:
    startReconTimes = sys.argv[
        argument.index(argumetsIndexSearch(["-sr", "--start-reconnect-times"])) + 1
    ]
if "-sr-time" in argument or "--start-reconnect-timeout" in argument:
    startReconTimesTimeout = sys.argv[
        argument.index(argumetsIndexSearch(["-sr-time", "--start-reconnect-timeout"]))
        + 1
    ]
if "-r" in argument or "--repeat" in argument:
    repeatIndex = sys.argv[argument.index(argumetsIndexSearch(["-r", "--repeat"])) + 1]
if "-wst" in argument or "--webSocketTests" in argument:
    desicion.append(argument.index(argumetsIndexSearch(["-wst", "--webSocketTests"])))
if "-srt" in argument or "--simpleRestTests" in argument:
    desicion.append(argument.index(argumetsIndexSearch(["-srt", "--simpleRestTests"])))
if "-th" in argument or "--threads" in argument:
    threadsCount = sys.argv[
        argument.index(argumetsIndexSearch(["-th", "--threads"])) + 1
    ]
if "--hash" in argument:
    temp.buildHash0 = (
        sys.argv[argument.index(argumetsIndexSearch(["--hash"])) + 1] + "/"
    )
    os.system(f"mkdir {allureLogsFolderPath}{temp.buildHash0}")
if "--allure-output-dir" in argument:
    allureLogsFolderPath = sys.argv[
        argument.index(argumetsIndexSearch(["--allure-output-dir"])) + 1
    ]
if "--simple-logs-output-dir" in argument:
    logsFolderPath = sys.argv[
        argument.index(argumetsIndexSearch(["--simple-logs-output-dir"])) + 1
    ]
if "-pk" in argument or "--process-killing" in argument:
    processKillingTime = sys.argv[
        argument.index(argumetsIndexSearch(["-pk", "--process-killing"])) + 1
    ]
    if processKillingTime == "off":
        processKillingTime = 0
if "-db" in argument or "--debug-level" in argument:
    print(str(sys.argv))
    debuglevel = sys.argv[
        argument.index(argumetsIndexSearch(["-db", "--debug-level"])) + 1
    ]
    debuglevelIndex = argument.index(argumetsIndexSearch(["-db", "--debug-level"]))
if "--no-ssl" in argument or "--ssl" in argument:
    noSslIndex = argument.index(argumetsIndexSearch(["--no-ssl", "--ssl"]))
if "-gen" in argument or "--generate" in argument:
    makeDeviceIniGreateAgain()
    sys.exit()
if "--delete-logs" in argument:
    logsDeleting()
    sys.exit()

if allureLogsFolderPath[-1] != "/":
    allureLogsFolderPath = allureLogsFolderPath + "/"
if logsFolderPath[-1] != "/":
    logsFolderPath = logsFolderPath + "/"


def reconFunnction(url, data, timeout, verify=None, cert=None):
    i = 0
    while i < startReconTimes:
        try:
            if verify == None and cert == None:
                postReqForAuth = requests.post(url, data=data, timeout=timeout)
                return postReqForAuth.cookies['seal']
            else:
                postReqForAuth = requests.post(
                    url, data=data, timeout=timeout, verify=False, cert=None
                )
                return postReqForAuth.cookies['seal']
        except Exception as e:
            time.sleep(startReconTimesTimeout)
            pass
        i += 1
    return print("[FAILED] " + e)


def restAuth(_is_this_websocket=0):
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
                temp.subprotocols = (
                    line.split(" = ")[1]
                    .replace("[", "")
                    .replace("]", "")
                    .replace('"', "")
                )
            if "[authId]" in line:
                temp.authID = line.split(" = ")[1]
            if "[login]" in line:
                temp.login = line.split(" = ")[1]
            if "[password]" in line:
                temp.password = line.split(" = ")[1]
            if "[newTestMachine]" in line:
                temp.newtestmachine = line.split(" = ")[1]
    data = {"login": temp.login, "password": temp.password}
    urllib3.disable_warnings()
    try:
        if "--no-ssl" in argument[noSslIndex]:
            postReqForAuth = requests.post(
                "https://" + temp.host + "/rest/account/login",
                data=data,
                timeout=waitForResponseTimeout,
                verify=False,
                cert=None,
            )
        else:
            postReqForAuth = requests.post(
                "http://" + temp.host + "/rest/account/login",
                data=data,
                timeout=waitForResponseTimeout,
            )
    except urllib3.exceptions.ReadTimeoutError:
        if "--no-ssl" in argument[noSslIndex]:
            postReqForAuth = reconFunnction(
                "http://" + temp.host + "/rest/account/login",
                data=data,
                timeout=waitForResponseTimeout,
                verify=False,
                cert=None,
            )
        else:
            postReqForAuth = reconFunnction(
                "http://" + temp.host + "/rest/account/login",
                data=data,
                timeout=waitForResponseTimeout,
            )
    #print(postReqForAuth.cookies["seal"])
    if "Service Unavailable" in postReqForAuth.text:
        logging.error("Service Unavailable, please, try again later")
        exit()
    assert (
        "displayName" in postReqForAuth.text
    ), "DisplayName not in post response. Something wrong with auth post respose."
    temp.seal = postReqForAuth.cookies["seal"].replace("%7C", "|")



def webSocketAuth():
    print(temp.seal)
    ws = create_connection(
        f"ws://{temp.host}/ws", subprotocols=temp.subprotocols.split(), timeout=10000, cookie=f"seal={temp.seal}",
    )
    ws.send(
        '[1,"realm1",{"roles":{"caller":{"features":{"caller_identification":true,"progressive_call_results":true}},"callee":{"features":{"caller_identification":true,"pattern_based_registration":true,"shared_registration":true,"progressive_call_results":true,"registration_revocation":true}},"publisher":{"features":{"publisher_identification":true,"subscriber_blackwhite_listing":true,"publisher_exclusion":true}},"subscriber":{"features":{"publisher_identification":true,"pattern_based_subscription":true,"subscription_revocation":true}}},"authmethods":["ticket"],"authid":"'
        + str(temp.authID)
        + '"}]'
    )
    assert '[4,"ticket",{}]' in ws.recv(), "Something wrong with webSocket connection."
    ws.send('[5,"",{}]')
    message = waitResponse(ws)
    print(message)
    assert temp.host in message, "Your host machine not found."
    listOfData = [ws, temp.seal, temp.authID, temp.newtestmachine, temp.host]
    return listOfData


def interlayer():
    restData = restAuth(1)
    print(restData)
    wsData = webSocketAuth()
    ws = wsData[0]
    seal = wsData[1]
    authId = wsData[2]
    waitForResponse(
        ws,
        '[48,1622279444960334,{},"api.konfigd.auth",["f0369b56-ad01-e919-dfe6-9f0589d147f6","{\\"username\\":\\"'
        + authId
        + '\\",\\"seal\\":\\"'
        + seal
        + '\\"}"],{}]',
        True,
        10,
        2,
    )
    waitForResponse(
        ws,
        '[48,4326942052087000,{"receive_progress":false},"api.konfigd.get",["aa1a64a8-c8f7-08d5-3617-62a983044efb","exec alertsedit.pl --list --json"],{}]',
        True,
        10,
        2,
    )
    return wsData


temp.warningFiles = (
    getFromConfig("warningFiles", "config.ini").replace(" ", "").split(",")
)

testsConters()
print("Count of tests -> " + str(temp.scriptsCount))


def makeRequestsWithoutSSL(filename, folderWithTests, ssl=True):
    def change(filename, oldLine, ssl):
        with open(filename, "r") as f:
            oldData = f.read()
            sss = oldLine.replace("http://", "https://")
            if "waitGetResponseToBeChanged" in oldLine:
                if "waitGetResponseToBeChanged" in oldLine and "True" in oldLine:
                    oldData = oldData.replace(", True", ", " + str(ssl))
                if "waitGetResponseToBeChanged" in oldLine and "False" in oldLine:
                    oldData = oldData.replace(", False", ", " + str(ssl))
                new_data = oldData.replace(sss, sss + ", " + str(ssl), 1)
            else:
                if ", verify=True" in oldData:
                    oldData = oldData.replace(
                        ", verify=True", ", cert=None, verify=" + str(ssl)
                    )
                if ", cert=None, verify=False" in oldData:
                    oldData = oldData.replace(
                        "cert=None, verify=False", ", verify=" + str(ssl)
                    )
                new_data = oldData.replace(sss, sss + ", verify=" + str(ssl), 1)
        open(filename, "w").write(new_data)

    filePath = folderWithTests
    with open(filePath + "/" + filename, "r") as file:
        fileText = open(filePath + "/" + filename, "r").read()
        for line in file:
            counter = 0
            while counter == 0:
                counter += 1
                if "requests." in line and "=" in line:
                    if "verify=" + str(ssl) in line:
                        continue
                    else:
                        oldLine = "requests." + line.split("requests.")[1].split(")")[0]
                        change(filePath + filename, oldLine, ssl)
                if "waitGetResponseToBeChanged" in line:
                    if "waitGetResponseToBeChanged" in line and ", " + str(ssl) in line:
                        continue
                    else:
                        oldLine = (
                            "waitGetResponseToBeChanged"
                            + line.split("waitGetResponseToBeChanged")[1].split(")")[0]
                        )
                        # oldLine = oldLine.replace(", True", ", " + str(ssl)).replace(", False", ", " + str(ssl))
                        change(filePath + filename, oldLine, ssl)
        file.close()


def makeTestsDebugMode(filename, folderWithTests):
    filePath = folderWithTests
    counter = 0
    while counter == 0:
        counter += 1
        with open(filePath + "/" + filename, "r") as file:
            if "from debug import *" in file.read():
                file.close()
            else:
                data = ""
                fileText = open(filePath + "/" + filename, "r").read()
                if "import sys" not in fileText:
                    data += "import sys\n"
                if "sys.path.append('../../imports/')" not in fileText:
                    data += "sys.path.append('../../imports/')\n"
                for i in range(len(fileText.split(" "))):
                    if (
                        "test_" in fileText.split(" ")[i]
                        and ":" in fileText.split(" ")[i]
                        and "def" in fileText.split(" ")[i - 1]
                    ):
                        if "," in fileText.split(" ")[i]:
                            functionName = fileText.split(" ")[i].replace(
                                ")", ", debugLevel)"
                            )
                            oldFunctionName = fileText.split(" ")[i]
                        if "()" in fileText.split(" ")[i]:
                            functionName = fileText.split(" ")[i].replace(
                                "()", "(debugLevel)"
                            )
                            oldFunctionName = fileText.split(" ")[i]
                        else:
                            functionName = fileText.split(" ")[i].replace(
                                ")", ", debugLevel)"
                            )
                            oldFunctionName = fileText.split(" ")[i]
                        if "debugEnable(int(debugLevel))" not in functionName:
                            functionName += "\tdebugEnable(int(debugLevel))\n"
                data += fileText.replace(oldFunctionName, functionName).replace(
                    "\t", "    "
                )
                if "from debug import *" not in fileText:
                    ndata = data.replace(
                        "sys.path.append('../../imports/')",
                        "sys.path.append('../../imports/')\nfrom debug import *",
                    )
                else:
                    ndata = data
                fileTextAdd = open(filePath + "/" + filename, "w").write(ndata)


def workWithFiles(file, processName, _dir_with_tests):
    def function0(file, processName, _dir_with_tests):
        if "--no-ssl" in argument[noSslIndex] or "--ssl" in argument[noSslIndex]:
            ssl = None
            if "--no-ssl" in argument[noSslIndex]:
                ssl = False
                makeRequestsWithoutSSL(file, _dir_with_tests, ssl)
            if "--ssl" in argument[noSslIndex]:
                ssl = True
                makeRequestsWithoutSSL(file, _dir_with_tests, ssl)
            makeRequestsWithoutSSL(file, _dir_with_tests, ssl)
        if (
            "-db" in argument[debuglevelIndex]
            or "--debug-level" in argument[debuglevelIndex]
        ) and processName != "wst":
            makeTestsDebugMode(file, _dir_with_tests)
        if temp.buildHash0 != "":
            filename = (
                logsFolderPath
                + "text_"
                + temp.buildHash0
                + file.replace(".py", "")
                + ".log"
            )
        else:
            filename = (
                logsFolderPath + temp.buildHash0 + file.replace(".py", "") + ".log"
            )
        if processName == "wst":
            os.system(
                "python3 -m pytest "
                + file
                + " --seal="
                + temp.seal.replace("|", "qweDelimqwe")
                + " "
                + commandLineLog
                + f" -s -q --alluredir={allureLogsFolderPath}{temp.buildHash0} | tee {logsFolderPath}{temp.buildHash0}"
                + file.replace(".py", "")
                + ".log && sed 's/\\\\r\\\\n/\\n/g' "
                + filename
                + " > "
                + filename
                + "O && mv "
                + filename
                + "O "
                + filename
                + " &"
            )
        else:

            def startRun():
                process = subprocess.Popen(
                    "python3 -m pytest "
                    + file
                    + " --seal="
                    + temp.seal.replace("|", "qweDelimqwe")
                    + " --debugLevel="
                    + str(debuglevel)
                    + " "
                    + commandLineLog
                    + f" -s -q --alluredir={allureLogsFolderPath}{temp.buildHash0} | tee {logsFolderPath}{temp.buildHash0}"
                    + file.replace(".py", "")
                    + ".log && sed 's/\\\\r\\\\n/\\n/g' "
                    + filename
                    + " > "
                    + filename
                    + "O && mv "
                    + filename
                    + "O "
                    + filename
                    + " &",
                    shell=True,
                    stdout=subprocess.PIPE,
                ).communicate()[0]
                # process = subprocess.check_output("python3 -m pytest " + file + " --seal=" + temp.seal.replace("|", "qweDelimqwe") + " --debugLevel=" + str(debuglevel) + " " + commandLineLog + f" -s -q --alluredir={allureLogsFolderPath}{temp.buildHash0} | tee {logsFolderPath}{temp.buildHash0}" + file.replace(".py", "") + ".log && sed 's/\\\\r\\\\n/\\n/g' " + filename + " > " + filename + "O && mv " + filename + "O "+ filename +" &", shell=True)
                print(process.decode("UTF-8"))
                if (
                    "-ll" in sys.argv[logLevelIndex]
                    or "--log-level" in sys.argv[logLevelIndex]
                ):
                    if (
                        sys.argv[logLevelIndex + 1] == "INFO"
                        or sys.argv[logLevelIndex + 1] == "info"
                    ):
                        print(process.decode("UTF-8"))
                if (
                    "0 failed " not in process.decode("UTF-8")
                    and "FAILED" in process.decode("UTF-8")
                    and "PASSED" not in process.decode("UTF-8")
                ):
                    arrayForFailedTests.append(file)
                    logging.info(f"[-] Failed -> {file}")
                if "passed in " in process.decode("UTF-8"):
                    logging.info(f"[+] Success -> {file}")

            thread0 = threading.Thread(target=startRun).start()
        # exitFunc()

    counter = 0
    while counter == 0:
        counter += 1
        if "." in file and "." not in file[0] and file not in temp.warningFiles:
            if file in skippedFiles:
                continue
            if (
                "-ll" in sys.argv[logLevelIndex]
                or "--log-level" in sys.argv[logLevelIndex]
            ):
                if sys.argv[logLevelIndex + 1] == "off":
                    commandLineLog = ""
                else:
                    commandLineLog = "--log-cli-level=" + sys.argv[logLevelIndex + 1]
            else:
                commandLineLog = "--log-cli-level=" + "INFO"
            if "-ot" in sys.argv[onlyIndex] or "--only-this" in sys.argv[onlyIndex]:
                while True:
                    if (
                        "," in argument[onlyIndex + 1]
                        or "." not in argument[onlyIndex + 1]
                    ):
                        for onlyWay in onlyThisWays:
                            if onlyWay in file:
                                function0(file, processName, _dir_with_tests)
                                pass
                            else:
                                pass
                    break
                if file in argument[onlyIndex + 1]:
                    function0(file, processName, _dir_with_tests)
            else:
                function0(file, processName, _dir_with_tests)
        else:
            pass
        try:
            threads.remove(processName)
        except:
            threads.remove(threads[0])


threads = []


def runTests(_dir_with_tests, folderWT, _is_socket_open=0):
    folderWT00 = []
    if "-s" in argument[skipIndex] or "--skip" in argument[skipIndex]:
        for test in folderWT:
            for arg in argument[skipIndex + 1].split(","):
                if arg in test:
                    folderWT00.append(test)
    for tests in folderWT00:
        folderWT.remove(tests)
    processCounter = 0
    os.chdir(_dir_with_tests)
    if _is_socket_open == 1:
        interlayer()
        for file in folderWT:
            threads.append("wst")
            checkRunning = subprocess.Popen(
                ["ps", "aux"], stdout=subprocess.PIPE
            ).communicate()[0]
            new_ps = str(checkRunning).replace("\n", "")
            if "killingProcess.py" not in str(new_ps):
                threading.Thread(
                    target=killingMachine, args=("KillingProcess",)
                ).start()
            workWithFiles(file, "wst", _dir_with_tests)
    else:
        restAuth()
        for file in folderWT:
            while True:
                if len(threads) >= 4:
                    time.sleep(0.1)
                    pass
                else:
                    checkRunning = subprocess.Popen(
                        ["ps", "aux"], stdout=subprocess.PIPE
                    ).communicate()[0]
                    new_ps = str(checkRunning).replace("\n", "")
                    if "killingProcess.py" not in str(new_ps):
                        threading.Thread(
                            target=killingMachine, args=("KillingProcess",)
                        ).start()
                    processCounter += 1
                    threads.append(f"Thread {processCounter}")
                    threading.Thread(
                        workWithFiles(
                            file, f"Thread {processCounter}", _dir_with_tests
                        ),
                        name=f"Thread {processCounter}",
                    ).start()
                    time.sleep(float(timeoutInSec))
                    break


def killingMachine(name):
    if processKillingTime != 0:
        if name == "KillingProcessRest":
            path = os.path.abspath(__file__).replace(
                os.path.abspath(__file__).split("/")[-1], "support/killingProcess.py"
            )
        else:
            path = os.path.abspath(__file__).replace(
                os.path.abspath(__file__).split("/")[-1],
                "../../support/killingProcess.py",
            )
        ps = subprocess.Popen(
            ["python3", str(path), str(int(processKillingTime))], stdout=subprocess.PIPE
        ).communicate()[0]


killingThread = threading.Thread(target=killingMachine, args=("KillingProcessRest",))
killingThread.start()

if len(desicion) == 0:
    runTests(folderDir, folderWithTests, 1)
    runTests(restFolderDir, restFolderWithTests, 0)
else:
    for i in range(len(desicion)):
        if (
            sys.argv[desicion[i]] == "-wst"
            or sys.argv[desicion[i]] == "--webSocketTests"
        ):
            runTests(folderDir, folderWithTests, 1)
        if (
            sys.argv[desicion[i]] == "-srt"
            or sys.argv[desicion[i]] == "--simpleRestTests"
        ):
            runTests(restFolderDir, restFolderWithTests, 0)

exitFunc()
