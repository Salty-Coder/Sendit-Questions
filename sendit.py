import requests
import json
import time

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
            print("🔴Question found in list, skipping...")
        else:
            print("🟢Question not found in list, adding to list...")
            file.write(question + "\n")

        time.sleep(cooldown)


print("Ending...")