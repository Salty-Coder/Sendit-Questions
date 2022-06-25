import requests
import json
import time
from colorama import Fore, Style, init

init(convert=True)

file = open("responses.txt", "a+", encoding='utf-8')


times = int(input("Times to test: "))
cooldown = float(input("Cooldown: "))

if times < 1:
    print("Times must be greater than 0")
else:
    for i in range(times):
        #the required first parameter of the 'get' method is the 'url':
        x = requests.get('https://el-gibberado.getsendit.com/1.0/provider/ama')
        y = x.json()

        question = y["question"]

        if question in file:
            print(f"{Fore.RED}Question found in list, skipping...{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Question not found in list, adding to list...{Style.RESET_ALL}")
            file.write(question + "\n")

        time.sleep(cooldown)

file.close()
print(f"{Fore.YELLOW}Ending...")