"""
Type annotations for route53 service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53 import Route53Client
    from mypy_boto3_route53.waiter import (
        ResourceRecordSetsChangedWaiter,
    )

    client: Route53Client = boto3.client("route53")

    resource_record_sets_changed_waiter: ResourceRecordSetsChangedWaiter = client.get_waiter("resource_record_sets_changed")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("ResourceRecordSetsChangedWaiter",)


class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/route53.html#Route53.Waiter.resource_record_sets_changed)[Show boto3-stubs documentation](./waiters.md#resourcerecordsetschangedwaiter)
    """

    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChangedWaiter)
        [Show boto3-stubs documentation](./waiters.md#resourcerecordsetschanged)
        """
