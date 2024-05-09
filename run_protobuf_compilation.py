
"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""
from grpc_tools import protoc

protoc.main((
    '',
    '-Iproto', #This is the location of the .proto files
    '--python_out=./grpc_compiled', #This is where the *_pb2.py files are generated
    '--grpc_python_out=./grpc_compiled', #This is where the *_pb2_grpc.py files are generated
    'proto/CameraSrv.proto'
))