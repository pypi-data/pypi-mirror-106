"""
Type annotations for discovery service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_discovery import ApplicationDiscoveryServiceClient

    client: ApplicationDiscoveryServiceClient = boto3.client("discovery")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ConfigurationItemTypeType, ExportDataFormatType
from .paginator import (
    DescribeAgentsPaginator,
    DescribeContinuousExportsPaginator,
    DescribeExportConfigurationsPaginator,
    DescribeExportTasksPaginator,
    DescribeTagsPaginator,
    ListConfigurationsPaginator,
)
from .type_defs import (
    BatchDeleteImportDataResponseTypeDef,
    CreateApplicationResponseTypeDef,
    DescribeAgentsResponseTypeDef,
    DescribeConfigurationsResponseTypeDef,
    DescribeContinuousExportsResponseTypeDef,
    DescribeExportConfigurationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeImportTasksResponseTypeDef,
    DescribeTagsResponseTypeDef,
    ExportConfigurationsResponseTypeDef,
    ExportFilterTypeDef,
    FilterTypeDef,
    GetDiscoverySummaryResponseTypeDef,
    ImportTaskFilterTypeDef,
    ListConfigurationsResponseTypeDef,
    ListServerNeighborsResponseTypeDef,
    OrderByElementTypeDef,
    StartContinuousExportResponseTypeDef,
    StartDataCollectionByAgentIdsResponseTypeDef,
    StartExportTaskResponseTypeDef,
    StartImportTaskResponseTypeDef,
    StopContinuousExportResponseTypeDef,
    StopDataCollectionByAgentIdsResponseTypeDef,
    TagFilterTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationDiscoveryServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AuthorizationErrorException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictErrorException: Type[BotocoreClientError]
    HomeRegionNotSetException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerInternalErrorException: Type[BotocoreClientError]


class ApplicationDiscoveryServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_configuration_items_to_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.associate_configuration_items_to_application)
        [Show boto3-stubs documentation](./client.md#associate_configuration_items_to_application)
        """

    def batch_delete_import_data(
        self, importTaskIds: List[str]
    ) -> BatchDeleteImportDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.batch_delete_import_data)
        [Show boto3-stubs documentation](./client.md#batch_delete_import_data)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_application(
        self, name: str, description: str = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_application)
        [Show boto3-stubs documentation](./client.md#create_application)
        """

    def create_tags(self, configurationIds: List[str], tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_tags)
        [Show boto3-stubs documentation](./client.md#create_tags)
        """

    def delete_applications(self, configurationIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_applications)
        [Show boto3-stubs documentation](./client.md#delete_applications)
        """

    def delete_tags(
        self, configurationIds: List[str], tags: List[TagTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_tags)
        [Show boto3-stubs documentation](./client.md#delete_tags)
        """

    def describe_agents(
        self,
        agentIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeAgentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_agents)
        [Show boto3-stubs documentation](./client.md#describe_agents)
        """

    def describe_configurations(
        self, configurationIds: List[str]
    ) -> DescribeConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_configurations)
        [Show boto3-stubs documentation](./client.md#describe_configurations)
        """

    def describe_continuous_exports(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeContinuousExportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_continuous_exports)
        [Show boto3-stubs documentation](./client.md#describe_continuous_exports)
        """

    def describe_export_configurations(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeExportConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_configurations)
        [Show boto3-stubs documentation](./client.md#describe_export_configurations)
        """

    def describe_export_tasks(
        self,
        exportIds: List[str] = None,
        filters: List[ExportFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_tasks)
        [Show boto3-stubs documentation](./client.md#describe_export_tasks)
        """

    def describe_import_tasks(
        self,
        filters: List[ImportTaskFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeImportTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_import_tasks)
        [Show boto3-stubs documentation](./client.md#describe_import_tasks)
        """

    def describe_tags(
        self, filters: List[TagFilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_tags)
        [Show boto3-stubs documentation](./client.md#describe_tags)
        """

    def disassociate_configuration_items_from_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application)
        [Show boto3-stubs documentation](./client.md#disassociate_configuration_items_from_application)
        """

    def export_configurations(self) -> ExportConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.export_configurations)
        [Show boto3-stubs documentation](./client.md#export_configurations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_discovery_summary(self) -> GetDiscoverySummaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.get_discovery_summary)
        [Show boto3-stubs documentation](./client.md#get_discovery_summary)
        """

    def list_configurations(
        self,
        configurationType: ConfigurationItemTypeType,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: List[OrderByElementTypeDef] = None,
    ) -> ListConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_configurations)
        [Show boto3-stubs documentation](./client.md#list_configurations)
        """

    def list_server_neighbors(
        self,
        configurationId: str,
        portInformationNeeded: bool = None,
        neighborConfigurationIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListServerNeighborsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_server_neighbors)
        [Show boto3-stubs documentation](./client.md#list_server_neighbors)
        """

    def start_continuous_export(self) -> StartContinuousExportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_continuous_export)
        [Show boto3-stubs documentation](./client.md#start_continuous_export)
        """

    def start_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> StartDataCollectionByAgentIdsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids)
        [Show boto3-stubs documentation](./client.md#start_data_collection_by_agent_ids)
        """

    def start_export_task(
        self,
        exportDataFormat: List[ExportDataFormatType] = None,
        filters: List[ExportFilterTypeDef] = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> StartExportTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_export_task)
        [Show boto3-stubs documentation](./client.md#start_export_task)
        """

    def start_import_task(
        self, name: str, importUrl: str, clientRequestToken: str = None
    ) -> StartImportTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_import_task)
        [Show boto3-stubs documentation](./client.md#start_import_task)
        """

    def stop_continuous_export(self, exportId: str) -> StopContinuousExportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_continuous_export)
        [Show boto3-stubs documentation](./client.md#stop_continuous_export)
        """

    def stop_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> StopDataCollectionByAgentIdsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids)
        [Show boto3-stubs documentation](./client.md#stop_data_collection_by_agent_ids)
        """

    def update_application(
        self, configurationId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Client.update_application)
        [Show boto3-stubs documentation](./client.md#update_application)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_agents"]) -> DescribeAgentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)[Show boto3-stubs documentation](./paginators.md#describeagentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_continuous_exports"]
    ) -> DescribeContinuousExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)[Show boto3-stubs documentation](./paginators.md#describecontinuousexportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_configurations"]
    ) -> DescribeExportConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)[Show boto3-stubs documentation](./paginators.md#describeexportconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)[Show boto3-stubs documentation](./paginators.md#describeexporttaskspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)[Show boto3-stubs documentation](./paginators.md#describetagspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> ListConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)[Show boto3-stubs documentation](./paginators.md#listconfigurationspaginator)
        """
