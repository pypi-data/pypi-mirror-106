"""
Type annotations for stepfunctions service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_stepfunctions import SFNClient
    from mypy_boto3_stepfunctions.paginator import (
        GetExecutionHistoryPaginator,
        ListActivitiesPaginator,
        ListExecutionsPaginator,
        ListStateMachinesPaginator,
    )

    client: SFNClient = boto3.client("stepfunctions")

    get_execution_history_paginator: GetExecutionHistoryPaginator = client.get_paginator("get_execution_history")
    list_activities_paginator: ListActivitiesPaginator = client.get_paginator("list_activities")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_state_machines_paginator: ListStateMachinesPaginator = client.get_paginator("list_state_machines")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ExecutionStatusType
from .type_defs import (
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListStateMachinesPaginator",
)


class GetExecutionHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)[Show boto3-stubs documentation](./paginators.md#getexecutionhistorypaginator)
    """

    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        includeExecutionData: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetExecutionHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory.paginate)
        [Show boto3-stubs documentation](./paginators.md#getexecutionhistorypaginator)
        """


class ListActivitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)[Show boto3-stubs documentation](./paginators.md#listactivitiespaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActivitiesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.ListActivities.paginate)
        [Show boto3-stubs documentation](./paginators.md#listactivitiespaginator)
        """


class ListExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)[Show boto3-stubs documentation](./paginators.md#listexecutionspaginator)
    """

    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: ExecutionStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listexecutionspaginator)
        """


class ListStateMachinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)[Show boto3-stubs documentation](./paginators.md#liststatemachinespaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStateMachinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines.paginate)
        [Show boto3-stubs documentation](./paginators.md#liststatemachinespaginator)
        """
