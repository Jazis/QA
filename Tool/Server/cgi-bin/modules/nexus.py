import requests, time, sys, os

class temp():
    _files_counter = 0
    founded_packs = []
    wht = 0
    yes = ["yes", "y"]
    no = ["no", "n"]
    _packs = []
    folders_couter = 0
    headers = {
        "authority": "local-nexus-repo-link",
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "NX-ANTI-CSRF-TOKEN=0.09213723604687796",
        "dnt": "1",
        "nx-anti-csrf-token": "0.09213723604687796",
        "origin": "https://local-nexus-repo-link",
        "referer": "https://local-nexus-repo-link/",
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
try:
    def nexusMainAuth(session):
        data = {"action":"node_NodeAccess",
                "method":"nodes",
                "data":None,
                "type":"rpc",
                "tid":1
                }
        temp.cookies = session.post("https://local-nexus-repo-link/service/extdirect", json=data, headers=temp.headers).cookies.get_dict()
        data = {"action":"rapture_Security","method":"getPermissions","data":None,"type":"rpc","tid":2}
        session.post("https://local-nexus-repo-link/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies)
        data = { 'action':'coreui_Repository','method':'readReferences','data':[{ 'page':1,'start':0,'limit':25}],'type':'rpc','tid':3}
        session.post("https://local-nexus-repo-link/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies)
        return session

    def getAllRepos(session):
        repos = []
        data = {
            "action": "coreui_Repository",
            "method": "readReferences",
            "data": [
            {
                "page": 1,
                "start": 0,
                "limit": 1000
            }
            ],
            "type": "rpc",
            "tid": 3
        }
        response = session.post("https://local-nexus-repo-link/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies).text
        for i in range(len(str(response).split("\""))):
            if "url" in str(response).split("\"")[i] and "local-nexus-repo-link" in str(response).split("\"")[i+2]:
                url = str(response).split("\"")[i+2]
            if "repositoryName" in str(response).split("\"")[i]:
                repo = str(response).split("\"")[i+2]
                repos.append([repo, url])
                url, repo = "", ""
        return repos
        
    def downloadingPacks():
        print("Founded packs list")
        for elem in temp.founded_packs:
            print(f"[{elem[0]}] {elem[1]}")
        o = input("\rInput pack(s) num (1,2,3...) -> ")
        os.system("mkdir -p /tmp/_modules/packs")
        for i in range(len(o.split(","))):
            for pack in temp.founded_packs:
                if int(o.split(",")[i]) == pack[0]:
                    get = os.system(f"wget -P /tmp/_modules/packs/ {pack[2]}")
            
    def getPacks(session, repo, _id="/", _text="", _type=""):
        if temp.wht == 1: return
        try:
            repo_struct  = []
            folders = ["PyPI-3.8", "docker"]
            for folder in folders:
                if folder in repo:
                    return
            data = {
                "action": "coreui_Browse",
                "method": "read",
                "data": [
                    {
                    "repositoryName": repo,
                    "node": _id
                    }
                ],
                "type": "rpc",
                "tid": 5
                }
            try:
                response = session.post("https://local-nexus-repo-link/service/extdirect", json=data, headers=temp.headers, cookies=temp.cookies, timeout=60000).text
            except requests.exceptions.ConnectionError:
                print("Wrong connection!")
                return
            _id,_text,_type = "", "", ""
            for i in range(len(str(response).split("\""))):
                if "id" in str(response).split("\"")[i]:
                    _id = str(response).split("\"")[i+2]
                if "text" in str(response).split("\"")[i]:
                    _text = str(response).split("\"")[i+2]
                if "type" in str(response).split("\"")[i]:
                    _type  = str(response).split("\"")[i+2]
                    if _id != "" and _text != "":
                        repo_struct.append([_id,_text,_type])
                        if _type == "folder":
                            print("Checked folders -> " + str(temp.folders_couter), end = "\r")
                            temp.folders_couter += 1
                            time.sleep(0.01)
                            getPacks(session, repo, _id,_text,_type)
                        if ".rpm" in _text:
                            for pack in temp._packs:
                                if pack in _text:
                                    temp._files_counter += 1
                                    temp.founded_packs.append([temp._files_counter, _text, f"https://local-nexus-repo-link/repository/{repo}/{_id}"])
                                    # print(f"[{counter}]Repo -> " + repo)
                                    print(f"[{temp._files_counter}] Founded pack -> " + _text)
                                    # print("Link -> " + f"https://local-nexus-repo-link/repository/{repo}/{_id}")
                    _id,_text,_type = "", "", ""
        except:
            while True:
                o = input("\rWanna stop searching? [y/N] -> ")
                if o.lower() in temp.yes: 
                    temp.wht = 1
                    break
                elif o.lower() in temp.no or o == "":
                    temp.wht = 0
                    break
                else:
                    pass
            if temp.wht == 1: return
                

    def finding(_input):
        temp.wht = 0
        temp._packs = []
        for elem in _input.replace(_input.split(" ")[0] + " ", "").split(","):
            temp._packs.append(elem)
        session = requests.Session()
        session = nexusMainAuth(session)
        repos = getAllRepos(session)
        for repo in repos:
            packs = getPacks(session, repo[0])
        downloadingPacks()

    def template(inp):
        if "help" in inp.split(" ")[0]:
            print("""
    help         - this menu
    find <arg>   - finding packages by part of name
    download     - download package, use after find
    """)
        if "find" in inp.split(" ")[0]:
            finding(inp)
        if "download" in inp.split(" ")[0]:
            downloadingPacks()
        
    def run():
        while (True):
            inp = input("-> ")
            template(inp)


    def banner():
        print("""
    Nexus Module successfully loaded!
    """)
except: 
    print("Something went wrong!") 
    exit()

if __name__ == "__main__":
    try:
        banner()
        run()
    except:
        pass