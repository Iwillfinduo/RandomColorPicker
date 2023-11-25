from flask import Flask, render_template
import scrapy
import requests
import json

app = Flask(__name__)

@app.route("/best")
def best():
    response = requests.get("http://127.0.0.1:4343/database", json={"type":"like"}).json()
    
    return render_template("best.html", first_color=response["fourth_color"],second_color = response["third_color"],
                           third_color=response["second_color"], fourth_color=response["first_color"], likes=response["likes"])

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/last")
def last():
    response = requests.get("http://127.0.0.1:4343/database", json={"type":"time"}).json()
    
    return render_template("last.html", first_color=response["fourth_color"],second_color = response["third_color"],
                           third_color=response["second_color"], fourth_color=response["first_color"], likes=response["likes"])
    

if __name__ == "__main__":
    app.run(port=5001)