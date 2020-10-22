# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/geo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clarifai.rest.grpc.proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/geo.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1cproto/clarifai/api/geo.proto\x12\x0c\x63larifai.api\x1a)proto/clarifai/api/utils/extensions.proto\";\n\x08GeoPoint\x12\x17\n\tlongitude\x18\x01 \x01(\x02\x42\x04\x80\xb5\x18\x01\x12\x16\n\x08latitude\x18\x02 \x01(\x02\x42\x04\x80\xb5\x18\x01\"-\n\x08GeoLimit\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x05value\x18\x02 \x01(\x02\x42\x04\x80\xb5\x18\x01\":\n\rGeoBoxedPoint\x12)\n\tgeo_point\x18\x01 \x01(\x0b\x32\x16.clarifai.api.GeoPoint\"\x89\x01\n\x03Geo\x12)\n\tgeo_point\x18\x01 \x01(\x0b\x32\x16.clarifai.api.GeoPoint\x12)\n\tgeo_limit\x18\x02 \x01(\x0b\x32\x16.clarifai.api.GeoLimit\x12,\n\x07geo_box\x18\x03 \x03(\x0b\x32\x1b.clarifai.api.GeoBoxedPointBZ\n\x1b\x63larifai2.internal.grpc.apiZ\x03\x61pi\xa2\x02\x04\x43\x41IP\xaa\x02\x16\x43larifai.Internal.GRPC\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,])




_GEOPOINT = _descriptor.Descriptor(
  name='GeoPoint',
  full_name='clarifai.api.GeoPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='longitude', full_name='clarifai.api.GeoPoint.longitude', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='clarifai.api.GeoPoint.latitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=148,
)


_GEOLIMIT = _descriptor.Descriptor(
  name='GeoLimit',
  full_name='clarifai.api.GeoLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='clarifai.api.GeoLimit.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='clarifai.api.GeoLimit.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=195,
)


_GEOBOXEDPOINT = _descriptor.Descriptor(
  name='GeoBoxedPoint',
  full_name='clarifai.api.GeoBoxedPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geo_point', full_name='clarifai.api.GeoBoxedPoint.geo_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=255,
)


_GEO = _descriptor.Descriptor(
  name='Geo',
  full_name='clarifai.api.Geo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geo_point', full_name='clarifai.api.Geo.geo_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_limit', full_name='clarifai.api.Geo.geo_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_box', full_name='clarifai.api.Geo.geo_box', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=395,
)

_GEOBOXEDPOINT.fields_by_name['geo_point'].message_type = _GEOPOINT
_GEO.fields_by_name['geo_point'].message_type = _GEOPOINT
_GEO.fields_by_name['geo_limit'].message_type = _GEOLIMIT
_GEO.fields_by_name['geo_box'].message_type = _GEOBOXEDPOINT
DESCRIPTOR.message_types_by_name['GeoPoint'] = _GEOPOINT
DESCRIPTOR.message_types_by_name['GeoLimit'] = _GEOLIMIT
DESCRIPTOR.message_types_by_name['GeoBoxedPoint'] = _GEOBOXEDPOINT
DESCRIPTOR.message_types_by_name['Geo'] = _GEO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeoPoint = _reflection.GeneratedProtocolMessageType('GeoPoint', (_message.Message,), dict(
  DESCRIPTOR = _GEOPOINT,
  __module__ = 'proto.clarifai.api.geo_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GeoPoint)
  ))
_sym_db.RegisterMessage(GeoPoint)

GeoLimit = _reflection.GeneratedProtocolMessageType('GeoLimit', (_message.Message,), dict(
  DESCRIPTOR = _GEOLIMIT,
  __module__ = 'proto.clarifai.api.geo_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GeoLimit)
  ))
_sym_db.RegisterMessage(GeoLimit)

GeoBoxedPoint = _reflection.GeneratedProtocolMessageType('GeoBoxedPoint', (_message.Message,), dict(
  DESCRIPTOR = _GEOBOXEDPOINT,
  __module__ = 'proto.clarifai.api.geo_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GeoBoxedPoint)
  ))
_sym_db.RegisterMessage(GeoBoxedPoint)

Geo = _reflection.GeneratedProtocolMessageType('Geo', (_message.Message,), dict(
  DESCRIPTOR = _GEO,
  __module__ = 'proto.clarifai.api.geo_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.Geo)
  ))
_sym_db.RegisterMessage(Geo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033clarifai2.internal.grpc.apiZ\003api\242\002\004CAIP\252\002\026Clarifai.Internal.GRPC\302\002\001_\312\002\021Clarifai\\Internal'))
_GEOPOINT.fields_by_name['longitude'].has_options = True
_GEOPOINT.fields_by_name['longitude']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
_GEOPOINT.fields_by_name['latitude'].has_options = True
_GEOPOINT.fields_by_name['latitude']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
_GEOLIMIT.fields_by_name['value'].has_options = True
_GEOLIMIT.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
# @@protoc_insertion_point(module_scope)
