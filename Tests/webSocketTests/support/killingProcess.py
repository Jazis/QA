import threading
import os
import subprocess
import time
import sys
def killingProcesses():
    class temp():
        precessWhat = [["1", "2", "3"]]
        procescCounter = 0
        
    start_time = time.time()
    print(start_time)
    if len(temp.precessWhat) == 2: 
        print("Exit")
        sys.exit()

    def func0(process):
        for i in range(len(temp.precessWhat)):
            if process.split()[1] in temp.precessWhat[i][0]:
                return True
        return False

    processListCount = 1
    processList = []
    while (len(processList) == 1):
        time.sleep(1)
        processList = []
        ps = subprocess.Popen(['ps', 'aux',], stdout=subprocess.PIPE).communicate()[0]
        processList = str(ps).split('\\n')

    while(processListCount == 1):
        processList = []
        ps = subprocess.Popen(['ps', 'aux',], stdout=subprocess.PIPE).communicate()[0]
        processList = str(ps).split('\\n')
        for process in processList:
            if "pytest" in process:
                if func0(process) == False:
                    temp.precessWhat.append([process.split()[1], process.split()[9], float(0)])
        if len(temp.precessWhat) == 1 : temp.procescCounter+=1
        if temp.procescCounter >= 60: return True 
        # print(temp.precessWhat, temp.procescCounter)
        for j in range(len(temp.precessWhat)):        
            if temp.precessWhat[j][2] == float(0):
                temp.precessWhat[j][2] = time.time()
            else: pass
        for i in range(len(temp.precessWhat)):
            try:
                if time.time() >= temp.precessWhat[i][2] + int(sys.argv[1]):
                    try:
                        # print(temp.precessWhat[i])
                        # print("kill -15 " + temp.precessWhat[i][0])
                        os.system("kill -15 " + temp.precessWhat[i][0] + " > /dev/null 2>&1")
                        # print(len(temp.precessWhat))
                        # print(temp.precessWhat)
                        if len(temp.precessWhat) == 2: 
                            # print("Exit")
                            return True
                        pass
                    except:
                        pass
                    temp.precessWhat.remove(temp.precessWhat[i])
                    processListCount = len(temp.precessWhat[i])
            except:
                pass
    endTime = time.time()
    # print(endTime)

start_time00 = time.time()
# print(sys.argv[1])

processList = []
while (len(processList) != 1):
    processList = []
    ps = subprocess.Popen(['ps', 'aux',], stdout=subprocess.PIPE).communicate()[0]
    processList = str(ps).split('\\n')
    killed = killingProcesses()
    if killed == True:
        print("Yaaaaaaay")
        endTime0 = time.time()
        break
    else:
        print("Another loop")