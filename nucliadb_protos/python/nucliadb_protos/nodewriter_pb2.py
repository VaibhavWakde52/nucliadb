# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/nodewriter.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nucliadb_protos import noderesources_pb2 as nucliadb__protos_dot_noderesources__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_noderesources__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_noderesources__pb2.nucliadb_protos.utils_pb2

from nucliadb_protos.noderesources_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n nucliadb_protos/nodewriter.proto\x12\nnodewriter\x1a#nucliadb_protos/noderesources.proto\"\xc9\x01\n\x08OpStatus\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.nodewriter.OpStatus.Status\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\x12\x13\n\x0b\x66ield_count\x18\x03 \x01(\x04\x12\x17\n\x0fparagraph_count\x18\x05 \x01(\x04\x12\x16\n\x0esentence_count\x18\x06 \x01(\x04\x12\x10\n\x08shard_id\x18\x04 \x01(\t\"(\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\x86\x02\n\x0cIndexMessage\x12\x0c\n\x04node\x18\x01 \x01(\t\x12\r\n\x05shard\x18\x02 \x01(\t\x12\x0c\n\x04txid\x18\x03 \x01(\x04\x12\x10\n\x08resource\x18\x04 \x01(\t\x12,\n\x0btypemessage\x18\x05 \x01(\x0e\x32\x17.nodewriter.TypeMessage\x12\x12\n\nreindex_id\x18\x06 \x01(\t\x12\x16\n\tpartition\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bstorage_key\x18\x08 \x01(\t\x12\x0c\n\x04kbid\x18\t \x01(\t\x12.\n\x06source\x18\n \x01(\x0e\x32\x1e.nodewriter.IndexMessageSourceB\x0c\n\n_partition\"x\n\x18GarbageCollectorResponse\x12;\n\x06status\x18\x01 \x01(\x0e\x32+.nodewriter.GarbageCollectorResponse.Status\"\x1f\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\r\n\tTRY_LATER\x10\x01\"|\n\x0fNewShardRequest\x12+\n\nsimilarity\x18\x01 \x01(\x0e\x32\x17.utils.VectorSimilarity\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12.\n\x0frelease_channel\x18\x03 \x01(\x0e\x32\x15.utils.ReleaseChannel\"j\n\x13NewVectorSetRequest\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.noderesources.VectorSetID\x12+\n\nsimilarity\x18\x02 \x01(\x0e\x32\x17.utils.VectorSimilarity\"\x92\x01\n\rMergeResponse\x12\x35\n\x06status\x18\x01 \x01(\x0e\x32%.nodewriter.MergeResponse.MergeStatus\x12\x17\n\x0fmerged_segments\x18\x02 \x01(\r\x12\x1a\n\x12remaining_segments\x18\x03 \x01(\r\"\x15\n\x0bMergeStatus\x12\x06\n\x02OK\x10\x00*)\n\x0bTypeMessage\x12\x0c\n\x08\x43REATION\x10\x00\x12\x0c\n\x08\x44\x45LETION\x10\x01*/\n\x12IndexMessageSource\x12\r\n\tPROCESSOR\x10\x00\x12\n\n\x06WRITER\x10\x01\x32\x85\x06\n\nNodeWriter\x12\x46\n\x08NewShard\x12\x1b.nodewriter.NewShardRequest\x1a\x1b.noderesources.ShardCreated\"\x00\x12?\n\x0b\x44\x65leteShard\x12\x16.noderesources.ShardId\x1a\x16.noderesources.ShardId\"\x00\x12\x42\n\nListShards\x12\x19.noderesources.EmptyQuery\x1a\x17.noderesources.ShardIds\"\x00\x12\x44\n\x02GC\x12\x16.noderesources.ShardId\x1a$.nodewriter.GarbageCollectorResponse\"\x00\x12<\n\x05Merge\x12\x16.noderesources.ShardId\x1a\x19.nodewriter.MergeResponse\"\x00\x12>\n\x0bSetResource\x12\x17.noderesources.Resource\x1a\x14.nodewriter.OpStatus\"\x00\x12\x43\n\x0eRemoveResource\x12\x19.noderesources.ResourceID\x1a\x14.nodewriter.OpStatus\"\x00\x12G\n\x0c\x41\x64\x64VectorSet\x12\x1f.nodewriter.NewVectorSetRequest\x1a\x14.nodewriter.OpStatus\"\x00\x12\x45\n\x0fRemoveVectorSet\x12\x1a.noderesources.VectorSetID\x1a\x14.nodewriter.OpStatus\"\x00\x12H\n\x0eListVectorSets\x12\x16.noderesources.ShardId\x1a\x1c.noderesources.VectorSetList\"\x00\x12G\n\x0bGetMetadata\x12\x19.noderesources.EmptyQuery\x1a\x1b.noderesources.NodeMetadata\"\x00P\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.nodewriter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TYPEMESSAGE']._serialized_start=1059
  _globals['_TYPEMESSAGE']._serialized_end=1100
  _globals['_INDEXMESSAGESOURCE']._serialized_start=1102
  _globals['_INDEXMESSAGESOURCE']._serialized_end=1149
  _globals['_OPSTATUS']._serialized_start=86
  _globals['_OPSTATUS']._serialized_end=287
  _globals['_OPSTATUS_STATUS']._serialized_start=247
  _globals['_OPSTATUS_STATUS']._serialized_end=287
  _globals['_INDEXMESSAGE']._serialized_start=290
  _globals['_INDEXMESSAGE']._serialized_end=552
  _globals['_GARBAGECOLLECTORRESPONSE']._serialized_start=554
  _globals['_GARBAGECOLLECTORRESPONSE']._serialized_end=674
  _globals['_GARBAGECOLLECTORRESPONSE_STATUS']._serialized_start=643
  _globals['_GARBAGECOLLECTORRESPONSE_STATUS']._serialized_end=674
  _globals['_NEWSHARDREQUEST']._serialized_start=676
  _globals['_NEWSHARDREQUEST']._serialized_end=800
  _globals['_NEWVECTORSETREQUEST']._serialized_start=802
  _globals['_NEWVECTORSETREQUEST']._serialized_end=908
  _globals['_MERGERESPONSE']._serialized_start=911
  _globals['_MERGERESPONSE']._serialized_end=1057
  _globals['_MERGERESPONSE_MERGESTATUS']._serialized_start=1036
  _globals['_MERGERESPONSE_MERGESTATUS']._serialized_end=1057
  _globals['_NODEWRITER']._serialized_start=1152
  _globals['_NODEWRITER']._serialized_end=1925
# @@protoc_insertion_point(module_scope)
