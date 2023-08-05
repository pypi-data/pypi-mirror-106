"""
Type annotations for iotsecuretunneling service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotsecuretunneling import IoTSecureTunnelingClient

    client: IoTSecureTunnelingClient = boto3.client("iotsecuretunneling")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    DescribeTunnelResponseTypeDef,
    DestinationConfigTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTunnelsResponseTypeDef,
    OpenTunnelResponseTypeDef,
    TagTypeDef,
    TimeoutConfigTypeDef,
)

__all__ = ("IoTSecureTunnelingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class IoTSecureTunnelingClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def close_tunnel(self, tunnelId: str, delete: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.close_tunnel)
        [Show boto3-stubs documentation](./client.md#close_tunnel)
        """
    def describe_tunnel(self, tunnelId: str) -> DescribeTunnelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.describe_tunnel)
        [Show boto3-stubs documentation](./client.md#describe_tunnel)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """
    def list_tunnels(
        self, thingName: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListTunnelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tunnels)
        [Show boto3-stubs documentation](./client.md#list_tunnels)
        """
    def open_tunnel(
        self,
        description: str = None,
        tags: List["TagTypeDef"] = None,
        destinationConfig: "DestinationConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
    ) -> OpenTunnelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.open_tunnel)
        [Show boto3-stubs documentation](./client.md#open_tunnel)
        """
    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """
