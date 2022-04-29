 
import ssl
import requests
from threading import active_count, Thread
from random import randint
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

r = requests.Session()
r.cookies.set_policy(BlockCookies())

def stats(item_id):
    while True:
        try: #this request is used to make views 
            with r.post(f"https://api.toutiao50.com/aweme/v1/aweme/stats/?channel=googleplay&device_type=SM-G9250&device_id={randint(1000000000000000000, 9999999999999999999)}&os_version=10&version_code=220400&app_name=musically_go&device_platform=android&aid=1340", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": "com.zhiliaoapp.musically.go/220400 (Linux; U; Android 10; en_US; SM-G9250; Build/MMB25K.G9250ZTU5DPC5; Cronet/TTNetVersion:5f9540e5 2021-05-20 QuicVersion:47555d5a 2020-10-15)"}, data=f"item_id={item_id}&play_delta=1", stream=True, verify=True) as response:
                if (response.json()["status_code"] == 0):
                    break
                else:
                    continue
        except:
            continue
    
if (__name__ == "__main__"):
#lol idiot skid
    item_id = str(input('''

██████╗░██╗░░░██╗░██████╗██╗░░██╗░█████╗░██████╗░░░░██╗░██╗░██████╗░░█████╗░░█████╗░░░███╗░░
██╔══██╗██║░░░██║██╔════╝██║░██╔╝██╔══██╗██╔══██╗██████████╗╚════██╗██╔══██╗██╔══██╗░████║░░
██████╔╝██║░░░██║╚█████╗░█████═╝░███████║██████╔╝╚═██╔═██╔═╝░█████╔╝╚██████║╚██████║██╔██║░░
██╔══██╗██║░░░██║░╚═══██╗██╔═██╗░██╔══██║██╔═══╝░██████████╗░╚═══██╗░╚═══██║░╚═══██║╚═╝██║░░
██║░░██║╚██████╔╝██████╔╝██║░╚██╗██║░░██║██║░░░░░╚██╔═██╔══╝██████╔╝░█████╔╝░█████╔╝███████╗
╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░╚═╝░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚══════╝
                                Pasted by: rUsKaP#3991
                                   
[?] Video Link >>> 
'''))

    if ("vm.tiktok.com" in item_id or "vt.tiktok.com" in item_id):
        item_id = r.head(item_id, stream=True, verify=False, allow_redirects=True).url.split("/")[5].split("?", 1)[0]
    else:
        item_id = item_id.split("/")[5].split("?", 1)[0]
    amount = int(input("[?] How many views do you want (0 = Infinite) >>> ")) #infinite stop at 6M views..
    print("")
    print("[i] Sending Views...") #sending skid views
    if (amount == 0):
        for _ in iter(int, 1):
            while True:
                if (active_count() <= 5000): #5000 views per seconds
                    Thread(target=(stats), args=(item_id,)).start()
                    break
    else:
        for _ in range(amount):
            while True:
                if (active_count() <= 5000):
                    Thread(target=(stats), args=(item_id,)).start()
                    break