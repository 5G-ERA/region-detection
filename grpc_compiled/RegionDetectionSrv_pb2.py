# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RegionDetectionSrv.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18RegionDetectionSrv.proto\x12\tCameraSrv\"(\n\x14\x44\x65tectRegionsRequest\x12\x10\n\x08settings\x18\x01 \x01(\t\"9\n\x15\x44\x65tectRegionsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07payload\x18\x02 \x01(\t2k\n\x12RegionDetectionSrv\x12U\n\x10TryDetectRegions\x12\x1f.CameraSrv.DetectRegionsRequest\x1a .CameraSrv.DetectRegionsResponseB\x18\xaa\x02\x15HAL._5G_ERA.DataTypesb\x06proto3')

_DETECTREGIONSREQUEST = DESCRIPTOR.message_types_by_name['DetectRegionsRequest']
_DETECTREGIONSRESPONSE = DESCRIPTOR.message_types_by_name['DetectRegionsResponse']

DetectRegionsRequest = _reflection.GeneratedProtocolMessageType('DetectRegionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETECTREGIONSREQUEST,
  '__module__' : 'RegionDetectionSrv_pb2'
})

DetectRegionsResponse = _reflection.GeneratedProtocolMessageType('DetectRegionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DETECTREGIONSRESPONSE,
  '__module__' : 'RegionDetectionSrv_pb2'
})

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RegionDetectionSrv_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\025HAL._5G_ERA.DataTypes'
  _globals['_DETECTREGIONSREQUEST']._serialized_start=39
  _globals['_DETECTREGIONSREQUEST']._serialized_end=79
  _globals['_DETECTREGIONSRESPONSE']._serialized_start=81
  _globals['_DETECTREGIONSRESPONSE']._serialized_end=138
  _globals['_REGIONDETECTIONSRV']._serialized_start=140
  _globals['_REGIONDETECTIONSRV']._serialized_end=247
# @@protoc_insertion_point(module_scope)
