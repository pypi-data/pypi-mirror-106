"""
Type annotations for iot-data service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_data import IoTDataPlaneClient

    client: IoTDataPlaneClient = boto3.client("iot-data")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta

from .type_defs import (
    DeleteThingShadowResponseTypeDef,
    GetThingShadowResponseTypeDef,
    ListNamedShadowsForThingResponseTypeDef,
    UpdateThingShadowResponseTypeDef,
)

__all__ = ("IoTDataPlaneClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    RequestEntityTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnsupportedDocumentEncodingException: Type[BotocoreClientError]

class IoTDataPlaneClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def delete_thing_shadow(
        self, thingName: str, shadowName: str = None
    ) -> DeleteThingShadowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.delete_thing_shadow)
        [Show boto3-stubs documentation](./client.md#delete_thing_shadow)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def get_thing_shadow(
        self, thingName: str, shadowName: str = None
    ) -> GetThingShadowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.get_thing_shadow)
        [Show boto3-stubs documentation](./client.md#get_thing_shadow)
        """
    def list_named_shadows_for_thing(
        self, thingName: str, nextToken: str = None, pageSize: int = None
    ) -> ListNamedShadowsForThingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.list_named_shadows_for_thing)
        [Show boto3-stubs documentation](./client.md#list_named_shadows_for_thing)
        """
    def publish(self, topic: str, qos: int = None, payload: Union[bytes, IO[bytes]] = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.publish)
        [Show boto3-stubs documentation](./client.md#publish)
        """
    def update_thing_shadow(
        self, thingName: str, payload: Union[bytes, IO[bytes]], shadowName: str = None
    ) -> UpdateThingShadowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/iot-data.html#IoTDataPlane.Client.update_thing_shadow)
        [Show boto3-stubs documentation](./client.md#update_thing_shadow)
        """
