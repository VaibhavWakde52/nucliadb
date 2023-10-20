"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PrimaryShardReplicationState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHARD_ID_FIELD_NUMBER: builtins.int
    GENERATION_ID_FIELD_NUMBER: builtins.int
    KBID_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    shard_id: builtins.str
    generation_id: builtins.str
    """ID to identify the generation of the shard to know
    if there is a new version of the shard available to download
    """
    kbid: builtins.str
    similarity: builtins.str
    def __init__(
        self,
        *,
        shard_id: builtins.str = ...,
        generation_id: builtins.str = ...,
        kbid: builtins.str = ...,
        similarity: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["generation_id", b"generation_id", "kbid", b"kbid", "shard_id", b"shard_id", "similarity", b"similarity"]) -> None: ...

global___PrimaryShardReplicationState = PrimaryShardReplicationState

@typing_extensions.final
class SecondaryShardReplicationState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHARD_ID_FIELD_NUMBER: builtins.int
    GENERATION_ID_FIELD_NUMBER: builtins.int
    shard_id: builtins.str
    generation_id: builtins.str
    """ID to identify the generation of the shard to know
    if there is a new version of the shard available to download
    """
    def __init__(
        self,
        *,
        shard_id: builtins.str = ...,
        generation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["generation_id", b"generation_id", "shard_id", b"shard_id"]) -> None: ...

global___SecondaryShardReplicationState = SecondaryShardReplicationState

@typing_extensions.final
class SecondaryCheckReplicationStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECONDARY_ID_FIELD_NUMBER: builtins.int
    SHARD_STATES_FIELD_NUMBER: builtins.int
    secondary_id: builtins.str
    @property
    def shard_states(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SecondaryShardReplicationState]: ...
    def __init__(
        self,
        *,
        secondary_id: builtins.str = ...,
        shard_states: collections.abc.Iterable[global___SecondaryShardReplicationState] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["secondary_id", b"secondary_id", "shard_states", b"shard_states"]) -> None: ...

global___SecondaryCheckReplicationStateRequest = SecondaryCheckReplicationStateRequest

@typing_extensions.final
class PrimaryCheckReplicationStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHARD_STATES_FIELD_NUMBER: builtins.int
    @property
    def shard_states(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PrimaryShardReplicationState]: ...
    def __init__(
        self,
        *,
        shard_states: collections.abc.Iterable[global___PrimaryShardReplicationState] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["shard_states", b"shard_states"]) -> None: ...

global___PrimaryCheckReplicationStateResponse = PrimaryCheckReplicationStateResponse

@typing_extensions.final
class SegmentIds(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["items", b"items"]) -> None: ...

global___SegmentIds = SegmentIds

@typing_extensions.final
class ReplicateShardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ExistingSegmentIdsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___SegmentIds: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___SegmentIds | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SHARD_ID_FIELD_NUMBER: builtins.int
    EXISTING_SEGMENT_IDS_FIELD_NUMBER: builtins.int
    CHUNK_SIZE_FIELD_NUMBER: builtins.int
    shard_id: builtins.str
    @property
    def existing_segment_ids(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___SegmentIds]:
        """list of existing segment ids so we replicate same shards again"""
    chunk_size: builtins.int
    def __init__(
        self,
        *,
        shard_id: builtins.str = ...,
        existing_segment_ids: collections.abc.Mapping[builtins.str, global___SegmentIds] | None = ...,
        chunk_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunk_size", b"chunk_size", "existing_segment_ids", b"existing_segment_ids", "shard_id", b"shard_id"]) -> None: ...

global___ReplicateShardRequest = ReplicateShardRequest

@typing_extensions.final
class ReplicateShardResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GENERATION_ID_FIELD_NUMBER: builtins.int
    FILEPATH_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    CHUNK_FIELD_NUMBER: builtins.int
    READ_POSITION_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    generation_id: builtins.str
    filepath: builtins.str
    data: builtins.bytes
    chunk: builtins.int
    read_position: builtins.int
    total_size: builtins.int
    def __init__(
        self,
        *,
        generation_id: builtins.str = ...,
        filepath: builtins.str = ...,
        data: builtins.bytes = ...,
        chunk: builtins.int = ...,
        read_position: builtins.int = ...,
        total_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunk", b"chunk", "data", b"data", "filepath", b"filepath", "generation_id", b"generation_id", "read_position", b"read_position", "total_size", b"total_size"]) -> None: ...

global___ReplicateShardResponse = ReplicateShardResponse
