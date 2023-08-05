"""
Type annotations for workmail service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_workmail import WorkMailClient

    client: WorkMailClient = boto3.client("workmail")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AccessControlRuleEffectType,
    MobileDeviceAccessRuleEffectType,
    PermissionTypeType,
    ResourceTypeType,
)
from .paginator import (
    ListAliasesPaginator,
    ListGroupMembersPaginator,
    ListGroupsPaginator,
    ListMailboxPermissionsPaginator,
    ListOrganizationsPaginator,
    ListResourceDelegatesPaginator,
    ListResourcesPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    BookingOptionsTypeDef,
    CreateGroupResponseTypeDef,
    CreateMobileDeviceAccessRuleResponseTypeDef,
    CreateOrganizationResponseTypeDef,
    CreateResourceResponseTypeDef,
    CreateUserResponseTypeDef,
    DeleteOrganizationResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeMailboxExportJobResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribeResourceResponseTypeDef,
    DescribeUserResponseTypeDef,
    DomainTypeDef,
    FolderConfigurationTypeDef,
    GetAccessControlEffectResponseTypeDef,
    GetDefaultRetentionPolicyResponseTypeDef,
    GetMailboxDetailsResponseTypeDef,
    GetMobileDeviceAccessEffectResponseTypeDef,
    ListAccessControlRulesResponseTypeDef,
    ListAliasesResponseTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxExportJobsResponseTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListMobileDeviceAccessRulesResponseTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    StartMailboxExportJobResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("WorkMailClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DirectoryInUseException: Type[BotocoreClientError]
    DirectoryServiceAuthenticationFailedException: Type[BotocoreClientError]
    DirectoryUnavailableException: Type[BotocoreClientError]
    EmailAddressInUseException: Type[BotocoreClientError]
    EntityAlreadyRegisteredException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    EntityStateException: Type[BotocoreClientError]
    InvalidConfigurationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailDomainNotFoundException: Type[BotocoreClientError]
    MailDomainStateException: Type[BotocoreClientError]
    NameAvailabilityException: Type[BotocoreClientError]
    OrganizationNotFoundException: Type[BotocoreClientError]
    OrganizationStateException: Type[BotocoreClientError]
    ReservedNameException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class WorkMailClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def associate_delegate_to_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.associate_delegate_to_resource)
        [Show boto3-stubs documentation](./client.md#associate_delegate_to_resource)
        """
    def associate_member_to_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.associate_member_to_group)
        [Show boto3-stubs documentation](./client.md#associate_member_to_group)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def cancel_mailbox_export_job(
        self, ClientToken: str, JobId: str, OrganizationId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.cancel_mailbox_export_job)
        [Show boto3-stubs documentation](./client.md#cancel_mailbox_export_job)
        """
    def create_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.create_alias)
        [Show boto3-stubs documentation](./client.md#create_alias)
        """
    def create_group(self, OrganizationId: str, Name: str) -> CreateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.create_group)
        [Show boto3-stubs documentation](./client.md#create_group)
        """
    def create_mobile_device_access_rule(
        self,
        OrganizationId: str,
        Name: str,
        Effect: MobileDeviceAccessRuleEffectType,
        ClientToken: str = None,
        Description: str = None,
        DeviceTypes: List[str] = None,
        NotDeviceTypes: List[str] = None,
        DeviceModels: List[str] = None,
        NotDeviceModels: List[str] = None,
        DeviceOperatingSystems: List[str] = None,
        NotDeviceOperatingSystems: List[str] = None,
        DeviceUserAgents: List[str] = None,
        NotDeviceUserAgents: List[str] = None,
    ) -> CreateMobileDeviceAccessRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.create_mobile_device_access_rule)
        [Show boto3-stubs documentation](./client.md#create_mobile_device_access_rule)
        """
    def create_organization(
        self,
        Alias: str,
        DirectoryId: str = None,
        ClientToken: str = None,
        Domains: List[DomainTypeDef] = None,
        KmsKeyArn: str = None,
        EnableInteroperability: bool = None,
    ) -> CreateOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.create_organization)
        [Show boto3-stubs documentation](./client.md#create_organization)
        """
    def create_resource(
        self, OrganizationId: str, Name: str, Type: ResourceTypeType
    ) -> CreateResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.create_resource)
        [Show boto3-stubs documentation](./client.md#create_resource)
        """
    def create_user(
        self, OrganizationId: str, Name: str, DisplayName: str, Password: str
    ) -> CreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.create_user)
        [Show boto3-stubs documentation](./client.md#create_user)
        """
    def delete_access_control_rule(self, OrganizationId: str, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_access_control_rule)
        [Show boto3-stubs documentation](./client.md#delete_access_control_rule)
        """
    def delete_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_alias)
        [Show boto3-stubs documentation](./client.md#delete_alias)
        """
    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_group)
        [Show boto3-stubs documentation](./client.md#delete_group)
        """
    def delete_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, GranteeId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_mailbox_permissions)
        [Show boto3-stubs documentation](./client.md#delete_mailbox_permissions)
        """
    def delete_mobile_device_access_rule(
        self, OrganizationId: str, MobileDeviceAccessRuleId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_mobile_device_access_rule)
        [Show boto3-stubs documentation](./client.md#delete_mobile_device_access_rule)
        """
    def delete_organization(
        self, OrganizationId: str, DeleteDirectory: bool, ClientToken: str = None
    ) -> DeleteOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_organization)
        [Show boto3-stubs documentation](./client.md#delete_organization)
        """
    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_resource)
        [Show boto3-stubs documentation](./client.md#delete_resource)
        """
    def delete_retention_policy(self, OrganizationId: str, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_retention_policy)
        [Show boto3-stubs documentation](./client.md#delete_retention_policy)
        """
    def delete_user(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.delete_user)
        [Show boto3-stubs documentation](./client.md#delete_user)
        """
    def deregister_from_work_mail(self, OrganizationId: str, EntityId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.deregister_from_work_mail)
        [Show boto3-stubs documentation](./client.md#deregister_from_work_mail)
        """
    def describe_group(self, OrganizationId: str, GroupId: str) -> DescribeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.describe_group)
        [Show boto3-stubs documentation](./client.md#describe_group)
        """
    def describe_mailbox_export_job(
        self, JobId: str, OrganizationId: str
    ) -> DescribeMailboxExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.describe_mailbox_export_job)
        [Show boto3-stubs documentation](./client.md#describe_mailbox_export_job)
        """
    def describe_organization(self, OrganizationId: str) -> DescribeOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.describe_organization)
        [Show boto3-stubs documentation](./client.md#describe_organization)
        """
    def describe_resource(
        self, OrganizationId: str, ResourceId: str
    ) -> DescribeResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.describe_resource)
        [Show boto3-stubs documentation](./client.md#describe_resource)
        """
    def describe_user(self, OrganizationId: str, UserId: str) -> DescribeUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.describe_user)
        [Show boto3-stubs documentation](./client.md#describe_user)
        """
    def disassociate_delegate_from_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.disassociate_delegate_from_resource)
        [Show boto3-stubs documentation](./client.md#disassociate_delegate_from_resource)
        """
    def disassociate_member_from_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.disassociate_member_from_group)
        [Show boto3-stubs documentation](./client.md#disassociate_member_from_group)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def get_access_control_effect(
        self, OrganizationId: str, IpAddress: str, Action: str, UserId: str
    ) -> GetAccessControlEffectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.get_access_control_effect)
        [Show boto3-stubs documentation](./client.md#get_access_control_effect)
        """
    def get_default_retention_policy(
        self, OrganizationId: str
    ) -> GetDefaultRetentionPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.get_default_retention_policy)
        [Show boto3-stubs documentation](./client.md#get_default_retention_policy)
        """
    def get_mailbox_details(
        self, OrganizationId: str, UserId: str
    ) -> GetMailboxDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.get_mailbox_details)
        [Show boto3-stubs documentation](./client.md#get_mailbox_details)
        """
    def get_mobile_device_access_effect(
        self,
        OrganizationId: str,
        DeviceType: str = None,
        DeviceModel: str = None,
        DeviceOperatingSystem: str = None,
        DeviceUserAgent: str = None,
    ) -> GetMobileDeviceAccessEffectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.get_mobile_device_access_effect)
        [Show boto3-stubs documentation](./client.md#get_mobile_device_access_effect)
        """
    def list_access_control_rules(
        self, OrganizationId: str
    ) -> ListAccessControlRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_access_control_rules)
        [Show boto3-stubs documentation](./client.md#list_access_control_rules)
        """
    def list_aliases(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_aliases)
        [Show boto3-stubs documentation](./client.md#list_aliases)
        """
    def list_group_members(
        self, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_group_members)
        [Show boto3-stubs documentation](./client.md#list_group_members)
        """
    def list_groups(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_groups)
        [Show boto3-stubs documentation](./client.md#list_groups)
        """
    def list_mailbox_export_jobs(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMailboxExportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_mailbox_export_jobs)
        [Show boto3-stubs documentation](./client.md#list_mailbox_export_jobs)
        """
    def list_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMailboxPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_mailbox_permissions)
        [Show boto3-stubs documentation](./client.md#list_mailbox_permissions)
        """
    def list_mobile_device_access_rules(
        self, OrganizationId: str
    ) -> ListMobileDeviceAccessRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_mobile_device_access_rules)
        [Show boto3-stubs documentation](./client.md#list_mobile_device_access_rules)
        """
    def list_organizations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_organizations)
        [Show boto3-stubs documentation](./client.md#list_organizations)
        """
    def list_resource_delegates(
        self, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceDelegatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_resource_delegates)
        [Show boto3-stubs documentation](./client.md#list_resource_delegates)
        """
    def list_resources(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_resources)
        [Show boto3-stubs documentation](./client.md#list_resources)
        """
    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def list_users(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.list_users)
        [Show boto3-stubs documentation](./client.md#list_users)
        """
    def put_access_control_rule(
        self,
        Name: str,
        Effect: AccessControlRuleEffectType,
        Description: str,
        OrganizationId: str,
        IpRanges: List[str] = None,
        NotIpRanges: List[str] = None,
        Actions: List[str] = None,
        NotActions: List[str] = None,
        UserIds: List[str] = None,
        NotUserIds: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.put_access_control_rule)
        [Show boto3-stubs documentation](./client.md#put_access_control_rule)
        """
    def put_mailbox_permissions(
        self,
        OrganizationId: str,
        EntityId: str,
        GranteeId: str,
        PermissionValues: List[PermissionTypeType],
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.put_mailbox_permissions)
        [Show boto3-stubs documentation](./client.md#put_mailbox_permissions)
        """
    def put_retention_policy(
        self,
        OrganizationId: str,
        Name: str,
        FolderConfigurations: List["FolderConfigurationTypeDef"],
        Id: str = None,
        Description: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.put_retention_policy)
        [Show boto3-stubs documentation](./client.md#put_retention_policy)
        """
    def register_to_work_mail(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.register_to_work_mail)
        [Show boto3-stubs documentation](./client.md#register_to_work_mail)
        """
    def reset_password(self, OrganizationId: str, UserId: str, Password: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.reset_password)
        [Show boto3-stubs documentation](./client.md#reset_password)
        """
    def start_mailbox_export_job(
        self,
        ClientToken: str,
        OrganizationId: str,
        EntityId: str,
        RoleArn: str,
        KmsKeyArn: str,
        S3BucketName: str,
        S3Prefix: str,
        Description: str = None,
    ) -> StartMailboxExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.start_mailbox_export_job)
        [Show boto3-stubs documentation](./client.md#start_mailbox_export_job)
        """
    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """
    def update_mailbox_quota(
        self, OrganizationId: str, UserId: str, MailboxQuota: int
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.update_mailbox_quota)
        [Show boto3-stubs documentation](./client.md#update_mailbox_quota)
        """
    def update_mobile_device_access_rule(
        self,
        OrganizationId: str,
        MobileDeviceAccessRuleId: str,
        Name: str,
        Effect: MobileDeviceAccessRuleEffectType,
        Description: str = None,
        DeviceTypes: List[str] = None,
        NotDeviceTypes: List[str] = None,
        DeviceModels: List[str] = None,
        NotDeviceModels: List[str] = None,
        DeviceOperatingSystems: List[str] = None,
        NotDeviceOperatingSystems: List[str] = None,
        DeviceUserAgents: List[str] = None,
        NotDeviceUserAgents: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.update_mobile_device_access_rule)
        [Show boto3-stubs documentation](./client.md#update_mobile_device_access_rule)
        """
    def update_primary_email_address(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.update_primary_email_address)
        [Show boto3-stubs documentation](./client.md#update_primary_email_address)
        """
    def update_resource(
        self,
        OrganizationId: str,
        ResourceId: str,
        Name: str = None,
        BookingOptions: "BookingOptionsTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Client.update_resource)
        [Show boto3-stubs documentation](./client.md#update_resource)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListAliases)[Show boto3-stubs documentation](./paginators.md#listaliasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_members"]
    ) -> ListGroupMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)[Show boto3-stubs documentation](./paginators.md#listgroupmemberspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListGroups)[Show boto3-stubs documentation](./paginators.md#listgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_mailbox_permissions"]
    ) -> ListMailboxPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)[Show boto3-stubs documentation](./paginators.md#listmailboxpermissionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizations"]
    ) -> ListOrganizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)[Show boto3-stubs documentation](./paginators.md#listorganizationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_delegates"]
    ) -> ListResourceDelegatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)[Show boto3-stubs documentation](./paginators.md#listresourcedelegatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_resources"]) -> ListResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListResources)[Show boto3-stubs documentation](./paginators.md#listresourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/workmail.html#WorkMail.Paginator.ListUsers)[Show boto3-stubs documentation](./paginators.md#listuserspaginator)
        """
