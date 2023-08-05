"""
Type annotations for mediapackage-vod service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackage_vod import MediaPackageVodClient

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)
from .type_defs import (
    AuthorizationTypeDef,
    CmafPackageTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateAssetResponseTypeDef,
    CreatePackagingConfigurationResponseTypeDef,
    CreatePackagingGroupResponseTypeDef,
    DashPackageTypeDef,
    DescribeAssetResponseTypeDef,
    DescribePackagingConfigurationResponseTypeDef,
    DescribePackagingGroupResponseTypeDef,
    EgressAccessLogsTypeDef,
    HlsPackageTypeDef,
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MssPackageTypeDef,
    UpdatePackagingGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaPackageVodClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]


class MediaPackageVodClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def configure_logs(
        self, Id: str, EgressAccessLogs: "EgressAccessLogsTypeDef" = None
    ) -> ConfigureLogsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.configure_logs)
        [Show boto3-stubs documentation](./client.md#configure_logs)
        """

    def create_asset(
        self,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateAssetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_asset)
        [Show boto3-stubs documentation](./client.md#create_asset)
        """

    def create_packaging_configuration(
        self,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: "CmafPackageTypeDef" = None,
        DashPackage: "DashPackageTypeDef" = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        MssPackage: "MssPackageTypeDef" = None,
        Tags: Dict[str, str] = None,
    ) -> CreatePackagingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_configuration)
        [Show boto3-stubs documentation](./client.md#create_packaging_configuration)
        """

    def create_packaging_group(
        self,
        Id: str,
        Authorization: "AuthorizationTypeDef" = None,
        EgressAccessLogs: "EgressAccessLogsTypeDef" = None,
        Tags: Dict[str, str] = None,
    ) -> CreatePackagingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_group)
        [Show boto3-stubs documentation](./client.md#create_packaging_group)
        """

    def delete_asset(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_asset)
        [Show boto3-stubs documentation](./client.md#delete_asset)
        """

    def delete_packaging_configuration(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_configuration)
        [Show boto3-stubs documentation](./client.md#delete_packaging_configuration)
        """

    def delete_packaging_group(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_group)
        [Show boto3-stubs documentation](./client.md#delete_packaging_group)
        """

    def describe_asset(self, Id: str) -> DescribeAssetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_asset)
        [Show boto3-stubs documentation](./client.md#describe_asset)
        """

    def describe_packaging_configuration(
        self, Id: str
    ) -> DescribePackagingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_configuration)
        [Show boto3-stubs documentation](./client.md#describe_packaging_configuration)
        """

    def describe_packaging_group(self, Id: str) -> DescribePackagingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_group)
        [Show boto3-stubs documentation](./client.md#describe_packaging_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def list_assets(
        self, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ListAssetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_assets)
        [Show boto3-stubs documentation](./client.md#list_assets)
        """

    def list_packaging_configurations(
        self, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ListPackagingConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_configurations)
        [Show boto3-stubs documentation](./client.md#list_packaging_configurations)
        """

    def list_packaging_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagingGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_groups)
        [Show boto3-stubs documentation](./client.md#list_packaging_groups)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_packaging_group(
        self, Id: str, Authorization: "AuthorizationTypeDef" = None
    ) -> UpdatePackagingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Client.update_packaging_group)
        [Show boto3-stubs documentation](./client.md#update_packaging_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assets"]) -> ListAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)[Show boto3-stubs documentation](./paginators.md#listassetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> ListPackagingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)[Show boto3-stubs documentation](./paginators.md#listpackagingconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_groups"]
    ) -> ListPackagingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)[Show boto3-stubs documentation](./paginators.md#listpackaginggroupspaginator)
        """
