"""
Type annotations for mwaa service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_mwaa import MWAAClient
    from mypy_boto3_mwaa.paginator import (
        ListEnvironmentsPaginator,
    )

    client: MWAAClient = boto3.client("mwaa")

    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListEnvironmentsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListEnvironmentsPaginator",)


class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments)[Show boto3-stubs documentation](./paginators.md#listenvironmentspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](./paginators.md#listenvironmentspaginator)
        """
