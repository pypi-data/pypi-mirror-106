"""
Type annotations for emr service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_emr import EMRClient
    from mypy_boto3_emr.waiter import (
        ClusterRunningWaiter,
        ClusterTerminatedWaiter,
        StepCompleteWaiter,
    )

    client: EMRClient = boto3.client("emr")

    cluster_running_waiter: ClusterRunningWaiter = client.get_waiter("cluster_running")
    cluster_terminated_waiter: ClusterTerminatedWaiter = client.get_waiter("cluster_terminated")
    step_complete_waiter: StepCompleteWaiter = client.get_waiter("step_complete")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("ClusterRunningWaiter", "ClusterTerminatedWaiter", "StepCompleteWaiter")


class ClusterRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/emr.html#EMR.Waiter.cluster_running)[Show boto3-stubs documentation](./waiters.md#clusterrunningwaiter)
    """

    def wait(self, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/emr.html#EMR.Waiter.ClusterRunningWaiter)
        [Show boto3-stubs documentation](./waiters.md#clusterrunning)
        """


class ClusterTerminatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/emr.html#EMR.Waiter.cluster_terminated)[Show boto3-stubs documentation](./waiters.md#clusterterminatedwaiter)
    """

    def wait(self, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/emr.html#EMR.Waiter.ClusterTerminatedWaiter)
        [Show boto3-stubs documentation](./waiters.md#clusterterminated)
        """


class StepCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/emr.html#EMR.Waiter.step_complete)[Show boto3-stubs documentation](./waiters.md#stepcompletewaiter)
    """

    def wait(self, ClusterId: str, StepId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/emr.html#EMR.Waiter.StepCompleteWaiter)
        [Show boto3-stubs documentation](./waiters.md#stepcomplete)
        """
