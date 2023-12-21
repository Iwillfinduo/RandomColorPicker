from flask import Flask, render_template
import requests
import json
import os

app = Flask(__name__)

@app.route("/best")
def best():
    try:
        response = requests.get(str(os.environ["DBADRESS"]), json={"type":"like"}).json()
        print(response)
        if response == None:
            return render_template("db_empty.html")
        
        return render_template("best.html", first_color=response["fourth_color"],second_color = response["third_color"],
                            third_color=response["second_color"], fourth_color=response["first_color"], likes=response["likes"])
    except:
        return render_template("db_empty.html")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/last")
def last():
    try:
        response = requests.get(str(os.environ["DBADRESS"]), json={"type":"time"}).json()
        print(response)
        if response == None:
            return render_template("db_empty.html")
        
        return render_template("last.html", first_color=response["fourth_color"],second_color = response["third_color"],
                            third_color=response["second_color"], fourth_color=response["first_color"], likes=response["likes"])
    except:
        return render_template("db_empty.html")
    

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")