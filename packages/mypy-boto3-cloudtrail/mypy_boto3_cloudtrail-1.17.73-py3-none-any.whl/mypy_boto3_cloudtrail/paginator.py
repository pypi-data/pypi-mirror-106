"""
Type annotations for cloudtrail service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudtrail import CloudTrailClient
    from mypy_boto3_cloudtrail.paginator import (
        ListPublicKeysPaginator,
        ListTagsPaginator,
        ListTrailsPaginator,
        LookupEventsPaginator,
    )

    client: CloudTrailClient = boto3.client("cloudtrail")

    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_trails_paginator: ListTrailsPaginator = client.get_paginator("list_trails")
    lookup_events_paginator: LookupEventsPaginator = client.get_paginator("lookup_events")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListPublicKeysResponseTypeDef,
    ListTagsResponseTypeDef,
    ListTrailsResponseTypeDef,
    LookupAttributeTypeDef,
    LookupEventsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)


class ListPublicKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)[Show boto3-stubs documentation](./paginators.md#listpublickeyspaginator)
    """

    def paginate(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPublicKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys.paginate)
        [Show boto3-stubs documentation](./paginators.md#listpublickeyspaginator)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)[Show boto3-stubs documentation](./paginators.md#listtagspaginator)
    """

    def paginate(
        self, ResourceIdList: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtagspaginator)
        """


class ListTrailsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)[Show boto3-stubs documentation](./paginators.md#listtrailspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtrailspaginator)
        """


class LookupEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)[Show boto3-stubs documentation](./paginators.md#lookupeventspaginator)
    """

    def paginate(
        self,
        LookupAttributes: List[LookupAttributeTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: Literal["insight"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[LookupEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents.paginate)
        [Show boto3-stubs documentation](./paginators.md#lookupeventspaginator)
        """
