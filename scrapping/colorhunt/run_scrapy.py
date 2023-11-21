#!/usr/bin/python
from colorhunt.spiders.sc import ScrapySpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

class Scrapper:
    def __init__(self):
        settings_file_path = 'colorhunt.settings' # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spiders = ScrapySpider # The spider you want to crawl

    def run_spiders(self):
        self.process.crawl(self.spiders, "-o out.json")
        self.process.start()  # the script will block here until the crawling is finished


sc = Scrapper()
sc.run_spiders()
