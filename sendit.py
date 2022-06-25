import requests
import json
import time
from colorama import Fore, Style, init

init(convert=True)

file = open("responses.txt", "a", encoding='utf-8')
fileR = open("responses.txt", encoding='utf-8')


times = int(input("Times to test: "))
cooldown = float(input("Cooldown: ") or 0)

if times < 1:
    print("Times must be greater than 0")
else:

    good = 0
    bad = 0
    total = 0

    for i in range(times):
        #the required first parameter of the 'get' method is the 'url':
        x = requests.get('https://el-gibberado.getsendit.com/1.0/provider/ama')
        y = x.json()

        question = y["question"]

        if question in fileR.read():
            print(f"{Fore.RED}Question found in list, skipping...{Style.RESET_ALL}")
            bad = bad + 1
        else:
            print(f"{Fore.GREEN}Question not found in list, adding to list...{Style.RESET_ALL}")
            file.write(question + "\n")
            good = good + 1
        total = total + 1
        time.sleep(cooldown)


print("\n")
print(f"{Fore.BLUE}{good} added to list\n{bad} already in list\n{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Ending...{Style.RESET_ALL}")
file.close()