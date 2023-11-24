import requests
import schedule

schedule.every(3).hours.do(requests.get("http://127.0.0.1:5000/scraping/", params={"type":0}))

def Polling():
    pass