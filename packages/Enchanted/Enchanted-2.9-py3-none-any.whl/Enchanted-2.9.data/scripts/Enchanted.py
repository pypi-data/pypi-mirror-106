import os,sys
import requests
import time
from time import time, sleep
import colorama
from colorama import *
import re
import asyncio
import datetime
import json
import aiohttp
import getpass
import warnings
import asyncio
import os
import time
import warnings
from datetime import datetime
from getpass import getpass
import aiohttp
import requests
from colorama import Fore
from importlib import *
import io
from colorama import init
import json
import subprocess
from bs4 import BeautifulSoup as bs
print("Use Ctrl + c to exit!")



def printRocket():
    sleep(1)
    os.system("cls")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(
f"""
{Fore.WHITE}
           _
          /^\\
          |-|
          |{Fore.RED}s{Fore.WHITE}|
          |{Fore.RED}n{Fore.WHITE}|
          |{Fore.RED}i{Fore.WHITE}|
          |{Fore.RED}p{Fore.WHITE}|
          |{Fore.RED}e{Fore.WHITE}|
         /|{Fore.RED}r{Fore.WHITE}|\\
        / | | \\
       |  | |  |
       `-\\"\\"\\"-`
     
""")
    
printRocket()
print("Launching Sniper...")
print("This sniper will auto update!")
sleep(2.5)
os.system("cls")
printRocket()
 
delay23 = 320
for i in range(40):
    print()
    sleep(delay23/2000)
    delay23 = delay23 * 0.9



try:  
    print("\u001b[0m")
    print("updateing...")
    sleep(0.4)
    os.system("pip uninstall Enchanted -y")

    os.system("pip install Enchanted")
    r = requests.get("https://og-sniper.jimdosite.com/downloads/")


    soup = bs(r.content, 'lxml')


    first = soup.find(["h2", "h2" ]).text


    print(first)




    #begin main code ds etc
    init(autoreset=True)
    os.system("cls")
    #begin prefix
    prefix = f"{Fore.WHITE}~ ({Fore.RED}Root{Fore.WHITE}@{Fore.MAGENTA}Enchanted) {Fore.WHITE}> "
    #end prefix
    #begin input prefix
    inputxd = f"{Fore.WHITE}~ ({Fore.RED}Root{Fore.WHITE}@{Fore.MAGENTA}Enchanted) {Fore.GREEN}Input {Fore.WHITE}> "
    #end input
    #begin info prefix
    info = f"{Fore.WHITE}~ ({Fore.RED}Root{Fore.WHITE}@{Fore.MAGENTA}Enchanted) \u001b[34;1mInfo  {Fore.WHITE}> "
    #end info
    warn = f"{Fore.WHITE}~ ({Fore.RED}Root{Fore.WHITE}@{Fore.MAGENTA}Enchanted) {Fore.RED}WARN! {Fore.WHITE}> "
    #begin bold message
    bold = "\u001b[1m"
    #end
    url = "https://discord.com/api/webhooks/842366281977167872/Be9ySAIRtSVyfWVbSJIY-ex8taBo3TY6xLakaP51h6qv-5tnzGFu6F3_hVVWknv4U4JH"
    #print the logo

        #\u001b[35m███████╗███╗   ██╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗████████╗███████╗██████╗     ██████╗ ██╗   ██╗
       # ██╔════╝████╗  ██║██╔════╝██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝
       # █████╗  ██╔██╗ ██║██║     ███████║███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝ 
       # ██╔══╝  ██║╚██╗██║██║     ██╔══██║██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║    ██╔═══╝   ╚██╔╝  
       # ███████╗██║ ╚████║╚██████╗██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝    ██║        ██║   
       # ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝     ╚═╝        ╚═╝  



    def logo():
        print(
        f"""
    \u001b[35m---------------------------------------------------------------------------------------------------------
    \u001b[35m███████╗███╗░░██╗░█████╗░██╗░░██╗░█████╗░███╗░░██╗████████╗███████╗██████╗░  ██████╗░██╗░░░██╗██████╗░██╗
    ██╔════╝████╗░██║██╔══██╗██║░░██║██╔══██╗████╗░██║╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝██╔══██╗██║           
    █████╗░░██╔██╗██║██║░░╚═╝███████║███████║██╔██╗██║░░░██║░░░█████╗░░██║░░██║  ██████╔╝░╚████╔╝░██████╔╝██║          
    ██╔══╝░░██║╚████║██║░░██╗██╔══██║██╔══██║██║╚████║░░░██║░░░██╔══╝░░██║░░██║  ██╔═══╝░░░╚██╔╝░░██╔═══╝░██║         
    ███████╗██║░╚███║╚█████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗██████╔╝  ██║░░░░░░░░██║░░░██║░░░░░██║          
    ╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝  
                                            \u001b[35m| {Fore.GREEN}Package on PyPi.org \u001b[35m|
                                     \u001b[35m| {Fore.GREEN}https://pypi.org/project/Enchanted/ \u001b[35m|
                                          \u001b[35m| {Fore.GREEN}Made by overnice.exe#4476 \u001b[35m|
                                         \u001b[35m| {Fore.GREEN}Discord serer boosters: {Fore.YELLOW}{first} \u001b[35m |
    \u001b[35m---------------------------------------------------------------------------------------------------------                                                                                                
    """
        )
    #logo print end
    #begin of kqzz api
    def api(username):
        try:
            statuscode = requests.get(f"https://api.kqzz.me/api/{username}")
            statuscode = statuscode.status_code
            droptimename = requests.get(f'https://api.kqzz.me/api/namemc/droptime/{username}').json()['droptime']
            print(droptimename)
        except:
            print(f"{warn} {Fore.RED}{bold}[{statuscode}] can't get droptime, api is down! (kqzz api)")
            sleep(1)
            print(f"{info}{Fore.GREEN} Connected to other api!")
    #end api

    def infolol():
        print(
    f"""\u001b[0m
\u001b[35m┏━(Message from Enchanted developers)
\u001b[35m┃
\u001b[35m┃ {Fore.WHITE}This is the \u001b[35mPyPi.org {Fore.WHITE}package 
\u001b[35m┃ {Fore.WHITE}want to install supplementary tools. Learn how:
\u001b[35m┃ {Fore.WHITE}(link soon!)
\u001b[35m┃
\u001b[35m┗━(Go to https://enchantedsniper.ga/ for more info)
    """    
        )



    #begin ds anouncement
    logo()
    infolol()
    username = input(f'{inputxd} Username : ')


    api(prefix + "" + username)
    print(f'{info} {bold}Continue ? (no for conection retry to kqzz api)')
    yesorno = input(f'{inputxd} {bold}({Fore.GREEN}YES{Fore.WHITE}/{Fore.RED}NO{Fore.WHITE}) : ')
    while True:
        if re.search("yes", yesorno):
            break
        if re.search("YES", yesorno):
            break
        if re.search("no", yesorno):
            for i in range(0 ,10):
                print(f"{info} retrying...")
                api(username)
                print(f"{warn} {Fore.RED}{bold}can't get droptime!")                                                                                                                     
            print(f"{info} Api is down! Sorry")                                                                                      
            sleep(3)
            break
        if re.search("NO", yesorno):
            for i in range(0 ,10):
                print(f"{info} retrying...")
                api(username) 
                print(f"{warn} {Fore.RED}{bold}can't get droptime!")                                                                                                                       
            print(f"{info} Api is down! Sorry")                                                                                      
            sleep(3)
            break
    link = "https://en.namemc.com/search?q=" + username

    print(f"{info} want a message in the Discord server to anounce that you are trying to snipe the name?")
    yesorno2 = input(f"{inputxd} (\u001b[32;1mYES\u001b[0m/\u001b[31;1mNO\u001b[0m) : ")

    if re.search("yes", yesorno2):
        discordusernames = input(f"{inputxd}Discord username (including the #): ")
        print(f"{Fore.GREEN}ok {Fore.BLUE}using " + "\u001b[1m" + discordusernames + "\u001b[0m")


        while True:
            sleep(0.5)
            message23 = f"**NEW recode SNIPE TRY : **\n**{discordusernames} is trying to snipe : **`{username}`**\n  - NameMC : <{link}> **\n ** - MC api : <https://mc-heads.net/minecraft/profile/{username}>**\n**Want to snipe `{username}`? use Enchanted Sniper today! go to <https://enchantedsniper.ga/> for more info ! **"
            r = requests.post(url, data={"content": message23})
            sleep(1)
            print("\u001b[1m\u001b[32;1mSend!")
            break
    if re.search("YES", yesorno2):
        discordusernames = input(f"{Fore.BLUE}Discord username (including the #): ")
        print(f"{Fore.GREEN}ok {Fore.BLUE}using " + "\u001b[1m" + discordusernames + "\u001b[0m")



        while True:
            sleep(0.5)
            message23 = f"**NEW recode SNIPE TRY : **\n**{discordusernames} is trying to snipe : **`{username}`**\n  - NameMC : <{link}> **\n ** - MC api : <https://mc-heads.net/minecraft/profile/{username}>**\n**Want to snipe `{username}`? use Enchanted Sniper today! go to <https://enchantedsniper.ga/> for more info ! **"
            r = requests.post(url, data={"content": message23})
            sleep(1)
            print("\u001b[1m\u001b[32;1mSend!")
            break
    if "no" in yesorno2:
        pass
    
    #some code of smart sniper xD but just better xD
    #end anouncement
    #main sniper
    end = []
    orgdel = 0
    global delay
    delay = 0
    global changeversion
    changeversion = ""
    global tuned_delay
    tuned_delay = None
    global success
    success=False

    reqnum = 3




    #get_config_data()


    def autonamemc(email, password  ):
        return
        


    def store(droptime: int, offset: int) -> None:                        # Dodgy timing script!
        print(offset, ": Delay Used")
        global reqnum
        if reqnum == 3:
            set = 1
        else:
            set=2
        stamp = end[set]
        datetime_time = datetime.fromtimestamp(droptime)
        finaldel = str(stamp - datetime_time).split(":")[2].split(".")

        print(finaldel)
        if int(finaldel[0]) != 0:
            changeversion = "inc"
            tuned_delay = 0

            print(
                f"""{Fore.LIGHTRED_EX}Cannot tune your delay, please sync your time\n
                using http://www.thinkman.com/dimension4/download.htm
                \nprogram will continue, if it fails again please restart after \n
                installing dimension4 and also set the delay to 0 for that{Fore.RESET}"""
            )

        else:
            change = finaldel[1]
            change3 = f"{change[0]}{change[1]}{change[2]}"
            if int(change[0]) == 0:
                changeversion = "dec"
                changeint = 100 - int(f"{change[1]}{change[2]}")
                print("Change Delay:", changeint)
            else:
                changeversion = "inc"
                changeint = int(change3) - 100
                print("Change Delay:", changeint)

            if changeversion == "dec":
                tuned_delay = int(offset) - int(changeint)
            if changeversion == "inc":
                tuned_delay = int(offset) + int(changeint)
            print(f"{Fore.CYAN}Delay:{Fore.RESET} {offset}  {Fore.LIGHTGREEN_EX}Tuned Delay:{Fore.RESET}  {tuned_delay}")


    async def send_request(s: aiohttp.ClientSession, bearer: str, name: str) -> None:
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + bearer
        }

        json = {"profileName": name}

        async with s.post(
                "https://api.minecraftservices.com/minecraft/profile",
                json=json,
                headers=headers
        ) as r:
            print(
                f"{Fore.LIGHTRED_EX if r.status != 200 else Fore.LIGHTGREEN_EX}Response received @ {datetime.now()}{Fore.RESET}"
                f"{Fore.LIGHTRED_EX if r.status != 200 else Fore.LIGHTGREEN_EX} with the status {r.status}{Fore.RESET}"
            )
            end.append(datetime.now())
            if await r.status()==200:
                success=True


    async def get_droptime(username: str, session: aiohttp.ClientSession) -> int:
        async with session.get(
                f"https://mojang-api.teun.lol/droptime/{username}"
        ) as r:
            try:
                r_json = await r.json()
                droptime = r_json["UNIX"]
                return droptime
            except:
                try:
                    prevOwner = input(
                        f'{Fore.CYAN}{info} What is the current username of the account that owned {username} before this?:   {Fore.RESET}')
                    r = requests.post('https://mojang-api.teun.lol/upload-droptime',
                                    json={'name': username, 'prevOwner': prevOwner})
                    print(r.text)
                    droptime = r.json()['UNIX']
                    return droptime
                except:
                    print(f"{Fore.LIGHTRED_EX}Droptime for name not found, make sure you entered the details into the feild correctly!{Fore.RESET}")

        # else:
        #     print(f"{Fore.LIGHTRED_EX}Droptime for name not found, Please check if name is still dropping{Fore.RESET}")
        #     time.sleep(2)
        #     input(f"{Fore.LIGHTRED_EX}Press Enter to exit: {Fore.RESET}")
        #     exit()


    async def snipe(target: str, offset: int, bearer_token: str) -> None:
        async with aiohttp.ClientSession() as session:
            droptime = await get_droptime(target, session) # find the droptime!
            offset = int(offset)
            print(offset)
            snipe_time = droptime - (offset / 1000)
            print("current time in unix format is: ",time.time())
            print("Calculating...")
            print(f"sniping {target} at {droptime} unix time")
            while time.time() < snipe_time:
                await asyncio.sleep(.001)
            coroutines = [
                send_request(session, bearer_token, target) for _ in range(6)
            ]
            await asyncio.gather(*coroutines)
            store(droptime, offset)






    async def send_mojang_request(s: aiohttp.ClientSession, bearer: str, name: str) -> None:
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + bearer
        }

        async with s.put(
                f"https://api.minecraftservices.com/minecraft/profile/name/{name}",
                headers=headers
        ) as r:
            print(
                f"{info}Response received @ {datetime.now()}"
                f" with the status {r.status}"
            )
            end.append(datetime.now())


    async def get_mojang_token(email: str, password: str) -> str:
        questions = []

        async with aiohttp.ClientSession() as session:
            authenticate_json = {"username": email, "password": password}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
                    "Content-Type": "application/json"}
            async with session.post("https://authserver.mojang.com/authenticate", json=authenticate_json,
                                    headers=headers) as r:
                # print(r.status)
                if r.status == 200:
                    resp_json = await r.json()
                    # print(resp_json)
                    auth = {"Authorization": "Bearer: " + resp_json["accessToken"]}
                    access_token = resp_json["accessToken"]
                    # print(f"{Fore.LIGHTGREEN_EX}Auth: {auth}\n\nAccess Token: {access_token}")
                else:
                    print(f"{Fore.LIGHTRED_EX}INVALID CREDENTIALS{Fore.RESET}")

            async with session.get("https://api.mojang.com/user/security/challenges", headers=auth) as r:
                answers = []
                if r.status < 300:
                    resp_json = await r.json()
                    if resp_json == []:
                        async with session.get("https://api.minecraftservices.com/minecraft/profile/namechange",
                                            headers={"Authorization": "Bearer " + access_token}) as nameChangeResponse:
                            ncjson = await nameChangeResponse.json()
                            print(ncjson)
                            try:
                                if ncjson["nameChangeAllowed"] is False:
                                    print(
                                        "Your Account is not"
                                        " eligible for a name change!"
                                    )
                                    exit()
                                else:
                                    print(f"{info}Logged into your account successfully!{Fore.RESET}")
                            except Exception:
                                print(f"{info} logged in correctly!")
                    else:
                        try:
                            for x in range(3):
                                ans = input(f"{inputxd} " + resp_json[x]["question"]["question"] + f" : ")
                                answers.append({"id": resp_json[x]["answer"]["id"], "answer": ans})
                        except IndexError:
                            print(f"{inputxd} Please provide answers to the security questions : {Fore.RESET}")
                            return
                        async with session.post("https://api.mojang.com/user/security/location", json=answers,
                                                headers=auth) as r:
                            if r.status < 300:
                                print(f"{info}{Fore.GREEN} Sucsess Logged in!{Fore.RESET}")
                            else:
                                print(f"{info}{Fore.RED} incorrect!{Fore.RESET}")
                                os.system("pause")
        return access_token


    async def mojang_snipe(target: str, offset: int, bearer_token: str) -> None:
        async with aiohttp.ClientSession() as session:
            droptime = await get_droptime(target, session)
            offset = int(offset)
            print(offset)
            snipe_time = droptime - (offset / 1000)
            print(f"{info} time : ")
            print(time.time())
            print(f"{info} sniping {target} at {droptime}")
            while time.time() < snipe_time:
                await asyncio.sleep(.001)
            coroutines = [
                send_mojang_request(session, bearer_token, target)
                for _ in range(3)
            ]
            await asyncio.gather(*coroutines)
            store(droptime, offset)




    async def gather_mojang_info() -> None:
        email = input(f"{inputxd} Account Email : ")
        password = getpass(f"{inputxd} Password : ")
        print(f"{info} Want to see your password?")
        passsee = input(f"{inputxd} (\u001b[32;1mYES\u001b[0m/\u001b[31;1mNO\u001b[0m) : ")
        if "yes" in passsee:

            print(f"{info} Your password : {Fore.GREEN}" + password)
        if "no" in passsee:
            pass
        else:
            pass
        token = await get_mojang_token(email, password)
        name = username
        delay = input(f"{inputxd} Delay for snipe:  ")
        tuned_delay = delay
        await mojang_snipe(name, delay, token)


    async def start() -> None:
        print(f"{info} options: 'm' for mojang account")
        mainset = input(f"{inputxd} type of account : ")
        if mainset == "m":

            reqnum = 3
            print(f"{info}{Fore.GREEN} Using Mojang Account!{Fore.RESET}")
            await gather_mojang_info()
            return
        else:
            print(f"{info}{Fore.RED} Error")
            exit()


    if __name__ == '__main__':
        try:
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(start())

        except Exception as e:
            print(e)
            print(f"{info}{Fore.LIGHTRED_EX} ERROR! {Fore.RESET}")


    #end main sniper
except KeyboardInterrupt:
    os.system("cls")
    print(f"{Fore.GREEN}{bold}Thx for using Enchanted Sniper :) {Fore.YELLOW}Bye!")
    print(f"{Fore.GREEN}{bold}be sure to join the discord{Fore.GREEN}: ")
    print(f"{Fore.BLUE}{bold}https://discord.gg/svNudNSFbU")
    print(f"{Fore.GREEN}{bold}The website: ")
    print(f"{Fore.BLUE}{bold}https://enchantedsniper.ga/")
    sleep(2)
    os.system("cls")
    exit()