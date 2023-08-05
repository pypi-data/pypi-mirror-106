"""
Type annotations for ssm-contacts service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_contacts import SSMContactsClient

    client: SSMContactsClient = boto3.client("ssm-contacts")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import AcceptTypeType, ChannelTypeType, ContactTypeType
from .paginator import (
    ListContactChannelsPaginator,
    ListContactsPaginator,
    ListEngagementsPaginator,
    ListPageReceiptsPaginator,
    ListPagesByContactPaginator,
    ListPagesByEngagementPaginator,
)
from .type_defs import (
    ContactChannelAddressTypeDef,
    CreateContactChannelResultTypeDef,
    CreateContactResultTypeDef,
    DescribeEngagementResultTypeDef,
    DescribePageResultTypeDef,
    GetContactChannelResultTypeDef,
    GetContactPolicyResultTypeDef,
    GetContactResultTypeDef,
    ListContactChannelsResultTypeDef,
    ListContactsResultTypeDef,
    ListEngagementsResultTypeDef,
    ListPageReceiptsResultTypeDef,
    ListPagesByContactResultTypeDef,
    ListPagesByEngagementResultTypeDef,
    ListTagsForResourceResultTypeDef,
    PlanTypeDef,
    StartEngagementResultTypeDef,
    TagTypeDef,
    TimeRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSMContactsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DataEncryptionException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SSMContactsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_page(
        self,
        PageId: str,
        AcceptType: AcceptTypeType,
        AcceptCode: str,
        ContactChannelId: str = None,
        Note: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.accept_page)
        [Show boto3-stubs documentation](./client.md#accept_page)
        """

    def activate_contact_channel(
        self, ContactChannelId: str, ActivationCode: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.activate_contact_channel)
        [Show boto3-stubs documentation](./client.md#activate_contact_channel)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_contact(
        self,
        Alias: str,
        Type: ContactTypeType,
        Plan: "PlanTypeDef",
        DisplayName: str = None,
        Tags: List["TagTypeDef"] = None,
        IdempotencyToken: str = None,
    ) -> CreateContactResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.create_contact)
        [Show boto3-stubs documentation](./client.md#create_contact)
        """

    def create_contact_channel(
        self,
        ContactId: str,
        Name: str,
        Type: ChannelTypeType,
        DeliveryAddress: "ContactChannelAddressTypeDef",
        DeferActivation: bool = None,
        IdempotencyToken: str = None,
    ) -> CreateContactChannelResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.create_contact_channel)
        [Show boto3-stubs documentation](./client.md#create_contact_channel)
        """

    def deactivate_contact_channel(self, ContactChannelId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.deactivate_contact_channel)
        [Show boto3-stubs documentation](./client.md#deactivate_contact_channel)
        """

    def delete_contact(self, ContactId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.delete_contact)
        [Show boto3-stubs documentation](./client.md#delete_contact)
        """

    def delete_contact_channel(self, ContactChannelId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.delete_contact_channel)
        [Show boto3-stubs documentation](./client.md#delete_contact_channel)
        """

    def describe_engagement(self, EngagementId: str) -> DescribeEngagementResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.describe_engagement)
        [Show boto3-stubs documentation](./client.md#describe_engagement)
        """

    def describe_page(self, PageId: str) -> DescribePageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.describe_page)
        [Show boto3-stubs documentation](./client.md#describe_page)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_contact(self, ContactId: str) -> GetContactResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.get_contact)
        [Show boto3-stubs documentation](./client.md#get_contact)
        """

    def get_contact_channel(self, ContactChannelId: str) -> GetContactChannelResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.get_contact_channel)
        [Show boto3-stubs documentation](./client.md#get_contact_channel)
        """

    def get_contact_policy(self, ContactArn: str) -> GetContactPolicyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.get_contact_policy)
        [Show boto3-stubs documentation](./client.md#get_contact_policy)
        """

    def list_contact_channels(
        self, ContactId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListContactChannelsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_contact_channels)
        [Show boto3-stubs documentation](./client.md#list_contact_channels)
        """

    def list_contacts(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        AliasPrefix: str = None,
        Type: ContactTypeType = None,
    ) -> ListContactsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_contacts)
        [Show boto3-stubs documentation](./client.md#list_contacts)
        """

    def list_engagements(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        IncidentId: str = None,
        TimeRangeValue: TimeRangeTypeDef = None,
    ) -> ListEngagementsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_engagements)
        [Show boto3-stubs documentation](./client.md#list_engagements)
        """

    def list_page_receipts(
        self, PageId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPageReceiptsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_page_receipts)
        [Show boto3-stubs documentation](./client.md#list_page_receipts)
        """

    def list_pages_by_contact(
        self, ContactId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPagesByContactResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_pages_by_contact)
        [Show boto3-stubs documentation](./client.md#list_pages_by_contact)
        """

    def list_pages_by_engagement(
        self, EngagementId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPagesByEngagementResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_pages_by_engagement)
        [Show boto3-stubs documentation](./client.md#list_pages_by_engagement)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def put_contact_policy(self, ContactArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.put_contact_policy)
        [Show boto3-stubs documentation](./client.md#put_contact_policy)
        """

    def send_activation_code(self, ContactChannelId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.send_activation_code)
        [Show boto3-stubs documentation](./client.md#send_activation_code)
        """

    def start_engagement(
        self,
        ContactId: str,
        Sender: str,
        Subject: str,
        Content: str,
        PublicSubject: str = None,
        PublicContent: str = None,
        IncidentId: str = None,
        IdempotencyToken: str = None,
    ) -> StartEngagementResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.start_engagement)
        [Show boto3-stubs documentation](./client.md#start_engagement)
        """

    def stop_engagement(self, EngagementId: str, Reason: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.stop_engagement)
        [Show boto3-stubs documentation](./client.md#stop_engagement)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_contact(
        self, ContactId: str, DisplayName: str = None, Plan: "PlanTypeDef" = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.update_contact)
        [Show boto3-stubs documentation](./client.md#update_contact)
        """

    def update_contact_channel(
        self,
        ContactChannelId: str,
        Name: str = None,
        DeliveryAddress: "ContactChannelAddressTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Client.update_contact_channel)
        [Show boto3-stubs documentation](./client.md#update_contact_channel)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_channels"]
    ) -> ListContactChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels)[Show boto3-stubs documentation](./paginators.md#listcontactchannelspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contacts"]) -> ListContactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts)[Show boto3-stubs documentation](./paginators.md#listcontactspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_engagements"]
    ) -> ListEngagementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements)[Show boto3-stubs documentation](./paginators.md#listengagementspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_page_receipts"]
    ) -> ListPageReceiptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts)[Show boto3-stubs documentation](./paginators.md#listpagereceiptspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pages_by_contact"]
    ) -> ListPagesByContactPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact)[Show boto3-stubs documentation](./paginators.md#listpagesbycontactpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pages_by_engagement"]
    ) -> ListPagesByEngagementPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement)[Show boto3-stubs documentation](./paginators.md#listpagesbyengagementpaginator)
        """
