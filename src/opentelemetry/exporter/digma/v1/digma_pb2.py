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
  serialized_pb=b'\n+opentelemetry/exporter/digma/v1/digma.proto\x12\x1copentelemetry.proto.digma.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a(opentelemetry/proto/trace/v1/trace.proto\x1a.opentelemetry/proto/resource/v1/resource.proto\"\xe1\x02\n\nErrorFrame\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x13\n\x0bmodule_path\x18\x02 \x01(\t\x12\x15\n\rexecuted_code\x18\x03 \x01(\t\x12\x13\n\x0bline_number\x18\x04 \x01(\x05\x12L\n\nparameters\x18\x05 \x03(\x0b\x32\x38.opentelemetry.proto.digma.v1.ErrorFrame.ParametersEntry\x12\x0e\n\x06repeat\x18\x06 \x01(\x05\x12\x0f\n\x07span_id\x18\x07 \x01(\t\x12\x45\n\x0fparameter_stats\x18\x08 \x03(\x0b\x32,.opentelemetry.proto.digma.v1.ParameterStats\x12\x14\n\x0cmodule_class\x18\t \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"h\n\x0eParameterStats\x12\x12\n\nparam_name\x18\x01 \x01(\t\x12\x12\n\nparam_type\x18\x02 \x01(\t\x12\x0e\n\x06length\x18\x03 \x01(\x05\x12\x0f\n\x07is_none\x18\x04 \x01(\x08\x12\r\n\x05value\x18\x05 \x01(\t\"\x92\x01\n\x0f\x45rrorFrameStack\x12\x38\n\x06\x66rames\x18\x01 \x03(\x0b\x32(.opentelemetry.proto.digma.v1.ErrorFrame\x12\x16\n\x0e\x65xception_type\x18\x02 \x01(\t\x12\x19\n\x11\x65xception_message\x18\x03 \x01(\t\x12\x12\n\nunexpected\x18\x04 \x01(\x08\"\xdd\x01\n\nErrorEvent\x12=\n\x06stacks\x18\x01 \x03(\x0b\x32-.opentelemetry.proto.digma.v1.ErrorFrameStack\x12\x19\n\x11\x65xception_message\x18\x02 \x01(\t\x12\x16\n\x0e\x65xception_type\x18\x03 \x01(\t\x12\x17\n\x0f\x65xception_stack\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07handled\x18\x07 \x01(\x08\x12\x12\n\nunexpected\x18\x08 \x01(\x08\"\xc8\x01\n\rExportRequest\x12\x13\n\x0b\x65nvironment\x18\x02 \x01(\t\x12\x11\n\tcommit_id\x18\x03 \x01(\t\x12\x1c\n\x14programming_language\x18\x04 \x01(\t\x12>\n\x0c\x65rror_events\x18\x05 \x03(\x0b\x32(.opentelemetry.proto.digma.v1.ErrorEvent\x12\x31\n\x05spans\x18\x07 \x03(\x0b\x32\".opentelemetry.proto.trace.v1.Span\"!\n\x0e\x45xportResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2u\n\x0e\x44igmaCollector\x12\x63\n\x06\x45xport\x12+.opentelemetry.proto.digma.v1.ExportRequest\x1a,.opentelemetry.proto.digma.v1.ExportResponseBA\n\x1fio.opentelemetry.proto.digma.v1B\nDigmaProtoP\x01\xaa\x02\x0f\x64igma_collectorb\x06proto3'
  ,
  dependencies=[opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2.DESCRIPTOR,opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2.DESCRIPTOR,opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2.DESCRIPTOR,])




_ERRORFRAME_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='opentelemetry.proto.digma.v1.ErrorFrame.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opentelemetry.proto.digma.v1.ErrorFrame.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='opentelemetry.proto.digma.v1.ErrorFrame.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=565,
)

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
      name='executed_code', full_name='opentelemetry.proto.digma.v1.ErrorFrame.executed_code', index=2,
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
    _descriptor.FieldDescriptor(
      name='parameters', full_name='opentelemetry.proto.digma.v1.ErrorFrame.parameters', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeat', full_name='opentelemetry.proto.digma.v1.ErrorFrame.repeat', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='span_id', full_name='opentelemetry.proto.digma.v1.ErrorFrame.span_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter_stats', full_name='opentelemetry.proto.digma.v1.ErrorFrame.parameter_stats', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_class', full_name='opentelemetry.proto.digma.v1.ErrorFrame.module_class', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ERRORFRAME_PARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=565,
)


_PARAMETERSTATS = _descriptor.Descriptor(
  name='ParameterStats',
  full_name='opentelemetry.proto.digma.v1.ParameterStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_name', full_name='opentelemetry.proto.digma.v1.ParameterStats.param_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='param_type', full_name='opentelemetry.proto.digma.v1.ParameterStats.param_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='opentelemetry.proto.digma.v1.ParameterStats.length', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_none', full_name='opentelemetry.proto.digma.v1.ParameterStats.is_none', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='opentelemetry.proto.digma.v1.ParameterStats.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=567,
  serialized_end=671,
)


_ERRORFRAMESTACK = _descriptor.Descriptor(
  name='ErrorFrameStack',
  full_name='opentelemetry.proto.digma.v1.ErrorFrameStack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frames', full_name='opentelemetry.proto.digma.v1.ErrorFrameStack.frames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_type', full_name='opentelemetry.proto.digma.v1.ErrorFrameStack.exception_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_message', full_name='opentelemetry.proto.digma.v1.ErrorFrameStack.exception_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unexpected', full_name='opentelemetry.proto.digma.v1.ErrorFrameStack.unexpected', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=674,
  serialized_end=820,
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
      name='stacks', full_name='opentelemetry.proto.digma.v1.ErrorEvent.stacks', index=0,
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
    _descriptor.FieldDescriptor(
      name='handled', full_name='opentelemetry.proto.digma.v1.ErrorEvent.handled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unexpected', full_name='opentelemetry.proto.digma.v1.ErrorEvent.unexpected', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=823,
  serialized_end=1044,
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
      name='environment', full_name='opentelemetry.proto.digma.v1.ExportRequest.environment', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commit_id', full_name='opentelemetry.proto.digma.v1.ExportRequest.commit_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='programming_language', full_name='opentelemetry.proto.digma.v1.ExportRequest.programming_language', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_events', full_name='opentelemetry.proto.digma.v1.ExportRequest.error_events', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spans', full_name='opentelemetry.proto.digma.v1.ExportRequest.spans', index=4,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=1047,
  serialized_end=1247,
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
  serialized_start=1249,
  serialized_end=1282,
)

_ERRORFRAME_PARAMETERSENTRY.containing_type = _ERRORFRAME
_ERRORFRAME.fields_by_name['parameters'].message_type = _ERRORFRAME_PARAMETERSENTRY
_ERRORFRAME.fields_by_name['parameter_stats'].message_type = _PARAMETERSTATS
_ERRORFRAMESTACK.fields_by_name['frames'].message_type = _ERRORFRAME
_ERROREVENT.fields_by_name['stacks'].message_type = _ERRORFRAMESTACK
_EXPORTREQUEST.fields_by_name['error_events'].message_type = _ERROREVENT
_EXPORTREQUEST.fields_by_name['spans'].message_type = opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2._SPAN
DESCRIPTOR.message_types_by_name['ErrorFrame'] = _ERRORFRAME
DESCRIPTOR.message_types_by_name['ParameterStats'] = _PARAMETERSTATS
DESCRIPTOR.message_types_by_name['ErrorFrameStack'] = _ERRORFRAMESTACK
DESCRIPTOR.message_types_by_name['ErrorEvent'] = _ERROREVENT
DESCRIPTOR.message_types_by_name['ExportRequest'] = _EXPORTREQUEST
DESCRIPTOR.message_types_by_name['ExportResponse'] = _EXPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorFrame = _reflection.GeneratedProtocolMessageType('ErrorFrame', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _ERRORFRAME_PARAMETERSENTRY,
    '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
    # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ErrorFrame.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _ERRORFRAME,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ErrorFrame)
  })
_sym_db.RegisterMessage(ErrorFrame)
_sym_db.RegisterMessage(ErrorFrame.ParametersEntry)

ParameterStats = _reflection.GeneratedProtocolMessageType('ParameterStats', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERSTATS,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ParameterStats)
  })
_sym_db.RegisterMessage(ParameterStats)

ErrorFrameStack = _reflection.GeneratedProtocolMessageType('ErrorFrameStack', (_message.Message,), {
  'DESCRIPTOR' : _ERRORFRAMESTACK,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ErrorFrameStack)
  })
_sym_db.RegisterMessage(ErrorFrameStack)

ErrorEvent = _reflection.GeneratedProtocolMessageType('ErrorEvent', (_message.Message,), {
  'DESCRIPTOR' : _ERROREVENT,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ErrorEvent)
  })
_sym_db.RegisterMessage(ErrorEvent)

ExportRequest = _reflection.GeneratedProtocolMessageType('ExportRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTREQUEST,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ExportRequest)
  })
_sym_db.RegisterMessage(ExportRequest)

ExportResponse = _reflection.GeneratedProtocolMessageType('ExportResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESPONSE,
  '__module__' : 'opentelemetry.exporter.digma.v1.digma_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.digma.v1.ExportResponse)
  })
_sym_db.RegisterMessage(ExportResponse)


DESCRIPTOR._options = None
_ERRORFRAME_PARAMETERSENTRY._options = None

_DIGMACOLLECTOR = _descriptor.ServiceDescriptor(
  name='DigmaCollector',
  full_name='opentelemetry.proto.digma.v1.DigmaCollector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1284,
  serialized_end=1401,
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
