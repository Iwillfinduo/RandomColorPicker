from flask import Flask
from flask_restful import Api
from flask_restful import Resource, reqparse
#from colorhunt.run_scrapy import Scrapper
import os
import json
import subprocess

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('type', type = str)

class Scraping(Resource):
    def get(self):
        args = parser.parse_args()
        if int(args['type']) == 0:   
            #full_path = os.path.abspath(__file__) + "/colorhunt/run_scrapy.py"
            #subprocess.call(["cd", "colorhunt"])
            subprocess.call(["python3", "colorhunt/run_scrapy.py"])
            return_dict = dict()
            with open("file.json", 'r') as f:
                return_dict = json.load(f)
            return return_dict[-len(return_dict)+1:] , 200
api.add_resource(Scraping, "/scraping/")

if __name__ == "__main__":
    app.run(port=6969, host="0.0.0.0")