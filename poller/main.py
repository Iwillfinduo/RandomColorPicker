import requests
import schedule
import time
import json



def Polling():
    response = requests.get("http://127.0.0.1:6969/scraping/", json= {"type": 0}).json()
    print(response)
    body = {"array" : response}
    requests.post("http://127.0.0.1:4343/database/", json=body)


schedule.every(3).minutes.do(Polling)

Polling()
while True:
    schedule.run_pending()
    time.sleep(1)
