#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
# -*- encoding: utf-8 -*-
import cfscrape
import requests,sys
from .color import *
from imp import reload
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

UserAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
def check_haveibeenpwned(email):
    #from haveibeenpwnd API docs from https://haveibeenpwned.com/API/v2#BreachesForAccount
    url = "https://haveibeenpwned.com/api/v2/breachedaccount/"+str(email)
    req = requests.get(url, headers=UserAgent)
    if req.status_code==200:
        return req.json()
    else:
        return False

def grab_password(email):
    # No docs(Because no API), just found it by analyzing the network and told the admin :D
    url  = "https://ghostproject.fr/search.php"
    data = {"param":email}
    scraper = cfscrape.create_scraper()
    req = scraper.post(url,headers=UserAgent,data=data)
    result = req.text.split("\\n")
    if "Error" in req.text or len(result)==2:
        return False
    else:
        return result[1:-1]

def parse_data(email,np):
    data = check_haveibeenpwned(email)
    if not data:
        error("No leaks found in Haveibeenpwned website!")
    else:
        status("Haveibeenpwned website results: "+Y+str(len(data)))
        form  = "Name : {web} | Date : {date} | What leaked : {details}"
        for website in data:
            line = form.format(web=M+website["Name"]+B,date=M+website["AddedDate"]+B,details=M+",".join(website["DataClasses"])+B)
            status(B+line)
        if not np:
            p = grab_password(email)
            if p:
                status("Plaintext password(s) found!")
                
                try:
                    for pp in p:
                        print (C+" │"+B+"  └──── "+W+pp.split(":")[1])
                        print (C+" (hash)" if len(pp.split(":")[1])==32 else C+" (cleartext)" )
                    
                except ValueError as e:
                    print("An error occurred, details: ",e)
            else:
                error("Didn't find any plaintext password published!")