import sys
sys.path.append('protos')

import grpc
import calc_pb2
import calc_pb2_grpc


def send_num():
    with grpc.insecure_channel('localhost:8001') as channel:
        stub = calc_pb2_grpc.multipleStub(channel)
        num1=3
        num2=4
        response = stub.calcSend(calc_pb2.SimpleRequest(first=int(num1), second=int(num2)))

    print('Reply: ', response.result_num)

if __name__=="__main__":
    send_num()