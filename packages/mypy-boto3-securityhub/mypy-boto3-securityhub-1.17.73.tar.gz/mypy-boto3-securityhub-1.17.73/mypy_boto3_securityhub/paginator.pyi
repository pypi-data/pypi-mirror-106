"""
Type annotations for securityhub service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_securityhub import SecurityHubClient
    from mypy_boto3_securityhub.paginator import (
        GetEnabledStandardsPaginator,
        GetFindingsPaginator,
        GetInsightsPaginator,
        ListEnabledProductsForImportPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
    )

    client: SecurityHubClient = boto3.client("securityhub")

    get_enabled_standards_paginator: GetEnabledStandardsPaginator = client.get_paginator("get_enabled_standards")
    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    get_insights_paginator: GetInsightsPaginator = client.get_paginator("get_insights")
    list_enabled_products_for_import_paginator: ListEnabledProductsForImportPaginator = client.get_paginator("list_enabled_products_for_import")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    AwsSecurityFindingFiltersTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightsResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    PaginatorConfigTypeDef,
    SortCriterionTypeDef,
)

__all__ = (
    "GetEnabledStandardsPaginator",
    "GetFindingsPaginator",
    "GetInsightsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
)

class GetEnabledStandardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)[Show boto3-stubs documentation](./paginators.md#getenabledstandardspaginator)
    """

    def paginate(
        self,
        StandardsSubscriptionArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetEnabledStandardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards.paginate)
        [Show boto3-stubs documentation](./paginators.md#getenabledstandardspaginator)
        """

class GetFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)[Show boto3-stubs documentation](./paginators.md#getfindingspaginator)
    """

    def paginate(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings.paginate)
        [Show boto3-stubs documentation](./paginators.md#getfindingspaginator)
        """

class GetInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)[Show boto3-stubs documentation](./paginators.md#getinsightspaginator)
    """

    def paginate(
        self, InsightArns: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights.paginate)
        [Show boto3-stubs documentation](./paginators.md#getinsightspaginator)
        """

class ListEnabledProductsForImportPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)[Show boto3-stubs documentation](./paginators.md#listenabledproductsforimportpaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledProductsForImportResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport.paginate)
        [Show boto3-stubs documentation](./paginators.md#listenabledproductsforimportpaginator)
        """

class ListInvitationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)[Show boto3-stubs documentation](./paginators.md#listinvitationspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvitationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations.paginate)
        [Show boto3-stubs documentation](./paginators.md#listinvitationspaginator)
        """

class ListMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)[Show boto3-stubs documentation](./paginators.md#listmemberspaginator)
    """

    def paginate(
        self, OnlyAssociated: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmemberspaginator)
        """
