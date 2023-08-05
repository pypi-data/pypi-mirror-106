"""
Type annotations for mediatailor service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_mediatailor import MediaTailorClient
    from mypy_boto3_mediatailor.paginator import (
        GetChannelSchedulePaginator,
        ListChannelsPaginator,
        ListPlaybackConfigurationsPaginator,
        ListSourceLocationsPaginator,
        ListVodSourcesPaginator,
    )

    client: MediaTailorClient = boto3.client("mediatailor")

    get_channel_schedule_paginator: GetChannelSchedulePaginator = client.get_paginator("get_channel_schedule")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_playback_configurations_paginator: ListPlaybackConfigurationsPaginator = client.get_paginator("list_playback_configurations")
    list_source_locations_paginator: ListSourceLocationsPaginator = client.get_paginator("list_source_locations")
    list_vod_sources_paginator: ListVodSourcesPaginator = client.get_paginator("list_vod_sources")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    GetChannelScheduleResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListPlaybackConfigurationsResponseTypeDef,
    ListSourceLocationsResponseTypeDef,
    ListVodSourcesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetChannelSchedulePaginator",
    "ListChannelsPaginator",
    "ListPlaybackConfigurationsPaginator",
    "ListSourceLocationsPaginator",
    "ListVodSourcesPaginator",
)


class GetChannelSchedulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.GetChannelSchedule)[Show boto3-stubs documentation](./paginators.md#getchannelschedulepaginator)
    """

    def paginate(
        self,
        ChannelName: str,
        DurationMinutes: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetChannelScheduleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.GetChannelSchedule.paginate)
        [Show boto3-stubs documentation](./paginators.md#getchannelschedulepaginator)
        """


class ListChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListChannels)[Show boto3-stubs documentation](./paginators.md#listchannelspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](./paginators.md#listchannelspaginator)
        """


class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)[Show boto3-stubs documentation](./paginators.md#listplaybackconfigurationspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaybackConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations.paginate)
        [Show boto3-stubs documentation](./paginators.md#listplaybackconfigurationspaginator)
        """


class ListSourceLocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListSourceLocations)[Show boto3-stubs documentation](./paginators.md#listsourcelocationspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSourceLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListSourceLocations.paginate)
        [Show boto3-stubs documentation](./paginators.md#listsourcelocationspaginator)
        """


class ListVodSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListVodSources)[Show boto3-stubs documentation](./paginators.md#listvodsourcespaginator)
    """

    def paginate(
        self, SourceLocationName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVodSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/mediatailor.html#MediaTailor.Paginator.ListVodSources.paginate)
        [Show boto3-stubs documentation](./paginators.md#listvodsourcespaginator)
        """
