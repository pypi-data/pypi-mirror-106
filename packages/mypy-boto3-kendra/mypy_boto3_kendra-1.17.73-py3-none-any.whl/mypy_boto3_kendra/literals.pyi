"""
Type annotations for kendra service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_kendra.literals import AdditionalResultAttributeValueTypeType

    data: AdditionalResultAttributeValueTypeType = "TEXT_WITH_HIGHLIGHTS_VALUE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdditionalResultAttributeValueTypeType",
    "ConfluenceAttachmentFieldNameType",
    "ConfluenceBlogFieldNameType",
    "ConfluencePageFieldNameType",
    "ConfluenceSpaceFieldNameType",
    "ConfluenceVersionType",
    "ContentTypeType",
    "DataSourceStatusType",
    "DataSourceSyncJobStatusType",
    "DataSourceTypeType",
    "DatabaseEngineTypeType",
    "DocumentAttributeValueTypeType",
    "ErrorCodeType",
    "FaqFileFormatType",
    "FaqStatusType",
    "HighlightTypeType",
    "IndexEditionType",
    "IndexStatusType",
    "KeyLocationType",
    "OrderType",
    "PrincipalTypeType",
    "QueryIdentifiersEnclosingOptionType",
    "QueryResultTypeType",
    "ReadAccessTypeType",
    "RelevanceTypeType",
    "SalesforceChatterFeedIncludeFilterTypeType",
    "SalesforceKnowledgeArticleStateType",
    "SalesforceStandardObjectNameType",
    "ScoreConfidenceType",
    "ServiceNowAuthenticationTypeType",
    "ServiceNowBuildVersionTypeType",
    "SharePointVersionType",
    "SortOrderType",
    "ThesaurusStatusType",
    "UserContextPolicyType",
)

AdditionalResultAttributeValueTypeType = Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
ConfluenceAttachmentFieldNameType = Literal[
    "AUTHOR",
    "CONTENT_TYPE",
    "CREATED_DATE",
    "DISPLAY_URL",
    "FILE_SIZE",
    "ITEM_TYPE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluenceBlogFieldNameType = Literal[
    "AUTHOR",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "PUBLISH_DATE",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluencePageFieldNameType = Literal[
    "AUTHOR",
    "CONTENT_STATUS",
    "CREATED_DATE",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "MODIFIED_DATE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluenceSpaceFieldNameType = Literal["DISPLAY_URL", "ITEM_TYPE", "SPACE_KEY", "URL"]
ConfluenceVersionType = Literal["CLOUD", "SERVER"]
ContentTypeType = Literal["HTML", "MS_WORD", "PDF", "PLAIN_TEXT", "PPT"]
DataSourceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
DataSourceSyncJobStatusType = Literal[
    "ABORTED", "FAILED", "INCOMPLETE", "STOPPING", "SUCCEEDED", "SYNCING", "SYNCING_INDEXING"
]
DataSourceTypeType = Literal[
    "CONFLUENCE",
    "CUSTOM",
    "DATABASE",
    "GOOGLEDRIVE",
    "ONEDRIVE",
    "S3",
    "SALESFORCE",
    "SERVICENOW",
    "SHAREPOINT",
]
DatabaseEngineTypeType = Literal[
    "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
]
DocumentAttributeValueTypeType = Literal[
    "DATE_VALUE", "LONG_VALUE", "STRING_LIST_VALUE", "STRING_VALUE"
]
ErrorCodeType = Literal["InternalError", "InvalidRequest"]
FaqFileFormatType = Literal["CSV", "CSV_WITH_HEADER", "JSON"]
FaqStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
HighlightTypeType = Literal["STANDARD", "THESAURUS_SYNONYM"]
IndexEditionType = Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "SYSTEM_UPDATING", "UPDATING"]
KeyLocationType = Literal["SECRET_MANAGER", "URL"]
OrderType = Literal["ASCENDING", "DESCENDING"]
PrincipalTypeType = Literal["GROUP", "USER"]
QueryIdentifiersEnclosingOptionType = Literal["DOUBLE_QUOTES", "NONE"]
QueryResultTypeType = Literal["ANSWER", "DOCUMENT", "QUESTION_ANSWER"]
ReadAccessTypeType = Literal["ALLOW", "DENY"]
RelevanceTypeType = Literal["NOT_RELEVANT", "RELEVANT"]
SalesforceChatterFeedIncludeFilterTypeType = Literal["ACTIVE_USER", "STANDARD_USER"]
SalesforceKnowledgeArticleStateType = Literal["ARCHIVED", "DRAFT", "PUBLISHED"]
SalesforceStandardObjectNameType = Literal[
    "ACCOUNT",
    "CAMPAIGN",
    "CASE",
    "CONTACT",
    "CONTRACT",
    "DOCUMENT",
    "GROUP",
    "IDEA",
    "LEAD",
    "OPPORTUNITY",
    "PARTNER",
    "PRICEBOOK",
    "PRODUCT",
    "PROFILE",
    "SOLUTION",
    "TASK",
    "USER",
]
ScoreConfidenceType = Literal["HIGH", "LOW", "MEDIUM", "VERY_HIGH"]
ServiceNowAuthenticationTypeType = Literal["HTTP_BASIC", "OAUTH2"]
ServiceNowBuildVersionTypeType = Literal["LONDON", "OTHERS"]
SharePointVersionType = Literal["SHAREPOINT_ONLINE"]
SortOrderType = Literal["ASC", "DESC"]
ThesaurusStatusType = Literal[
    "ACTIVE", "ACTIVE_BUT_UPDATE_FAILED", "CREATING", "DELETING", "FAILED", "UPDATING"
]
UserContextPolicyType = Literal["ATTRIBUTE_FILTER", "USER_TOKEN"]
