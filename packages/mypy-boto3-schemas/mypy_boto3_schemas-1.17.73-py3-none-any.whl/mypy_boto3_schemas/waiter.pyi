"""
Type annotations for schemas service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_schemas import SchemasClient
    from mypy_boto3_schemas.waiter import (
        CodeBindingExistsWaiter,
    )

    client: SchemasClient = boto3.client("schemas")

    code_binding_exists_waiter: CodeBindingExistsWaiter = client.get_waiter("code_binding_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("CodeBindingExistsWaiter",)

class CodeBindingExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/schemas.html#Schemas.Waiter.code_binding_exists)[Show boto3-stubs documentation](./waiters.md#codebindingexistswaiter)
    """

    def wait(
        self,
        Language: str,
        RegistryName: str,
        SchemaName: str,
        SchemaVersion: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/schemas.html#Schemas.Waiter.CodeBindingExistsWaiter)
        [Show boto3-stubs documentation](./waiters.md#codebindingexists)
        """
