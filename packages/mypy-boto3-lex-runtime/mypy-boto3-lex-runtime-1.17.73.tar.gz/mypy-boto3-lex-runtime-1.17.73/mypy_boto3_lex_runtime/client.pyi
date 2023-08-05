"""
Type annotations for lex-runtime service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_lex_runtime import LexRuntimeServiceClient

    client: LexRuntimeServiceClient = boto3.client("lex-runtime")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from .type_defs import (
    ActiveContextTypeDef,
    DeleteSessionResponseTypeDef,
    DialogActionTypeDef,
    GetSessionResponseTypeDef,
    IntentSummaryTypeDef,
    PostContentResponseTypeDef,
    PostTextResponseTypeDef,
    PutSessionResponseTypeDef,
)

__all__ = ("LexRuntimeServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadGatewayException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailedException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LoopDetectedException: Type[BotocoreClientError]
    NotAcceptableException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    UnsupportedMediaTypeException: Type[BotocoreClientError]

class LexRuntimeServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def delete_session(
        self, botName: str, botAlias: str, userId: str
    ) -> DeleteSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.delete_session)
        [Show boto3-stubs documentation](./client.md#delete_session)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def get_session(
        self, botName: str, botAlias: str, userId: str, checkpointLabelFilter: str = None
    ) -> GetSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.get_session)
        [Show boto3-stubs documentation](./client.md#get_session)
        """
    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO[bytes]],
        sessionAttributes: str = None,
        requestAttributes: str = None,
        accept: str = None,
        activeContexts: str = None,
    ) -> PostContentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.post_content)
        [Show boto3-stubs documentation](./client.md#post_content)
        """
    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, str] = None,
        requestAttributes: Dict[str, str] = None,
        activeContexts: List["ActiveContextTypeDef"] = None,
    ) -> PostTextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.post_text)
        [Show boto3-stubs documentation](./client.md#post_text)
        """
    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, str] = None,
        dialogAction: "DialogActionTypeDef" = None,
        recentIntentSummaryView: List["IntentSummaryTypeDef"] = None,
        accept: str = None,
        activeContexts: List["ActiveContextTypeDef"] = None,
    ) -> PutSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/lex-runtime.html#LexRuntimeService.Client.put_session)
        [Show boto3-stubs documentation](./client.md#put_session)
        """
