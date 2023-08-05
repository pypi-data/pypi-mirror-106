"""
Type annotations for devops-guru service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_devops_guru import DevopsGuruClient
    from mypy_boto3_devops_guru.paginator import (
        DescribeResourceCollectionHealthPaginator,
        GetCostEstimationPaginator,
        GetResourceCollectionPaginator,
        ListAnomaliesForInsightPaginator,
        ListEventsPaginator,
        ListInsightsPaginator,
        ListNotificationChannelsPaginator,
        ListRecommendationsPaginator,
        SearchInsightsPaginator,
    )

    client: DevopsGuruClient = boto3.client("devops-guru")

    describe_resource_collection_health_paginator: DescribeResourceCollectionHealthPaginator = client.get_paginator("describe_resource_collection_health")
    get_cost_estimation_paginator: GetCostEstimationPaginator = client.get_paginator("get_cost_estimation")
    get_resource_collection_paginator: GetResourceCollectionPaginator = client.get_paginator("get_resource_collection")
    list_anomalies_for_insight_paginator: ListAnomaliesForInsightPaginator = client.get_paginator("list_anomalies_for_insight")
    list_events_paginator: ListEventsPaginator = client.get_paginator("list_events")
    list_insights_paginator: ListInsightsPaginator = client.get_paginator("list_insights")
    list_notification_channels_paginator: ListNotificationChannelsPaginator = client.get_paginator("list_notification_channels")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    search_insights_paginator: SearchInsightsPaginator = client.get_paginator("search_insights")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import InsightTypeType, LocaleType, ResourceCollectionTypeType
from .type_defs import (
    DescribeResourceCollectionHealthResponseTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
)

__all__ = (
    "DescribeResourceCollectionHealthPaginator",
    "GetCostEstimationPaginator",
    "GetResourceCollectionPaginator",
    "ListAnomaliesForInsightPaginator",
    "ListEventsPaginator",
    "ListInsightsPaginator",
    "ListNotificationChannelsPaginator",
    "ListRecommendationsPaginator",
    "SearchInsightsPaginator",
)

class DescribeResourceCollectionHealthPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.DescribeResourceCollectionHealth)[Show boto3-stubs documentation](./paginators.md#describeresourcecollectionhealthpaginator)
    """

    def paginate(
        self,
        ResourceCollectionType: ResourceCollectionTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeResourceCollectionHealthResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.DescribeResourceCollectionHealth.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeresourcecollectionhealthpaginator)
        """

class GetCostEstimationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.GetCostEstimation)[Show boto3-stubs documentation](./paginators.md#getcostestimationpaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCostEstimationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.GetCostEstimation.paginate)
        [Show boto3-stubs documentation](./paginators.md#getcostestimationpaginator)
        """

class GetResourceCollectionPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.GetResourceCollection)[Show boto3-stubs documentation](./paginators.md#getresourcecollectionpaginator)
    """

    def paginate(
        self,
        ResourceCollectionType: ResourceCollectionTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourceCollectionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.GetResourceCollection.paginate)
        [Show boto3-stubs documentation](./paginators.md#getresourcecollectionpaginator)
        """

class ListAnomaliesForInsightPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListAnomaliesForInsight)[Show boto3-stubs documentation](./paginators.md#listanomaliesforinsightpaginator)
    """

    def paginate(
        self,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAnomaliesForInsightResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListAnomaliesForInsight.paginate)
        [Show boto3-stubs documentation](./paginators.md#listanomaliesforinsightpaginator)
        """

class ListEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListEvents)[Show boto3-stubs documentation](./paginators.md#listeventspaginator)
    """

    def paginate(
        self, Filters: ListEventsFiltersTypeDef, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListEvents.paginate)
        [Show boto3-stubs documentation](./paginators.md#listeventspaginator)
        """

class ListInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListInsights)[Show boto3-stubs documentation](./paginators.md#listinsightspaginator)
    """

    def paginate(
        self,
        StatusFilter: ListInsightsStatusFilterTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListInsights.paginate)
        [Show boto3-stubs documentation](./paginators.md#listinsightspaginator)
        """

class ListNotificationChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListNotificationChannels)[Show boto3-stubs documentation](./paginators.md#listnotificationchannelspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListNotificationChannels.paginate)
        [Show boto3-stubs documentation](./paginators.md#listnotificationchannelspaginator)
        """

class ListRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListRecommendations)[Show boto3-stubs documentation](./paginators.md#listrecommendationspaginator)
    """

    def paginate(
        self,
        InsightId: str,
        Locale: LocaleType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](./paginators.md#listrecommendationspaginator)
        """

class SearchInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.SearchInsights)[Show boto3-stubs documentation](./paginators.md#searchinsightspaginator)
    """

    def paginate(
        self,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: SearchInsightsFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/devops-guru.html#DevopsGuru.Paginator.SearchInsights.paginate)
        [Show boto3-stubs documentation](./paginators.md#searchinsightspaginator)
        """
