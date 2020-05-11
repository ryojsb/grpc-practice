import os
from flask import Flask, render_template, request
from concurrent import futures

import sys
sys.path.append('app/protos')

import grpc
import calc_pb2
import calc_pb2_grpc

app = Flask(__name__)

def send_num(num1, num2):
    with grpc.insecure_channel('localhost:8001') as channel:
        stub = calc_pb2_grpc.multipleStub(channel)
        response = stub.calcSend(calc_pb2.SimpleRequest(first=int(num1), second=int(num2)))
    return response.result_num


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        html = render_template("index.html", result="")
        return html
    elif request.method == "POST":
        num1 = int(request.form["first"])
        num2 = int(request.form["second"])
        
        res = send_num(num1, num2)

        html = render_template("index.html", result=res)
        return html
    

if __name__ == '__main__':
    app.run()
