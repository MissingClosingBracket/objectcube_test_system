# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mads.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mads.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmads.proto\"\"\n\x06Object\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0b\n\x03URI\x18\x02 \x01(\t\"9\n\x03Tag\x12\x0b\n\x03tid\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x04type\x18\x03 \x01(\x0e\x32\x08.TagType\"&\n\x17UserCreateObjectRequest\x12\x0b\n\x03URI\x18\x01 \x01(\t\"3\n\x18UserCreateObjectResponse\x12\x17\n\x06object\x18\x01 \x01(\x0b\x32\x07.Object\"B\n\x1ePluginCreateDescriptionRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"4\n\x1fPluginCreateDescriptionResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\"E\n!PluginTranslateDescriptionRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"7\n\"PluginTranslateDescriptionResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\"P\n\x1cPluginExtractExifDataRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02\"2\n\x1dPluginExtractExifDataResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\":\n\x1aPluginSupplyGeodataRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0f\n\x07geodata\x18\x02 \x01(\t\"0\n\x1bPluginSupplyGeodataResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\"/\n UserRequestsTagsForObjectRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\"6\n!UserRequestsTagsForObjectResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\"2\n\x14UserChangeTagRequest\x12\x0b\n\x03tid\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t\"*\n\x15UserChangeTagResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag*Q\n\x07TagType\x12\x0e\n\nNOT_IN_USE\x10\x00\x12\x0b\n\x07GEODATA\x10\x01\x12\t\n\x05\x44\x45SCR\x10\x02\x12\x10\n\x0cTRANSL_DESCR\x10\x03\x12\x0c\n\x08\x45XIFDATA\x10\x04\x32\xec\x04\n\x0cmads_service\x12G\n\x10userCreateObject\x12\x18.UserCreateObjectRequest\x1a\x19.UserCreateObjectResponse\x12\\\n\x17pluginCreateDescription\x12\x1f.PluginCreateDescriptionRequest\x1a .PluginCreateDescriptionResponse\x12\x65\n\x1apluginTranslateDescription\x12\".PluginTranslateDescriptionRequest\x1a#.PluginTranslateDescriptionResponse\x12V\n\x15pluginExtractExifData\x12\x1d.PluginExtractExifDataRequest\x1a\x1e.PluginExtractExifDataResponse\x12P\n\x13pluginSupplyGeodata\x12\x1b.PluginSupplyGeodataRequest\x1a\x1c.PluginSupplyGeodataResponse\x12\x64\n\x19userRequestsTagsForObject\x12!.UserRequestsTagsForObjectRequest\x1a\".UserRequestsTagsForObjectResponse0\x01\x12>\n\ruserChangeTag\x12\x15.UserChangeTagRequest\x1a\x16.UserChangeTagResponseb\x06proto3'
)

_TAGTYPE = _descriptor.EnumDescriptor(
  name='TagType',
  full_name='TagType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_IN_USE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEODATA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESCR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRANSL_DESCR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIFDATA', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=897,
  serialized_end=978,
)
_sym_db.RegisterEnumDescriptor(_TAGTYPE)

TagType = enum_type_wrapper.EnumTypeWrapper(_TAGTYPE)
NOT_IN_USE = 0
GEODATA = 1
DESCR = 2
TRANSL_DESCR = 3
EXIFDATA = 4



_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='Object.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='URI', full_name='Object.URI', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=48,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='Tag.tid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Tag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Tag.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=50,
  serialized_end=107,
)


_USERCREATEOBJECTREQUEST = _descriptor.Descriptor(
  name='UserCreateObjectRequest',
  full_name='UserCreateObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='URI', full_name='UserCreateObjectRequest.URI', index=0,
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
  serialized_start=109,
  serialized_end=147,
)


_USERCREATEOBJECTRESPONSE = _descriptor.Descriptor(
  name='UserCreateObjectResponse',
  full_name='UserCreateObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='UserCreateObjectResponse.object', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=149,
  serialized_end=200,
)


_PLUGINCREATEDESCRIPTIONREQUEST = _descriptor.Descriptor(
  name='PluginCreateDescriptionRequest',
  full_name='PluginCreateDescriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginCreateDescriptionRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='PluginCreateDescriptionRequest.description', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=268,
)


_PLUGINCREATEDESCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='PluginCreateDescriptionResponse',
  full_name='PluginCreateDescriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginCreateDescriptionResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=270,
  serialized_end=322,
)


_PLUGINTRANSLATEDESCRIPTIONREQUEST = _descriptor.Descriptor(
  name='PluginTranslateDescriptionRequest',
  full_name='PluginTranslateDescriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginTranslateDescriptionRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='PluginTranslateDescriptionRequest.description', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=393,
)


_PLUGINTRANSLATEDESCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='PluginTranslateDescriptionResponse',
  full_name='PluginTranslateDescriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginTranslateDescriptionResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=395,
  serialized_end=450,
)


_PLUGINEXTRACTEXIFDATAREQUEST = _descriptor.Descriptor(
  name='PluginExtractExifDataRequest',
  full_name='PluginExtractExifDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginExtractExifDataRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PluginExtractExifDataRequest.latitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PluginExtractExifDataRequest.longitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=452,
  serialized_end=532,
)


_PLUGINEXTRACTEXIFDATARESPONSE = _descriptor.Descriptor(
  name='PluginExtractExifDataResponse',
  full_name='PluginExtractExifDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginExtractExifDataResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=534,
  serialized_end=584,
)


_PLUGINSUPPLYGEODATAREQUEST = _descriptor.Descriptor(
  name='PluginSupplyGeodataRequest',
  full_name='PluginSupplyGeodataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginSupplyGeodataRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geodata', full_name='PluginSupplyGeodataRequest.geodata', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=644,
)


_PLUGINSUPPLYGEODATARESPONSE = _descriptor.Descriptor(
  name='PluginSupplyGeodataResponse',
  full_name='PluginSupplyGeodataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginSupplyGeodataResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=646,
  serialized_end=694,
)


_USERREQUESTSTAGSFOROBJECTREQUEST = _descriptor.Descriptor(
  name='UserRequestsTagsForObjectRequest',
  full_name='UserRequestsTagsForObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='UserRequestsTagsForObjectRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=696,
  serialized_end=743,
)


_USERREQUESTSTAGSFOROBJECTRESPONSE = _descriptor.Descriptor(
  name='UserRequestsTagsForObjectResponse',
  full_name='UserRequestsTagsForObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='UserRequestsTagsForObjectResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=745,
  serialized_end=799,
)


_USERCHANGETAGREQUEST = _descriptor.Descriptor(
  name='UserChangeTagRequest',
  full_name='UserChangeTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='UserChangeTagRequest.tid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='UserChangeTagRequest.value', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=851,
)


_USERCHANGETAGRESPONSE = _descriptor.Descriptor(
  name='UserChangeTagResponse',
  full_name='UserChangeTagResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='UserChangeTagResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=853,
  serialized_end=895,
)

_TAG.fields_by_name['type'].enum_type = _TAGTYPE
_USERCREATEOBJECTRESPONSE.fields_by_name['object'].message_type = _OBJECT
_PLUGINCREATEDESCRIPTIONRESPONSE.fields_by_name['tag'].message_type = _TAG
_PLUGINTRANSLATEDESCRIPTIONRESPONSE.fields_by_name['tag'].message_type = _TAG
_PLUGINEXTRACTEXIFDATARESPONSE.fields_by_name['tag'].message_type = _TAG
_PLUGINSUPPLYGEODATARESPONSE.fields_by_name['tag'].message_type = _TAG
_USERREQUESTSTAGSFOROBJECTRESPONSE.fields_by_name['tag'].message_type = _TAG
_USERCHANGETAGRESPONSE.fields_by_name['tag'].message_type = _TAG
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['UserCreateObjectRequest'] = _USERCREATEOBJECTREQUEST
DESCRIPTOR.message_types_by_name['UserCreateObjectResponse'] = _USERCREATEOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['PluginCreateDescriptionRequest'] = _PLUGINCREATEDESCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['PluginCreateDescriptionResponse'] = _PLUGINCREATEDESCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name['PluginTranslateDescriptionRequest'] = _PLUGINTRANSLATEDESCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['PluginTranslateDescriptionResponse'] = _PLUGINTRANSLATEDESCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name['PluginExtractExifDataRequest'] = _PLUGINEXTRACTEXIFDATAREQUEST
DESCRIPTOR.message_types_by_name['PluginExtractExifDataResponse'] = _PLUGINEXTRACTEXIFDATARESPONSE
DESCRIPTOR.message_types_by_name['PluginSupplyGeodataRequest'] = _PLUGINSUPPLYGEODATAREQUEST
DESCRIPTOR.message_types_by_name['PluginSupplyGeodataResponse'] = _PLUGINSUPPLYGEODATARESPONSE
DESCRIPTOR.message_types_by_name['UserRequestsTagsForObjectRequest'] = _USERREQUESTSTAGSFOROBJECTREQUEST
DESCRIPTOR.message_types_by_name['UserRequestsTagsForObjectResponse'] = _USERREQUESTSTAGSFOROBJECTRESPONSE
DESCRIPTOR.message_types_by_name['UserChangeTagRequest'] = _USERCHANGETAGREQUEST
DESCRIPTOR.message_types_by_name['UserChangeTagResponse'] = _USERCHANGETAGRESPONSE
DESCRIPTOR.enum_types_by_name['TagType'] = _TAGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:Object)
  })
_sym_db.RegisterMessage(Object)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:Tag)
  })
_sym_db.RegisterMessage(Tag)

UserCreateObjectRequest = _reflection.GeneratedProtocolMessageType('UserCreateObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEOBJECTREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserCreateObjectRequest)
  })
_sym_db.RegisterMessage(UserCreateObjectRequest)

UserCreateObjectResponse = _reflection.GeneratedProtocolMessageType('UserCreateObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEOBJECTRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserCreateObjectResponse)
  })
_sym_db.RegisterMessage(UserCreateObjectResponse)

PluginCreateDescriptionRequest = _reflection.GeneratedProtocolMessageType('PluginCreateDescriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINCREATEDESCRIPTIONREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginCreateDescriptionRequest)
  })
_sym_db.RegisterMessage(PluginCreateDescriptionRequest)

PluginCreateDescriptionResponse = _reflection.GeneratedProtocolMessageType('PluginCreateDescriptionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINCREATEDESCRIPTIONRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginCreateDescriptionResponse)
  })
_sym_db.RegisterMessage(PluginCreateDescriptionResponse)

PluginTranslateDescriptionRequest = _reflection.GeneratedProtocolMessageType('PluginTranslateDescriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINTRANSLATEDESCRIPTIONREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginTranslateDescriptionRequest)
  })
_sym_db.RegisterMessage(PluginTranslateDescriptionRequest)

PluginTranslateDescriptionResponse = _reflection.GeneratedProtocolMessageType('PluginTranslateDescriptionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINTRANSLATEDESCRIPTIONRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginTranslateDescriptionResponse)
  })
_sym_db.RegisterMessage(PluginTranslateDescriptionResponse)

PluginExtractExifDataRequest = _reflection.GeneratedProtocolMessageType('PluginExtractExifDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINEXTRACTEXIFDATAREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginExtractExifDataRequest)
  })
_sym_db.RegisterMessage(PluginExtractExifDataRequest)

PluginExtractExifDataResponse = _reflection.GeneratedProtocolMessageType('PluginExtractExifDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINEXTRACTEXIFDATARESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginExtractExifDataResponse)
  })
_sym_db.RegisterMessage(PluginExtractExifDataResponse)

PluginSupplyGeodataRequest = _reflection.GeneratedProtocolMessageType('PluginSupplyGeodataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINSUPPLYGEODATAREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginSupplyGeodataRequest)
  })
_sym_db.RegisterMessage(PluginSupplyGeodataRequest)

PluginSupplyGeodataResponse = _reflection.GeneratedProtocolMessageType('PluginSupplyGeodataResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINSUPPLYGEODATARESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginSupplyGeodataResponse)
  })
_sym_db.RegisterMessage(PluginSupplyGeodataResponse)

UserRequestsTagsForObjectRequest = _reflection.GeneratedProtocolMessageType('UserRequestsTagsForObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUESTSTAGSFOROBJECTREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserRequestsTagsForObjectRequest)
  })
_sym_db.RegisterMessage(UserRequestsTagsForObjectRequest)

UserRequestsTagsForObjectResponse = _reflection.GeneratedProtocolMessageType('UserRequestsTagsForObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUESTSTAGSFOROBJECTRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserRequestsTagsForObjectResponse)
  })
_sym_db.RegisterMessage(UserRequestsTagsForObjectResponse)

UserChangeTagRequest = _reflection.GeneratedProtocolMessageType('UserChangeTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCHANGETAGREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserChangeTagRequest)
  })
_sym_db.RegisterMessage(UserChangeTagRequest)

UserChangeTagResponse = _reflection.GeneratedProtocolMessageType('UserChangeTagResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERCHANGETAGRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserChangeTagResponse)
  })
_sym_db.RegisterMessage(UserChangeTagResponse)



_MADS_SERVICE = _descriptor.ServiceDescriptor(
  name='mads_service',
  full_name='mads_service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=981,
  serialized_end=1601,
  methods=[
  _descriptor.MethodDescriptor(
    name='userCreateObject',
    full_name='mads_service.userCreateObject',
    index=0,
    containing_service=None,
    input_type=_USERCREATEOBJECTREQUEST,
    output_type=_USERCREATEOBJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginCreateDescription',
    full_name='mads_service.pluginCreateDescription',
    index=1,
    containing_service=None,
    input_type=_PLUGINCREATEDESCRIPTIONREQUEST,
    output_type=_PLUGINCREATEDESCRIPTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginTranslateDescription',
    full_name='mads_service.pluginTranslateDescription',
    index=2,
    containing_service=None,
    input_type=_PLUGINTRANSLATEDESCRIPTIONREQUEST,
    output_type=_PLUGINTRANSLATEDESCRIPTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginExtractExifData',
    full_name='mads_service.pluginExtractExifData',
    index=3,
    containing_service=None,
    input_type=_PLUGINEXTRACTEXIFDATAREQUEST,
    output_type=_PLUGINEXTRACTEXIFDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginSupplyGeodata',
    full_name='mads_service.pluginSupplyGeodata',
    index=4,
    containing_service=None,
    input_type=_PLUGINSUPPLYGEODATAREQUEST,
    output_type=_PLUGINSUPPLYGEODATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userRequestsTagsForObject',
    full_name='mads_service.userRequestsTagsForObject',
    index=5,
    containing_service=None,
    input_type=_USERREQUESTSTAGSFOROBJECTREQUEST,
    output_type=_USERREQUESTSTAGSFOROBJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userChangeTag',
    full_name='mads_service.userChangeTag',
    index=6,
    containing_service=None,
    input_type=_USERCHANGETAGREQUEST,
    output_type=_USERCHANGETAGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MADS_SERVICE)

DESCRIPTOR.services_by_name['mads_service'] = _MADS_SERVICE

# @@protoc_insertion_point(module_scope)
