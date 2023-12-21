import requests
import schedule
import time
import json
import os



def Polling():
    response = requests.get(str(os.environ["SCRAPING"]), json= {"type": 0}).json()
    print(response)
    body = {"array" : response}
    requests.post(str(os.environ["DBADRESS"]), json=body)


schedule.every(3).minutes.do(Polling)

Polling()
while True:
    schedule.run_pending()
    time.sleep(1)
