# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: incoming_connection_complete.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='incoming_connection_complete.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\"incoming_connection_complete.proto\x12\x03sdk\"J\n\x1aIncomingConnectionComplete\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\tb\x06proto3'
)




_INCOMINGCONNECTIONCOMPLETE = _descriptor.Descriptor(
  name='IncomingConnectionComplete',
  full_name='sdk.IncomingConnectionComplete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.IncomingConnectionComplete.anchor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_name', full_name='sdk.IncomingConnectionComplete.connection_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['IncomingConnectionComplete'] = _INCOMINGCONNECTIONCOMPLETE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncomingConnectionComplete = _reflection.GeneratedProtocolMessageType('IncomingConnectionComplete', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGCONNECTIONCOMPLETE,
  '__module__' : 'incoming_connection_complete_pb2'
  # @@protoc_insertion_point(class_scope:sdk.IncomingConnectionComplete)
  })
_sym_db.RegisterMessage(IncomingConnectionComplete)


# @@protoc_insertion_point(module_scope)
