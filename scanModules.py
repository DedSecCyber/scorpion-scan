import requests

def admin_scan(target):
    fname = "wordlist/admin.txt"
    with open(fname) as f:
        content = f.readlines()
    payloads = [x.strip() for x in content]
    url = target
    vuln = []
    for payload in payloads:
        payload = payload
        adminurl = url+payload
        r = requests.get(adminurl)
        print("[*]Starting Scanning")
        if payload.lower() in r.text.lower():
            print("[!]Admin Panel link: "+ url +payload)
            if(payload not in vuln):
                vuln.append(payload)
        else:
            print ("[*]Admin Page Not Found!") 

    print ("[*]Scanning Completed")


def sqli_scan(target):
    fname = "wordlist/sql.txt"
    with open(fname) as f:
        content = f.readlines()
    payloads = [x.strip() for x in content]
    url = target
    vuln = []
    for payload in payloads:
        payload = payload
        sqlurl = url+payload
        r = requests.get(sqlurl)
        if payload.lower() in r.text.lower():
            print("[!]SQLii vulnerable link: "+ url +payload)
            if(payload not in vuln):
                vuln.append(payload)
        else:
            print ("[*]Not vulnerable!") 

    print ("[*]Scanning Completed")


def xss_scan(target):
    fname = "wordlist/xsspyload.txt"
    with open(fname) as f:
        content = f.readlines()
    payloads = [x.strip() for x in content]
    url = target
    vuln = []
    for payload in payloads:
        payload = payload
        xssurl = url+payload
        r = requests.get(xssurl)
        if payload.lower() in r.text.lower():
            print("[!]XSS vulnerable link: " +url +payload)
            if(payload not in vuln):
                vuln.append(payload)
        else:
            print ("[*]Not vulnerable!")

    print ("[*]Scanning Completed")
    
