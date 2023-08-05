# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_room.proto',
  package='data_room',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x64\x61ta_room.proto\x12\tdata_room\"\x8e\x01\n\x08\x44\x61taRoom\x12\n\n\x02id\x18\x01 \x02(\t\x12 \n\x06tables\x18\x02 \x03(\x0b\x32\x10.data_room.Table\x12!\n\x07queries\x18\x03 \x03(\x0b\x32\x10.data_room.Query\x12\x1e\n\x05roles\x18\x04 \x03(\x0b\x32\x0f.data_room.Role\x12\x11\n\tmrenclave\x18\x06 \x01(\t\"b\n\x05Table\x12\x1f\n\x17sqlCreateTableStatement\x18\x01 \x02(\t\x12\x38\n\x15submissionConstraints\x18\x02 \x03(\x0b\x32\x19.data_room.TimeConstraint\"b\n\x05Query\x12\x11\n\tqueryName\x18\x01 \x02(\t\x12\x1a\n\x12sqlSelectStatement\x18\x02 \x02(\t\x12*\n\x0b\x63onstraints\x18\x03 \x03(\x0b\x32\x15.data_room.Constraint\"\x97\x01\n\x04Role\x12\x10\n\x08roleName\x18\x01 \x02(\t\x12\x12\n\nemailRegex\x18\x02 \x02(\t\x12=\n\x14\x61uthenticationMethod\x18\x03 \x02(\x0b\x32\x1f.data_room.AuthenticationMethod\x12*\n\x0bpermissions\x18\x04 \x03(\x0b\x32\x15.data_room.Permission\"~\n\x14\x41uthenticationMethod\x12)\n\ntrustedPki\x18\x01 \x02(\x0b\x32\x15.data_room.TrustedPki\x12#\n\x07mailPki\x18\x02 \x01(\x0b\x32\x12.data_room.MailPki\x12\x16\n\x0epasswordSha256\x18\x03 \x01(\t\"%\n\nTrustedPki\x12\x17\n\x0frootCertificate\x18\x01 \x02(\x0c\"\x1e\n\x07MailPki\x12\x13\n\x0brootCaStore\x18\x01 \x02(\x0c\"\xba\x02\n\nPermission\x12\x41\n\x15submitQueryPermission\x18\x01 \x01(\x0b\x32 .data_room.SubmitQueryPermissionH\x00\x12=\n\x13tableCrudPermission\x18\x02 \x01(\x0b\x32\x1e.data_room.TableCrudPermissionH\x00\x12M\n\x1b\x64\x61taRoomRetrievalPermission\x18\x03 \x01(\x0b\x32&.data_room.DataroomRetrievalPermissionH\x00\x12M\n\x1b\x61uditLogRetrievalPermission\x18\x04 \x01(\x0b\x32&.data_room.AuditLogRetrievalPermissionH\x00\x42\x0c\n\npermission\"*\n\x15SubmitQueryPermission\x12\x11\n\tqueryName\x18\x01 \x02(\t\"(\n\x13TableCrudPermission\x12\x11\n\ttableName\x18\x01 \x02(\t\"\x1d\n\x1b\x44\x61taroomRetrievalPermission\"\x1d\n\x1b\x41uditLogRetrievalPermission\"\x97\x01\n\nConstraint\x12\x13\n\x0b\x64\x65scription\x18\x01 \x02(\t\x12\x31\n\rsqlConstraint\x18\x02 \x01(\x0b\x32\x18.data_room.SqlConstraintH\x00\x12\x33\n\x0etimeConstraint\x18\x03 \x01(\x0b\x32\x19.data_room.TimeConstraintH\x00\x42\x0c\n\nconstraint\"\"\n\rSqlConstraint\x12\x11\n\tstatement\x18\x01 \x02(\t\"3\n\x0eTimeConstraint\x12\x11\n\ttimestamp\x18\x01 \x02(\x03\x12\x0e\n\x06\x62\x65\x66ore\x18\x02 \x02(\x08'
)




_DATAROOM = _descriptor.Descriptor(
  name='DataRoom',
  full_name='data_room.DataRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='data_room.DataRoom.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tables', full_name='data_room.DataRoom.tables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queries', full_name='data_room.DataRoom.queries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roles', full_name='data_room.DataRoom.roles', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mrenclave', full_name='data_room.DataRoom.mrenclave', index=4,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=173,
)


_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='data_room.Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sqlCreateTableStatement', full_name='data_room.Table.sqlCreateTableStatement', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submissionConstraints', full_name='data_room.Table.submissionConstraints', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=273,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='data_room.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='queryName', full_name='data_room.Query.queryName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sqlSelectStatement', full_name='data_room.Query.sqlSelectStatement', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='data_room.Query.constraints', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=373,
)


_ROLE = _descriptor.Descriptor(
  name='Role',
  full_name='data_room.Role',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleName', full_name='data_room.Role.roleName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='emailRegex', full_name='data_room.Role.emailRegex', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authenticationMethod', full_name='data_room.Role.authenticationMethod', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='data_room.Role.permissions', index=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=527,
)


_AUTHENTICATIONMETHOD = _descriptor.Descriptor(
  name='AuthenticationMethod',
  full_name='data_room.AuthenticationMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trustedPki', full_name='data_room.AuthenticationMethod.trustedPki', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mailPki', full_name='data_room.AuthenticationMethod.mailPki', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passwordSha256', full_name='data_room.AuthenticationMethod.passwordSha256', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=655,
)


_TRUSTEDPKI = _descriptor.Descriptor(
  name='TrustedPki',
  full_name='data_room.TrustedPki',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rootCertificate', full_name='data_room.TrustedPki.rootCertificate', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=657,
  serialized_end=694,
)


_MAILPKI = _descriptor.Descriptor(
  name='MailPki',
  full_name='data_room.MailPki',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rootCaStore', full_name='data_room.MailPki.rootCaStore', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=726,
)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='data_room.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='submitQueryPermission', full_name='data_room.Permission.submitQueryPermission', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tableCrudPermission', full_name='data_room.Permission.tableCrudPermission', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataRoomRetrievalPermission', full_name='data_room.Permission.dataRoomRetrievalPermission', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auditLogRetrievalPermission', full_name='data_room.Permission.auditLogRetrievalPermission', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='permission', full_name='data_room.Permission.permission',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=729,
  serialized_end=1043,
)


_SUBMITQUERYPERMISSION = _descriptor.Descriptor(
  name='SubmitQueryPermission',
  full_name='data_room.SubmitQueryPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='queryName', full_name='data_room.SubmitQueryPermission.queryName', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1045,
  serialized_end=1087,
)


_TABLECRUDPERMISSION = _descriptor.Descriptor(
  name='TableCrudPermission',
  full_name='data_room.TableCrudPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tableName', full_name='data_room.TableCrudPermission.tableName', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1089,
  serialized_end=1129,
)


_DATAROOMRETRIEVALPERMISSION = _descriptor.Descriptor(
  name='DataroomRetrievalPermission',
  full_name='data_room.DataroomRetrievalPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1131,
  serialized_end=1160,
)


_AUDITLOGRETRIEVALPERMISSION = _descriptor.Descriptor(
  name='AuditLogRetrievalPermission',
  full_name='data_room.AuditLogRetrievalPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1162,
  serialized_end=1191,
)


_CONSTRAINT = _descriptor.Descriptor(
  name='Constraint',
  full_name='data_room.Constraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='data_room.Constraint.description', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sqlConstraint', full_name='data_room.Constraint.sqlConstraint', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeConstraint', full_name='data_room.Constraint.timeConstraint', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='constraint', full_name='data_room.Constraint.constraint',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1194,
  serialized_end=1345,
)


_SQLCONSTRAINT = _descriptor.Descriptor(
  name='SqlConstraint',
  full_name='data_room.SqlConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='statement', full_name='data_room.SqlConstraint.statement', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1347,
  serialized_end=1381,
)


_TIMECONSTRAINT = _descriptor.Descriptor(
  name='TimeConstraint',
  full_name='data_room.TimeConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='data_room.TimeConstraint.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='data_room.TimeConstraint.before', index=1,
      number=2, type=8, cpp_type=7, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1383,
  serialized_end=1434,
)

_DATAROOM.fields_by_name['tables'].message_type = _TABLE
_DATAROOM.fields_by_name['queries'].message_type = _QUERY
_DATAROOM.fields_by_name['roles'].message_type = _ROLE
_TABLE.fields_by_name['submissionConstraints'].message_type = _TIMECONSTRAINT
_QUERY.fields_by_name['constraints'].message_type = _CONSTRAINT
_ROLE.fields_by_name['authenticationMethod'].message_type = _AUTHENTICATIONMETHOD
_ROLE.fields_by_name['permissions'].message_type = _PERMISSION
_AUTHENTICATIONMETHOD.fields_by_name['trustedPki'].message_type = _TRUSTEDPKI
_AUTHENTICATIONMETHOD.fields_by_name['mailPki'].message_type = _MAILPKI
_PERMISSION.fields_by_name['submitQueryPermission'].message_type = _SUBMITQUERYPERMISSION
_PERMISSION.fields_by_name['tableCrudPermission'].message_type = _TABLECRUDPERMISSION
_PERMISSION.fields_by_name['dataRoomRetrievalPermission'].message_type = _DATAROOMRETRIEVALPERMISSION
_PERMISSION.fields_by_name['auditLogRetrievalPermission'].message_type = _AUDITLOGRETRIEVALPERMISSION
_PERMISSION.oneofs_by_name['permission'].fields.append(
  _PERMISSION.fields_by_name['submitQueryPermission'])
_PERMISSION.fields_by_name['submitQueryPermission'].containing_oneof = _PERMISSION.oneofs_by_name['permission']
_PERMISSION.oneofs_by_name['permission'].fields.append(
  _PERMISSION.fields_by_name['tableCrudPermission'])
_PERMISSION.fields_by_name['tableCrudPermission'].containing_oneof = _PERMISSION.oneofs_by_name['permission']
_PERMISSION.oneofs_by_name['permission'].fields.append(
  _PERMISSION.fields_by_name['dataRoomRetrievalPermission'])
_PERMISSION.fields_by_name['dataRoomRetrievalPermission'].containing_oneof = _PERMISSION.oneofs_by_name['permission']
_PERMISSION.oneofs_by_name['permission'].fields.append(
  _PERMISSION.fields_by_name['auditLogRetrievalPermission'])
_PERMISSION.fields_by_name['auditLogRetrievalPermission'].containing_oneof = _PERMISSION.oneofs_by_name['permission']
_CONSTRAINT.fields_by_name['sqlConstraint'].message_type = _SQLCONSTRAINT
_CONSTRAINT.fields_by_name['timeConstraint'].message_type = _TIMECONSTRAINT
_CONSTRAINT.oneofs_by_name['constraint'].fields.append(
  _CONSTRAINT.fields_by_name['sqlConstraint'])
_CONSTRAINT.fields_by_name['sqlConstraint'].containing_oneof = _CONSTRAINT.oneofs_by_name['constraint']
_CONSTRAINT.oneofs_by_name['constraint'].fields.append(
  _CONSTRAINT.fields_by_name['timeConstraint'])
_CONSTRAINT.fields_by_name['timeConstraint'].containing_oneof = _CONSTRAINT.oneofs_by_name['constraint']
DESCRIPTOR.message_types_by_name['DataRoom'] = _DATAROOM
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Role'] = _ROLE
DESCRIPTOR.message_types_by_name['AuthenticationMethod'] = _AUTHENTICATIONMETHOD
DESCRIPTOR.message_types_by_name['TrustedPki'] = _TRUSTEDPKI
DESCRIPTOR.message_types_by_name['MailPki'] = _MAILPKI
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['SubmitQueryPermission'] = _SUBMITQUERYPERMISSION
DESCRIPTOR.message_types_by_name['TableCrudPermission'] = _TABLECRUDPERMISSION
DESCRIPTOR.message_types_by_name['DataroomRetrievalPermission'] = _DATAROOMRETRIEVALPERMISSION
DESCRIPTOR.message_types_by_name['AuditLogRetrievalPermission'] = _AUDITLOGRETRIEVALPERMISSION
DESCRIPTOR.message_types_by_name['Constraint'] = _CONSTRAINT
DESCRIPTOR.message_types_by_name['SqlConstraint'] = _SQLCONSTRAINT
DESCRIPTOR.message_types_by_name['TimeConstraint'] = _TIMECONSTRAINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataRoom = _reflection.GeneratedProtocolMessageType('DataRoom', (_message.Message,), {
  'DESCRIPTOR' : _DATAROOM,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.DataRoom)
  })
_sym_db.RegisterMessage(DataRoom)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.Table)
  })
_sym_db.RegisterMessage(Table)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.Query)
  })
_sym_db.RegisterMessage(Query)

Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), {
  'DESCRIPTOR' : _ROLE,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.Role)
  })
_sym_db.RegisterMessage(Role)

AuthenticationMethod = _reflection.GeneratedProtocolMessageType('AuthenticationMethod', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONMETHOD,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.AuthenticationMethod)
  })
_sym_db.RegisterMessage(AuthenticationMethod)

TrustedPki = _reflection.GeneratedProtocolMessageType('TrustedPki', (_message.Message,), {
  'DESCRIPTOR' : _TRUSTEDPKI,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.TrustedPki)
  })
_sym_db.RegisterMessage(TrustedPki)

MailPki = _reflection.GeneratedProtocolMessageType('MailPki', (_message.Message,), {
  'DESCRIPTOR' : _MAILPKI,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.MailPki)
  })
_sym_db.RegisterMessage(MailPki)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.Permission)
  })
_sym_db.RegisterMessage(Permission)

SubmitQueryPermission = _reflection.GeneratedProtocolMessageType('SubmitQueryPermission', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITQUERYPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.SubmitQueryPermission)
  })
_sym_db.RegisterMessage(SubmitQueryPermission)

TableCrudPermission = _reflection.GeneratedProtocolMessageType('TableCrudPermission', (_message.Message,), {
  'DESCRIPTOR' : _TABLECRUDPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.TableCrudPermission)
  })
_sym_db.RegisterMessage(TableCrudPermission)

DataroomRetrievalPermission = _reflection.GeneratedProtocolMessageType('DataroomRetrievalPermission', (_message.Message,), {
  'DESCRIPTOR' : _DATAROOMRETRIEVALPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.DataroomRetrievalPermission)
  })
_sym_db.RegisterMessage(DataroomRetrievalPermission)

AuditLogRetrievalPermission = _reflection.GeneratedProtocolMessageType('AuditLogRetrievalPermission', (_message.Message,), {
  'DESCRIPTOR' : _AUDITLOGRETRIEVALPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.AuditLogRetrievalPermission)
  })
_sym_db.RegisterMessage(AuditLogRetrievalPermission)

Constraint = _reflection.GeneratedProtocolMessageType('Constraint', (_message.Message,), {
  'DESCRIPTOR' : _CONSTRAINT,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.Constraint)
  })
_sym_db.RegisterMessage(Constraint)

SqlConstraint = _reflection.GeneratedProtocolMessageType('SqlConstraint', (_message.Message,), {
  'DESCRIPTOR' : _SQLCONSTRAINT,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.SqlConstraint)
  })
_sym_db.RegisterMessage(SqlConstraint)

TimeConstraint = _reflection.GeneratedProtocolMessageType('TimeConstraint', (_message.Message,), {
  'DESCRIPTOR' : _TIMECONSTRAINT,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.TimeConstraint)
  })
_sym_db.RegisterMessage(TimeConstraint)


# @@protoc_insertion_point(module_scope)
