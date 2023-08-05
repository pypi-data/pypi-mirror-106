"""
Type annotations for identitystore service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_identitystore import IdentityStoreClient

    client: IdentityStoreClient = boto3.client("identitystore")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    DescribeGroupResponseTypeDef,
    DescribeUserResponseTypeDef,
    FilterTypeDef,
    ListGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
)

__all__ = ("IdentityStoreClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IdentityStoreClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def describe_group(self, IdentityStoreId: str, GroupId: str) -> DescribeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client.describe_group)
        [Show boto3-stubs documentation](./client.md#describe_group)
        """
    def describe_user(self, IdentityStoreId: str, UserId: str) -> DescribeUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client.describe_user)
        [Show boto3-stubs documentation](./client.md#describe_user)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def list_groups(
        self,
        IdentityStoreId: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client.list_groups)
        [Show boto3-stubs documentation](./client.md#list_groups)
        """
    def list_users(
        self,
        IdentityStoreId: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/identitystore.html#IdentityStore.Client.list_users)
        [Show boto3-stubs documentation](./client.md#list_users)
        """
