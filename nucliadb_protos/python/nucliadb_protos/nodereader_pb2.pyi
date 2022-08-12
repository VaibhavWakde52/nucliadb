"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions
from nucliadb_protos.noderesources_pb2 import (
    EmptyQuery as EmptyQuery,
    EmptyResponse as EmptyResponse,
    IndexMetadata as IndexMetadata,
    IndexParagraph as IndexParagraph,
    IndexParagraphs as IndexParagraphs,
    Resource as Resource,
    ResourceID as ResourceID,
    Shard as Shard,
    ShardCreated as ShardCreated,
    ShardId as ShardId,
    ShardIds as ShardIds,
    ShardList as ShardList,
    TextInformation as TextInformation,
    VectorSentence as VectorSentence,
)

from nucliadb_protos.utils_pb2 import (
    EntityRelation as EntityRelation,
    ExtractedText as ExtractedText,
    Relation as Relation,
    Vector as Vector,
    VectorObject as VectorObject,
    Vectors as Vectors,
)


DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Filter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        tags: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tags",b"tags"]) -> None: ...
global___Filter = Filter

class Faceted(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TAGS_FIELD_NUMBER: builtins.int
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        tags: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tags",b"tags"]) -> None: ...
global___Faceted = Faceted

class OrderBy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _OrderType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OrderTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[OrderBy._OrderType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DESC: OrderBy._OrderType.ValueType  # 0
        ASC: OrderBy._OrderType.ValueType  # 1
    class OrderType(_OrderType, metaclass=_OrderTypeEnumTypeWrapper):
        pass

    DESC: OrderBy.OrderType.ValueType  # 0
    ASC: OrderBy.OrderType.ValueType  # 1

    FIELD_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    field: typing.Text
    type: global___OrderBy.OrderType.ValueType
    def __init__(self,
        *,
        field: typing.Text = ...,
        type: global___OrderBy.OrderType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["field",b"field","type",b"type"]) -> None: ...
global___OrderBy = OrderBy

class Timestamps(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FROM_MODIFIED_FIELD_NUMBER: builtins.int
    TO_MODIFIED_FIELD_NUMBER: builtins.int
    FROM_CREATED_FIELD_NUMBER: builtins.int
    TO_CREATED_FIELD_NUMBER: builtins.int
    @property
    def from_modified(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def to_modified(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def from_created(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def to_created(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        from_modified: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        to_modified: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        from_created: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        to_created: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["from_created",b"from_created","from_modified",b"from_modified","to_created",b"to_created","to_modified",b"to_modified"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["from_created",b"from_created","from_modified",b"from_modified","to_created",b"to_created","to_modified",b"to_modified"]) -> None: ...
global___Timestamps = Timestamps

class FacetResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TAG_FIELD_NUMBER: builtins.int
    TOTAL_FIELD_NUMBER: builtins.int
    tag: typing.Text
    total: builtins.int
    def __init__(self,
        *,
        tag: typing.Text = ...,
        total: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tag",b"tag","total",b"total"]) -> None: ...
global___FacetResult = FacetResult

class FacetResults(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FACETRESULTS_FIELD_NUMBER: builtins.int
    @property
    def facetresults(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FacetResult]: ...
    def __init__(self,
        *,
        facetresults: typing.Optional[typing.Iterable[global___FacetResult]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["facetresults",b"facetresults"]) -> None: ...
global___FacetResults = FacetResults

class DocumentSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    FACETED_FIELD_NUMBER: builtins.int
    PAGE_NUMBER_FIELD_NUMBER: builtins.int
    RESULT_PER_PAGE_FIELD_NUMBER: builtins.int
    TIMESTAMPS_FIELD_NUMBER: builtins.int
    RELOAD_FIELD_NUMBER: builtins.int
    id: typing.Text
    body: typing.Text
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def filter(self) -> global___Filter: ...
    @property
    def order(self) -> global___OrderBy: ...
    @property
    def faceted(self) -> global___Faceted: ...
    page_number: builtins.int
    result_per_page: builtins.int
    @property
    def timestamps(self) -> global___Timestamps: ...
    reload: builtins.bool
    def __init__(self,
        *,
        id: typing.Text = ...,
        body: typing.Text = ...,
        fields: typing.Optional[typing.Iterable[typing.Text]] = ...,
        filter: typing.Optional[global___Filter] = ...,
        order: typing.Optional[global___OrderBy] = ...,
        faceted: typing.Optional[global___Faceted] = ...,
        page_number: builtins.int = ...,
        result_per_page: builtins.int = ...,
        timestamps: typing.Optional[global___Timestamps] = ...,
        reload: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["faceted",b"faceted","filter",b"filter","order",b"order","timestamps",b"timestamps"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","faceted",b"faceted","fields",b"fields","filter",b"filter","id",b"id","order",b"order","page_number",b"page_number","reload",b"reload","result_per_page",b"result_per_page","timestamps",b"timestamps"]) -> None: ...
global___DocumentSearchRequest = DocumentSearchRequest

class ParagraphSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    FACETED_FIELD_NUMBER: builtins.int
    PAGE_NUMBER_FIELD_NUMBER: builtins.int
    RESULT_PER_PAGE_FIELD_NUMBER: builtins.int
    TIMESTAMPS_FIELD_NUMBER: builtins.int
    RELOAD_FIELD_NUMBER: builtins.int
    id: typing.Text
    uuid: typing.Text
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    body: typing.Text
    """query this text in all the paragraphs"""

    @property
    def filter(self) -> global___Filter: ...
    @property
    def order(self) -> global___OrderBy: ...
    @property
    def faceted(self) -> global___Faceted:
        """Faceted{ tags: Vec<String>}"""
        pass
    page_number: builtins.int
    result_per_page: builtins.int
    @property
    def timestamps(self) -> global___Timestamps: ...
    reload: builtins.bool
    def __init__(self,
        *,
        id: typing.Text = ...,
        uuid: typing.Text = ...,
        fields: typing.Optional[typing.Iterable[typing.Text]] = ...,
        body: typing.Text = ...,
        filter: typing.Optional[global___Filter] = ...,
        order: typing.Optional[global___OrderBy] = ...,
        faceted: typing.Optional[global___Faceted] = ...,
        page_number: builtins.int = ...,
        result_per_page: builtins.int = ...,
        timestamps: typing.Optional[global___Timestamps] = ...,
        reload: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["faceted",b"faceted","filter",b"filter","order",b"order","timestamps",b"timestamps"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","faceted",b"faceted","fields",b"fields","filter",b"filter","id",b"id","order",b"order","page_number",b"page_number","reload",b"reload","result_per_page",b"result_per_page","timestamps",b"timestamps","uuid",b"uuid"]) -> None: ...
global___ParagraphSearchRequest = ParagraphSearchRequest

class DocumentResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UUID_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    SCORE_BM25_FIELD_NUMBER: builtins.int
    FIELD_FIELD_NUMBER: builtins.int
    uuid: typing.Text
    score: builtins.int
    score_bm25: builtins.float
    field: typing.Text
    def __init__(self,
        *,
        uuid: typing.Text = ...,
        score: builtins.int = ...,
        score_bm25: builtins.float = ...,
        field: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["field",b"field","score",b"score","score_bm25",b"score_bm25","uuid",b"uuid"]) -> None: ...
global___DocumentResult = DocumentResult

class DocumentSearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class FacetsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___FacetResults: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___FacetResults] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    TOTAL_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    FACETS_FIELD_NUMBER: builtins.int
    PAGE_NUMBER_FIELD_NUMBER: builtins.int
    RESULT_PER_PAGE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    total: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DocumentResult]: ...
    @property
    def facets(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___FacetResults]: ...
    page_number: builtins.int
    result_per_page: builtins.int
    query: typing.Text
    """The text that lead to this results"""

    def __init__(self,
        *,
        total: builtins.int = ...,
        results: typing.Optional[typing.Iterable[global___DocumentResult]] = ...,
        facets: typing.Optional[typing.Mapping[typing.Text, global___FacetResults]] = ...,
        page_number: builtins.int = ...,
        result_per_page: builtins.int = ...,
        query: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["facets",b"facets","page_number",b"page_number","query",b"query","result_per_page",b"result_per_page","results",b"results","total",b"total"]) -> None: ...
global___DocumentSearchResponse = DocumentSearchResponse

class ParagraphResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UUID_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    FIELD_FIELD_NUMBER: builtins.int
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    PARAGRAPH_FIELD_NUMBER: builtins.int
    SPLIT_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    uuid: typing.Text
    score: builtins.float
    field: typing.Text
    start: builtins.int
    end: builtins.int
    paragraph: typing.Text
    split: typing.Text
    index: builtins.int
    def __init__(self,
        *,
        uuid: typing.Text = ...,
        score: builtins.float = ...,
        field: typing.Text = ...,
        start: builtins.int = ...,
        end: builtins.int = ...,
        paragraph: typing.Text = ...,
        split: typing.Text = ...,
        index: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["end",b"end","field",b"field","index",b"index","paragraph",b"paragraph","score",b"score","split",b"split","start",b"start","uuid",b"uuid"]) -> None: ...
global___ParagraphResult = ParagraphResult

class ParagraphSearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class FacetsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___FacetResults: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___FacetResults] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    TOTAL_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    FACETS_FIELD_NUMBER: builtins.int
    PAGE_NUMBER_FIELD_NUMBER: builtins.int
    RESULT_PER_PAGE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    total: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParagraphResult]:
        """"""
        pass
    @property
    def facets(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___FacetResults]:
        """For each field what facets are."""
        pass
    page_number: builtins.int
    """What page is the answer."""

    result_per_page: builtins.int
    """How many results are in this page."""

    query: typing.Text
    """The text that lead to this results"""

    def __init__(self,
        *,
        total: builtins.int = ...,
        results: typing.Optional[typing.Iterable[global___ParagraphResult]] = ...,
        facets: typing.Optional[typing.Mapping[typing.Text, global___FacetResults]] = ...,
        page_number: builtins.int = ...,
        result_per_page: builtins.int = ...,
        query: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["facets",b"facets","page_number",b"page_number","query",b"query","result_per_page",b"result_per_page","results",b"results","total",b"total"]) -> None: ...
global___ParagraphSearchResponse = ParagraphSearchResponse

class VectorSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VECTOR_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    RELOAD_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Shard ID"""

    @property
    def vector(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Embedded vector search."""
        pass
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """tags to filter"""
        pass
    reload: builtins.bool
    def __init__(self,
        *,
        id: typing.Text = ...,
        vector: typing.Optional[typing.Iterable[builtins.float]] = ...,
        tags: typing.Optional[typing.Iterable[typing.Text]] = ...,
        reload: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","reload",b"reload","tags",b"tags","vector",b"vector"]) -> None: ...
global___VectorSearchRequest = VectorSearchRequest

class DocumentVectorIdentifier(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___DocumentVectorIdentifier = DocumentVectorIdentifier

class DocumentScored(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOC_ID_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    @property
    def doc_id(self) -> global___DocumentVectorIdentifier: ...
    score: builtins.float
    def __init__(self,
        *,
        doc_id: typing.Optional[global___DocumentVectorIdentifier] = ...,
        score: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["doc_id",b"doc_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["doc_id",b"doc_id","score",b"score"]) -> None: ...
global___DocumentScored = DocumentScored

class VectorSearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOCUMENTS_FIELD_NUMBER: builtins.int
    @property
    def documents(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DocumentScored]:
        """List of docs closer to the asked one."""
        pass
    def __init__(self,
        *,
        documents: typing.Optional[typing.Iterable[global___DocumentScored]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["documents",b"documents"]) -> None: ...
global___VectorSearchResponse = VectorSearchResponse

class RelationSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RelationSearchRequest = RelationSearchRequest

class RelationSearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RelationSearchResponse = RelationSearchResponse

class SearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHARD_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    FACETED_FIELD_NUMBER: builtins.int
    PAGE_NUMBER_FIELD_NUMBER: builtins.int
    RESULT_PER_PAGE_FIELD_NUMBER: builtins.int
    TIMESTAMPS_FIELD_NUMBER: builtins.int
    VECTOR_FIELD_NUMBER: builtins.int
    RELOAD_FIELD_NUMBER: builtins.int
    PARAGRAPH_FIELD_NUMBER: builtins.int
    DOCUMENT_FIELD_NUMBER: builtins.int
    shard: typing.Text
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    body: typing.Text
    """query this text in all the paragraphs"""

    @property
    def filter(self) -> global___Filter: ...
    @property
    def order(self) -> global___OrderBy: ...
    @property
    def faceted(self) -> global___Faceted:
        """Faceted{ tags: Vec<String>}"""
        pass
    page_number: builtins.int
    result_per_page: builtins.int
    @property
    def timestamps(self) -> global___Timestamps: ...
    @property
    def vector(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Embedded vector search."""
        pass
    reload: builtins.bool
    paragraph: builtins.bool
    document: builtins.bool
    def __init__(self,
        *,
        shard: typing.Text = ...,
        fields: typing.Optional[typing.Iterable[typing.Text]] = ...,
        body: typing.Text = ...,
        filter: typing.Optional[global___Filter] = ...,
        order: typing.Optional[global___OrderBy] = ...,
        faceted: typing.Optional[global___Faceted] = ...,
        page_number: builtins.int = ...,
        result_per_page: builtins.int = ...,
        timestamps: typing.Optional[global___Timestamps] = ...,
        vector: typing.Optional[typing.Iterable[builtins.float]] = ...,
        reload: builtins.bool = ...,
        paragraph: builtins.bool = ...,
        document: builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["faceted",b"faceted","filter",b"filter","order",b"order","timestamps",b"timestamps"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","document",b"document","faceted",b"faceted","fields",b"fields","filter",b"filter","order",b"order","page_number",b"page_number","paragraph",b"paragraph","reload",b"reload","result_per_page",b"result_per_page","shard",b"shard","timestamps",b"timestamps","vector",b"vector"]) -> None: ...
global___SearchRequest = SearchRequest

class SuggestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHARD_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    TIMESTAMPS_FIELD_NUMBER: builtins.int
    shard: typing.Text
    body: typing.Text
    @property
    def filter(self) -> global___Filter: ...
    @property
    def timestamps(self) -> global___Timestamps: ...
    def __init__(self,
        *,
        shard: typing.Text = ...,
        body: typing.Text = ...,
        filter: typing.Optional[global___Filter] = ...,
        timestamps: typing.Optional[global___Timestamps] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter","timestamps",b"timestamps"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","filter",b"filter","shard",b"shard","timestamps",b"timestamps"]) -> None: ...
global___SuggestRequest = SuggestRequest

class SuggestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOTAL_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    total: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParagraphResult]: ...
    query: typing.Text
    """The text that lead to this results"""

    def __init__(self,
        *,
        total: builtins.int = ...,
        results: typing.Optional[typing.Iterable[global___ParagraphResult]] = ...,
        query: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["query",b"query","results",b"results","total",b"total"]) -> None: ...
global___SuggestResponse = SuggestResponse

class SearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOCUMENT_FIELD_NUMBER: builtins.int
    PARAGRAPH_FIELD_NUMBER: builtins.int
    VECTOR_FIELD_NUMBER: builtins.int
    @property
    def document(self) -> global___DocumentSearchResponse: ...
    @property
    def paragraph(self) -> global___ParagraphSearchResponse: ...
    @property
    def vector(self) -> global___VectorSearchResponse: ...
    def __init__(self,
        *,
        document: typing.Optional[global___DocumentSearchResponse] = ...,
        paragraph: typing.Optional[global___ParagraphSearchResponse] = ...,
        vector: typing.Optional[global___VectorSearchResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["document",b"document","paragraph",b"paragraph","vector",b"vector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["document",b"document","paragraph",b"paragraph","vector",b"vector"]) -> None: ...
global___SearchResponse = SearchResponse

class IdCollection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IDS_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ids",b"ids"]) -> None: ...
global___IdCollection = IdCollection
