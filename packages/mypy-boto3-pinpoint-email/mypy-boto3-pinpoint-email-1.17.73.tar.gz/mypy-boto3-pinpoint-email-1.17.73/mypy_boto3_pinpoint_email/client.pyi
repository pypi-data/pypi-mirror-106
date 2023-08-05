"""
Type annotations for pinpoint-email service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_email import PinpointEmailClient

    client: PinpointEmailClient = boto3.client("pinpoint-email")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import BehaviorOnMxFailureType, TlsPolicyType
from .paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)
from .type_defs import (
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EventDestinationDefinitionTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListDomainDeliverabilityCampaignsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageTagTypeDef,
    ReputationOptionsTypeDef,
    SendEmailResponseTypeDef,
    SendingOptionsTypeDef,
    TagTypeDef,
    TrackingOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PinpointEmailClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccountSuspendedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    SendingPausedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class PinpointEmailClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def create_configuration_set(
        self,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set)
        [Show boto3-stubs documentation](./client.md#create_configuration_set)
        """
    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](./client.md#create_configuration_set_event_destination)
        """
    def create_dedicated_ip_pool(
        self, PoolName: str, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.create_dedicated_ip_pool)
        [Show boto3-stubs documentation](./client.md#create_dedicated_ip_pool)
        """
    def create_deliverability_test_report(
        self,
        FromEmailAddress: str,
        Content: EmailContentTypeDef,
        ReportName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.create_deliverability_test_report)
        [Show boto3-stubs documentation](./client.md#create_deliverability_test_report)
        """
    def create_email_identity(
        self, EmailIdentity: str, Tags: List["TagTypeDef"] = None
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.create_email_identity)
        [Show boto3-stubs documentation](./client.md#create_email_identity)
        """
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set)
        [Show boto3-stubs documentation](./client.md#delete_configuration_set)
        """
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](./client.md#delete_configuration_set_event_destination)
        """
    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_dedicated_ip_pool)
        [Show boto3-stubs documentation](./client.md#delete_dedicated_ip_pool)
        """
    def delete_email_identity(self, EmailIdentity: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_email_identity)
        [Show boto3-stubs documentation](./client.md#delete_email_identity)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def get_account(self) -> GetAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_account)
        [Show boto3-stubs documentation](./client.md#get_account)
        """
    def get_blacklist_reports(
        self, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_blacklist_reports)
        [Show boto3-stubs documentation](./client.md#get_blacklist_reports)
        """
    def get_configuration_set(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set)
        [Show boto3-stubs documentation](./client.md#get_configuration_set)
        """
    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set_event_destinations)
        [Show boto3-stubs documentation](./client.md#get_configuration_set_event_destinations)
        """
    def get_dedicated_ip(self, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ip)
        [Show boto3-stubs documentation](./client.md#get_dedicated_ip)
        """
    def get_dedicated_ips(
        self, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ips)
        [Show boto3-stubs documentation](./client.md#get_dedicated_ips)
        """
    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_dashboard_options)
        [Show boto3-stubs documentation](./client.md#get_deliverability_dashboard_options)
        """
    def get_deliverability_test_report(
        self, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_test_report)
        [Show boto3-stubs documentation](./client.md#get_deliverability_test_report)
        """
    def get_domain_deliverability_campaign(
        self, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_deliverability_campaign)
        [Show boto3-stubs documentation](./client.md#get_domain_deliverability_campaign)
        """
    def get_domain_statistics_report(
        self, Domain: str, StartDate: datetime, EndDate: datetime
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_statistics_report)
        [Show boto3-stubs documentation](./client.md#get_domain_statistics_report)
        """
    def get_email_identity(self, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.get_email_identity)
        [Show boto3-stubs documentation](./client.md#get_email_identity)
        """
    def list_configuration_sets(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.list_configuration_sets)
        [Show boto3-stubs documentation](./client.md#list_configuration_sets)
        """
    def list_dedicated_ip_pools(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.list_dedicated_ip_pools)
        [Show boto3-stubs documentation](./client.md#list_dedicated_ip_pools)
        """
    def list_deliverability_test_reports(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.list_deliverability_test_reports)
        [Show boto3-stubs documentation](./client.md#list_deliverability_test_reports)
        """
    def list_domain_deliverability_campaigns(
        self,
        StartDate: datetime,
        EndDate: datetime,
        SubscribedDomain: str,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListDomainDeliverabilityCampaignsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.list_domain_deliverability_campaigns)
        [Show boto3-stubs documentation](./client.md#list_domain_deliverability_campaigns)
        """
    def list_email_identities(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.list_email_identities)
        [Show boto3-stubs documentation](./client.md#list_email_identities)
        """
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def put_account_dedicated_ip_warmup_attributes(
        self, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](./client.md#put_account_dedicated_ip_warmup_attributes)
        """
    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_sending_attributes)
        [Show boto3-stubs documentation](./client.md#put_account_sending_attributes)
        """
    def put_configuration_set_delivery_options(
        self,
        ConfigurationSetName: str,
        TlsPolicy: TlsPolicyType = None,
        SendingPoolName: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](./client.md#put_configuration_set_delivery_options)
        """
    def put_configuration_set_reputation_options(
        self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_reputation_options)
        [Show boto3-stubs documentation](./client.md#put_configuration_set_reputation_options)
        """
    def put_configuration_set_sending_options(
        self, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_sending_options)
        [Show boto3-stubs documentation](./client.md#put_configuration_set_sending_options)
        """
    def put_configuration_set_tracking_options(
        self, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_tracking_options)
        [Show boto3-stubs documentation](./client.md#put_configuration_set_tracking_options)
        """
    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_in_pool)
        [Show boto3-stubs documentation](./client.md#put_dedicated_ip_in_pool)
        """
    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](./client.md#put_dedicated_ip_warmup_attributes)
        """
    def put_deliverability_dashboard_option(
        self,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_deliverability_dashboard_option)
        [Show boto3-stubs documentation](./client.md#put_deliverability_dashboard_option)
        """
    def put_email_identity_dkim_attributes(
        self, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_dkim_attributes)
        [Show boto3-stubs documentation](./client.md#put_email_identity_dkim_attributes)
        """
    def put_email_identity_feedback_attributes(
        self, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_feedback_attributes)
        [Show boto3-stubs documentation](./client.md#put_email_identity_feedback_attributes)
        """
    def put_email_identity_mail_from_attributes(
        self,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: BehaviorOnMxFailureType = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_mail_from_attributes)
        [Show boto3-stubs documentation](./client.md#put_email_identity_mail_from_attributes)
        """
    def send_email(
        self,
        Destination: DestinationTypeDef,
        Content: EmailContentTypeDef,
        FromEmailAddress: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        EmailTags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.send_email)
        [Show boto3-stubs documentation](./client.md#send_email)
        """
    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """
    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](./client.md#update_configuration_set_event_destination)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_dedicated_ips"]
    ) -> GetDedicatedIpsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)[Show boto3-stubs documentation](./paginators.md#getdedicatedipspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> ListConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)[Show boto3-stubs documentation](./paginators.md#listconfigurationsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dedicated_ip_pools"]
    ) -> ListDedicatedIpPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)[Show boto3-stubs documentation](./paginators.md#listdedicatedippoolspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deliverability_test_reports"]
    ) -> ListDeliverabilityTestReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)[Show boto3-stubs documentation](./paginators.md#listdeliverabilitytestreportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_email_identities"]
    ) -> ListEmailIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)[Show boto3-stubs documentation](./paginators.md#listemailidentitiespaginator)
        """
