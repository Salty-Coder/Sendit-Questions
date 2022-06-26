import requests
import json
import time
from colorama import Fore, Style, init
import os
import math

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

init(convert=True)

file = open("responses.txt", "a", encoding='utf-8')

cls()

times = int(input("Times to test: "))
cooldown = float(input("Cooldown: ") or 0)

if times < 1:
    print("Times must be greater than 0")
else:
    print("\n")
    good = 0
    bad = 0
    total = 0

    tengood = 0
    tenbad = 0
    step = 0

    for i in range(times):

        fileR = open("responses.txt", encoding='utf-8')

        #the required first parameter of the 'get' method is the 'url':
        x = requests.get('https://el-gibberado.getsendit.com/1.0/provider/ama')
        y = x.json()

        question = y["question"]

        if question in fileR.read():
            print(f"{Fore.RED}Question found in list, skipping...{Style.RESET_ALL}")
            bad = bad + 1
            tenbad = tenbad + 1
        else:
            print(f"{Fore.GREEN}Question not found in list, adding to list...{Style.RESET_ALL}")
            file.write(question + "\n")
            good = good + 1
            tengood = tengood + 1
        total = total + 1

        step = step + 1
        if step == 10:
            step = 0
            quotient = tengood / 10
            percent = quotient * 100
            print(f"{math.floor(percent)}% of last 10 questions were new")
            tengood = 0
            tenbad = 0

        time.sleep(cooldown)


print("\n")
print(f"{Fore.BLUE}{good} added to list\n{bad} already in list\n{Style.RESET_ALL}")
percent = (good / total) * 100
print(f"{math.floor(percent)}% were new")
percent = (bad / total) * 100
print(f"{math.floor(percent)}% were not new")
print(f"{Fore.YELLOW}Ending...{Style.RESET_ALL}")
file.close()