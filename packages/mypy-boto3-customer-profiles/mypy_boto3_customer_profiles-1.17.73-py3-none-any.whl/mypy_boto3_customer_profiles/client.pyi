"""
Type annotations for customer-profiles service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_customer_profiles import CustomerProfilesClient

    client: CustomerProfilesClient = boto3.client("customer-profiles")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import GenderType, PartyTypeType
from .type_defs import (
    AddProfileKeyResponseTypeDef,
    AddressTypeDef,
    CreateDomainResponseTypeDef,
    CreateProfileResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteProfileKeyResponseTypeDef,
    DeleteProfileObjectResponseTypeDef,
    DeleteProfileObjectTypeResponseTypeDef,
    DeleteProfileResponseTypeDef,
    FieldSourceProfileIdsTypeDef,
    FlowDefinitionTypeDef,
    GetDomainResponseTypeDef,
    GetIntegrationResponseTypeDef,
    GetMatchesResponseTypeDef,
    GetProfileObjectTypeResponseTypeDef,
    GetProfileObjectTypeTemplateResponseTypeDef,
    ListAccountIntegrationsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListIntegrationsResponseTypeDef,
    ListProfileObjectsResponseTypeDef,
    ListProfileObjectTypesResponseTypeDef,
    ListProfileObjectTypeTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MatchingRequestTypeDef,
    MergeProfilesResponseTypeDef,
    ObjectTypeFieldTypeDef,
    ObjectTypeKeyTypeDef,
    PutIntegrationResponseTypeDef,
    PutProfileObjectResponseTypeDef,
    PutProfileObjectTypeResponseTypeDef,
    SearchProfilesResponseTypeDef,
    UpdateAddressTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateProfileResponseTypeDef,
)

__all__ = ("CustomerProfilesClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class CustomerProfilesClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def add_profile_key(
        self, ProfileId: str, KeyName: str, Values: List[str], DomainName: str
    ) -> AddProfileKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.add_profile_key)
        [Show boto3-stubs documentation](./client.md#add_profile_key)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def create_domain(
        self,
        DomainName: str,
        DefaultExpirationDays: int,
        DefaultEncryptionKey: str = None,
        DeadLetterQueueUrl: str = None,
        Matching: MatchingRequestTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.create_domain)
        [Show boto3-stubs documentation](./client.md#create_domain)
        """
    def create_profile(
        self,
        DomainName: str,
        AccountNumber: str = None,
        AdditionalInformation: str = None,
        PartyType: PartyTypeType = None,
        BusinessName: str = None,
        FirstName: str = None,
        MiddleName: str = None,
        LastName: str = None,
        BirthDate: str = None,
        Gender: GenderType = None,
        PhoneNumber: str = None,
        MobilePhoneNumber: str = None,
        HomePhoneNumber: str = None,
        BusinessPhoneNumber: str = None,
        EmailAddress: str = None,
        PersonalEmailAddress: str = None,
        BusinessEmailAddress: str = None,
        Address: "AddressTypeDef" = None,
        ShippingAddress: "AddressTypeDef" = None,
        MailingAddress: "AddressTypeDef" = None,
        BillingAddress: "AddressTypeDef" = None,
        Attributes: Dict[str, str] = None,
    ) -> CreateProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.create_profile)
        [Show boto3-stubs documentation](./client.md#create_profile)
        """
    def delete_domain(self, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_domain)
        [Show boto3-stubs documentation](./client.md#delete_domain)
        """
    def delete_integration(self, DomainName: str, Uri: str) -> DeleteIntegrationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_integration)
        [Show boto3-stubs documentation](./client.md#delete_integration)
        """
    def delete_profile(self, ProfileId: str, DomainName: str) -> DeleteProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile)
        [Show boto3-stubs documentation](./client.md#delete_profile)
        """
    def delete_profile_key(
        self, ProfileId: str, KeyName: str, Values: List[str], DomainName: str
    ) -> DeleteProfileKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_key)
        [Show boto3-stubs documentation](./client.md#delete_profile_key)
        """
    def delete_profile_object(
        self, ProfileId: str, ProfileObjectUniqueKey: str, ObjectTypeName: str, DomainName: str
    ) -> DeleteProfileObjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object)
        [Show boto3-stubs documentation](./client.md#delete_profile_object)
        """
    def delete_profile_object_type(
        self, DomainName: str, ObjectTypeName: str
    ) -> DeleteProfileObjectTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object_type)
        [Show boto3-stubs documentation](./client.md#delete_profile_object_type)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def get_domain(self, DomainName: str) -> GetDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.get_domain)
        [Show boto3-stubs documentation](./client.md#get_domain)
        """
    def get_integration(self, DomainName: str, Uri: str) -> GetIntegrationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.get_integration)
        [Show boto3-stubs documentation](./client.md#get_integration)
        """
    def get_matches(
        self, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> GetMatchesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.get_matches)
        [Show boto3-stubs documentation](./client.md#get_matches)
        """
    def get_profile_object_type(
        self, DomainName: str, ObjectTypeName: str
    ) -> GetProfileObjectTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type)
        [Show boto3-stubs documentation](./client.md#get_profile_object_type)
        """
    def get_profile_object_type_template(
        self, TemplateId: str
    ) -> GetProfileObjectTypeTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type_template)
        [Show boto3-stubs documentation](./client.md#get_profile_object_type_template)
        """
    def list_account_integrations(
        self, Uri: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountIntegrationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_account_integrations)
        [Show boto3-stubs documentation](./client.md#list_account_integrations)
        """
    def list_domains(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_domains)
        [Show boto3-stubs documentation](./client.md#list_domains)
        """
    def list_integrations(
        self, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIntegrationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_integrations)
        [Show boto3-stubs documentation](./client.md#list_integrations)
        """
    def list_profile_object_type_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileObjectTypeTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_type_templates)
        [Show boto3-stubs documentation](./client.md#list_profile_object_type_templates)
        """
    def list_profile_object_types(
        self, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileObjectTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_types)
        [Show boto3-stubs documentation](./client.md#list_profile_object_types)
        """
    def list_profile_objects(
        self,
        DomainName: str,
        ObjectTypeName: str,
        ProfileId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListProfileObjectsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_objects)
        [Show boto3-stubs documentation](./client.md#list_profile_objects)
        """
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def merge_profiles(
        self,
        DomainName: str,
        MainProfileId: str,
        ProfileIdsToBeMerged: List[str],
        FieldSourceProfileIds: FieldSourceProfileIdsTypeDef = None,
    ) -> MergeProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.merge_profiles)
        [Show boto3-stubs documentation](./client.md#merge_profiles)
        """
    def put_integration(
        self,
        DomainName: str,
        ObjectTypeName: str,
        Uri: str = None,
        Tags: Dict[str, str] = None,
        FlowDefinition: FlowDefinitionTypeDef = None,
    ) -> PutIntegrationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.put_integration)
        [Show boto3-stubs documentation](./client.md#put_integration)
        """
    def put_profile_object(
        self, ObjectTypeName: str, Object: str, DomainName: str
    ) -> PutProfileObjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object)
        [Show boto3-stubs documentation](./client.md#put_profile_object)
        """
    def put_profile_object_type(
        self,
        DomainName: str,
        ObjectTypeName: str,
        Description: str,
        TemplateId: str = None,
        ExpirationDays: int = None,
        EncryptionKey: str = None,
        AllowProfileCreation: bool = None,
        Fields: Dict[str, "ObjectTypeFieldTypeDef"] = None,
        Keys: Dict[str, List["ObjectTypeKeyTypeDef"]] = None,
        Tags: Dict[str, str] = None,
    ) -> PutProfileObjectTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object_type)
        [Show boto3-stubs documentation](./client.md#put_profile_object_type)
        """
    def search_profiles(
        self,
        DomainName: str,
        KeyName: str,
        Values: List[str],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> SearchProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.search_profiles)
        [Show boto3-stubs documentation](./client.md#search_profiles)
        """
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """
    def update_domain(
        self,
        DomainName: str,
        DefaultExpirationDays: int = None,
        DefaultEncryptionKey: str = None,
        DeadLetterQueueUrl: str = None,
        Matching: MatchingRequestTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> UpdateDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.update_domain)
        [Show boto3-stubs documentation](./client.md#update_domain)
        """
    def update_profile(
        self,
        DomainName: str,
        ProfileId: str,
        AdditionalInformation: str = None,
        AccountNumber: str = None,
        PartyType: PartyTypeType = None,
        BusinessName: str = None,
        FirstName: str = None,
        MiddleName: str = None,
        LastName: str = None,
        BirthDate: str = None,
        Gender: GenderType = None,
        PhoneNumber: str = None,
        MobilePhoneNumber: str = None,
        HomePhoneNumber: str = None,
        BusinessPhoneNumber: str = None,
        EmailAddress: str = None,
        PersonalEmailAddress: str = None,
        BusinessEmailAddress: str = None,
        Address: UpdateAddressTypeDef = None,
        ShippingAddress: UpdateAddressTypeDef = None,
        MailingAddress: UpdateAddressTypeDef = None,
        BillingAddress: UpdateAddressTypeDef = None,
        Attributes: Dict[str, str] = None,
    ) -> UpdateProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/customer-profiles.html#CustomerProfiles.Client.update_profile)
        [Show boto3-stubs documentation](./client.md#update_profile)
        """
