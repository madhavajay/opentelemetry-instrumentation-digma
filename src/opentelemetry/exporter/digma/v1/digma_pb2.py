# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/exporter/digma/v1/digma.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
from opentelemetry.proto.trace.v1 import trace_pb2 as opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2
from opentelemetry.proto.resource.v1 import resource_pb2 as opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='opentelemetry/exporter/digma/v1/digma.proto',
  package='opentelemetry.proto.digma.v1',
  syntax='proto3',
  serialized_options=b'\n\037io.opentelemetry.proto.digma.v1B\nDigmaProtoP\001\252\002\017digma_collector',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+opentelemetry/exporter/digma/v1/digma.proto\x12\x1copentelemetry.proto.digma.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a(opentelemetry/proto/trace/v1/trace.proto\x1a.opentelemetry/proto/resource/v1/resource.proto\"a\n\nErrorFrame\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x13\n\x0bmodule_path\x18\x02 \x01(\t\x12\x14\n\x0c\x65xcuted_code\x18\x03 \x01(\t\x12\x13\n\x0bline_number\x18\x04 \x01(\x05\"\xb3\x01\n\nErrorEvent\x12\x38\n\x06\x66rames\x18\x01 \x03(\x0b\x32(.opentelemetry.proto.digma.v1.ErrorFrame\x12\x19\n\x11\x65xception_message\x18\x02 \x01(\t\x12\x16\n\x0e\x65xception_type\x18\x03 \x01(\t\x12\x17\n\x0f\x65xception_stack\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\"\xe8\x02\n\rExportRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x02 \x01(\t\x12\x11\n\tcommit_id\x18\x03 \x01(\t\x12\x1c\n\x14programming_language\x18\x04 \x01(\t\x12J\n\x05spans\x18\x05 \x03(\x0b\x32;.opentelemetry.proto.digma.v1.ExportRequest.SpanInformation\x1a\xae\x01\n\x0fSpanInformation\x12\x0f\n\x07span_id\x18\x01 \x01(\t\x12\x10\n\x08trace_id\x18\x02 \x01(\t\x12\x38\n\x06\x65vents\x18\x03 \x03(\x0b\x32(.opentelemetry.proto.trace.v1.Span.Event\x12>\n\x0c\x65rror_events\x18\x04 \x03(\x0b\x32(.opentelemetry.proto.digma.v1.ErrorEvent\"!\n\x0e\x45xportResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2u\n\x0e\x44igmaCollector\x12\x63\n\x06\x45xport\x12+.opentelemetry.proto.digma.v1.ExportRequest\x1a,.opentelemetry.proto.digma.v1.ExportResponseBA\n\x1fio.opentelemetry.proto.digma.v1B\nDigmaProtoP\x01\xaa\x02\x0f\x64igma_collectorb\x06proto3'
  ,
  dependencies=[opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2.DESCRIPTOR,opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2.DESCRIPTOR,opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2.DESCRIPTOR,])




_ERRORFRAME = _descriptor.Descriptor(
  name='ErrorFrame',
  full_name='opentelemetry.proto.digma.v1.ErrorFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_name', full_name='opentelemetry.proto.digma.v1.ErrorFrame.module_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_path', full_name='opentelemetry.proto.digma.v1.ErrorFrame.module_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='excuted_code', full_name='opentelemetry.proto.digma.v1.ErrorFrame.excuted_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line_number', full_name='opentelemetry.proto.digma.v1.ErrorFrame.line_number', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=211,
  serialized_end=308,
)


_ERROREVENT = _descriptor.Descriptor(
  name='ErrorEvent',
  full_name='opentelemetry.proto.digma.v1.ErrorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frames', full_name='opentelemetry.proto.digma.v1.ErrorEvent.frames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_message', full_name='opentelemetry.proto.digma.v1.ErrorEvent.exception_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_type', full_name='opentelemetry.proto.digma.v1.ErrorEvent.exception_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_stack', full_name='opentelemetry.proto.digma.v1.ErrorEvent.exception_stack', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='opentelemetry.proto.digma.v1.ErrorEvent.timestamp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='opentelemetry.proto.digma.v1.ErrorEvent.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=311,
  serialized_end=490,
)


_EXPORTREQUEST_SPANINFORMATION = _descriptor.Descriptor(
  name='SpanInformation',
  full_name='opentelemetry.proto.digma.v1.ExportRequest.SpanInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='span_id', full_name='opentelemetry.proto.digma.v1.ExportRequest.SpanInformation.span_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='opentelemetry.proto.digma.v1.ExportRequest.SpanInformation.trace_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='opentelemetry.proto.digma.v1.ExportRequest.SpanInformation.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_events', full_name='opentelemetry.proto.digma.v1.ExportRequest.SpanInformation.error_events', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=679,
  serialized_end=853,
)

_EXPORTREQUEST = _descriptor.Descriptor(
  name='ExportRequest',
  full_name='opentelemetry.proto.digma.v1.ExportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='opentelemetry.proto.digma.v1.ExportRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment', full_name='opentelemetry.proto.digma.v1.ExportRequest.environment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commit_id', full_name='opentelemetry.proto.digma.v1.ExportRequest.commit_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='programming_language', full_name='opentelemetry.proto.digma.v1.ExportRequest.programming_language', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spans', full_name='opentelemetry.proto.digma.v1.ExportRequest.spans', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXPORTREQUEST_SPANINFORMATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=853,
)


_EXPORTRESPONSE = _descriptor.Descriptor(
  name='ExportResponse',
  full_name='opentelemetry.proto.digma.v1.ExportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='opentelemetry.proto.digma.v1.ExportResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=855,
  serialized_end=888,
)

_ERROREVENT.fields_by_name['frames'].message_type = _ERRORFRAME
_EXPORTREQUEST_SPANINFORMATION.fields_by_name['events'].message_type = opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2._SPAN_EVENT
_EXPORTREQUEST_SPANINFORMATION.fields_by_name['error_events'].message_type = _ERROREVENT
_EXPORTREQUEST_SPANINFORMATION.containing_type = _EXPORTREQUEST
_EXPORTREQUEST.fields_by_name['spans'].message_type = _EXPORTREQUEST_SPANINFORMATION
DESCRIPTOR.message_types_by_name['ErrorFrame'] = _ERRORFRAME
DESCRIPTOR.message_types_by_name['ErrorEvent'] = _ERROREVENT
DESCRIPTOR.message_types_by_name['ExportRequest'] = _EXPORTREQUEST
DESCRIPTOR.message_types_by_name['ExportResponse'] = _EXPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorFrame = _reflection.GeneratedProtocolMessageType('ErrorFrame', (_message.Message,), {
  'DESCRIPTOR' : _ERRORFRAME,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ErrorFrame)
  })
_sym_db.RegisterMessage(ErrorFrame)

ErrorEvent = _reflection.GeneratedProtocolMessageType('ErrorEvent', (_message.Message,), {
  'DESCRIPTOR' : _ERROREVENT,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ErrorEvent)
  })
_sym_db.RegisterMessage(ErrorEvent)

ExportRequest = _reflection.GeneratedProtocolMessageType('ExportRequest', (_message.Message,), {

  'SpanInformation' : _reflection.GeneratedProtocolMessageType('SpanInformation', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTREQUEST_SPANINFORMATION,
    '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
    # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ExportRequest.SpanInformation)
    })
  ,
  'DESCRIPTOR' : _EXPORTREQUEST,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ExportRequest)
  })
_sym_db.RegisterMessage(ExportRequest)
_sym_db.RegisterMessage(ExportRequest.SpanInformation)

ExportResponse = _reflection.GeneratedProtocolMessageType('ExportResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESPONSE,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ExportResponse)
  })
_sym_db.RegisterMessage(ExportResponse)


DESCRIPTOR._options = None

_DIGMACOLLECTOR = _descriptor.ServiceDescriptor(
  name='DigmaCollector',
  full_name='opentelemetry.proto.digma.v1.DigmaCollector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=890,
  serialized_end=1007,
  methods=[
  _descriptor.MethodDescriptor(
    name='Export',
    full_name='opentelemetry.proto.digma.v1.DigmaCollector.Export',
    index=0,
    containing_service=None,
    input_type=_EXPORTREQUEST,
    output_type=_EXPORTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGMACOLLECTOR)

DESCRIPTOR.services_by_name['DigmaCollector'] = _DIGMACOLLECTOR

# @@protoc_insertion_point(module_scope)
