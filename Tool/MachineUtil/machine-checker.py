#version = 1.1
#UPDATE

import time
class TempClass:
    url_with_git = "http://url-to-server"
    hostName = "server-hostname"
    packs_save_dir = "/tmp/_modules/"
    yes = ["yes", "y"]
    no = ["no", "n"]
    yum = ["y", "yum"]
    wget = ["w", "wget"]
    CAMUNDA_LOCATION = ""
    COUNTER = 0
    LOCALHOSTNAME = ""
    RUN_AUTO_MODE = False
    configs_data = []
    ssh = None
    used_sets = []
    arguments = []
    hosts = []
    PRESET_PATH = ""
    TEMP_PACKS = ""
    GET_OUT = False
    tags = []
    session_id = ""
    CONNECTION_STATUS_CODE = 0
    COLORIZE = 1

class color():
    def green(text):
        return "\033[38;5;76m" + text + "\033[00m"
    def red(text):
        return "\033[38;5;9m" + text + "\033[00m"
    def simple_green(text):
        return "\033[38;5;64m" + text + "\033[00m"
    def orange(text):
        return "\033[38;5;214m" + text + "\033[00m"
    def simple_blue(text):
        return "\033[38;5;117m" + text + "\033[00m"
    def dark_blue(text):
        return "\033[38;5;26m"  + text + "\033[00m"
    def dark_red(text):
        return "\033[38;5;1m" + text + "\033[00m"
    def light_green(text):
        return "\033[38;5;46m" + text + "\033[00m"    
    def light_yellow(text):
        return "\033[38;5;142m" + text + "\033[00m"

def outtext(string, model = "out", named_tuple = None, time_string = None):
    timeStringForLine = "" if named_tuple == None and time_string == None else f"[{time_string}]"
    if model == "info":
        if TempClass.COLORIZE == 0: return(f"{timeStringForLine}[INFO] - {string}")
        else: return(color.simple_green(f"{timeStringForLine}[INFO] - {string}"))
    if model == "error":
        if TempClass.COLORIZE == 0: return(f"{timeStringForLine}[ERROR] - {string}")
        else: return(color.red(f"{timeStringForLine}[ERROR] - {string}"))
    if model == "warning":
        if TempClass.COLORIZE == 0: return(f"{timeStringForLine}[WARNING] - {string}")
        else: return(color.orange(f"{timeStringForLine}[WARNING] - {string}"))
    if model == "out":
        if TempClass.COLORIZE == 0: return(f"{timeStringForLine} - {string}")
        else: return(color.simple_blue(f"{timeStringForLine} - {string}"))
    if model == "except":
        if TempClass.COLORIZE == 0: return(f"{timeStringForLine}[EXCEPTION] - {string}")
        else: return(color.dark_red(f"{timeStringForLine}[EXCEPTION] - {string}"))
    if model == "success":
        if TempClass.COLORIZE == 0: return(f"{timeStringForLine}[SUCCESS] - {string}")
        else: return(color.light_green(f"{timeStringForLine}[SUCCESS] - {string}"))
    if model == "information":
        if TempClass.COLORIZE == 0: return(f"{string}")
        else: return(color.light_yellow(f"{string}"))
    
def log(string, model = "info", verbose = False):
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    if verbose != True or TempClass.GET_OUT != False:
        print(outtext(string, model, named_tuple, time_string))
    
def input_man(choose, batch):
    choose = batch if TempClass.RUN_AUTO_MODE is True else input(choose)
    return choose

import sys
packets = ["threading", "subprocess", "requests", "paramiko", "urllib3", "socket"]
def get_requirements():
    open("requirements.txt", "w")
    for packet in packets:
        open("requirements.txt", "a+").write(f"{packet}\n")
    log("File requirements.txt generated successfully!\n\tUse `pip install -r requirements.txt`")

argument = sys.argv
if "--get-req" in argument and "-h" not in argument:
    try:
        get_requirements()
    except IndexError:
        log("[--get-req] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
        sys.exit()


try:
    import sys
    import collections.abc
    if sys.version_info.major == 3 and sys.version_info.minor >= 10:
        import collections
        setattr(collections, "MutableMapping", collections.abc.MutableMapping)
    import os
    import random
    import string
    from os.path import exists
    import subprocess
    import requests
    import paramiko
    import urllib3
    import socket
    import threading
except Exception as e:
    log(e, "except")
    while True:
        try:
            choose = input_man("Something wrong with python3 pip imports!\nFix it?[Y/n] -> ", "Y")
            if choose.lower() in TempClass.yes or choose == "":
                import os
                import sys
                from os.path import exists
                if (sys.platform == "linux"):
                    os.system("yum install 'dnf-command(python3-pip)'")
                    os.system("python -m pip install --upgrade pip")
                    os.system("yum install python3-devel -y")
                    os.system("yum install libffi libffi-devel -y")
                    for packet in packets:
                        os.system(f"python -m pip install {packet}")
                elif (sys.platform == "win32"):
                    for packet in packets:
                        os.system(f"python -m pip install {packet}")
                import socket
                import urllib3
                import subprocess
                import requests
                import paramiko
                import random
                import string
                import threading
                break
            if choose.lower() in TempClass.no:
                log("\nGo your own way, traveler...", "out")
                sys.exit()
        except Exception:
            log("\nGo your own way, traveler...", "out")
            sys.exit()
try:
    def session_id_gen():
        let = string.ascii_lowercase + string.digits
        TempClass.session_id = ''.join(random.choice(let) for _ in range(10))
    session_id_gen()

    def banner():
        return print("""
        -h, --help                                    - Short banner and full banner
        --get-req                                     - Generate requirements
        --get-license                                 - Get license
        --kill-process <proc name>                    - Kill process
        -v, --verbose                                 - Show log

        
        --get-scenarios                                      - Get scenarios on server
        --get-configs                                        - Get configs on server
        --get-chains                                         - Get saved presets from server
        --get-chains-full                                    - Get full info about presets
        --get-preset-cmd <chain number or scenario name>     - Show all variables from configs in as cmd line 
        --get-preset-screen <chain number or scenario name>  - Show all variables from configs in as simple sceen text 
        --modules                                            - Show all modules
        
        --scenario-local <local-path-to-scenario>          - run scenario from local machine
        --scenario-remote <scenario-name-from-server>      - run scenario from server machine
        --scenario-description <scenario-name-from-server> - Show scenario description
        --load-module <module-name>                        - Load module from server
        
        --set-camunda-path                            - Set camunda path
        --install-config <config-name-from-server>    - Get config from server
        --import-file <file-path>                     - File import for easy scenario generation

        --run-chain <name or number of chain>         - Run selected chain
        --batch                                       - Selects default values everywhere
        --preset <preset filename>                    - Run chain or scenario with prepared preset
        
        --clear-temp-logs                             - Delete all logs from /tmp/ (locally only)
        --upgrade                                     - Install updates from server
        
        Scenario commands help:
                 Unzip - <folder to unzip>:<zip file>
                  Wget - <path and name of save file>:<link for file>
                Manual - <type any command you want>
        Service status - <name of service>
           Get license - type "-" to get license
           Make backup - <path to file>
                  Edit - xml editor
          Kill process - Killing processes
        """)

    class temp():
        headers = {
            "authority": "link-to-nexus",
            "accept": "*/*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "NX-ANTI-CSRF-TOKEN=0.09213723604687796",
            "dnt": "1",
            "nx-anti-csrf-token": "0.09213723604687796",
            "origin": "https://link-to-nexus",
            "referer": "https://link-to-nexus/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
            "x-nexus-ui": "true",
            "x-requested-with": "XMLHttpRequest",
            "Content-type": "application/json"
        }
        cookies = {}

    def subprocess_check_output(command):
        if TempClass.GET_OUT is True:
            return subprocess.check_output(command, shell=True, encoding="WINDOWS-1251")
        else:
            # print("\n\n\n Here \n\n\n")
            out = subprocess.check_output(command, shell=True, encoding="WINDOWS-1251")
        if (sys.platform == "linux"):
            if "HTTP request sent, awaiting response" in str(out):
                print(out)
            open(f"/tmp/output_{TempClass.session_id}.log", "a+").write(str(out) + "\n")
        return out

    def argumets_index_search(values):  # sourcery skip: use-itertools-product
        for value in values:
            for i in range(len(sys.argv)):
                if value == str(sys.argv[i]):
                    index0 = sys.argv[i]
        return str(index0)

    def get_license(ssh=None):
        try:
            if ssh is None:
                get_output(subprocess_check_output("get-license.pl"))
                get_output(subprocess_check_output("/usr/local/avalon/bin/apachectl restart"))
                get_output(subprocess_check_output('su - avalon -c \"license.pl\"'))
            else:
                stdin, stdout, stderr = ssh.exec_command("get-license.pl")
                get_output(stdout)
                stdin, stdout, stderr = ssh.exec_command("/usr/local/avalon/bin/apachectl restart")

                get_output(stdout)
                stdin, stdout, stderr = ssh.exec_command('su - avalon -c \"license.pl\"')
                get_output(stdout)
        except subprocess.CalledProcessError as exception_this:
            log(f"[--get-license] Something went wrong!\n\t{exception_this}", "warning")
        
    def get_output(output, model = "info"):
        if (sys.platform == "linux"):
            open(f"/tmp/output_{TempClass.session_id}.log", "a+").write(str(output) + "\n")
        if "HTTP request sent, awaiting response" in str(output):
            print(outtext(output))
        if TempClass.GET_OUT is True:
            if TempClass.ssh is None:
                print(outtext(output))
            else:
                try:
                    print(output.splitlines())
                except Exception:
                    pass
        return str(output)
    
    def get_config_variables(response):
        pull_variables = []
        for line in response.splitlines():
            for i in range(len(line.split("{~"))):
                if "~}" in line.split("{~")[i]:
                    ll = line.split("{~")[i].split("~}")[0]
                    if ll not in pull_variables:
                        pull_variables.append(ll)
        return pull_variables


    def get_preset(PRESET_SCENARIO, mode = 0):
        pull_variables = []
        if ".scenario" not in PRESET_SCENARIO:
            response = requests.get(f"{TempClass.url_with_git}/chains/list.txt").text
            cell_line = response.splitlines()[int(PRESET_SCENARIO)]
            output = cell_line.split("]")[1].split(";")
            for machine in output:
                if machine != "":
                    resp = requests.get(f"{TempClass.url_with_git}/scenarios/" + machine.split("->")[1]).text
                    for line in resp.splitlines():
                        for elem in line.split(" "):
                            if f"{TempClass.url_with_git}" in elem and "/configs/" in elem:
                                # nedded_link = elem
                                resp = requests.get(elem.split("<")[0]).text
                                pull_variables += get_config_variables(resp)
        else:
            response = requests.get(f"{TempClass.url_with_git}/scenarios/{PRESET_SCENARIO}").text
            for line in response.splitlines():
                for elem in line.split(" "):
                    if f"{TempClass.url_with_git}" in elem and "/configs/" in elem :
                        # nedded_link = elem
                        resp = requests.get(elem.split("<")[0]).text
                        pull_variables += get_config_variables(resp)
        pvariables = []
        for elem in pull_variables:
            if elem not in pvariables:
                pvariables.append(elem)
        if mode == 0:
            get_output(f"*{PRESET_SCENARIO}*\n")
            for el in pvariables:
                print(f"{el}=")
        if mode == 1:
            if ".scenario" in PRESET_SCENARIO:
                output = f"python machine-checker.py --scenario-remote {PRESET_SCENARIO} "
                for elem in pvariables:
                    output += f" --tag \"{elem}=your_value\""
            else:
                output = f"python machine-checker.py --run-chain {PRESET_SCENARIO} "
                for elem in pvariables:
                    output += f" --tag \"{elem}=your_value\""
            print(output)
        
    def make_backup(filepath):
        filename = filepath.split("/")[-1] or filepath.split("\\")[-1]
        if TempClass.ssh != None:
            if os.path.exists("/home/backups/") is not True:
                os.system("mkdir /home/backups/")
            os.system(f"zip -r 9 /home/backups/{filename}.zip {filepath}") 
        else:
            if os.path.exists("/home/backups/") is not True:
                os.system("mkdir /home/backups/")
            stdin, stdout, stderr = TempClass.ssh.exec_command(f"zip -r 9 /home/backups/{filename}.zip {filepath}")
            get_output(stdout)
    
    def nexusMainAuth(session):
        data = {"action":"node_NodeAccess",
                "method":"nodes",
                "data":None,
                "type":"rpc",
                "tid":1
                }
        temp.cookies = session.post("https://link-to-nexus/service/extdirect", json=data, headers=temp.headers).cookies.get_dict()
        data = {"action":"rapture_Security","method":"getPermissions","data":None,"type":"rpc","tid":2}
        session.post("https://link-to-nexus/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies)
        data = { 'action':'coreui_Repository','method':'readReferences','data':[{ 'page':1,'start':0,'limit':25}],'type':'rpc','tid':3}
        session.post("https://link-to-nexus/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies)
        return session
    
    def getResponseFromNexusToGetLastVersionOfPackage(session, repo, branch, package, parameters):
        path = branch + "/" + package.replace(package.split("/")[-1], "")
        pack = package.split("/")[-1].replace("\n", "").replace("\r", "")
        data = {'action': 'coreui_Browse', 'method': 'read', 'data': [{'repositoryName': f'{repo}', 'node': f'{path}'}], 'type': 'rpc', 'tid': 6}
        log(pack, model = "information",  verbose=True)   
        log(branch + "/" + package.replace(package.split("/")[-1], ""), model = "information",  verbose=True)   
        log(data, model = "information",  verbose=True)   
        response = session.post("https://link-to-nexus/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies).text
        log(response, model="information", verbose=True)
        lastVersionOfPackage = 0
        lastNameOfPackage = ""
        log("Full list of packages", model = "information",  verbose=True)
        for elem in response.split('\"'):
            if pack in elem and "/" not in elem:
                for el in elem.replace("-", ".").split("."):
                    if len(el) == 12:
                        date = el
                        break
                if len(date) == 12 and int(date) > int(lastVersionOfPackage):
                    log(lastNameOfPackage, model = "information",  verbose=True)
                    lastVersionOfPackage = date
                    lastNameOfPackage = elem
        log(f"\nPackage last name: {lastVersionOfPackage}\nPackage last version: {lastNameOfPackage}", model = "information",  verbose=True)    
        TempClass.TEMP_PACKS = lastNameOfPackage
        save_dir = parameters.split("-P ")[1].split(" http")[0].replace(parameters.split("-P ")[1].split(" http")[0].split("/")[-1], "") # + lastNameOfPackage
        file_to_save = parameters.replace("</parameters>", "").split(parameters.split("-P ")[1].split(" http")[0])[1].replace(parameters.split(" http")[1].split("/")[-1], "") + lastNameOfPackage
        log(f"wget -P {save_dir} {file_to_save}", model = "information",  verbose=True)
        return f"wget -P {save_dir} {file_to_save}"
    
    def killProcess(parameters):
        output = ""
        if TempClass.ssh is None:
            output = get_output(subprocess_check_output(f"ps aux | grep {parameters}")).splitlines()
        else:
            stdin, output, stderr = TempClass.ssh.exec_command(f"ps aux | grep {parameters}")
        for line in output:
            pid = line.split()[1]
            if sys.argv[0] in line:
                continue
            get_output(f"Killing this pid -> {pid}")
            if TempClass.ssh is None:
                os.system(f"sudo kill -9 {pid}")
            else:
                TempClass.ssh.exec_command(f"sudo kill -9 {pid}")

    def checkLastVersionOfPackage(parameters):
        _install = False
        if "<install>" in parameters:
            _install = True
        parameters = parameters.replace("<install>", "")
        repo = parameters.split("/repository/")[1].split("/")[0]
        branch = parameters.split(f"{repo}/")[1].split("/")[0]
        package = parameters.split(f"{branch}/")[1].split("<")[0].replace("-last-version", "")
        session = requests.Session()
        session = nexusMainAuth(session)
        parameters = getResponseFromNexusToGetLastVersionOfPackage(session, repo, branch, package, parameters)
        return parameters, _install
    
    def remakeConfig(parameters):
        for elem in parameters.split(" "):
            if "http://" in elem:
                url = elem
        output = requests.get(url).text
        data = ""
        for elem in parameters.split(" "):
            if "/" in elem and "://" not in elem:
                path = elem
        if "{~" in output and "~}" in output:
            get_output(f"""
            \r--------------------------------
            \r+
            \r+   This one changes {path}
            \r+
            \r--------------------------------
            """)
        for line in output.splitlines():
            nline = line
            for i in range(len(line.split("{~"))):
                # print(line.split("{~")[i])
                if "~}" in line.split("{~")[i]:
                    ll = line.split("{~")[i].split("~}")[0]
                    default = ""
                    newchar = ""
                    for item in TempClass.configs_data:
                        if ll in item[0]:
                            default = item[1]
                    if TempClass.PRESET_PATH == "":
                        skip = False
                        if TempClass.tags != []:
                            for el in TempClass.tags:
                                if ll in el[0]:
                                    TempClass.configs_data.append([ll, el[1]])
                                    newchar = el[1]
                                    skip = True
                                    break
                        if skip is False:
                            if default == "":
                                newchar = input(f"Please, input value of param -> [{ll}] -> ")
                                TempClass.configs_data.append([ll, newchar])
                            else:
                                newchar = input(f"Please, input value of param -> [{ll}] -> default ({default}) press enter -> ")  
                                if newchar == "":
                                    newchar = default
                    else:
                        get_output("RUN WITH PRESET!", "out")
                        with open(TempClass.PRESET_PATH, "r") as file:
                            for line in file:
                                if ll in line:
                                    newchar = line.split("=")[1].replace("\n", "")
                        get_output("{~" + ll + "~} -> " + newchar)
                    nline = nline.replace("{~" + ll + "~}", newchar)
            data += nline + "\n"
        if TempClass.ssh is None:
            open(path, "w").write(data)
        else:
            ftp = TempClass.ssh.open_sftp()
            file=ftp.file(f"{path}", "w", -1)
            file.write(data)
            file.flush()
            ftp.close()
        get_output("Config successfully created!", "success")
        return True
            
                        
    class make_xml():
        tags = ["host", "port", "serverUrl", "managerDn", "managerPassword",
                "baseDn", "userFirstnameAttribute", "userPasswordAttribute",
                "groupIdAttribute", "groupNameAttribute", "administratorGroupName",
                "administratorUserName", "username", "password", "port",
                "redirectPort", "name"]
        
        choose = 0
        def make_new_param(self, nameOfParameter, oldParameter):
            nameOfParameter = nameOfParameter.replace('\n', '').replace('\r', '')
            oldParameter = oldParameter.replace('\n', '').replace('\r', '')
            newParameter = ""
            if self.choose == 1:
                for elem in self.tags:
                    if elem.lower() == nameOfParameter.lower():
                        newParameter = input_man(f"Param name [{nameOfParameter}] default value [{oldParameter}] [Press enter to default] -> ", "")
            elif self.choose == 0:
                newParameter = input_man(f"Param name [{nameOfParameter}] default value [{oldParameter}] [Press enter to default] -> ", "")
            return newParameter
        
        def makeXml(parameters):
            fileBackup = []
            newParameter = ""
            choose = input_man("You want to change all params? [y]es/[N]o ->", "N")
            if choose.lower() in TempClass.yes:
                make_xml.choose = 0
            if choose.lower() in TempClass.no or choose == "":
                make_xml.choose = 1
            with open(parameters, "r") as file:
                for line in file:
                    if ">" in line or "<" in line or '\"' in line:
                        line = line.replace("\n", "")
                        if "value" in line and 'name' in value and "/>" in line and "<" in line:
                            nline = line.split('\"')
                            for f in range(len(line.split('\"'))):
                                if "name=" in line.split('\"')[f]:
                                    name = line.split('\"')[f + 1]
                                if "value=" in line.split('\"')[f]:
                                    value = line.split('\"')[f + 1]
                            newParameter = make_xml.make_new_param(self=make_xml, nameOfParameter=name, oldParameter=value)
                        else:
                            for i in range(len(line.split(" "))):
                                if "=" in line.split(" ")[i]:
                                    nline = line.split(" ")[i]
                                    if " />" not in str(line):
                                        name = nline.split("=")[1].split(">")[0].replace('\"', "")
                                        try:
                                            value = nline.split(">")[1].split("<")[0].replace('\"', "")
                                            newParameter = make_xml.make_new_param(self=make_xml, nameOfParameter=name, oldParameter=value)
                                        except Exception:
                                            newParameter = ""
                                    if "/>" in str(line):
                                        name = nline.split("=")[0]
                                        value = nline.split("=")[1].replace(nline.split("=")[1][0], "")
                                        newParameter = make_xml.make_new_param(self=make_xml, nameOfParameter=name, oldParameter=value)
                            indexes0 = [i for i, c in enumerate(line) if c == "<"]
                            indexes1 = [i for i, c in enumerate(line) if c == ">"]
                            if '\"' not in line and ">" in line and "<" in line and len(indexes0) > 1 and len(indexes1) > 1:
                                for elem in line.split(">"):
                                    if "</" in elem:
                                        name = "Undef"
                                        value = elem.replace("\n", "").split("</")[0]
                                        newParameter = make_xml.make_new_param(self=make_xml, nameOfParameter=name, oldParameter=value)
                        if newParameter != "":
                            line = line.replace(value, newParameter)
                        fileBackup.append(line)
            if TempClass.ssh != None:
                open(parameters, "w")
                for elem in fileBackup:
                    open(parameters, "a+").write(elem + "\n")
            else:
                ftp = TempClass.ssh.open_sftp()
                file=ftp.file(f"{parameters}", "w", -1)
                for elem in fileBackup:
                    file.write(elem + "\n")
                file.flush()
                ftp.close()
        
    def run_command(id_of_step, action, parameters):
        if not exists(TempClass.packs_save_dir):
            if TempClass.ssh is None:
                os.mkdir(TempClass.packs_save_dir)
                if id_of_step == 1:
                    os.system(f"sudo rm -r {TempClass.packs_save_dir}*")
            else:
                stdin, stdout, stderr = TempClass.ssh.exec_command(f"mkdir -p {TempClass.packs_save_dir}")
                for line in stdout:
                    get_output(line)
                if id_of_step == 1:
                    stdin, stdout, stderr = TempClass.ssh.exec_command(f"sudo rm -r {TempClass.packs_save_dir}*")
                    for line in stdout:
                        get_output(line)
        else:
            if TempClass.ssh is None:
                if len(os.listdir(TempClass.packs_save_dir)) > 0:
                    if id_of_step == 1:
                        os.system(f"sudo rm -r {TempClass.packs_save_dir}*")
                    os.system(f"yes 2>/dev/null | mkdir -p {TempClass.packs_save_dir}")
            else:
                if id_of_step == 1:
                    stdin, stdout, stderr = TempClass.ssh.exec_command(f"sudo rm -r {TempClass.packs_save_dir}*")
        log(f"Step: {id_of_step}; Action: {action}; Params: {parameters}")
        new_params = parameters
        if "{" in parameters and "}" in parameters:
            for i in range(len(parameters.split("{"))):
                if "}" in parameters.split("{")[i]:
                    pr = parameters.split("{")[i].split("}")[0]
                    newParam = input(f"Please input value [{pr}] -> ")
                    new_params = new_params.replace("{" + pr + "}", newParam)
        parameters = new_params
        if action == "Unzip":
            try:
                save_dir = parameters.split(":")[0]
                file_to_save = parameters.replace(save_dir, "")
                if file_to_save[0] == ":":
                    file_to_save = file_to_save.replace(file_to_save[0], "")
                if TempClass.ssh is None:
                    get_output(subprocess_check_output(f"unzip {file_to_save} -d {save_dir}"))

                else:
                    stdin, stdout, stderr = TempClass.ssh.exec_command(f"unzip {file_to_save} -d {save_dir}")
                    for line in stdout:
                        get_output(line)
            except Exception as this_exception:
                log(f"[EXCEPTION] {this_exception}", "except")
        if action == "Kill process":
            try:
                killProcess(parameters)
            except Exception as this_exception:
                log(f"[EXCEPTION] {this_exception}", "except")
        if action == "Wget":
            try:
                save_dir = parameters.split(":")[0]
                file_to_save = parameters.replace(save_dir, "")
                if file_to_save[0] == ":":
                    file_to_save = file_to_save.replace(file_to_save[0], "")
                if TempClass.ssh is None:
                    get_output(subprocess_check_output(f"wget -O {save_dir} {file_to_save}"))

                else:
                    stdin, stdout, stderr = TempClass.ssh.exec_command(f"wget -O {save_dir} {file_to_save}")
                    for line in stdout:
                        get_output(line)
            except Exception as this_exception:
                log(f"[EXCEPTION] {this_exception}", "except")
        if action == "Manual":
            try:
                _isinstall = False
                def func0(parameters, _isinstall):
                    if "wget" in parameters and "/configs/" in parameters and TempClass.hostName in parameters:
                        parameters = remakeConfig(parameters)
                        _isinstall = False
                        log(f"Configs path identificated!\nParams: {parameters}\nInstall flag?: {_isinstall}", model="information", verbose=True)
                    elif "-last-version" in parameters:
                        get_output(f"Get output from -> {parameters}")
                        log(f"Params: {parameters}\nInstall flag?: {_isinstall}", model="information", verbose=True)
                        parameters, _isinstall = checkLastVersionOfPackage(parameters)
                    elif "<install>" in parameters and "-last-version" not in parameters:
                        TempClass.TEMP_PACKS = parameters.split("/")[-1].replace("<install>", "")
                        parameters = parameters.replace("<install>", "")
                        _isinstall = True
                    else:
                        _isinstall = False
                    return parameters, _isinstall
                if TempClass.ssh is None and parameters != "True":
                    parameters, _isinstall = func0(parameters, _isinstall)
                    get_output([parameters, _isinstall])
                    # log(f"\nssh: {str(TempClass.ssh)}\nIs install: {str(_isinstall)}\nParams: {parameters}\n","information")
                    # get_output(f"#3 {parameters}")
                    if parameters == True or parameters == False:
                        pass
                    else:
                        get_output(subprocess_check_output(f"yes 2>/dev/null | {str(parameters)}"))
                    # get_output(subprocess_check_output(f"yes | {str(parameters)}"))
                elif TempClass.ssh != None and parameters != True:
                    parameters, _isinstall = func0(parameters, _isinstall)
                    # log(f"\nssh: {str(TempClass.ssh)}\nIs install: {str(_isinstall)}\nParams: {parameters}\n","information")
                    # get_output(f"#4 {parameters}")
                    stdin, stdout, stderr = TempClass.ssh.exec_command(f"yes 2>/dev/null | {str(parameters)}")
                    for line in stdout:
                        get_output(line)
                if _isinstall is True:
                    get_output("Installing....")
                    if TempClass.ssh != None:
                        if TempClass.GET_OUT == True:
                            stdin, stdout, stderr = TempClass.ssh.exec_command(f"rpm -ivv {TempClass.packs_save_dir}{TempClass.TEMP_PACKS}")
                        else:
                            stdin, stdout, stderr = TempClass.ssh.exec_command(f"rpm -i {TempClass.packs_save_dir}{TempClass.TEMP_PACKS}")
                    else:
                        if TempClass.GET_OUT == True:
                            get_output(subprocess_check_output(f"rpm -ivv {TempClass.packs_save_dir}{TempClass.TEMP_PACKS}"))       
                        else: 
                            get_output(subprocess_check_output(f"rpm -i {TempClass.packs_save_dir}{TempClass.TEMP_PACKS}"))          
                    for line in stdout:
                        if TempClass.GET_OUT == True:
                            get_output(line)
            except subprocess.CalledProcessError:
                pass
            except Exception as this_exception:
                log(f"[EXCEPTION] {this_exception}", "except")
        if action == "Service status":
            try:
                if TempClass.ssh is None:
                    get_output(subprocess_check_output(f"sudo systemctl status {parameters}"))

                else:
                    stdin, stdout, stderr = TempClass.ssh.exec_command(f"sudo systemctl status {parameters}")
                    get_output(stdout)
            except Exception as this_exception:
                log(f"[EXCEPTION] {this_exception}", "except")
        if action == "Get license":
            if TempClass.ssh is None:
                get_output(get_license())
            else:
                get_output(get_license(TempClass.ssh))
        if action == "Make backup":
            make_backup(parameters)
        if action == "Edit":
            make_xml.makeXml(parameters)
    def scenario_run():
        id_of_step = ""
        action_of_step = ""
        parameters_of_step = ""
        step_num = 0
        try:
            with open(SCENARIO_DIR, "r") as file:
                for line in file:
                    if "<id>" in line:
                        id_of_step = line.split("<id>")[1].split("</id>")[0]
                        step_num += 1
                    if "<action>" in line:
                        action_of_step = line.split("<action>")[1].split("</action>")[0]
                    if "<parameters>" in line:
                        parameters_of_step = line.split("<parameters>")[1].split("</parameters>")[0]
                    if id_of_step != "" and action_of_step != "" and parameters_of_step != "":
                        run_command(step_num, action_of_step, parameters_of_step)
                        id_of_step = ""; action_of_step = ""; parameters_of_step = ""
        except FileNotFoundError:
            log("Wrong path! No such file", "error")
       
    def get_scenario_run(SCENARIO_NAME=""):
        id_of_step = ""
        action_of_step = ""
        parameters_of_step = ""
        response = requests.get(f"{TempClass.url_with_git}/scenarios/{SCENARIO_NAME}").text
        step_num = 0
        for line in response.split("\n"):
            if "<id>" in line:
                id_of_step = line.split("<id>")[1].split("</id>")[0]
                step_num += 1
            if "<action>" in line:
                action_of_step = line.split("<action>")[1].split("</action>")[0]
            if "<parameters>" in line:
                parameters_of_step = line.split("<parameters>")[1].split("</parameters>")[0]
            if id_of_step != "" and action_of_step != "" and parameters_of_step != "":
                run_command(step_num, action_of_step, parameters_of_step)
                id_of_step = ""
                action_of_step = ""
                parameters_of_step = ""
                    
    def get_list_of_files(directory=""):
        # sourcery skip: use-contextlib-suppress
        massive_of_scripts = []
        response_config_file = ""
        if directory == "configs":
            response_config_file = requests.get(f"{TempClass.url_with_git}/{directory}/config.manage").text
            # "https://git.link-to.ru/andrey.gulko/server-side/-/raw/master/configs/config.manage"
        response = requests.get(f"{TempClass.url_with_git}/{directory}/").text
        # print(response)
        for i in range(len(response.split('\"'))):
            if "href=" in response.split('\"')[i] and ".manage" not in response.split('\"')[i + 1]:
                added_line = response.split('\"')[i + 1]
                massive_of_scripts.append(added_line)
                # print(massive_of_scripts)
                if len(response_config_file) > 1:
                    for line in response_config_file.splitlines():
                        # print(line)
                        if added_line in line:
                            added_line = f"{added_line} -> Install path: " + line.split(";")[1].replace("{camunda_path}", TempClass.CAMUNDA_LOCATION)
                            print(added_line)
                            # get_output(added_line)
        # print(massive_of_scripts)
        return massive_of_scripts
    
    def get_online_description_in_scenario():
        response = requests.get(f"{TempClass.url_with_git}/scenarios/{DESCRIPTION_FILENAME}")
        response.encoding = 'utf-8'
        description = response.text.split("<description>")[1].split("</description>")[0]
        return description
                
    def get_online_description():
        response = requests.get(f"{TempClass.url_with_git}/descriptions/{DESCRIPTION_FILENAME}.txt")
        if "Error response" in response.text or "Message: File not found." in response.text:
            print("\tNo such file! :(")
        else:
            response.encoding = 'utf-8'
            print("\t" + response.text.replace("\n", "\n\t"))
        


    # def get_config_list():
    
    def checking_camunda_location():
        path = "/tmp/camunda_folder.tmp"
        if exists(path) is True:
            TempClass.CAMUNDA_LOCATION = open(path).read().replace("\n", "")
        else:
            output = get_output(subprocess_check_output("find / -name 'camunda' | grep /camunda/server/ | head -n 1"))
            if "/camunda/" not in str(output):
                path_to_camunda = input("We cannot found camunda! Please, input path to camunda here -> ")
            else: path_to_camunda = output.split("/server/apache")[0]
            TempClass.CAMUNDA_LOCATION = path_to_camunda.replace("\n", "")
            if TempClass.ssh != None:
                open(path, "w").write(path_to_camunda.replace("\n", ""))
            else:
                ftp = TempClass.ssh.open_sftp()
                file=ftp.file(f"{path}", "w", -1)
                file.write(path_to_camunda.replace("\n", ""))
                file.flush()
                ftp.close()
    
    def bb():
        print("This is gui!")
    def run_gui():
        bb()
        while True:
            req = input("->")
            
        
    def install_config():
        path_to_install = ""
        response = requests.get(f"{TempClass.url_with_git}/configs/{CONFIG_NAME}").text

        response_config_file = requests.get(f"{TempClass.url_with_git}/configs/config.manage")

        for line in response_config_file.text.splitlines():
            if CONFIG_NAME in line:
                path_to_install = line.split(";")[1]
        if "/server/" in path_to_install:
            only_path = path_to_install.replace(path_to_install.split("/")[-1], "")
            if not exists(only_path):
                pass
                # checking_camunda_location()
        open(path_to_install, "w").write(response)
        get_output(f"Successfully saved -> {path_to_install}", "success")
    
    def setView(line):  # sourcery skip: use-contextlib-suppress
        set_name = line.split("]")[0].split("[")[1]
        print(f"[Chain #{TempClass.COUNTER}]===========================")
        print(f"Chain name: {set_name}")
        new_line = ""
        print("---------------")
        for elem in line.split("]")[1].split(";"):
            try:
                new_line += "Device: " + elem.split("->")[0].strip()+ "\nRun with scenario: " + elem.split("->")[1].strip() +  "\n"
            except IndexError:
                pass
        print(new_line)
        print("---------------")
        print(f"[end chain #{TempClass.COUNTER}]===========================")
        TempClass.COUNTER += 1
    
    def sets_view(show=False):            
        # sourcery skip: move-assign-in-block, remove-str-from-print, use-fstring-for-concatenation
        TempClass.COUNTER = 0
        response = requests.get(f"{TempClass.url_with_git}/chains/list.txt").text
        for line in response.splitlines():
            if line != "":
                if show is False:
                    print(f"[{TempClass.COUNTER}]" + line.split("]")[0].split("[")[1])
                    TempClass.COUNTER += 1
                if show is True:
                    setView(line)

    def run_set(SET_INDEX):
        logins_data = []
        response = requests.get(f"{TempClass.url_with_git}/chains/list.txt").text
        x = SET_INDEX
        cell_line = ""
        if SET_INDEX.isdigit():
            cell_line = response.splitlines()[int(x)]
        else:
            for i in range(len(response.splitlines())):
                if f"[{x}]" in response.splitlines()[i]:
                    cell_line = response.splitlines()[i]
                    print(cell_line)
                    x = i
        TempClass.COUNTER = int(x)
        setView(cell_line)
        output = cell_line.split("]")[1].split(";")
        if TempClass.PRESET_PATH != "":
            with open(TempClass.PRESET_PATH, "r") as file:
                for line in file:
                    if "{host}" in line:
                        TempClass.hosts.append(line.replace("\n", "").split("=")[1])
        for i in range(len(output)):
            if output[i] != "":
                if "{" in output[i] and "}" in output[i]:
                    if TempClass.hosts == []:
                        host = input("Please, input host for " + output[i].split("->")[1] + " -> ")
                        username = input(f"Please, input username for {host} -> ")
                        password = input(f"Please, input password for {username} of {host} -> ")
                        machine = output[i].replace(output[i].split("{")[1].split("}")[0], host)
                    else:
                        host = TempClass.hosts[i].split("@")[1].split(":")[0]
                        username = TempClass.hosts[i].split("@")[0]
                        password = TempClass.hosts[i].split(":")[1]
                else:
                    if TempClass.hosts == []:
                        host = output[i].split("->")[0]
                        username = input(f"Please, input username for {host} -> ")
                        password = input(f"Please, input password for {username} of {host} -> ")
                    else:
                        host = output[i].split("->")[0]
                        username = TempClass.hosts[i].split("@")[0]
                        password = TempClass.hosts[i].split(":")[1]
                logins_data.append([host, username, password, output[i].split("->")[1]])
        for machine in logins_data:
            SCENARIO_NAME = machine[3]
            if TempClass.LOCALHOSTNAME in machine or "localhost" in machine:
                get_output(f"We are running scenario {SCENARIO_NAME}", "out")
                get_output(TempClass.LOCALHOSTNAME, "out")
                get_scenario_run(SCENARIO_NAME)
            else:
                ssh = paramiko.SSHClient()
                ip = ""
                hostname = str(machine[0])
                print()
                ip = socket.gethostbyname(hostname)
                TempClass.used_sets.append([machine[0], SCENARIO_NAME])
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                log(f"We are running scenario {SCENARIO_NAME}", "out")
                log(f"Host: {machine[0]}, Username: {machine[1]}, Passwd: {machine[2]}", "out")
                print()
                ssh.connect(f"{ip}", port=22, username=machine[1], password=f"{machine[2]}", look_for_keys=False)
                TempClass.ssh = ssh
                get_scenario_run(SCENARIO_NAME = SCENARIO_NAME)

    SCENARIO_DIR = ""
    SCENARIO_NAME = ""
    DESCRIPTION_FILENAME = ""
    desicion = []
    avaliableArguments = [
                          ["-h", "--help"],             #0
                          ["-v", "--verbose"],                    #1
                          ["--get-license"],            #2
                          ["--scenario-local"],               #3
                          ["--scenario-remote"],           #4
                          ["--get-scenarios"],               #5
                          ["--test"],                   #6
                          ["--scenario-description"],        #7
                          ["--install-repo"],           #8
                          ["--get-configs"],            #9
                          ["--set-camunda-path"],       #10
                          ["--install-config"],         #11
                          ["--get-chains"],               #12
                          ["--get-chains-full"],          #13
                          ["--run-chain"],                #14
                          ["--batch"],                    #15
                          ["--get-preset-cmd", "--get-preset-screen"],               #16
                          ["--preset"],               #17
                          ["--tag"],                 #18
                          ["--clear-temp-logs"],     #19
                          ["--get-req"],             #20
                          ["--upgrade"],             #21
                          ["--installation-ending-deleting-temp"],  #22
                          ["--import-file"], #23
                          ["--kill-process"], #24
                          ["--modules"], #25
                          ["--load-module"], #26
                          ["-G", "--gui"], #27
                          ]
    def logs_clear():
        files = os.listdir("/tmp/")
        for file in files:
            if "output_" in file and ".log" in file:
                os.system(f"yes 2>/dev/null | rm -r /tmp/{file}")
        
                
    def createScenarioAbout(massive_scripts, args):
        def chars_add(where, lenscript, char):
            hchar = ""
            for i in range(where-lenscript):
                hchar += char
            return hchar
        same = ""
        for i in range(args[0] + args[1]):
            same += "+"
        # print(same)
        rows, columns = os.popen('stty size', 'r').read().split()
        head = ["Scenario name", "Scenario description"]
        if int(columns) > args[0] + args[1] + 3:
            print(chars_add(args[0] + args[1] + 3, 0, "_"))
            print("| " + chars_add(args[0] + 1, 0, " ") + "|" + chars_add(args[1]-2, 0, " ") + "|")
            print(f"| {head[0]}" + chars_add(args[0], len(head[0]), " ") + " | " + head[1] + chars_add(args[1] - 3, len(head[1]), " ") + "|" + "\n" + "|" + chars_add(args[0] + 2, 0, "_") + "|" + chars_add(args[1] - 2, 0, "_") + "|")
            for script in massive_scripts:
                print("+" + chars_add(args[0] + args[1], 0, "+") + "++")
                print("+ " + chars_add(args[0], 0, " ") + " + " + chars_add(args[1]-3, 0, " ") + "+")
                description_up = ""
                script_up = f"+ {script[0]}" + chars_add(args[0], len(script[0]), " ") + " + "
                for elem in script[1].replace("\r", "").split("\n"):
                    if elem != "":
                        description_up += elem + chars_add(args[0] + args[1] + 1, len(script_up) + len(elem), " ") + " +\n+" + chars_add(args[0] + 2, 0, " ") + "+ "
                output = script_up + description_up.replace("\r", "") + chars_add(args[1]-3, 0, " ") + "+"
                print(output)
            print("+" + chars_add(args[0] + args[1], 0, "+") + "++")
        else:
            for script in massive_scripts:
                print(script[0] + "\n\t" + script[1].replace("\n", "\n\t"))
    
    def loadMOduleFromServer(MODULE_NAME):
        wht = f"/tmp/_modules/modules/{MODULE_NAME}.py"
        if not exists(wht):
            resp = requests.get(f"{TempClass.url_with_git}/modules/{MODULE_NAME}.py").text
            os.system("mkdir -p /tmp/_modules/modules/")
            open(wht, "w").write(resp)
            # os.system(f"wget -P /tmp/_modules/modules/ {TempClass.url_with_git}/modules/{MODULE_NAME}.py")
        os.system(f"python3 /tmp/_modules/modules/{MODULE_NAME}.py")    
        
        
    def showModulesFromServer():
        resp = requests.get(f"{TempClass.url_with_git}/modules/").text
        # print(resp)
        modules_name = []
        for line in resp.splitlines():
            if "href" in line and ".py" in line:
                for i in range(len(line.split("\""))):
                    if ".py</a>" in line.split("\"")[i]:
                        module = line.split("\"")[i].replace("</a></li>", "").replace(">", "")
                        modules_name.append([len(modules_name), module])
        print("\tModules list")
        for elem in modules_name:
            elem = elem[1].replace(".py", "")
            print(f"-> {elem}")
    
    def update():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        text = requests.get(f"{TempClass.url_with_git}/common/file.py").text.replace("", "").replace("", "")
        response = text.replace("\\", "\\\\").replace("\"", "\\\"")
        try:
            if text.splitlines()[0].split("=")[1] != open("machine-checker.py", "r").readlines()[0].split(" = ")[1]:
                open("/tmp/temp.py", "w").write(f"""\n
                \rimport os,time,subprocess
                \rtime.sleep(2)
                \rlines = \"\"\"{response}\"\"\"
                \rtemp = open("{current_dir}/machine-checker.py", "w")
                \rfor line in lines:
                \r  temp.write(line)
                \rtemp.close()
                \rsubprocess.Popen(["python","{current_dir}/machine-checker.py","--installation-ending-deleting-temp"])
                """)
                subprocess.Popen(["python","/tmp/temp.py"])
            else:
                get_output("App already updated!", "success")
        except:
            get_output("Error while updating", "error")
    
    def import_file_for_generation(filepath):
        try:
            importedFileLines = open(filepath, "r").readlines()
            if len(importedFileLines[0].split(",")) >= 2 and importedFileLines[0].split(",")[0].isdigit():
                string = ""
                for line in importedFileLines:
                    string += "<id>" +  line.split(",")[0] + "</id>\n"
                    string += "\t<action>" +  line.split(",")[1] + "</action>\n"
                    string += "\t<parameters>" +  line.replace(line.split(",")[0] + ",", "").replace(line.split(",")[1] + ",", "").replace("\n", "").replace("\r", "") + "</parameters>\n"
            else:
                string = ""
                for i in range(len(importedFileLines)):
                    string += "<id>" +  str(i) + "</id>\n"
                    string += "\t<action>" +  "Manual" + "</action>\n"
                    string += "\t<parameters>" + importedFileLines[i].replace("\n", "").replace("\r", "")  + "</parameters>\n"
            open("runme.scenario", "w").write(string)
            log("File successfull created!", "success")
        except:
            log("Something went wrong!", "error")
            sys.exit()
        
    
    def conn_check():
        def check_version():
            response = requests.get(f"{TempClass.url_with_git}/common/file.py").text
            # print(response.splitlines()[0] + "     |     " + open("machine-checker.py", "r").readlines()[0])
            if response.splitlines()[0].split("=")[1] != open("machine-checker.py", "r").readlines()[0].split("=")[1]:
                if "#NOT_UPDATE" in response.splitlines()[1]:
                    pass
                elif "#UPDATE" in response.splitlines()[1]:
                    print("++++++++++++++NEW VERSION AVALIABLE++++++++++++++")
                    print("++++++++++++++NEW VERSION AVALIABLE++++++++++++++")
                    print("++++++++++++++NEW VERSION AVALIABLE++++++++++++++")
                    print("++++++++++++++NEW VERSION AVALIABLE++++++++++++++")
                    print("++++++++++++++NEW VERSION AVALIABLE++++++++++++++")
                elif "#FORCE_UPDATE" in response.splitlines()[1]:
                    update()
                    threading.current_thread().abort()
                else:
                    threading.current_thread().abort()
        # Description - TempClass.CONNECTION_STATUS_CODE
        # 0 - not checking
        # 1 - already checked (not 200)
        # 200 - success
        if not os.path.exists("/tmp/connection_checking.tmp") and TempClass.CONNECTION_STATUS_CODE != 1:
            try:
                TempClass.CONNECTION_STATUS_CODE = requests.get(TempClass.url_with_git).status_code
                open("/tmp/connection_checking.tmp", "w").write(str(TempClass.CONNECTION_STATUS_CODE))
                check_version()
            except:
                TempClass.CONNECTION_STATUS_CODE = 1
                open("/tmp/connection_checking.tmp", "w").write(str(TempClass.CONNECTION_STATUS_CODE))

        # print(TempClass.CONNECTION_STATUS_CODE)
    connection_check = threading.Thread(target=conn_check).start()
    
    if avaliableArguments[0][0] in argument and argument.index(argumets_index_search(["-h"])) != 1:
        # print(argument.index(argumets_index_search(["-h"])))
        for i in range(len(argument)):
            # print(str(i) + " | " + str(argument.index(argumets_index_search(["-h"]))))
            if "-" in argument[i] and i < int(argument.index(argumets_index_search(["-h"]))):    
                # print(argument[i])
                if avaliableArguments[2][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --get-license`\n[INFO]Use locally only! """, "information")
                if avaliableArguments[3][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --scenario-local test.scenario`\n[INFO]Run scenarios from local machine! """, "information")
                if avaliableArguments[4][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --scenario-remote test.scenario`\n[INFO]Run scenarios from server! """, "information")
                if avaliableArguments[5][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --get-scenarios`\n[INFO]Get list of all scenarios from server""", "information")
                if avaliableArguments[6][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --test`\n[INFO]Test function, nothing else""", "information")
                if avaliableArguments[7][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --scenario-description test.scenario`\n[INFO]Get scenario's description""", "information")
                if avaliableArguments[8][0] in argument[i]:
                    log("""\r[INFO]I dont know about this func""", "information")
                if avaliableArguments[9][0] in argument[i]:
                    log("""\n\r[INFO]Type this command -> `python machine-checker.py --get-configs`\n[INFO]Get list of all configs from server
                          \r\n[INFO]Example:
                          \r\ttest.file -> Install path: /tmp/test.file
                          \r\t[config file] -> Installation path:[full path]
                          \r\tThe rules are located on the server, in the config.manage file
                          """, "information")
                if avaliableArguments[10][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --set-camunda-path`\n[INFO]Set camunda path (local usage)""", "information")
                if avaliableArguments[11][0] in argument[i]:
                    log("""\n\r[INFO]Command for example -> `python machine-checker.py --install-config config.ini`\n[INFO]Install config by server rules.
                          \r[INFO]For example: Type `python machine-checker.py --get-configs`
                          """, "information")
                if avaliableArguments[12][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --get-chains`\n[INFO]Get list of all chains from server""", "information")
                if avaliableArguments[13][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --get-chains-full`\n[INFO]Get full info about chains from server""", "information")
                if avaliableArguments[14][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --run-chain [chain number or name here]`\n[INFO]Run configs chain""", "information")
                if avaliableArguments[15][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py ... --batch`\n[INFO]Automatic selection of preset answers (for example [Y/n] - choose Y)""", "information")
                if avaliableArguments[16][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --get-preset-cmd [chain number]`\n[INFO]Make cmd line with tags
                          \r Line example: `python machine-checker.py --run-chain 2  --tag "zookeeper_port=your_value" --tag "clickhouse_port=your_value" --tag "zookeeper_host=your_value" --tag "main_host=your_value" --tag "clickhouse_host=your_value"`""", "information")
                if avaliableArguments[16][1] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --get-preset-screen [chain number]`\n[INFO]Show all tags on sceen. Must be saved and filled in for use""", "information")
                if avaliableArguments[17][0] in argument[i]:
                    log("""\r[INFO]Type this command -> `python machine-checker.py --run-chain 2 --preset [path to preset.txt]`\n[INFO]About preset see -> `python machine-checker.py --get-preset-screen -h`""", "information")
                if avaliableArguments[18][0] in argument[i]:
                    log("""\r[INFO]Im lazy""", "information")
                if avaliableArguments[19][0] in argument[i]:
                    log("""\r[INFO]Clear temp logs from /tmp (local use only)""", "information")
                if avaliableArguments[20][0] in argument[i]:
                    log("""\r[INFO]Create requirements.txt for installation""", "information")
                if avaliableArguments[23][0] in argument[i]:
                    log("""\r[INFO]Function for creating scenarios.
                        \rAccepts two types of text documents, simple list of commands(ex1) or <id>,<instruction>,<command>(ex2).
                        \rExample 1:
                        \r\tyum install qwerty
                        \rExample 2:
                        \r\t0,Manual,yum install qwerty
                        """, "information")
                if avaliableArguments[24][0] in argument[i]:
                    log("""\r[INFO]Killing process""", "information")
        sys.exit()
    
    TempClass.arguments = avaliableArguments
    if avaliableArguments[18][0] in argument:
        try:
            for i in range(len(sys.argv)):
                if avaliableArguments[18][0] in sys.argv[i]:
                    # print([sys.argv[i+1].replace("\"", "").split("=")[0], sys.argv[i+1].replace("\"", "").split("=")[1]])
                    TempClass.tags.append([sys.argv[i+1].replace("\"", "").split("=")[0], sys.argv[i+1].replace("\"", "").split("=")[1]])
                    if "{host}=" in sys.argv[i+1]:
                        print(sys.argv[i+1])
                        TempClass.hosts.append(sys.argv[i+1].replace("\"", "").split("=")[1])
        except IndexError:
            log("Wrong command, wrong tag is possible", "error")
    if avaliableArguments[1][0] in argument or avaliableArguments[1][1] in argument:
        TempClass.GET_OUT = True
    TempClass.LOCALHOSTNAME = get_output(subprocess_check_output("hostname")).replace("\n", "").replace("\r", "")
    if avaliableArguments[15][0] in argument:
        TempClass.RUN_AUTO_MODE = True
    if avaliableArguments[17][0] in argument:
        TempClass.PRESET_PATH = sys.argv[argument.index(argumets_index_search(["--preset"])) + 1]
    if avaliableArguments[0][0] in argument:
        banner()
        sys.exit()
    if avaliableArguments[0][1] in argument:
        massive_scripts = []
        banner()
        listofScripts = get_list_of_files(directory="scenarios")
        for script in listofScripts:
            try:
                DESCRIPTION_FILENAME = script
                response = get_online_description_in_scenario()
                if response == "\n\n":
                    massive_scripts.append([script, "No description :("])
                else:
                    massive_scripts.append([script, response])
            except IndexError:
                massive_scripts.append([script, "[EXCEPTION] Wrong scenario format. Maybe missing <description> tag."])
            except Exception as this_exception:
                log(f"[EXCEPTION] {this_exception}", "except")
                sys.exit()
            except urllib3.exceptions.ProtocolError:
                pass
            except:
                log("Something went wrong!", "error")
                sys.exit()
        maxLenNameScript = 0
        maxLenDescription = 0
        for script in massive_scripts:
            if len(script[0]) > maxLenNameScript:
                maxLenNameScript = len(script[0])
            if len(script[1]) > maxLenDescription:
                for line in script[1].split("\n"):
                    if len(script[1]) > maxLenDescription:
                        maxLenDescription = len(line)       
                maxLenDescription = len(script[1])
        createScenarioAbout(massive_scripts, [maxLenNameScript, maxLenDescription])
        # print([maxLenNameScript, maxLenDescription])
        sys.exit(0)

    # get_scenario_run()
    if avaliableArguments[2][0] in argument:
        if (sys.platform == "linux"):
            log("Get license process start")
            get_license()
            sys.exit()
        else:
                log("System error, use linux to run command", "error") 
                sys.exit()
    if avaliableArguments[3][0] in argument:
        try:
            if (sys.platform == "linux"):
                SCENARIO_DIR = sys.argv[argument.index(argumets_index_search(["--scenario-local"])) + 1]
                if ".scenario" not in SCENARIO_DIR:
                    SCENARIO_DIR = SCENARIO_DIR + ".scenario"
                log("Start reading scenario")
                scenario_run()
            else:
                log("System error, use linux to run command", "error") 
                sys.exit()
        except IndexError:
            log("[--scenario-local] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()
    if avaliableArguments[4][0] in argument:
        try:
            SCENARIO_NAME = sys.argv[argument.index(argumets_index_search(["--scenario-remote"])) + 1]
            if ".scenario" not in SCENARIO_NAME:
                SCENARIO_NAME = SCENARIO_NAME + ".scenario"
            conn_check()
            get_scenario_run(SCENARIO_NAME)
            sys.exit()
        except IndexError:
            log("[--scenario-remote] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()
    if avaliableArguments[5][0] in argument:
        filesList = get_list_of_files(directory="scenarios")
        for file in filesList:
            print("-> " + file)
        sys.exit()
    if avaliableArguments[6][0] in argument:
        try:
            log("test")
            get_output("qwerty")
            get_output("Run run run")
            # get_output(subprocess_check_output("sudo rm -r /etc/clickhouse-server/"))
        except subprocess.CalledProcessError:
            pass
        # get_output(output)
        # test()
        # check_git()
        # checking_camunda_location()
    if avaliableArguments[7][0] in argument:
        try:
            threading.Thread(target=conn_check).start()
            DESCRIPTION_FILENAME = sys.argv[argument.index(argumets_index_search(["--scenario-description"])) + 1]
            print(get_online_description_in_scenario())
            sys.exit()
        except IndexError:
            log("[--scenario-description] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()
    if avaliableArguments[9][0] in argument:
        # checking_camunda_location()
        filesList = get_list_of_files(directory="configs")
        sys.exit()
    if avaliableArguments[10][0] in argument:
        if (sys.platform == "linux"):
            TempClass.CAMUNDA_LOCATION = input("Please, input path to camunda here -> ")
            open("/tmp/camunda_folder.tmp", "w").write(TempClass.CAMUNDA_LOCATION)
            print("Path to camunda -> " + TempClass.CAMUNDA_LOCATION)
            sys.exit()        
        else:
            log("System error, use linux to run command", "error") 
            sys.exit()        
    if avaliableArguments[11][0] in argument:
        try:
            if (sys.platform == "linux"):
            # checking_camunda_location()
                threading.Thread(target=conn_check).start()
                CONFIG_NAME = sys.argv[argument.index(argumets_index_search(["--install-config"])) + 1]
                log("Start downloading configuration")
                install_config()            
            else:
                log("System error, use linux to run command", "error")
                sys.exit()        
        except IndexError:
            log("[--install-config] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()
    if avaliableArguments[12][0] in argument or avaliableArguments[13][0] in argument:
        try:
            if avaliableArguments[13][0] in argument:
                sets_view(True)
            else:
                sets_view(False)
        except IndexError:
            log("[--get-chains] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
    if avaliableArguments[14][0] in argument:
        try:
            if (sys.platform == "linux"):
                conn_check()
                SET_INDEX = sys.argv[argument.index(argumets_index_search(["--run-chain"])) + 1]
                run_set(SET_INDEX)
            else:
                log("System error, use linux to run command", "error")
                sys.exit()        
        except IndexError:
            log("[--run-chain] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[16][0] in argument or avaliableArguments[16][1]in argument:
        try:
            mode = 0
            if avaliableArguments[16][0] in argument:
                mode = 0
            if avaliableArguments[16][0] in argument:
                mode = 1
            PRESET_SCENARIO = sys.argv[argument.index(argumets_index_search(["--get-preset-cmd", "--get-preset-screen"])) + 1]
            get_preset(PRESET_SCENARIO, mode)
        except IndexError:
            log("[--get-chains] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
    if avaliableArguments[19][0] in argument:
        try:
            if (sys.platform == "linux"):
                logs_clear()
            else:
                log("System error, use linux to run command", "error")
        except IndexError:
            log("[--clear-temp-logs] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[21][0] in argument:
        try:
            if (sys.platform == "linux"):
                update()
            else:
                log("System error, use linux to run command", "error")
        except IndexError:
            log("[--upgrade] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[22][0] in argument:
        try:
            if (sys.platform == "linux"):
                os.system("yes 2>/dev/null | rm -r /tmp/temp.py > /dev/null 2>&1")
                log("Software successfully updated!", "success")
                sys.exit()
            else:
                log("System error, use linux to run command", "error")
        except IndexError:
            log("[--installation-ending-deleting-temp] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[23][0] in argument:
        try:
            FILE_FULL_PATH = sys.argv[argument.index(argumets_index_search(["--import-file"])) + 1]
            import_file_for_generation(FILE_FULL_PATH)
            sys.exit()
        except IndexError:
            log("[--import-file] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[24][0] in argument:
        try:
            PROCCESS_NAME = sys.argv[argument.index(argumets_index_search(["--kill-process"])) + 1]
            killProcess(PROCCESS_NAME)
            sys.exit()
        except IndexError:
            log("[--kill-process] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[25][0] in argument:
        try:
            # MODULE_NAME = sys.argv[argument.index(argumets_index_search(["--modules"])) + 1]
            showModulesFromServer()
            sys.exit()
        except IndexError:
            log("[--modules] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[26][0] in argument:
        try:
            MODULE_NAME = sys.argv[argument.index(argumets_index_search(["--load-module"])) + 1]
            loadMOduleFromServer(MODULE_NAME)
            sys.exit()
        except IndexError:
            log("[--load-module] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
    if avaliableArguments[27][0] in argument:
        try:
            run_gui()
            sys.exit()
        except IndexError:
            log("[--gui] Something wrong with arguments!\nYou can see an example of the command in ['-h', '--help']", "warning")
            sys.exit()  
except (requests.exceptions.ConnectionError, urllib3.exceptions.ProtocolError):
    log("Cannot connect to server!", "error")
    sys.exit()
except KeyboardInterrupt:
    log("Exiting...", "out")
    sys.exit()
try:
    for j in range(len(sys.argv)):
        if sys.argv[j] not in TempClass.arguments and not sys.argv[0] :
            if "-" not in sys.argv[j] and "/" not in sys.argv[j]:
                print(sys.argv[j])
                log("Add [-h, --help] as argument for more information!", "information")
                connection_check.abort()
                sys.exit()
    if len(sys.argv) == 1:
        log("Add [-h, --help] as argument for more information!", "information")
        sys.exit()
except KeyboardInterrupt:
    log("Exiting...", "out")
    sys.exit(0)