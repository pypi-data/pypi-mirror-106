"""
Type annotations for ssm-incidents service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm_incidents import SSMIncidentsClient
    from mypy_boto3_ssm_incidents.waiter import (
        WaitForReplicationSetActiveWaiter,
        WaitForReplicationSetDeletedWaiter,
    )

    client: SSMIncidentsClient = boto3.client("ssm-incidents")

    wait_for_replication_set_active_waiter: WaitForReplicationSetActiveWaiter = client.get_waiter("wait_for_replication_set_active")
    wait_for_replication_set_deleted_waiter: WaitForReplicationSetDeletedWaiter = client.get_waiter("wait_for_replication_set_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("WaitForReplicationSetActiveWaiter", "WaitForReplicationSetDeletedWaiter")


class WaitForReplicationSetActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-incidents.html#SSMIncidents.Waiter.wait_for_replication_set_active)[Show boto3-stubs documentation](./waiters.md#waitforreplicationsetactivewaiter)
    """

    def wait(self, arn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-incidents.html#SSMIncidents.Waiter.WaitForReplicationSetActiveWaiter)
        [Show boto3-stubs documentation](./waiters.md#waitforreplicationsetactive)
        """


class WaitForReplicationSetDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-incidents.html#SSMIncidents.Waiter.wait_for_replication_set_deleted)[Show boto3-stubs documentation](./waiters.md#waitforreplicationsetdeletedwaiter)
    """

    def wait(self, arn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm-incidents.html#SSMIncidents.Waiter.WaitForReplicationSetDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#waitforreplicationsetdeleted)
        """
