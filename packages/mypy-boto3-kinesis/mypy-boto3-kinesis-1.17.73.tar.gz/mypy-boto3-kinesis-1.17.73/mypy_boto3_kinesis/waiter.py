"""
Type annotations for kinesis service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesis import KinesisClient
    from mypy_boto3_kinesis.waiter import (
        StreamExistsWaiter,
        StreamNotExistsWaiter,
    )

    client: KinesisClient = boto3.client("kinesis")

    stream_exists_waiter: StreamExistsWaiter = client.get_waiter("stream_exists")
    stream_not_exists_waiter: StreamNotExistsWaiter = client.get_waiter("stream_not_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("StreamExistsWaiter", "StreamNotExistsWaiter")


class StreamExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kinesis.html#Kinesis.Waiter.stream_exists)[Show boto3-stubs documentation](./waiters.md#streamexistswaiter)
    """

    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kinesis.html#Kinesis.Waiter.StreamExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#streamexists)
        """


class StreamNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kinesis.html#Kinesis.Waiter.stream_not_exists)[Show boto3-stubs documentation](./waiters.md#streamnotexistswaiter)
    """

    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#streamnotexists)
        """
