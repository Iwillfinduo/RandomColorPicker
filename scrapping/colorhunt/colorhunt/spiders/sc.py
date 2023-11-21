import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
import json


class ScrapySpider(scrapy.Spider):
    name = "scrapy"
    def start_requests(self):
        yield scrapy.Request('https://colorhunt.co/', meta={'playwright':True})
    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        mydivs = soup.find_all("div", class_="feed global")
        items = mydivs[0].find_all("div", class_="item")
        out = []
        for item in items:
            out.append({"first_color": item.find("div", class_="place c3").find("span").text,
                   "second_color": item.find("div", class_="place c2").find("span").text,
                   "third_color": item.find("div", class_="place c1").find("span").text,
                   "fourth_color": item.find("div", class_="place c0").find("span").text,
                   "likes" : item.find("div", class_="button like").find("span").text})
            yield
        with open("file.json", "w") as f:
            json.dump(out, f)
        
        
                
        