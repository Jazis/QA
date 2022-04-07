import os,sys,threading,time,subprocess
class colors:
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

try:
    class temp():
        monFiles = 0   
        _exit = 0  
        _isSnmpwalkInstalled = 0
        _list = [
            ["/var/log/", 1],
            ["/usr/local/lanlot/var/lanlot-logs/", 1],
            ["/home/bob/Documents/GITHUB/machine-checker-stock/machine-checker/MachineUtil/modules/0/", 0]
        ] 

    def mon(_dir):
        prevLine = "" 
        try:
            while(True):
                if temp._exit == 1:
                    sys.exit(0)
                lastline = subprocess.check_output(f"tail -n1 {_dir}", shell=True, encoding="WINDOWS-1251")
                if prevLine != lastline:   
                    prevLine = lastline
                    print("\033[38;5;214m[" + _dir + "]\033[00m" + lastline.replace("\n", ""))
                    time.sleep(0.1)
                    print(f"Monitoring files: {temp.monFiles} | Reload file: {_dir}",end="\r")    
        except KeyboardInterrupt:
            temp._exit = 1
        except (PermissionError, subprocess.CalledProcessError):
            print("Permission Error")
            sys.exit(0) 
        
    def runMonitor(dirs):
        for _dir in dirs:
            try:
                threading.Thread(target=mon, args=(_dir,)).start()
            except KeyboardInterrupt:
                temp._exit = 1

    def snmpMonitor(_version, _communityName, _ip): 
        lines = []
        while (True):
            _output = subprocess.check_output(f"snmpwalk -v{_version} -c {_communityName} {_ip}", shell=True, encoding="WINDOWS-1251")
            for line in _output.splitlines():
                if line not in lines:
                    if "INTEGER" in line:
                        continue
                    if "Counter32" in line or "Counter64" in line:
                        continue
                    if "STRING" in line:
                        print("\033[38;5;214m[" + line.replace("\n", "") + "]\033[00m")
                    else:
                        print(line.replace("\n", ""))
                    lines.append(line)
                    if len(lines) == 20000:
                        lines = []
                     
    def template(inp):
        if "help" in inp.split(" ")[0]:
            print("""
                help                            - this menu
                paths                           - Show paths list
                disable                         - disable monitoring path
                enable                          - enable monitoring path""")
            if temp._isSnmpwalkInstalled == 1:
                print("                snmp <version> <comName> <ip>   - monitor snmp")
        pathCounter = 0
        if "paths" in inp.split(" ")[0]:
            for _path in temp._list:
                if _path[1] == 0:
                    print(colors.red(f"[PATH {pathCounter}] " + _path[0])) 
                if _path[1] == 1:
                    print(colors.green(f"[PATH {pathCounter}] " + _path[0])) 
                pathCounter += 1
        if "disable" in inp.split(" ")[0]:
            path = inp.split(" ")[1]
            if path.isdigit():  
                temp._list[int(path)][1] = 0                  
            else:
                for i in range(len(temp._list)):
                    # print(temp._list[i][1] , path)
                    if temp._list[i][0] in path:
                        temp._list[i][1] = 0
                
        if "enable" in inp.split(" ")[0]:
            path = inp.split(" ")[1]
            if path.isdigit():  
                temp._list[int(path)][1] = 1
            else:        
                for i in range(len(temp._list)):
                    print(temp._list[i][1] , path)
                    if temp._list[i][0] in path:
                        temp._list[i][1] = 1
                        
        if "snmp" in inp.split(" ")[0]:
            version = inp.split(" ")[1]
            comLine = inp.split(" ")[2]
            _ip = inp.split(" ")[3]
            snmpMonitor(version, comLine, _ip)
                        
        if "run" in inp.split(" ")[0]:
            paths = temp._list
            allDirs = []
            _count = 0
            for path in paths:
                count =+ 1
                if path[1] == 0:
                    continue
                for file in os.listdir(path[0]):
                    if file[-4::] == ".log":
                        allDirs.append(path[0] + file)
                        temp.monFiles += 1
                        print(path[0] + file)
            runMonitor(allDirs)
            
    def run():
        _snmpwalkOutput = str(subprocess.check_output(f"ls /usr/bin/ | grep snmpwalk", shell=True, encoding="WINDOWS-1251")).replace("\n", "").replace("\r", "")
        # print(_snmpwalkOutput)
        if "snmpwalk" in _snmpwalkOutput:
            temp._isSnmpwalkInstalled = 1
        while (True):
            inp = input("-> ")
            template(inp)

    if __name__=="__main__":
        run()
except KeyboardInterrupt:
    temp._exit = 1