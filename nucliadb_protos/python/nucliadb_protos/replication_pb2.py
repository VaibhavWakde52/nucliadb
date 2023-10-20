# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/replication.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!nucliadb_protos/replication.proto\x12\x0breplication\"i\n\x1cPrimaryShardReplicationState\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x15\n\rgeneration_id\x18\x02 \x01(\t\x12\x0c\n\x04kbid\x18\x03 \x01(\t\x12\x12\n\nsimilarity\x18\x04 \x01(\t\"I\n\x1eSecondaryShardReplicationState\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x15\n\rgeneration_id\x18\x02 \x01(\t\"\x80\x01\n%SecondaryCheckReplicationStateRequest\x12\x14\n\x0csecondary_id\x18\x01 \x01(\t\x12\x41\n\x0cshard_states\x18\x02 \x03(\x0b\x32+.replication.SecondaryShardReplicationState\"g\n$PrimaryCheckReplicationStateResponse\x12?\n\x0cshard_states\x18\x01 \x03(\x0b\x32).replication.PrimaryShardReplicationState\"\x1b\n\nSegmentIds\x12\r\n\x05items\x18\x01 \x03(\t\"\xeb\x01\n\x15ReplicateShardRequest\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12X\n\x14\x65xisting_segment_ids\x18\x02 \x03(\x0b\x32:.replication.ReplicateShardRequest.ExistingSegmentIdsEntry\x12\x12\n\nchunk_size\x18\x03 \x01(\x04\x1aR\n\x17\x45xistingSegmentIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.replication.SegmentIds:\x02\x38\x01\"\x89\x01\n\x16ReplicateShardResponse\x12\x15\n\rgeneration_id\x18\x01 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\r\n\x05\x63hunk\x18\x04 \x01(\r\x12\x15\n\rread_position\x18\x05 \x01(\x04\x12\x12\n\ntotal_size\x18\x06 \x01(\x04\x32\xf6\x01\n\x12ReplicationService\x12\x80\x01\n\x15\x43heckReplicationState\x12\x32.replication.SecondaryCheckReplicationStateRequest\x1a\x31.replication.PrimaryCheckReplicationStateResponse\"\x00\x12]\n\x0eReplicateShard\x12\".replication.ReplicateShardRequest\x1a#.replication.ReplicateShardResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.replication_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPLICATESHARDREQUEST_EXISTINGSEGMENTIDSENTRY._options = None
  _REPLICATESHARDREQUEST_EXISTINGSEGMENTIDSENTRY._serialized_options = b'8\001'
  _globals['_PRIMARYSHARDREPLICATIONSTATE']._serialized_start=50
  _globals['_PRIMARYSHARDREPLICATIONSTATE']._serialized_end=155
  _globals['_SECONDARYSHARDREPLICATIONSTATE']._serialized_start=157
  _globals['_SECONDARYSHARDREPLICATIONSTATE']._serialized_end=230
  _globals['_SECONDARYCHECKREPLICATIONSTATEREQUEST']._serialized_start=233
  _globals['_SECONDARYCHECKREPLICATIONSTATEREQUEST']._serialized_end=361
  _globals['_PRIMARYCHECKREPLICATIONSTATERESPONSE']._serialized_start=363
  _globals['_PRIMARYCHECKREPLICATIONSTATERESPONSE']._serialized_end=466
  _globals['_SEGMENTIDS']._serialized_start=468
  _globals['_SEGMENTIDS']._serialized_end=495
  _globals['_REPLICATESHARDREQUEST']._serialized_start=498
  _globals['_REPLICATESHARDREQUEST']._serialized_end=733
  _globals['_REPLICATESHARDREQUEST_EXISTINGSEGMENTIDSENTRY']._serialized_start=651
  _globals['_REPLICATESHARDREQUEST_EXISTINGSEGMENTIDSENTRY']._serialized_end=733
  _globals['_REPLICATESHARDRESPONSE']._serialized_start=736
  _globals['_REPLICATESHARDRESPONSE']._serialized_end=873
  _globals['_REPLICATIONSERVICE']._serialized_start=876
  _globals['_REPLICATIONSERVICE']._serialized_end=1122
# @@protoc_insertion_point(module_scope)
