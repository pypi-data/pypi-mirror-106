"""
Type annotations for nimble service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_nimble import NimbleStudioClient

    client: NimbleStudioClient = boto3.client("nimble")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import StreamingInstanceTypeType, StudioComponentSubtypeType, StudioComponentTypeType
from .paginator import (
    ListEulaAcceptancesPaginator,
    ListEulasPaginator,
    ListLaunchProfileMembersPaginator,
    ListLaunchProfilesPaginator,
    ListStreamingImagesPaginator,
    ListStreamingSessionsPaginator,
    ListStudioComponentsPaginator,
    ListStudioMembersPaginator,
    ListStudiosPaginator,
)
from .type_defs import (
    AcceptEulasResponseTypeDef,
    CreateLaunchProfileResponseTypeDef,
    CreateStreamingImageResponseTypeDef,
    CreateStreamingSessionResponseTypeDef,
    CreateStreamingSessionStreamResponseTypeDef,
    CreateStudioComponentResponseTypeDef,
    CreateStudioResponseTypeDef,
    DeleteLaunchProfileResponseTypeDef,
    DeleteStreamingImageResponseTypeDef,
    DeleteStreamingSessionResponseTypeDef,
    DeleteStudioComponentResponseTypeDef,
    DeleteStudioResponseTypeDef,
    GetEulaResponseTypeDef,
    GetLaunchProfileDetailsResponseTypeDef,
    GetLaunchProfileInitializationResponseTypeDef,
    GetLaunchProfileMemberResponseTypeDef,
    GetLaunchProfileResponseTypeDef,
    GetStreamingImageResponseTypeDef,
    GetStreamingSessionResponseTypeDef,
    GetStreamingSessionStreamResponseTypeDef,
    GetStudioComponentResponseTypeDef,
    GetStudioMemberResponseTypeDef,
    GetStudioResponseTypeDef,
    ListEulaAcceptancesResponseTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NewLaunchProfileMemberTypeDef,
    NewStudioMemberTypeDef,
    ScriptParameterKeyValueTypeDef,
    StartStudioSSOConfigurationRepairResponseTypeDef,
    StreamConfigurationCreateTypeDef,
    StudioComponentConfigurationTypeDef,
    StudioComponentInitializationScriptTypeDef,
    StudioEncryptionConfigurationTypeDef,
    UpdateLaunchProfileMemberResponseTypeDef,
    UpdateLaunchProfileResponseTypeDef,
    UpdateStreamingImageResponseTypeDef,
    UpdateStudioComponentResponseTypeDef,
    UpdateStudioResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NimbleStudioClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class NimbleStudioClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_eulas(
        self, studioId: str, clientToken: str = None, eulaIds: List[str] = None
    ) -> AcceptEulasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.accept_eulas)
        [Show boto3-stubs documentation](./client.md#accept_eulas)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_launch_profile(
        self,
        ec2SubnetIds: List[str],
        launchProfileProtocolVersions: List[str],
        name: str,
        streamConfiguration: StreamConfigurationCreateTypeDef,
        studioComponentIds: List[str],
        studioId: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateLaunchProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.create_launch_profile)
        [Show boto3-stubs documentation](./client.md#create_launch_profile)
        """

    def create_streaming_image(
        self,
        ec2ImageId: str,
        name: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateStreamingImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.create_streaming_image)
        [Show boto3-stubs documentation](./client.md#create_streaming_image)
        """

    def create_streaming_session(
        self,
        studioId: str,
        clientToken: str = None,
        ec2InstanceType: StreamingInstanceTypeType = None,
        launchProfileId: str = None,
        streamingImageId: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateStreamingSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session)
        [Show boto3-stubs documentation](./client.md#create_streaming_session)
        """

    def create_streaming_session_stream(
        self,
        sessionId: str,
        studioId: str,
        clientToken: str = None,
        expirationInSeconds: int = None,
    ) -> CreateStreamingSessionStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session_stream)
        [Show boto3-stubs documentation](./client.md#create_streaming_session_stream)
        """

    def create_studio(
        self,
        adminRoleArn: str,
        displayName: str,
        studioName: str,
        userRoleArn: str,
        clientToken: str = None,
        studioEncryptionConfiguration: "StudioEncryptionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateStudioResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.create_studio)
        [Show boto3-stubs documentation](./client.md#create_studio)
        """

    def create_studio_component(
        self,
        name: str,
        studioId: str,
        type: StudioComponentTypeType,
        clientToken: str = None,
        configuration: "StudioComponentConfigurationTypeDef" = None,
        description: str = None,
        ec2SecurityGroupIds: List[str] = None,
        initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
        scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
        subtype: StudioComponentSubtypeType = None,
        tags: Dict[str, str] = None,
    ) -> CreateStudioComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.create_studio_component)
        [Show boto3-stubs documentation](./client.md#create_studio_component)
        """

    def delete_launch_profile(
        self, launchProfileId: str, studioId: str, clientToken: str = None
    ) -> DeleteLaunchProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile)
        [Show boto3-stubs documentation](./client.md#delete_launch_profile)
        """

    def delete_launch_profile_member(
        self, launchProfileId: str, principalId: str, studioId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile_member)
        [Show boto3-stubs documentation](./client.md#delete_launch_profile_member)
        """

    def delete_streaming_image(
        self, streamingImageId: str, studioId: str, clientToken: str = None
    ) -> DeleteStreamingImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_image)
        [Show boto3-stubs documentation](./client.md#delete_streaming_image)
        """

    def delete_streaming_session(
        self, sessionId: str, studioId: str, clientToken: str = None
    ) -> DeleteStreamingSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_session)
        [Show boto3-stubs documentation](./client.md#delete_streaming_session)
        """

    def delete_studio(self, studioId: str, clientToken: str = None) -> DeleteStudioResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_studio)
        [Show boto3-stubs documentation](./client.md#delete_studio)
        """

    def delete_studio_component(
        self, studioComponentId: str, studioId: str, clientToken: str = None
    ) -> DeleteStudioComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_studio_component)
        [Show boto3-stubs documentation](./client.md#delete_studio_component)
        """

    def delete_studio_member(
        self, principalId: str, studioId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.delete_studio_member)
        [Show boto3-stubs documentation](./client.md#delete_studio_member)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_eula(self, eulaId: str) -> GetEulaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_eula)
        [Show boto3-stubs documentation](./client.md#get_eula)
        """

    def get_launch_profile(
        self, launchProfileId: str, studioId: str
    ) -> GetLaunchProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile)
        [Show boto3-stubs documentation](./client.md#get_launch_profile)
        """

    def get_launch_profile_details(
        self, launchProfileId: str, studioId: str
    ) -> GetLaunchProfileDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_details)
        [Show boto3-stubs documentation](./client.md#get_launch_profile_details)
        """

    def get_launch_profile_initialization(
        self,
        launchProfileId: str,
        launchProfileProtocolVersions: List[str],
        launchPurpose: str,
        platform: str,
        studioId: str,
    ) -> GetLaunchProfileInitializationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_initialization)
        [Show boto3-stubs documentation](./client.md#get_launch_profile_initialization)
        """

    def get_launch_profile_member(
        self, launchProfileId: str, principalId: str, studioId: str
    ) -> GetLaunchProfileMemberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_member)
        [Show boto3-stubs documentation](./client.md#get_launch_profile_member)
        """

    def get_streaming_image(
        self, streamingImageId: str, studioId: str
    ) -> GetStreamingImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_streaming_image)
        [Show boto3-stubs documentation](./client.md#get_streaming_image)
        """

    def get_streaming_session(
        self, sessionId: str, studioId: str
    ) -> GetStreamingSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session)
        [Show boto3-stubs documentation](./client.md#get_streaming_session)
        """

    def get_streaming_session_stream(
        self, sessionId: str, streamId: str, studioId: str
    ) -> GetStreamingSessionStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_stream)
        [Show boto3-stubs documentation](./client.md#get_streaming_session_stream)
        """

    def get_studio(self, studioId: str) -> GetStudioResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_studio)
        [Show boto3-stubs documentation](./client.md#get_studio)
        """

    def get_studio_component(
        self, studioComponentId: str, studioId: str
    ) -> GetStudioComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_studio_component)
        [Show boto3-stubs documentation](./client.md#get_studio_component)
        """

    def get_studio_member(self, principalId: str, studioId: str) -> GetStudioMemberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.get_studio_member)
        [Show boto3-stubs documentation](./client.md#get_studio_member)
        """

    def list_eula_acceptances(
        self, studioId: str, eulaIds: List[str] = None, nextToken: str = None
    ) -> ListEulaAcceptancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_eula_acceptances)
        [Show boto3-stubs documentation](./client.md#list_eula_acceptances)
        """

    def list_eulas(
        self, eulaIds: List[str] = None, nextToken: str = None
    ) -> ListEulasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_eulas)
        [Show boto3-stubs documentation](./client.md#list_eulas)
        """

    def list_launch_profile_members(
        self, launchProfileId: str, studioId: str, maxResults: int = None, nextToken: str = None
    ) -> ListLaunchProfileMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_launch_profile_members)
        [Show boto3-stubs documentation](./client.md#list_launch_profile_members)
        """

    def list_launch_profiles(
        self,
        studioId: str,
        maxResults: int = None,
        nextToken: str = None,
        principalId: str = None,
        states: List[str] = None,
    ) -> ListLaunchProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_launch_profiles)
        [Show boto3-stubs documentation](./client.md#list_launch_profiles)
        """

    def list_streaming_images(
        self, studioId: str, nextToken: str = None, owner: str = None
    ) -> ListStreamingImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_streaming_images)
        [Show boto3-stubs documentation](./client.md#list_streaming_images)
        """

    def list_streaming_sessions(
        self, studioId: str, createdBy: str = None, nextToken: str = None, sessionIds: str = None
    ) -> ListStreamingSessionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_streaming_sessions)
        [Show boto3-stubs documentation](./client.md#list_streaming_sessions)
        """

    def list_studio_components(
        self,
        studioId: str,
        maxResults: int = None,
        nextToken: str = None,
        states: List[str] = None,
        types: List[str] = None,
    ) -> ListStudioComponentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_studio_components)
        [Show boto3-stubs documentation](./client.md#list_studio_components)
        """

    def list_studio_members(
        self, studioId: str, maxResults: int = None, nextToken: str = None
    ) -> ListStudioMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_studio_members)
        [Show boto3-stubs documentation](./client.md#list_studio_members)
        """

    def list_studios(self, nextToken: str = None) -> ListStudiosResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_studios)
        [Show boto3-stubs documentation](./client.md#list_studios)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def put_launch_profile_members(
        self,
        identityStoreId: str,
        launchProfileId: str,
        members: List[NewLaunchProfileMemberTypeDef],
        studioId: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.put_launch_profile_members)
        [Show boto3-stubs documentation](./client.md#put_launch_profile_members)
        """

    def put_studio_members(
        self,
        identityStoreId: str,
        members: List[NewStudioMemberTypeDef],
        studioId: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.put_studio_members)
        [Show boto3-stubs documentation](./client.md#put_studio_members)
        """

    def start_studio_sso_configuration_repair(
        self, studioId: str, clientToken: str = None
    ) -> StartStudioSSOConfigurationRepairResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.start_studio_sso_configuration_repair)
        [Show boto3-stubs documentation](./client.md#start_studio_sso_configuration_repair)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_launch_profile(
        self,
        launchProfileId: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        launchProfileProtocolVersions: List[str] = None,
        name: str = None,
        streamConfiguration: StreamConfigurationCreateTypeDef = None,
        studioComponentIds: List[str] = None,
    ) -> UpdateLaunchProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile)
        [Show boto3-stubs documentation](./client.md#update_launch_profile)
        """

    def update_launch_profile_member(
        self,
        launchProfileId: str,
        persona: Literal["USER"],
        principalId: str,
        studioId: str,
        clientToken: str = None,
    ) -> UpdateLaunchProfileMemberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile_member)
        [Show boto3-stubs documentation](./client.md#update_launch_profile_member)
        """

    def update_streaming_image(
        self,
        streamingImageId: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        name: str = None,
    ) -> UpdateStreamingImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.update_streaming_image)
        [Show boto3-stubs documentation](./client.md#update_streaming_image)
        """

    def update_studio(
        self,
        studioId: str,
        adminRoleArn: str = None,
        clientToken: str = None,
        displayName: str = None,
        userRoleArn: str = None,
    ) -> UpdateStudioResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.update_studio)
        [Show boto3-stubs documentation](./client.md#update_studio)
        """

    def update_studio_component(
        self,
        studioComponentId: str,
        studioId: str,
        clientToken: str = None,
        configuration: "StudioComponentConfigurationTypeDef" = None,
        description: str = None,
        ec2SecurityGroupIds: List[str] = None,
        initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
        name: str = None,
        scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
        subtype: StudioComponentSubtypeType = None,
        type: StudioComponentTypeType = None,
    ) -> UpdateStudioComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Client.update_studio_component)
        [Show boto3-stubs documentation](./client.md#update_studio_component)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_eula_acceptances"]
    ) -> ListEulaAcceptancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances)[Show boto3-stubs documentation](./paginators.md#listeulaacceptancespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_eulas"]) -> ListEulasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas)[Show boto3-stubs documentation](./paginators.md#listeulaspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_profile_members"]
    ) -> ListLaunchProfileMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers)[Show boto3-stubs documentation](./paginators.md#listlaunchprofilememberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_profiles"]
    ) -> ListLaunchProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles)[Show boto3-stubs documentation](./paginators.md#listlaunchprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_images"]
    ) -> ListStreamingImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages)[Show boto3-stubs documentation](./paginators.md#liststreamingimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_sessions"]
    ) -> ListStreamingSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions)[Show boto3-stubs documentation](./paginators.md#liststreamingsessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_components"]
    ) -> ListStudioComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents)[Show boto3-stubs documentation](./paginators.md#liststudiocomponentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_members"]
    ) -> ListStudioMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers)[Show boto3-stubs documentation](./paginators.md#liststudiomemberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_studios"]) -> ListStudiosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios)[Show boto3-stubs documentation](./paginators.md#liststudiospaginator)
        """
