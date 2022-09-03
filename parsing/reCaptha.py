import requests
from data.cfg import *


def cap():
    req = requests.get(f"http://rucaptcha.com/in.php?key={rucaptcha_key}&method=userrecaptcha&googlekey={site_key}&pageurl={url}")
    res = req.text.replace("OK|", "")
    return res



def check_cap(res):
    res_req = requests.get(f"http://rucaptcha.com/res.php?key={rucaptcha_key}&action=get&id={res}")
    return res_req.text.replace("OK|", "")


def hcap():
    req = requests.get(f"http://rucaptcha.com/in.php?key={rucaptcha_key}&method=hcaptcha&sitekey={hsite_key}&pageurl={url}")
    res = req.text.replace("OK|", "")
    return res

def hcheck_cap(res):
    res_req = requests.get(f"http://rucaptcha.com/res.php?key={rucaptcha_key}&action=get&id={res}")
    return res_req.text.replace("OK|", "")