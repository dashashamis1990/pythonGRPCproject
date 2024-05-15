from datetime import datetime

import grpc

from src.proto.pb2 import myproto_pb2_grpc, myproto_pb2


def trigger_message_printing(request_body):
    message = request_body.message
    number_of_times = request_body.number_of_times
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        client_stub = myproto_pb2_grpc.MyServiceControllerStub(channel)
        request = myproto_pb2.Request(message=message, number_of_times=number_of_times)
        response = client_stub.SayHello(request)
        status = response.status
    return status


def trigger_messaging(request_body):
    status = True
    message = request_body.message
    number_of_times = request_body.number_of_times
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        client_stub = myproto_pb2_grpc.MyServiceControllerStub(channel)
        responses = client_stub.ProcessMessaging(generate_requests(message, number_of_times))
        for response in responses:
            print(f"{datetime.now()}: Received response with status: ", response.status)
            if not response.status:
                status = response.status
    return status


def generate_requests(message, number_of_times):
    for i in range(1, number_of_times+1):
        yield myproto_pb2.Request(message=f"{message} - {i}")
