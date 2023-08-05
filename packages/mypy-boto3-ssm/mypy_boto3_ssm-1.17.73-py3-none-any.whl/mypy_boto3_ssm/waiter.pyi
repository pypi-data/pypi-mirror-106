"""
Type annotations for ssm service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm import SSMClient
    from mypy_boto3_ssm.waiter import (
        CommandExecutedWaiter,
    )

    client: SSMClient = boto3.client("ssm")

    command_executed_waiter: CommandExecutedWaiter = client.get_waiter("command_executed")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("CommandExecutedWaiter",)

class CommandExecutedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm.html#SSM.Waiter.command_executed)[Show boto3-stubs documentation](./waiters.md#commandexecutedwaiter)
    """

    def wait(
        self,
        CommandId: str,
        InstanceId: str,
        PluginName: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/ssm.html#SSM.Waiter.CommandExecutedWaiter)
        [Show boto3-stubs documentation](./waiters.md#commandexecuted)
        """
