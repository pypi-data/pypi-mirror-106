"""
Type annotations for signer service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_signer import SignerClient
    from mypy_boto3_signer.paginator import (
        ListSigningJobsPaginator,
        ListSigningPlatformsPaginator,
        ListSigningProfilesPaginator,
    )

    client: SignerClient = boto3.client("signer")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import SigningProfileStatusType, SigningStatusType
from .type_defs import (
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)

class ListSigningJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/signer.html#Signer.Paginator.ListSigningJobs)[Show boto3-stubs documentation](./paginators.md#listsigningjobspaginator)
    """

    def paginate(
        self,
        status: SigningStatusType = None,
        platformId: str = None,
        requestedBy: str = None,
        isRevoked: bool = None,
        signatureExpiresBefore: datetime = None,
        signatureExpiresAfter: datetime = None,
        jobInvoker: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSigningJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/signer.html#Signer.Paginator.ListSigningJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listsigningjobspaginator)
        """

class ListSigningPlatformsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)[Show boto3-stubs documentation](./paginators.md#listsigningplatformspaginator)
    """

    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSigningPlatformsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms.paginate)
        [Show boto3-stubs documentation](./paginators.md#listsigningplatformspaginator)
        """

class ListSigningProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)[Show boto3-stubs documentation](./paginators.md#listsigningprofilespaginator)
    """

    def paginate(
        self,
        includeCanceled: bool = None,
        platformId: str = None,
        statuses: List[SigningProfileStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSigningProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/signer.html#Signer.Paginator.ListSigningProfiles.paginate)
        [Show boto3-stubs documentation](./paginators.md#listsigningprofilespaginator)
        """
