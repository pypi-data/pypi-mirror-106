"""
Type annotations for events service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_events import EventBridgeClient
    from mypy_boto3_events.paginator import (
        ListRuleNamesByTargetPaginator,
        ListRulesPaginator,
        ListTargetsByRulePaginator,
    )

    client: EventBridgeClient = boto3.client("events")

    list_rule_names_by_target_paginator: ListRuleNamesByTargetPaginator = client.get_paginator("list_rule_names_by_target")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_targets_by_rule_paginator: ListTargetsByRulePaginator = client.get_paginator("list_targets_by_rule")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTargetsByRuleResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListRuleNamesByTargetPaginator", "ListRulesPaginator", "ListTargetsByRulePaginator")


class ListRuleNamesByTargetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)[Show boto3-stubs documentation](./paginators.md#listrulenamesbytargetpaginator)
    """

    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRuleNamesByTargetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget.paginate)
        [Show boto3-stubs documentation](./paginators.md#listrulenamesbytargetpaginator)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/events.html#EventBridge.Paginator.ListRules)[Show boto3-stubs documentation](./paginators.md#listrulespaginator)
    """

    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/events.html#EventBridge.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](./paginators.md#listrulespaginator)
        """


class ListTargetsByRulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)[Show boto3-stubs documentation](./paginators.md#listtargetsbyrulepaginator)
    """

    def paginate(
        self, Rule: str, EventBusName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsByRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtargetsbyrulepaginator)
        """
