"""
Type annotations for mobile service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_mobile import MobileClient
    from mypy_boto3_mobile.paginator import (
        ListBundlesPaginator,
        ListProjectsPaginator,
    )

    client: MobileClient = boto3.client("mobile")

    list_bundles_paginator: ListBundlesPaginator = client.get_paginator("list_bundles")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListBundlesResultTypeDef, ListProjectsResultTypeDef, PaginatorConfigTypeDef

__all__ = ("ListBundlesPaginator", "ListProjectsPaginator")


class ListBundlesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mobile.html#Mobile.Paginator.ListBundles)[Show boto3-stubs documentation](./paginators.md#listbundlespaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mobile.html#Mobile.Paginator.ListBundles.paginate)
        [Show boto3-stubs documentation](./paginators.md#listbundlespaginator)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mobile.html#Mobile.Paginator.ListProjects)[Show boto3-stubs documentation](./paginators.md#listprojectspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mobile.html#Mobile.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](./paginators.md#listprojectspaginator)
        """
