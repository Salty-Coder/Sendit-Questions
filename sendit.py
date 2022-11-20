import requests
import json
import time
from colorama import Fore, Style, init
import os
import math

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

init(convert=True)

file = open("responses.txt", "a+", encoding='utf-8')
file.close()

cls()

def request():
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

        with open('responses.txt', 'r', encoding='utf-8') as file:
            responses = file.read().split('\n')

        def writeToFile():
            with open('responses.txt', 'w', encoding='utf-8') as f:
                for response in responses:
                    f.write(f"{response}\n")        

        try:
            for i in range(times):
            
                    try:
                        x = requests.get('https://el-gibberado.getsendit.com/1.0/provider/ama')
                        y = x.json()
                    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
                        print(f"{Fore.RED}Decoding the response has failed. Sendit server is likely down...{Style.RESET_ALL}")
                        return writeToFile()

                    question = y["question"]

                    if question in responses:
                        print(f"{Fore.RED}Question found in list, skipping...{Style.RESET_ALL}")
                        bad = bad + 1
                        tenbad = tenbad + 1
                    else:
                        print(f"{Fore.GREEN}Question not found in list, adding to list...{Style.RESET_ALL}")
                        responses.append(question)
                        good = good + 1
                        tengood = tengood + 1
                    total = total + 1

                    step = step + 1
                    if step == 10:
                        step = 0
                        quotient = tengood / 10
                        percent = quotient * 100
                        print(f"{math.floor(percent)}% of last 10 questions were new.\n{i+1}/{times} done.")
                        tengood = 0
                        tenbad = 0

                    #fileR.close()
                    time.sleep(cooldown)
        except KeyboardInterrupt:
            pass
        
        writeToFile()


    print("\n")
    print(f"{Fore.BLUE}{good} added to list\n{bad} already in list\n{Style.RESET_ALL}")
    percent = (good / total) * 100
    print(f"{math.floor(percent)}% were new")
    percent = (bad / total) * 100
    print(f"{math.floor(percent)}% were not new")
    print(f"{Fore.YELLOW}Ending...{Style.RESET_ALL}")
    file.close()


def sort():
    cls()
    with open("responses.txt", 'r', encoding="utf-8") as r:
        print("Sorting...")
        lines = r.readlines()
        lines.sort()
    cls()
    with open('responses_sorted.txt', 'w', encoding='utf-8') as f:
        print("Writing...")
        cls()
        length = len(lines)
        iteration = 0
        for line in lines:
            iteration = iteration + 1
            if iteration % 10 == 0:
                print(f"Writing... {iteration}/{length}")
                cls()
            if line != "" and line != " " and line != "\n":
                f.write(f"{line}") 
    print("Sorted!")    



print("1: Request Questions\n2: Sort Questions")
option = int(input("> "))
if option == 1: request()
elif option == 2: sort()
else: print("Invalid option")