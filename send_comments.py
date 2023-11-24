import os
import httpx
from bs4 import BeautifulSoup 
red = "\033[1;91m"
grenn = "\033[1;92m"
yellow = "\033[1;93m"
blue = "\033[1;94m"
blues = "\033[1;96m"
def clear():
    os.system('clear')
def logo():
    clear()
    print(f'''{red} ┌─────────────────────────────────────────┐
 │ {blue}[✓]DEVELOPER{yellow} :{grenn} Mohamed Bougrina{blues} !{red}       │
 │ {blue}[✓]TOOL   {yellow}   : {grenn}Face-Comments    {blues} !{red}      │
 │ {blue}[✓]STATUS  {yellow}  :{grenn} FREE{blues} ! {red}                  │
 │ {blue}[✓]GITHUB  {yellow}  : {grenn}Mohamedbougrina123 {blues}!{red}     │
 │ {blue}[✓]FACEBOOK {yellow} :{grenn} Mohamed Bougrina {blues}!{red}       │
 └─────────────────────────────────────────┘''')
def start():
    logo()
    print(f"{grenn}×"*44)
    url = input(f"{red}---|{grenn}Enter Url Post{red}: {blues}")
    cookie = input(f"{red}---|{grenn}Enter Cookies{red}: {blues}")
    comments  = input(f"{red}---|{grenn}Enter Comments{red}: {blues}")
    headers = {
        "Host": "m.facebook.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "Origin": "https://m.facebook.com",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "x-requested-with": "com.dv.adm",
        "Referer": "https://m.facebook.com/",
        "Accept-Language": "ar-MA,ar;q=0.9,en-MA;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cookie": cookie
    }
    num = int(0)
    for x in range(5000):
            try:
                url = url.replace("https://www.facebook.com/", "https://free.facebook.com/")
                html = httpx.get(url=url, headers=headers).text
                soup = BeautifulSoup(html, "html.parser")
                form = soup.find("form")
                submit = form.get("action")
                data_json = {}
                for inputs in form.find_all("input"):
                     if inputs.get("name"):
                         data_json[inputs.get("name")]=inputs.get("value", "")
                         data_json['comment_text'] = comments
                         response = httpx.post("https://free.facebook.com"+submit, data=data_json, headers=headers)
                         num+=1
                         print(f"{blues}Code Request:{red}",response,f"{grenn}Send comments number :{red}",num)
            except Exception as e:
                print(str(e))                     
start()    