"""
Type annotations for elasticache service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_elasticache import ElastiCacheClient
    from mypy_boto3_elasticache.paginator import (
        DescribeCacheClustersPaginator,
        DescribeCacheEngineVersionsPaginator,
        DescribeCacheParameterGroupsPaginator,
        DescribeCacheParametersPaginator,
        DescribeCacheSecurityGroupsPaginator,
        DescribeCacheSubnetGroupsPaginator,
        DescribeEngineDefaultParametersPaginator,
        DescribeEventsPaginator,
        DescribeGlobalReplicationGroupsPaginator,
        DescribeReplicationGroupsPaginator,
        DescribeReservedCacheNodesPaginator,
        DescribeReservedCacheNodesOfferingsPaginator,
        DescribeServiceUpdatesPaginator,
        DescribeSnapshotsPaginator,
        DescribeUpdateActionsPaginator,
        DescribeUserGroupsPaginator,
        DescribeUsersPaginator,
    )

    client: ElastiCacheClient = boto3.client("elasticache")

    describe_cache_clusters_paginator: DescribeCacheClustersPaginator = client.get_paginator("describe_cache_clusters")
    describe_cache_engine_versions_paginator: DescribeCacheEngineVersionsPaginator = client.get_paginator("describe_cache_engine_versions")
    describe_cache_parameter_groups_paginator: DescribeCacheParameterGroupsPaginator = client.get_paginator("describe_cache_parameter_groups")
    describe_cache_parameters_paginator: DescribeCacheParametersPaginator = client.get_paginator("describe_cache_parameters")
    describe_cache_security_groups_paginator: DescribeCacheSecurityGroupsPaginator = client.get_paginator("describe_cache_security_groups")
    describe_cache_subnet_groups_paginator: DescribeCacheSubnetGroupsPaginator = client.get_paginator("describe_cache_subnet_groups")
    describe_engine_default_parameters_paginator: DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_global_replication_groups_paginator: DescribeGlobalReplicationGroupsPaginator = client.get_paginator("describe_global_replication_groups")
    describe_replication_groups_paginator: DescribeReplicationGroupsPaginator = client.get_paginator("describe_replication_groups")
    describe_reserved_cache_nodes_paginator: DescribeReservedCacheNodesPaginator = client.get_paginator("describe_reserved_cache_nodes")
    describe_reserved_cache_nodes_offerings_paginator: DescribeReservedCacheNodesOfferingsPaginator = client.get_paginator("describe_reserved_cache_nodes_offerings")
    describe_service_updates_paginator: DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_update_actions_paginator: DescribeUpdateActionsPaginator = client.get_paginator("describe_update_actions")
    describe_user_groups_paginator: DescribeUserGroupsPaginator = client.get_paginator("describe_user_groups")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ServiceUpdateStatusType, SourceTypeType, UpdateActionStatusType
from .type_defs import (
    CacheClusterMessageTypeDef,
    CacheEngineVersionMessageTypeDef,
    CacheParameterGroupDetailsTypeDef,
    CacheParameterGroupsMessageTypeDef,
    CacheSecurityGroupMessageTypeDef,
    CacheSubnetGroupMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeGlobalReplicationGroupsResultTypeDef,
    DescribeSnapshotsListMessageTypeDef,
    DescribeUserGroupsResultTypeDef,
    DescribeUsersResultTypeDef,
    EventsMessageTypeDef,
    FilterTypeDef,
    PaginatorConfigTypeDef,
    ReplicationGroupMessageTypeDef,
    ReservedCacheNodeMessageTypeDef,
    ReservedCacheNodesOfferingMessageTypeDef,
    ServiceUpdatesMessageTypeDef,
    TimeRangeFilterTypeDef,
    UpdateActionsMessageTypeDef,
)

__all__ = (
    "DescribeCacheClustersPaginator",
    "DescribeCacheEngineVersionsPaginator",
    "DescribeCacheParameterGroupsPaginator",
    "DescribeCacheParametersPaginator",
    "DescribeCacheSecurityGroupsPaginator",
    "DescribeCacheSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalReplicationGroupsPaginator",
    "DescribeReplicationGroupsPaginator",
    "DescribeReservedCacheNodesPaginator",
    "DescribeReservedCacheNodesOfferingsPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeUpdateActionsPaginator",
    "DescribeUserGroupsPaginator",
    "DescribeUsersPaginator",
)

class DescribeCacheClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)[Show boto3-stubs documentation](./paginators.md#describecacheclusterspaginator)
    """

    def paginate(
        self,
        CacheClusterId: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CacheClusterMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters.paginate)
        [Show boto3-stubs documentation](./paginators.md#describecacheclusterspaginator)
        """

class DescribeCacheEngineVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)[Show boto3-stubs documentation](./paginators.md#describecacheengineversionspaginator)
    """

    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CacheEngineVersionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions.paginate)
        [Show boto3-stubs documentation](./paginators.md#describecacheengineversionspaginator)
        """

class DescribeCacheParameterGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)[Show boto3-stubs documentation](./paginators.md#describecacheparametergroupspaginator)
    """

    def paginate(
        self, CacheParameterGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#describecacheparametergroupspaginator)
        """

class DescribeCacheParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)[Show boto3-stubs documentation](./paginators.md#describecacheparameterspaginator)
    """

    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CacheParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters.paginate)
        [Show boto3-stubs documentation](./paginators.md#describecacheparameterspaginator)
        """

class DescribeCacheSecurityGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)[Show boto3-stubs documentation](./paginators.md#describecachesecuritygroupspaginator)
    """

    def paginate(
        self, CacheSecurityGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheSecurityGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#describecachesecuritygroupspaginator)
        """

class DescribeCacheSubnetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)[Show boto3-stubs documentation](./paginators.md#describecachesubnetgroupspaginator)
    """

    def paginate(
        self, CacheSubnetGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#describecachesubnetgroupspaginator)
        """

class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)[Show boto3-stubs documentation](./paginators.md#describeenginedefaultparameterspaginator)
    """

    def paginate(
        self, CacheParameterGroupFamily: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeenginedefaultparameterspaginator)
        """

class DescribeEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)[Show boto3-stubs documentation](./paginators.md#describeeventspaginator)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeeventspaginator)
        """

class DescribeGlobalReplicationGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups)[Show boto3-stubs documentation](./paginators.md#describeglobalreplicationgroupspaginator)
    """

    def paginate(
        self,
        GlobalReplicationGroupId: str = None,
        ShowMemberInfo: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeGlobalReplicationGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeglobalreplicationgroupspaginator)
        """

class DescribeReplicationGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)[Show boto3-stubs documentation](./paginators.md#describereplicationgroupspaginator)
    """

    def paginate(
        self, ReplicationGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReplicationGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#describereplicationgroupspaginator)
        """

class DescribeReservedCacheNodesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)[Show boto3-stubs documentation](./paginators.md#describereservedcachenodespaginator)
    """

    def paginate(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ReservedCacheNodeMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes.paginate)
        [Show boto3-stubs documentation](./paginators.md#describereservedcachenodespaginator)
        """

class DescribeReservedCacheNodesOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)[Show boto3-stubs documentation](./paginators.md#describereservedcachenodesofferingspaginator)
    """

    def paginate(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ReservedCacheNodesOfferingMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings.paginate)
        [Show boto3-stubs documentation](./paginators.md#describereservedcachenodesofferingspaginator)
        """

class DescribeServiceUpdatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)[Show boto3-stubs documentation](./paginators.md#describeserviceupdatespaginator)
    """

    def paginate(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[ServiceUpdateStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ServiceUpdatesMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeserviceupdatespaginator)
        """

class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)[Show boto3-stubs documentation](./paginators.md#describesnapshotspaginator)
    """

    def paginate(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        ShowNodeGroupConfig: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSnapshotsListMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](./paginators.md#describesnapshotspaginator)
        """

class DescribeUpdateActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)[Show boto3-stubs documentation](./paginators.md#describeupdateactionspaginator)
    """

    def paginate(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[ServiceUpdateStatusType] = None,
        ServiceUpdateTimeRange: TimeRangeFilterTypeDef = None,
        UpdateActionStatus: List[UpdateActionStatusType] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[UpdateActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeupdateactionspaginator)
        """

class DescribeUserGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups)[Show boto3-stubs documentation](./paginators.md#describeusergroupspaginator)
    """

    def paginate(
        self, UserGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUserGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeusergroupspaginator)
        """

class DescribeUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers)[Show boto3-stubs documentation](./paginators.md#describeuserspaginator)
    """

    def paginate(
        self,
        Engine: str = None,
        UserId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeUsersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](./paginators.md#describeuserspaginator)
        """
