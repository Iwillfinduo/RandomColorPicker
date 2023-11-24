from flask import Flask, render_template
import scrapy
import requests

app = Flask(__name__)

@app.route("/best")
def hello_world():
    response = requests.get("http://127.0.0.1:6060/database", params={"type":"like"})
    
    return render_template("index.html", first_color=response["first_color"],second_color = response["second_color"],
                           third_color=response["third_color"], fourth_color=response["fourth_color"], likes=response["likes"])

if __name__ == "__main__":
    app.run()