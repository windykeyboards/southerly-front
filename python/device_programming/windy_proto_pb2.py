# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: 1.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='1.proto',
  package='windy.keyboards',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x07\x31.proto\x12\x0fwindy.keyboards\"/\n\x05Macro\x12&\n\x06micros\x18\x01 \x03(\x0b\x32\x16.windy.keyboards.Micro\"F\n\x05Micro\x12\x0f\n\x05\x64\x65lay\x18\x01 \x01(\x05H\x00\x12\x0f\n\x05press\x18\x02 \x01(\x05H\x00\x12\x11\n\x07release\x18\x03 \x01(\x05H\x00\x42\x08\n\x06\x61\x63tionb\x06proto3'
)




_MACRO = _descriptor.Descriptor(
  name='Macro',
  full_name='windy.keyboards.Macro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='micros', full_name='windy.keyboards.Macro.micros', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=28,
  serialized_end=75,
)


_MICRO = _descriptor.Descriptor(
  name='Micro',
  full_name='windy.keyboards.Micro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='delay', full_name='windy.keyboards.Micro.delay', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='press', full_name='windy.keyboards.Micro.press', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release', full_name='windy.keyboards.Micro.release', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='windy.keyboards.Micro.action',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=77,
  serialized_end=147,
)

_MACRO.fields_by_name['micros'].message_type = _MICRO
_MICRO.oneofs_by_name['action'].fields.append(
  _MICRO.fields_by_name['delay'])
_MICRO.fields_by_name['delay'].containing_oneof = _MICRO.oneofs_by_name['action']
_MICRO.oneofs_by_name['action'].fields.append(
  _MICRO.fields_by_name['press'])
_MICRO.fields_by_name['press'].containing_oneof = _MICRO.oneofs_by_name['action']
_MICRO.oneofs_by_name['action'].fields.append(
  _MICRO.fields_by_name['release'])
_MICRO.fields_by_name['release'].containing_oneof = _MICRO.oneofs_by_name['action']
DESCRIPTOR.message_types_by_name['Macro'] = _MACRO
DESCRIPTOR.message_types_by_name['Micro'] = _MICRO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Macro = _reflection.GeneratedProtocolMessageType('Macro', (_message.Message,), {
  'DESCRIPTOR' : _MACRO,
  '__module__' : '1_pb2'
  # @@protoc_insertion_point(class_scope:windy.keyboards.Macro)
  })
_sym_db.RegisterMessage(Macro)

Micro = _reflection.GeneratedProtocolMessageType('Micro', (_message.Message,), {
  'DESCRIPTOR' : _MICRO,
  '__module__' : '1_pb2'
  # @@protoc_insertion_point(class_scope:windy.keyboards.Micro)
  })
_sym_db.RegisterMessage(Micro)


# @@protoc_insertion_point(module_scope)