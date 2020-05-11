import grpc

import calc_pb2 as calc__pb2


class multipleStub(object):
    """interface
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.calcSend = channel.unary_unary(
                '/calc.multiple/calcSend',
                request_serializer=calc__pb2.SimpleRequest.SerializeToString,
                response_deserializer=calc__pb2.SimpleResponse.FromString,
                )


class multipleServicer(object):
    """interface
    """

    def calcSend(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_multipleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'calcSend': grpc.unary_unary_rpc_method_handler(
                    servicer.calcSend,
                    request_deserializer=calc__pb2.SimpleRequest.FromString,
                    response_serializer=calc__pb2.SimpleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calc.multiple', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class multiple(object):
    """interface
    """

    @staticmethod
    def calcSend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calc.multiple/calcSend',
            calc__pb2.SimpleRequest.SerializeToString,
            calc__pb2.SimpleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
