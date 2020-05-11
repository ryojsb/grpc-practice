import os
from flask import Flask, render_template, request

app = Flask(__name__)
api = "自分が叩きたいAPI" # https://xxx

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        html = render_template("index.html", result="")
        return html
    elif request.method == "POST":
        num1 = int(request.form["first"])
        num2 = int(request.form["second"])
        res = num1 * num2
        html = render_template("index.html", result=res)
        return html
    

if __name__ == '__main__':
    app.run()