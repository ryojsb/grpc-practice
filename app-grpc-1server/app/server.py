import os
from concurrent import futures
import sys
sys.path.append('app/protos')

import grpc
import calc_pb2
import calc_pb2_grpc

class multipleServicer(calc_pb2_grpc.multipleServicer): #service名+Servicerを書く
    def __init__(self):
        pass

    def calcSend(self, request, context):
        res = request.first * request.second
        return calc_pb2.SimpleResponse(result_num = res)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_multipleServicer_to_server(multipleServicer(), server)
    server.add_insecure_port('localhost:8001')
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    main()