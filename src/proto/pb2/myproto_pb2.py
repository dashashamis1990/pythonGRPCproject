# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: myproto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmyproto.proto\x12\nmy_service\"L\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1c\n\x0fnumber_of_times\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x12\n\x10_number_of_times\"\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\x93\x01\n\x13MyServiceController\x12\x37\n\x08SayHello\x12\x13.my_service.Request\x1a\x14.my_service.Response\"\x00\x12\x43\n\x10ProcessMessaging\x12\x13.my_service.Request\x1a\x14.my_service.Response\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'myproto_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=29
  _globals['_REQUEST']._serialized_end=105
  _globals['_RESPONSE']._serialized_start=107
  _globals['_RESPONSE']._serialized_end=133
  _globals['_MYSERVICECONTROLLER']._serialized_start=136
  _globals['_MYSERVICECONTROLLER']._serialized_end=283
# @@protoc_insertion_point(module_scope)
