"""
Type annotations for transfer service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_transfer import TransferClient
    from mypy_boto3_transfer.paginator import (
        ListServersPaginator,
    )

    client: TransferClient = boto3.client("transfer")

    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListServersResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListServersPaginator",)

class ListServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/transfer.html#Transfer.Paginator.ListServers)[Show boto3-stubs documentation](./paginators.md#listserverspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        [Show boto3-stubs documentation](./paginators.md#listserverspaginator)
        """
