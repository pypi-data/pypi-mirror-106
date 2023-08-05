# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk_tool_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import incoming_connection_complete_pb2 as incoming__connection__complete__pb2
from . import incoming_record_packet_push_pb2 as incoming__record__packet__push__pb2
from . import incoming_data_push_pb2 as incoming__data__push__pb2
from . import plugin_initialization_data_pb2 as plugin__initialization__data__pb2
from . import transport_pb2 as transport__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk_tool_service.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16sdk_tool_service.proto\x12\x03sdk\x1a\"incoming_connection_complete.proto\x1a!incoming_record_packet_push.proto\x1a\x18incoming_data_push.proto\x1a plugin_initialization_data.proto\x1a\x0ftransport.proto2\xaf\x03\n\x07SdkTool\x12@\n\x1f\x43onfirmSdkToolServiceConnection\x12\n.sdk.Empty\x1a\x11.sdk.ReturnStatus\x12G\n\x13InitializeSdkPlugin\x12\x1d.sdk.PluginInitializationData\x1a\x11.sdk.ReturnStatus\x12L\n\x18PushIncomingRecordPacket\x12\x1d.sdk.IncomingRecordPacketPush\x1a\x11.sdk.ReturnStatus\x12<\n\x10PushIncomingData\x12\x15.sdk.IncomingDataPush\x1a\x11.sdk.ReturnStatus\x12V\n NotifyIncomingConnectionComplete\x12\x1f.sdk.IncomingConnectionComplete\x1a\x11.sdk.ReturnStatus\x12\x35\n\x14NotifyPluginComplete\x12\n.sdk.Empty\x1a\x11.sdk.ReturnStatusb\x06proto3'
  ,
  dependencies=[incoming__connection__complete__pb2.DESCRIPTOR,incoming__record__packet__push__pb2.DESCRIPTOR,incoming__data__push__pb2.DESCRIPTOR,plugin__initialization__data__pb2.DESCRIPTOR,transport__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SDKTOOL = _descriptor.ServiceDescriptor(
  name='SdkTool',
  full_name='sdk.SdkTool',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=180,
  serialized_end=611,
  methods=[
  _descriptor.MethodDescriptor(
    name='ConfirmSdkToolServiceConnection',
    full_name='sdk.SdkTool.ConfirmSdkToolServiceConnection',
    index=0,
    containing_service=None,
    input_type=transport__pb2._EMPTY,
    output_type=transport__pb2._RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InitializeSdkPlugin',
    full_name='sdk.SdkTool.InitializeSdkPlugin',
    index=1,
    containing_service=None,
    input_type=plugin__initialization__data__pb2._PLUGININITIALIZATIONDATA,
    output_type=transport__pb2._RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PushIncomingRecordPacket',
    full_name='sdk.SdkTool.PushIncomingRecordPacket',
    index=2,
    containing_service=None,
    input_type=incoming__record__packet__push__pb2._INCOMINGRECORDPACKETPUSH,
    output_type=transport__pb2._RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PushIncomingData',
    full_name='sdk.SdkTool.PushIncomingData',
    index=3,
    containing_service=None,
    input_type=incoming__data__push__pb2._INCOMINGDATAPUSH,
    output_type=transport__pb2._RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotifyIncomingConnectionComplete',
    full_name='sdk.SdkTool.NotifyIncomingConnectionComplete',
    index=4,
    containing_service=None,
    input_type=incoming__connection__complete__pb2._INCOMINGCONNECTIONCOMPLETE,
    output_type=transport__pb2._RETURNSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotifyPluginComplete',
    full_name='sdk.SdkTool.NotifyPluginComplete',
    index=5,
    containing_service=None,
    input_type=transport__pb2._EMPTY,
    output_type=transport__pb2._RETURNSTATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SDKTOOL)

DESCRIPTOR.services_by_name['SdkTool'] = _SDKTOOL

# @@protoc_insertion_point(module_scope)
