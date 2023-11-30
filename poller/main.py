import requests
import schedule
import time
import json



def Polling():
    response = requests.get("http://localhost:6969/scraping/", json= {"type": 0}).json()
    print(response)
    body = {"array" : response}
    requests.post("http://localhost:4343/database/", json=body)


schedule.every(3).minutes.do(Polling)

time.sleep(60)
Polling()
while True:
    schedule.run_pending()
    time.sleep(1)
