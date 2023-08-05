"""
Type annotations for dynamodbstreams service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodbstreams import DynamoDBStreamsClient

    client: DynamoDBStreamsClient = boto3.client("dynamodbstreams")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .literals import ShardIteratorTypeType
from .type_defs import (
    DescribeStreamOutputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListStreamsOutputTypeDef,
)

__all__ = ("DynamoDBStreamsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredIteratorException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TrimmedDataAccessException: Type[BotocoreClientError]


class DynamoDBStreamsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def describe_stream(
        self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.describe_stream)
        [Show boto3-stubs documentation](./client.md#describe_stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_records(self, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_records)
        [Show boto3-stubs documentation](./client.md#get_records)
        """

    def get_shard_iterator(
        self,
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: ShardIteratorTypeType,
        SequenceNumber: str = None,
    ) -> GetShardIteratorOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_shard_iterator)
        [Show boto3-stubs documentation](./client.md#get_shard_iterator)
        """

    def list_streams(
        self, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.list_streams)
        [Show boto3-stubs documentation](./client.md#list_streams)
        """
