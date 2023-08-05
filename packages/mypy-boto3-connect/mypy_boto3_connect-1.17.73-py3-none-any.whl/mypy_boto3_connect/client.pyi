"""
Type annotations for connect service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_connect import ConnectClient

    client: ConnectClient = boto3.client("connect")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ContactFlowTypeType,
    DirectoryTypeType,
    GroupingType,
    InstanceAttributeTypeType,
    InstanceStorageResourceTypeType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    SourceTypeType,
)
from .paginator import (
    GetMetricDataPaginator,
    ListApprovedOriginsPaginator,
    ListContactFlowsPaginator,
    ListHoursOfOperationsPaginator,
    ListInstanceAttributesPaginator,
    ListInstancesPaginator,
    ListInstanceStorageConfigsPaginator,
    ListIntegrationAssociationsPaginator,
    ListLambdaFunctionsPaginator,
    ListLexBotsPaginator,
    ListPhoneNumbersPaginator,
    ListPromptsPaginator,
    ListQueueQuickConnectsPaginator,
    ListQueuesPaginator,
    ListQuickConnectsPaginator,
    ListRoutingProfileQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListSecurityKeysPaginator,
    ListSecurityProfilesPaginator,
    ListUseCasesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AssociateInstanceStorageConfigResponseTypeDef,
    AssociateSecurityKeyResponseTypeDef,
    ChatMessageTypeDef,
    CreateContactFlowResponseTypeDef,
    CreateInstanceResponseTypeDef,
    CreateIntegrationAssociationResponseTypeDef,
    CreateQueueResponseTypeDef,
    CreateQuickConnectResponseTypeDef,
    CreateRoutingProfileResponseTypeDef,
    CreateUseCaseResponseTypeDef,
    CreateUserHierarchyGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    CurrentMetricTypeDef,
    DescribeContactFlowResponseTypeDef,
    DescribeHoursOfOperationResponseTypeDef,
    DescribeInstanceAttributeResponseTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribeInstanceStorageConfigResponseTypeDef,
    DescribeQueueResponseTypeDef,
    DescribeQuickConnectResponseTypeDef,
    DescribeRoutingProfileResponseTypeDef,
    DescribeUserHierarchyGroupResponseTypeDef,
    DescribeUserHierarchyStructureResponseTypeDef,
    DescribeUserResponseTypeDef,
    FiltersTypeDef,
    GetContactAttributesResponseTypeDef,
    GetCurrentMetricDataResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetMetricDataResponseTypeDef,
    HierarchyStructureUpdateTypeDef,
    HistoricalMetricTypeDef,
    InstanceStorageConfigTypeDef,
    LexBotTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListContactFlowsResponseTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    MediaConcurrencyTypeDef,
    OutboundCallerConfigTypeDef,
    ParticipantDetailsTypeDef,
    QuickConnectConfigTypeDef,
    ReferenceTypeDef,
    RoutingProfileQueueConfigTypeDef,
    RoutingProfileQueueReferenceTypeDef,
    StartChatContactResponseTypeDef,
    StartOutboundVoiceContactResponseTypeDef,
    StartTaskContactResponseTypeDef,
    UserIdentityInfoTypeDef,
    UserPhoneConfigTypeDef,
    VoiceRecordingConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ContactFlowNotPublishedException: Type[BotocoreClientError]
    ContactNotFoundException: Type[BotocoreClientError]
    DestinationNotAllowedException: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidContactFlowException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OutboundContactNotPermittedException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]

class ConnectClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def associate_approved_origin(self, InstanceId: str, Origin: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_approved_origin)
        [Show boto3-stubs documentation](./client.md#associate_approved_origin)
        """
    def associate_instance_storage_config(
        self,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        StorageConfig: "InstanceStorageConfigTypeDef",
    ) -> AssociateInstanceStorageConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_instance_storage_config)
        [Show boto3-stubs documentation](./client.md#associate_instance_storage_config)
        """
    def associate_lambda_function(self, InstanceId: str, FunctionArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_lambda_function)
        [Show boto3-stubs documentation](./client.md#associate_lambda_function)
        """
    def associate_lex_bot(self, InstanceId: str, LexBot: "LexBotTypeDef") -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_lex_bot)
        [Show boto3-stubs documentation](./client.md#associate_lex_bot)
        """
    def associate_queue_quick_connects(
        self, InstanceId: str, QueueId: str, QuickConnectIds: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_queue_quick_connects)
        [Show boto3-stubs documentation](./client.md#associate_queue_quick_connects)
        """
    def associate_routing_profile_queues(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: List[RoutingProfileQueueConfigTypeDef],
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_routing_profile_queues)
        [Show boto3-stubs documentation](./client.md#associate_routing_profile_queues)
        """
    def associate_security_key(
        self, InstanceId: str, Key: str
    ) -> AssociateSecurityKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.associate_security_key)
        [Show boto3-stubs documentation](./client.md#associate_security_key)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def create_contact_flow(
        self,
        InstanceId: str,
        Name: str,
        Type: ContactFlowTypeType,
        Content: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateContactFlowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_contact_flow)
        [Show boto3-stubs documentation](./client.md#create_contact_flow)
        """
    def create_instance(
        self,
        IdentityManagementType: DirectoryTypeType,
        InboundCallsEnabled: bool,
        OutboundCallsEnabled: bool,
        ClientToken: str = None,
        InstanceAlias: str = None,
        DirectoryId: str = None,
    ) -> CreateInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_instance)
        [Show boto3-stubs documentation](./client.md#create_instance)
        """
    def create_integration_association(
        self,
        InstanceId: str,
        IntegrationType: Literal["EVENT"],
        IntegrationArn: str,
        SourceApplicationUrl: str,
        SourceApplicationName: str,
        SourceType: SourceTypeType,
        Tags: Dict[str, str] = None,
    ) -> CreateIntegrationAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_integration_association)
        [Show boto3-stubs documentation](./client.md#create_integration_association)
        """
    def create_queue(
        self,
        InstanceId: str,
        Name: str,
        HoursOfOperationId: str,
        Description: str = None,
        OutboundCallerConfig: "OutboundCallerConfigTypeDef" = None,
        MaxContacts: int = None,
        QuickConnectIds: List[str] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateQueueResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_queue)
        [Show boto3-stubs documentation](./client.md#create_queue)
        """
    def create_quick_connect(
        self,
        InstanceId: str,
        Name: str,
        QuickConnectConfig: "QuickConnectConfigTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateQuickConnectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_quick_connect)
        [Show boto3-stubs documentation](./client.md#create_quick_connect)
        """
    def create_routing_profile(
        self,
        InstanceId: str,
        Name: str,
        Description: str,
        DefaultOutboundQueueId: str,
        MediaConcurrencies: List["MediaConcurrencyTypeDef"],
        QueueConfigs: List[RoutingProfileQueueConfigTypeDef] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateRoutingProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_routing_profile)
        [Show boto3-stubs documentation](./client.md#create_routing_profile)
        """
    def create_use_case(
        self,
        InstanceId: str,
        IntegrationAssociationId: str,
        UseCaseType: Literal["RULES_EVALUATION"],
        Tags: Dict[str, str] = None,
    ) -> CreateUseCaseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_use_case)
        [Show boto3-stubs documentation](./client.md#create_use_case)
        """
    def create_user(
        self,
        Username: str,
        PhoneConfig: "UserPhoneConfigTypeDef",
        SecurityProfileIds: List[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str = None,
        IdentityInfo: "UserIdentityInfoTypeDef" = None,
        DirectoryUserId: str = None,
        HierarchyGroupId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_user)
        [Show boto3-stubs documentation](./client.md#create_user)
        """
    def create_user_hierarchy_group(
        self, Name: str, InstanceId: str, ParentGroupId: str = None
    ) -> CreateUserHierarchyGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.create_user_hierarchy_group)
        [Show boto3-stubs documentation](./client.md#create_user_hierarchy_group)
        """
    def delete_instance(self, InstanceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.delete_instance)
        [Show boto3-stubs documentation](./client.md#delete_instance)
        """
    def delete_integration_association(
        self, InstanceId: str, IntegrationAssociationId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.delete_integration_association)
        [Show boto3-stubs documentation](./client.md#delete_integration_association)
        """
    def delete_quick_connect(self, InstanceId: str, QuickConnectId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.delete_quick_connect)
        [Show boto3-stubs documentation](./client.md#delete_quick_connect)
        """
    def delete_use_case(
        self, InstanceId: str, IntegrationAssociationId: str, UseCaseId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.delete_use_case)
        [Show boto3-stubs documentation](./client.md#delete_use_case)
        """
    def delete_user(self, InstanceId: str, UserId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.delete_user)
        [Show boto3-stubs documentation](./client.md#delete_user)
        """
    def delete_user_hierarchy_group(self, HierarchyGroupId: str, InstanceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.delete_user_hierarchy_group)
        [Show boto3-stubs documentation](./client.md#delete_user_hierarchy_group)
        """
    def describe_contact_flow(
        self, InstanceId: str, ContactFlowId: str
    ) -> DescribeContactFlowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_contact_flow)
        [Show boto3-stubs documentation](./client.md#describe_contact_flow)
        """
    def describe_hours_of_operation(
        self, InstanceId: str, HoursOfOperationId: str
    ) -> DescribeHoursOfOperationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_hours_of_operation)
        [Show boto3-stubs documentation](./client.md#describe_hours_of_operation)
        """
    def describe_instance(self, InstanceId: str) -> DescribeInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_instance)
        [Show boto3-stubs documentation](./client.md#describe_instance)
        """
    def describe_instance_attribute(
        self, InstanceId: str, AttributeType: InstanceAttributeTypeType
    ) -> DescribeInstanceAttributeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_instance_attribute)
        [Show boto3-stubs documentation](./client.md#describe_instance_attribute)
        """
    def describe_instance_storage_config(
        self, InstanceId: str, AssociationId: str, ResourceType: InstanceStorageResourceTypeType
    ) -> DescribeInstanceStorageConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_instance_storage_config)
        [Show boto3-stubs documentation](./client.md#describe_instance_storage_config)
        """
    def describe_queue(self, InstanceId: str, QueueId: str) -> DescribeQueueResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_queue)
        [Show boto3-stubs documentation](./client.md#describe_queue)
        """
    def describe_quick_connect(
        self, InstanceId: str, QuickConnectId: str
    ) -> DescribeQuickConnectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_quick_connect)
        [Show boto3-stubs documentation](./client.md#describe_quick_connect)
        """
    def describe_routing_profile(
        self, InstanceId: str, RoutingProfileId: str
    ) -> DescribeRoutingProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_routing_profile)
        [Show boto3-stubs documentation](./client.md#describe_routing_profile)
        """
    def describe_user(self, UserId: str, InstanceId: str) -> DescribeUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_user)
        [Show boto3-stubs documentation](./client.md#describe_user)
        """
    def describe_user_hierarchy_group(
        self, HierarchyGroupId: str, InstanceId: str
    ) -> DescribeUserHierarchyGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_user_hierarchy_group)
        [Show boto3-stubs documentation](./client.md#describe_user_hierarchy_group)
        """
    def describe_user_hierarchy_structure(
        self, InstanceId: str
    ) -> DescribeUserHierarchyStructureResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.describe_user_hierarchy_structure)
        [Show boto3-stubs documentation](./client.md#describe_user_hierarchy_structure)
        """
    def disassociate_approved_origin(self, InstanceId: str, Origin: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_approved_origin)
        [Show boto3-stubs documentation](./client.md#disassociate_approved_origin)
        """
    def disassociate_instance_storage_config(
        self, InstanceId: str, AssociationId: str, ResourceType: InstanceStorageResourceTypeType
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_instance_storage_config)
        [Show boto3-stubs documentation](./client.md#disassociate_instance_storage_config)
        """
    def disassociate_lambda_function(self, InstanceId: str, FunctionArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_lambda_function)
        [Show boto3-stubs documentation](./client.md#disassociate_lambda_function)
        """
    def disassociate_lex_bot(self, InstanceId: str, BotName: str, LexRegion: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_lex_bot)
        [Show boto3-stubs documentation](./client.md#disassociate_lex_bot)
        """
    def disassociate_queue_quick_connects(
        self, InstanceId: str, QueueId: str, QuickConnectIds: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_queue_quick_connects)
        [Show boto3-stubs documentation](./client.md#disassociate_queue_quick_connects)
        """
    def disassociate_routing_profile_queues(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        QueueReferences: List["RoutingProfileQueueReferenceTypeDef"],
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_routing_profile_queues)
        [Show boto3-stubs documentation](./client.md#disassociate_routing_profile_queues)
        """
    def disassociate_security_key(self, InstanceId: str, AssociationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.disassociate_security_key)
        [Show boto3-stubs documentation](./client.md#disassociate_security_key)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def get_contact_attributes(
        self, InstanceId: str, InitialContactId: str
    ) -> GetContactAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.get_contact_attributes)
        [Show boto3-stubs documentation](./client.md#get_contact_attributes)
        """
    def get_current_metric_data(
        self,
        InstanceId: str,
        Filters: FiltersTypeDef,
        CurrentMetrics: List["CurrentMetricTypeDef"],
        Groupings: List[GroupingType] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetCurrentMetricDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.get_current_metric_data)
        [Show boto3-stubs documentation](./client.md#get_current_metric_data)
        """
    def get_federation_token(self, InstanceId: str) -> GetFederationTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.get_federation_token)
        [Show boto3-stubs documentation](./client.md#get_federation_token)
        """
    def get_metric_data(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: FiltersTypeDef,
        HistoricalMetrics: List["HistoricalMetricTypeDef"],
        Groupings: List[GroupingType] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetMetricDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.get_metric_data)
        [Show boto3-stubs documentation](./client.md#get_metric_data)
        """
    def list_approved_origins(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListApprovedOriginsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_approved_origins)
        [Show boto3-stubs documentation](./client.md#list_approved_origins)
        """
    def list_contact_flows(
        self,
        InstanceId: str,
        ContactFlowTypes: List[ContactFlowTypeType] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListContactFlowsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_contact_flows)
        [Show boto3-stubs documentation](./client.md#list_contact_flows)
        """
    def list_hours_of_operations(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListHoursOfOperationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_hours_of_operations)
        [Show boto3-stubs documentation](./client.md#list_hours_of_operations)
        """
    def list_instance_attributes(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListInstanceAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_instance_attributes)
        [Show boto3-stubs documentation](./client.md#list_instance_attributes)
        """
    def list_instance_storage_configs(
        self,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListInstanceStorageConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_instance_storage_configs)
        [Show boto3-stubs documentation](./client.md#list_instance_storage_configs)
        """
    def list_instances(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_instances)
        [Show boto3-stubs documentation](./client.md#list_instances)
        """
    def list_integration_associations(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIntegrationAssociationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_integration_associations)
        [Show boto3-stubs documentation](./client.md#list_integration_associations)
        """
    def list_lambda_functions(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLambdaFunctionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_lambda_functions)
        [Show boto3-stubs documentation](./client.md#list_lambda_functions)
        """
    def list_lex_bots(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLexBotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_lex_bots)
        [Show boto3-stubs documentation](./client.md#list_lex_bots)
        """
    def list_phone_numbers(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[PhoneNumberTypeType] = None,
        PhoneNumberCountryCodes: List[PhoneNumberCountryCodeType] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_phone_numbers)
        [Show boto3-stubs documentation](./client.md#list_phone_numbers)
        """
    def list_prompts(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPromptsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_prompts)
        [Show boto3-stubs documentation](./client.md#list_prompts)
        """
    def list_queue_quick_connects(
        self, InstanceId: str, QueueId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListQueueQuickConnectsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_queue_quick_connects)
        [Show boto3-stubs documentation](./client.md#list_queue_quick_connects)
        """
    def list_queues(
        self,
        InstanceId: str,
        QueueTypes: List[QueueTypeType] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListQueuesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_queues)
        [Show boto3-stubs documentation](./client.md#list_queues)
        """
    def list_quick_connects(
        self,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        QuickConnectTypes: List[QuickConnectTypeType] = None,
    ) -> ListQuickConnectsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_quick_connects)
        [Show boto3-stubs documentation](./client.md#list_quick_connects)
        """
    def list_routing_profile_queues(
        self, InstanceId: str, RoutingProfileId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRoutingProfileQueuesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_routing_profile_queues)
        [Show boto3-stubs documentation](./client.md#list_routing_profile_queues)
        """
    def list_routing_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRoutingProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_routing_profiles)
        [Show boto3-stubs documentation](./client.md#list_routing_profiles)
        """
    def list_security_keys(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityKeysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_security_keys)
        [Show boto3-stubs documentation](./client.md#list_security_keys)
        """
    def list_security_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_security_profiles)
        [Show boto3-stubs documentation](./client.md#list_security_profiles)
        """
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def list_use_cases(
        self,
        InstanceId: str,
        IntegrationAssociationId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListUseCasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_use_cases)
        [Show boto3-stubs documentation](./client.md#list_use_cases)
        """
    def list_user_hierarchy_groups(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUserHierarchyGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_user_hierarchy_groups)
        [Show boto3-stubs documentation](./client.md#list_user_hierarchy_groups)
        """
    def list_users(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.list_users)
        [Show boto3-stubs documentation](./client.md#list_users)
        """
    def resume_contact_recording(
        self, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.resume_contact_recording)
        [Show boto3-stubs documentation](./client.md#resume_contact_recording)
        """
    def start_chat_contact(
        self,
        InstanceId: str,
        ContactFlowId: str,
        ParticipantDetails: ParticipantDetailsTypeDef,
        Attributes: Dict[str, str] = None,
        InitialMessage: ChatMessageTypeDef = None,
        ClientToken: str = None,
    ) -> StartChatContactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.start_chat_contact)
        [Show boto3-stubs documentation](./client.md#start_chat_contact)
        """
    def start_contact_recording(
        self,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.start_contact_recording)
        [Show boto3-stubs documentation](./client.md#start_contact_recording)
        """
    def start_outbound_voice_contact(
        self,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        ClientToken: str = None,
        SourcePhoneNumber: str = None,
        QueueId: str = None,
        Attributes: Dict[str, str] = None,
    ) -> StartOutboundVoiceContactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.start_outbound_voice_contact)
        [Show boto3-stubs documentation](./client.md#start_outbound_voice_contact)
        """
    def start_task_contact(
        self,
        InstanceId: str,
        ContactFlowId: str,
        Name: str,
        PreviousContactId: str = None,
        Attributes: Dict[str, str] = None,
        References: Dict[str, ReferenceTypeDef] = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> StartTaskContactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.start_task_contact)
        [Show boto3-stubs documentation](./client.md#start_task_contact)
        """
    def stop_contact(self, ContactId: str, InstanceId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.stop_contact)
        [Show boto3-stubs documentation](./client.md#stop_contact)
        """
    def stop_contact_recording(
        self, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.stop_contact_recording)
        [Show boto3-stubs documentation](./client.md#stop_contact_recording)
        """
    def suspend_contact_recording(
        self, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.suspend_contact_recording)
        [Show boto3-stubs documentation](./client.md#suspend_contact_recording)
        """
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """
    def update_contact_attributes(
        self, InitialContactId: str, InstanceId: str, Attributes: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_contact_attributes)
        [Show boto3-stubs documentation](./client.md#update_contact_attributes)
        """
    def update_contact_flow_content(
        self, InstanceId: str, ContactFlowId: str, Content: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_contact_flow_content)
        [Show boto3-stubs documentation](./client.md#update_contact_flow_content)
        """
    def update_contact_flow_name(
        self, InstanceId: str, ContactFlowId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_contact_flow_name)
        [Show boto3-stubs documentation](./client.md#update_contact_flow_name)
        """
    def update_instance_attribute(
        self, InstanceId: str, AttributeType: InstanceAttributeTypeType, Value: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_instance_attribute)
        [Show boto3-stubs documentation](./client.md#update_instance_attribute)
        """
    def update_instance_storage_config(
        self,
        InstanceId: str,
        AssociationId: str,
        ResourceType: InstanceStorageResourceTypeType,
        StorageConfig: "InstanceStorageConfigTypeDef",
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_instance_storage_config)
        [Show boto3-stubs documentation](./client.md#update_instance_storage_config)
        """
    def update_queue_hours_of_operation(
        self, InstanceId: str, QueueId: str, HoursOfOperationId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_queue_hours_of_operation)
        [Show boto3-stubs documentation](./client.md#update_queue_hours_of_operation)
        """
    def update_queue_max_contacts(
        self, InstanceId: str, QueueId: str, MaxContacts: int = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_queue_max_contacts)
        [Show boto3-stubs documentation](./client.md#update_queue_max_contacts)
        """
    def update_queue_name(
        self, InstanceId: str, QueueId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_queue_name)
        [Show boto3-stubs documentation](./client.md#update_queue_name)
        """
    def update_queue_outbound_caller_config(
        self, InstanceId: str, QueueId: str, OutboundCallerConfig: "OutboundCallerConfigTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_queue_outbound_caller_config)
        [Show boto3-stubs documentation](./client.md#update_queue_outbound_caller_config)
        """
    def update_queue_status(self, InstanceId: str, QueueId: str, Status: QueueStatusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_queue_status)
        [Show boto3-stubs documentation](./client.md#update_queue_status)
        """
    def update_quick_connect_config(
        self, InstanceId: str, QuickConnectId: str, QuickConnectConfig: "QuickConnectConfigTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_quick_connect_config)
        [Show boto3-stubs documentation](./client.md#update_quick_connect_config)
        """
    def update_quick_connect_name(
        self, InstanceId: str, QuickConnectId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_quick_connect_name)
        [Show boto3-stubs documentation](./client.md#update_quick_connect_name)
        """
    def update_routing_profile_concurrency(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        MediaConcurrencies: List["MediaConcurrencyTypeDef"],
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_routing_profile_concurrency)
        [Show boto3-stubs documentation](./client.md#update_routing_profile_concurrency)
        """
    def update_routing_profile_default_outbound_queue(
        self, InstanceId: str, RoutingProfileId: str, DefaultOutboundQueueId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_routing_profile_default_outbound_queue)
        [Show boto3-stubs documentation](./client.md#update_routing_profile_default_outbound_queue)
        """
    def update_routing_profile_name(
        self, InstanceId: str, RoutingProfileId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_routing_profile_name)
        [Show boto3-stubs documentation](./client.md#update_routing_profile_name)
        """
    def update_routing_profile_queues(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: List[RoutingProfileQueueConfigTypeDef],
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_routing_profile_queues)
        [Show boto3-stubs documentation](./client.md#update_routing_profile_queues)
        """
    def update_user_hierarchy(
        self, UserId: str, InstanceId: str, HierarchyGroupId: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_hierarchy)
        [Show boto3-stubs documentation](./client.md#update_user_hierarchy)
        """
    def update_user_hierarchy_group_name(
        self, Name: str, HierarchyGroupId: str, InstanceId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_hierarchy_group_name)
        [Show boto3-stubs documentation](./client.md#update_user_hierarchy_group_name)
        """
    def update_user_hierarchy_structure(
        self, HierarchyStructure: HierarchyStructureUpdateTypeDef, InstanceId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_hierarchy_structure)
        [Show boto3-stubs documentation](./client.md#update_user_hierarchy_structure)
        """
    def update_user_identity_info(
        self, IdentityInfo: "UserIdentityInfoTypeDef", UserId: str, InstanceId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_identity_info)
        [Show boto3-stubs documentation](./client.md#update_user_identity_info)
        """
    def update_user_phone_config(
        self, PhoneConfig: "UserPhoneConfigTypeDef", UserId: str, InstanceId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_phone_config)
        [Show boto3-stubs documentation](./client.md#update_user_phone_config)
        """
    def update_user_routing_profile(
        self, RoutingProfileId: str, UserId: str, InstanceId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_routing_profile)
        [Show boto3-stubs documentation](./client.md#update_user_routing_profile)
        """
    def update_user_security_profiles(
        self, SecurityProfileIds: List[str], UserId: str, InstanceId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Client.update_user_security_profiles)
        [Show boto3-stubs documentation](./client.md#update_user_security_profiles)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_metric_data"]) -> GetMetricDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.GetMetricData)[Show boto3-stubs documentation](./paginators.md#getmetricdatapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_approved_origins"]
    ) -> ListApprovedOriginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins)[Show boto3-stubs documentation](./paginators.md#listapprovedoriginspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flows"]
    ) -> ListContactFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListContactFlows)[Show boto3-stubs documentation](./paginators.md#listcontactflowspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> ListHoursOfOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)[Show boto3-stubs documentation](./paginators.md#listhoursofoperationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_attributes"]
    ) -> ListInstanceAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes)[Show boto3-stubs documentation](./paginators.md#listinstanceattributespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_storage_configs"]
    ) -> ListInstanceStorageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs)[Show boto3-stubs documentation](./paginators.md#listinstancestorageconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListInstances)[Show boto3-stubs documentation](./paginators.md#listinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_integration_associations"]
    ) -> ListIntegrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations)[Show boto3-stubs documentation](./paginators.md#listintegrationassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_lambda_functions"]
    ) -> ListLambdaFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions)[Show boto3-stubs documentation](./paginators.md#listlambdafunctionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_lex_bots"]) -> ListLexBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListLexBots)[Show boto3-stubs documentation](./paginators.md#listlexbotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers"]
    ) -> ListPhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)[Show boto3-stubs documentation](./paginators.md#listphonenumberspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_prompts"]) -> ListPromptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListPrompts)[Show boto3-stubs documentation](./paginators.md#listpromptspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_quick_connects"]
    ) -> ListQueueQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects)[Show boto3-stubs documentation](./paginators.md#listqueuequickconnectspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListQueues)[Show boto3-stubs documentation](./paginators.md#listqueuespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_connects"]
    ) -> ListQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListQuickConnects)[Show boto3-stubs documentation](./paginators.md#listquickconnectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profile_queues"]
    ) -> ListRoutingProfileQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues)[Show boto3-stubs documentation](./paginators.md#listroutingprofilequeuespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profiles"]
    ) -> ListRoutingProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)[Show boto3-stubs documentation](./paginators.md#listroutingprofilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_keys"]
    ) -> ListSecurityKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListSecurityKeys)[Show boto3-stubs documentation](./paginators.md#listsecuritykeyspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)[Show boto3-stubs documentation](./paginators.md#listsecurityprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_use_cases"]) -> ListUseCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListUseCases)[Show boto3-stubs documentation](./paginators.md#listusecasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> ListUserHierarchyGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)[Show boto3-stubs documentation](./paginators.md#listuserhierarchygroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/connect.html#Connect.Paginator.ListUsers)[Show boto3-stubs documentation](./paginators.md#listuserspaginator)
        """
