"""
Type annotations for kendra service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra import KendraClient

    client: KendraClient = boto3.client("kendra")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    FaqFileFormatType,
    IndexEditionType,
    QueryResultTypeType,
    UserContextPolicyType,
)
from .type_defs import (
    AttributeFilterTypeDef,
    BatchDeleteDocumentResponseTypeDef,
    BatchPutDocumentResponseTypeDef,
    CapacityUnitsConfigurationTypeDef,
    ClickFeedbackTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFaqResponseTypeDef,
    CreateIndexResponseTypeDef,
    CreateThesaurusResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DataSourceSyncJobMetricTargetTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeFaqResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DescribeThesaurusResponseTypeDef,
    DocumentMetadataConfigurationTypeDef,
    DocumentRelevanceConfigurationTypeDef,
    DocumentTypeDef,
    FacetTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListFaqsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThesauriResponseTypeDef,
    QueryResultTypeDef,
    RelevanceFeedbackTypeDef,
    S3PathTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    SortingConfigurationTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    TagTypeDef,
    TimeRangeTypeDef,
    UserContextTypeDef,
    UserTokenConfigurationTypeDef,
)

__all__ = ("KendraClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceAlreadyExistException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class KendraClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def batch_delete_document(
        self,
        IndexId: str,
        DocumentIdList: List[str],
        DataSourceSyncJobMetricTarget: DataSourceSyncJobMetricTargetTypeDef = None,
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.batch_delete_document)
        [Show boto3-stubs documentation](./client.md#batch_delete_document)
        """
    def batch_put_document(
        self, IndexId: str, Documents: List[DocumentTypeDef], RoleArn: str = None
    ) -> BatchPutDocumentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.batch_put_document)
        [Show boto3-stubs documentation](./client.md#batch_put_document)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def create_data_source(
        self,
        Name: str,
        IndexId: str,
        Type: DataSourceTypeType,
        Configuration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.create_data_source)
        [Show boto3-stubs documentation](./client.md#create_data_source)
        """
    def create_faq(
        self,
        IndexId: str,
        Name: str,
        S3Path: "S3PathTypeDef",
        RoleArn: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        FileFormat: FaqFileFormatType = None,
        ClientToken: str = None,
    ) -> CreateFaqResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.create_faq)
        [Show boto3-stubs documentation](./client.md#create_faq)
        """
    def create_index(
        self,
        Name: str,
        RoleArn: str,
        Edition: IndexEditionType = None,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef" = None,
        Description: str = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None,
        UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
        UserContextPolicy: UserContextPolicyType = None,
    ) -> CreateIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.create_index)
        [Show boto3-stubs documentation](./client.md#create_index)
        """
    def create_thesaurus(
        self,
        IndexId: str,
        Name: str,
        RoleArn: str,
        SourceS3Path: "S3PathTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
    ) -> CreateThesaurusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.create_thesaurus)
        [Show boto3-stubs documentation](./client.md#create_thesaurus)
        """
    def delete_data_source(self, Id: str, IndexId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.delete_data_source)
        [Show boto3-stubs documentation](./client.md#delete_data_source)
        """
    def delete_faq(self, Id: str, IndexId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.delete_faq)
        [Show boto3-stubs documentation](./client.md#delete_faq)
        """
    def delete_index(self, Id: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.delete_index)
        [Show boto3-stubs documentation](./client.md#delete_index)
        """
    def delete_thesaurus(self, Id: str, IndexId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.delete_thesaurus)
        [Show boto3-stubs documentation](./client.md#delete_thesaurus)
        """
    def describe_data_source(self, Id: str, IndexId: str) -> DescribeDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.describe_data_source)
        [Show boto3-stubs documentation](./client.md#describe_data_source)
        """
    def describe_faq(self, Id: str, IndexId: str) -> DescribeFaqResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.describe_faq)
        [Show boto3-stubs documentation](./client.md#describe_faq)
        """
    def describe_index(self, Id: str) -> DescribeIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.describe_index)
        [Show boto3-stubs documentation](./client.md#describe_index)
        """
    def describe_thesaurus(self, Id: str, IndexId: str) -> DescribeThesaurusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.describe_thesaurus)
        [Show boto3-stubs documentation](./client.md#describe_thesaurus)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def list_data_source_sync_jobs(
        self,
        Id: str,
        IndexId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartTimeFilter: TimeRangeTypeDef = None,
        StatusFilter: DataSourceSyncJobStatusType = None,
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.list_data_source_sync_jobs)
        [Show boto3-stubs documentation](./client.md#list_data_source_sync_jobs)
        """
    def list_data_sources(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.list_data_sources)
        [Show boto3-stubs documentation](./client.md#list_data_sources)
        """
    def list_faqs(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFaqsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.list_faqs)
        [Show boto3-stubs documentation](./client.md#list_faqs)
        """
    def list_indices(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.list_indices)
        [Show boto3-stubs documentation](./client.md#list_indices)
        """
    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def list_thesauri(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThesauriResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.list_thesauri)
        [Show boto3-stubs documentation](./client.md#list_thesauri)
        """
    def query(
        self,
        IndexId: str,
        QueryText: str,
        AttributeFilter: "AttributeFilterTypeDef" = None,
        Facets: List[FacetTypeDef] = None,
        RequestedDocumentAttributes: List[str] = None,
        QueryResultTypeFilter: QueryResultTypeType = None,
        DocumentRelevanceOverrideConfigurations: List[DocumentRelevanceConfigurationTypeDef] = None,
        PageNumber: int = None,
        PageSize: int = None,
        SortingConfiguration: SortingConfigurationTypeDef = None,
        UserContext: UserContextTypeDef = None,
        VisitorId: str = None,
    ) -> QueryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.query)
        [Show boto3-stubs documentation](./client.md#query)
        """
    def start_data_source_sync_job(
        self, Id: str, IndexId: str
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.start_data_source_sync_job)
        [Show boto3-stubs documentation](./client.md#start_data_source_sync_job)
        """
    def stop_data_source_sync_job(self, Id: str, IndexId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.stop_data_source_sync_job)
        [Show boto3-stubs documentation](./client.md#stop_data_source_sync_job)
        """
    def submit_feedback(
        self,
        IndexId: str,
        QueryId: str,
        ClickFeedbackItems: List[ClickFeedbackTypeDef] = None,
        RelevanceFeedbackItems: List[RelevanceFeedbackTypeDef] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.submit_feedback)
        [Show boto3-stubs documentation](./client.md#submit_feedback)
        """
    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """
    def update_data_source(
        self,
        Id: str,
        IndexId: str,
        Name: str = None,
        Configuration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.update_data_source)
        [Show boto3-stubs documentation](./client.md#update_data_source)
        """
    def update_index(
        self,
        Id: str,
        Name: str = None,
        RoleArn: str = None,
        Description: str = None,
        DocumentMetadataConfigurationUpdates: List["DocumentMetadataConfigurationTypeDef"] = None,
        CapacityUnits: "CapacityUnitsConfigurationTypeDef" = None,
        UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
        UserContextPolicy: UserContextPolicyType = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.update_index)
        [Show boto3-stubs documentation](./client.md#update_index)
        """
    def update_thesaurus(
        self,
        Id: str,
        IndexId: str,
        Name: str = None,
        Description: str = None,
        RoleArn: str = None,
        SourceS3Path: "S3PathTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kendra.html#Kendra.Client.update_thesaurus)
        [Show boto3-stubs documentation](./client.md#update_thesaurus)
        """
