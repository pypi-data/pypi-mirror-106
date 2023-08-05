"""
Type annotations for sagemaker service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker import SageMakerClient
    from mypy_boto3_sagemaker.paginator import (
        ListActionsPaginator,
        ListAlgorithmsPaginator,
        ListAppImageConfigsPaginator,
        ListAppsPaginator,
        ListArtifactsPaginator,
        ListAssociationsPaginator,
        ListAutoMLJobsPaginator,
        ListCandidatesForAutoMLJobPaginator,
        ListCodeRepositoriesPaginator,
        ListCompilationJobsPaginator,
        ListContextsPaginator,
        ListDataQualityJobDefinitionsPaginator,
        ListDeviceFleetsPaginator,
        ListDevicesPaginator,
        ListDomainsPaginator,
        ListEdgePackagingJobsPaginator,
        ListEndpointConfigsPaginator,
        ListEndpointsPaginator,
        ListExperimentsPaginator,
        ListFeatureGroupsPaginator,
        ListFlowDefinitionsPaginator,
        ListHumanTaskUisPaginator,
        ListHyperParameterTuningJobsPaginator,
        ListImageVersionsPaginator,
        ListImagesPaginator,
        ListLabelingJobsPaginator,
        ListLabelingJobsForWorkteamPaginator,
        ListModelBiasJobDefinitionsPaginator,
        ListModelExplainabilityJobDefinitionsPaginator,
        ListModelPackageGroupsPaginator,
        ListModelPackagesPaginator,
        ListModelQualityJobDefinitionsPaginator,
        ListModelsPaginator,
        ListMonitoringExecutionsPaginator,
        ListMonitoringSchedulesPaginator,
        ListNotebookInstanceLifecycleConfigsPaginator,
        ListNotebookInstancesPaginator,
        ListPipelineExecutionStepsPaginator,
        ListPipelineExecutionsPaginator,
        ListPipelineParametersForExecutionPaginator,
        ListPipelinesPaginator,
        ListProcessingJobsPaginator,
        ListSubscribedWorkteamsPaginator,
        ListTagsPaginator,
        ListTrainingJobsPaginator,
        ListTrainingJobsForHyperParameterTuningJobPaginator,
        ListTransformJobsPaginator,
        ListTrialComponentsPaginator,
        ListTrialsPaginator,
        ListUserProfilesPaginator,
        ListWorkforcesPaginator,
        ListWorkteamsPaginator,
        SearchPaginator,
    )

    client: SageMakerClient = boto3.client("sagemaker")

    list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
    list_algorithms_paginator: ListAlgorithmsPaginator = client.get_paginator("list_algorithms")
    list_app_image_configs_paginator: ListAppImageConfigsPaginator = client.get_paginator("list_app_image_configs")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_artifacts_paginator: ListArtifactsPaginator = client.get_paginator("list_artifacts")
    list_associations_paginator: ListAssociationsPaginator = client.get_paginator("list_associations")
    list_auto_ml_jobs_paginator: ListAutoMLJobsPaginator = client.get_paginator("list_auto_ml_jobs")
    list_candidates_for_auto_ml_job_paginator: ListCandidatesForAutoMLJobPaginator = client.get_paginator("list_candidates_for_auto_ml_job")
    list_code_repositories_paginator: ListCodeRepositoriesPaginator = client.get_paginator("list_code_repositories")
    list_compilation_jobs_paginator: ListCompilationJobsPaginator = client.get_paginator("list_compilation_jobs")
    list_contexts_paginator: ListContextsPaginator = client.get_paginator("list_contexts")
    list_data_quality_job_definitions_paginator: ListDataQualityJobDefinitionsPaginator = client.get_paginator("list_data_quality_job_definitions")
    list_device_fleets_paginator: ListDeviceFleetsPaginator = client.get_paginator("list_device_fleets")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_edge_packaging_jobs_paginator: ListEdgePackagingJobsPaginator = client.get_paginator("list_edge_packaging_jobs")
    list_endpoint_configs_paginator: ListEndpointConfigsPaginator = client.get_paginator("list_endpoint_configs")
    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_feature_groups_paginator: ListFeatureGroupsPaginator = client.get_paginator("list_feature_groups")
    list_flow_definitions_paginator: ListFlowDefinitionsPaginator = client.get_paginator("list_flow_definitions")
    list_human_task_uis_paginator: ListHumanTaskUisPaginator = client.get_paginator("list_human_task_uis")
    list_hyper_parameter_tuning_jobs_paginator: ListHyperParameterTuningJobsPaginator = client.get_paginator("list_hyper_parameter_tuning_jobs")
    list_image_versions_paginator: ListImageVersionsPaginator = client.get_paginator("list_image_versions")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    list_labeling_jobs_paginator: ListLabelingJobsPaginator = client.get_paginator("list_labeling_jobs")
    list_labeling_jobs_for_workteam_paginator: ListLabelingJobsForWorkteamPaginator = client.get_paginator("list_labeling_jobs_for_workteam")
    list_model_bias_job_definitions_paginator: ListModelBiasJobDefinitionsPaginator = client.get_paginator("list_model_bias_job_definitions")
    list_model_explainability_job_definitions_paginator: ListModelExplainabilityJobDefinitionsPaginator = client.get_paginator("list_model_explainability_job_definitions")
    list_model_package_groups_paginator: ListModelPackageGroupsPaginator = client.get_paginator("list_model_package_groups")
    list_model_packages_paginator: ListModelPackagesPaginator = client.get_paginator("list_model_packages")
    list_model_quality_job_definitions_paginator: ListModelQualityJobDefinitionsPaginator = client.get_paginator("list_model_quality_job_definitions")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_monitoring_executions_paginator: ListMonitoringExecutionsPaginator = client.get_paginator("list_monitoring_executions")
    list_monitoring_schedules_paginator: ListMonitoringSchedulesPaginator = client.get_paginator("list_monitoring_schedules")
    list_notebook_instance_lifecycle_configs_paginator: ListNotebookInstanceLifecycleConfigsPaginator = client.get_paginator("list_notebook_instance_lifecycle_configs")
    list_notebook_instances_paginator: ListNotebookInstancesPaginator = client.get_paginator("list_notebook_instances")
    list_pipeline_execution_steps_paginator: ListPipelineExecutionStepsPaginator = client.get_paginator("list_pipeline_execution_steps")
    list_pipeline_executions_paginator: ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
    list_pipeline_parameters_for_execution_paginator: ListPipelineParametersForExecutionPaginator = client.get_paginator("list_pipeline_parameters_for_execution")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_processing_jobs_paginator: ListProcessingJobsPaginator = client.get_paginator("list_processing_jobs")
    list_subscribed_workteams_paginator: ListSubscribedWorkteamsPaginator = client.get_paginator("list_subscribed_workteams")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_training_jobs_paginator: ListTrainingJobsPaginator = client.get_paginator("list_training_jobs")
    list_training_jobs_for_hyper_parameter_tuning_job_paginator: ListTrainingJobsForHyperParameterTuningJobPaginator = client.get_paginator("list_training_jobs_for_hyper_parameter_tuning_job")
    list_transform_jobs_paginator: ListTransformJobsPaginator = client.get_paginator("list_transform_jobs")
    list_trial_components_paginator: ListTrialComponentsPaginator = client.get_paginator("list_trial_components")
    list_trials_paginator: ListTrialsPaginator = client.get_paginator("list_trials")
    list_user_profiles_paginator: ListUserProfilesPaginator = client.get_paginator("list_user_profiles")
    list_workforces_paginator: ListWorkforcesPaginator = client.get_paginator("list_workforces")
    list_workteams_paginator: ListWorkteamsPaginator = client.get_paginator("list_workteams")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AlgorithmSortByType,
    AppImageConfigSortKeyType,
    AssociationEdgeTypeType,
    AutoMLJobStatusType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    CandidateSortByType,
    CandidateStatusType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    EdgePackagingJobStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    ImageSortByType,
    ImageSortOrderType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    LabelingJobStatusType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgePackagingJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    ModelApprovalStatusType,
    ModelPackageGroupSortByType,
    ModelPackageSortByType,
    ModelPackageTypeType,
    ModelSortKeyType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    OfflineStoreStatusValueType,
    OrderKeyType,
    ProcessingJobStatusType,
    ResourceTypeType,
    ScheduleStatusType,
    SearchSortOrderType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformJobStatusType,
    UserProfileSortKeyType,
)
from .type_defs import (
    ListActionsResponseTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAppImageConfigsResponseTypeDef,
    ListAppsResponseTypeDef,
    ListArtifactsResponseTypeDef,
    ListAssociationsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListContextsResponseTypeDef,
    ListDataQualityJobDefinitionsResponseTypeDef,
    ListDeviceFleetsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEdgePackagingJobsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeatureGroupsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListModelBiasJobDefinitionsResponseTypeDef,
    ListModelExplainabilityJobDefinitionsResponseTypeDef,
    ListModelPackageGroupsOutputTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelQualityJobDefinitionsResponseTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListPipelineExecutionsResponseTypeDef,
    ListPipelineExecutionStepsResponseTypeDef,
    ListPipelineParametersForExecutionResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkforcesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListActionsPaginator",
    "ListAlgorithmsPaginator",
    "ListAppImageConfigsPaginator",
    "ListAppsPaginator",
    "ListArtifactsPaginator",
    "ListAssociationsPaginator",
    "ListAutoMLJobsPaginator",
    "ListCandidatesForAutoMLJobPaginator",
    "ListCodeRepositoriesPaginator",
    "ListCompilationJobsPaginator",
    "ListContextsPaginator",
    "ListDataQualityJobDefinitionsPaginator",
    "ListDeviceFleetsPaginator",
    "ListDevicesPaginator",
    "ListDomainsPaginator",
    "ListEdgePackagingJobsPaginator",
    "ListEndpointConfigsPaginator",
    "ListEndpointsPaginator",
    "ListExperimentsPaginator",
    "ListFeatureGroupsPaginator",
    "ListFlowDefinitionsPaginator",
    "ListHumanTaskUisPaginator",
    "ListHyperParameterTuningJobsPaginator",
    "ListImageVersionsPaginator",
    "ListImagesPaginator",
    "ListLabelingJobsPaginator",
    "ListLabelingJobsForWorkteamPaginator",
    "ListModelBiasJobDefinitionsPaginator",
    "ListModelExplainabilityJobDefinitionsPaginator",
    "ListModelPackageGroupsPaginator",
    "ListModelPackagesPaginator",
    "ListModelQualityJobDefinitionsPaginator",
    "ListModelsPaginator",
    "ListMonitoringExecutionsPaginator",
    "ListMonitoringSchedulesPaginator",
    "ListNotebookInstanceLifecycleConfigsPaginator",
    "ListNotebookInstancesPaginator",
    "ListPipelineExecutionStepsPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelineParametersForExecutionPaginator",
    "ListPipelinesPaginator",
    "ListProcessingJobsPaginator",
    "ListSubscribedWorkteamsPaginator",
    "ListTagsPaginator",
    "ListTrainingJobsPaginator",
    "ListTrainingJobsForHyperParameterTuningJobPaginator",
    "ListTransformJobsPaginator",
    "ListTrialComponentsPaginator",
    "ListTrialsPaginator",
    "ListUserProfilesPaginator",
    "ListWorkforcesPaginator",
    "ListWorkteamsPaginator",
    "SearchPaginator",
)

class ListActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListActions)[Show boto3-stubs documentation](./paginators.md#listactionspaginator)
    """

    def paginate(
        self,
        SourceUri: str = None,
        ActionType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortActionsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListActions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listactionspaginator)
        """

class ListAlgorithmsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)[Show boto3-stubs documentation](./paginators.md#listalgorithmspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: AlgorithmSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAlgorithmsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms.paginate)
        [Show boto3-stubs documentation](./paginators.md#listalgorithmspaginator)
        """

class ListAppImageConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs)[Show boto3-stubs documentation](./paginators.md#listappimageconfigspaginator)
    """

    def paginate(
        self,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        ModifiedTimeBefore: datetime = None,
        ModifiedTimeAfter: datetime = None,
        SortBy: AppImageConfigSortKeyType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAppImageConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listappimageconfigspaginator)
        """

class ListAppsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)[Show boto3-stubs documentation](./paginators.md#listappspaginator)
    """

    def paginate(
        self,
        SortOrder: SortOrderType = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAppsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListApps.paginate)
        [Show boto3-stubs documentation](./paginators.md#listappspaginator)
        """

class ListArtifactsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts)[Show boto3-stubs documentation](./paginators.md#listartifactspaginator)
    """

    def paginate(
        self,
        SourceUri: str = None,
        ArtifactType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListArtifactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts.paginate)
        [Show boto3-stubs documentation](./paginators.md#listartifactspaginator)
        """

class ListAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations)[Show boto3-stubs documentation](./paginators.md#listassociationspaginator)
    """

    def paginate(
        self,
        SourceArn: str = None,
        DestinationArn: str = None,
        SourceType: str = None,
        DestinationType: str = None,
        AssociationType: AssociationEdgeTypeType = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortAssociationsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations.paginate)
        [Show boto3-stubs documentation](./paginators.md#listassociationspaginator)
        """

class ListAutoMLJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)[Show boto3-stubs documentation](./paginators.md#listautomljobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: AutoMLJobStatusType = None,
        SortOrder: AutoMLSortOrderType = None,
        SortBy: AutoMLSortByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAutoMLJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listautomljobspaginator)
        """

class ListCandidatesForAutoMLJobPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)[Show boto3-stubs documentation](./paginators.md#listcandidatesforautomljobpaginator)
    """

    def paginate(
        self,
        AutoMLJobName: str,
        StatusEquals: CandidateStatusType = None,
        CandidateNameEquals: str = None,
        SortOrder: AutoMLSortOrderType = None,
        SortBy: CandidateSortByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCandidatesForAutoMLJobResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob.paginate)
        [Show boto3-stubs documentation](./paginators.md#listcandidatesforautomljobpaginator)
        """

class ListCodeRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)[Show boto3-stubs documentation](./paginators.md#listcoderepositoriespaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: CodeRepositorySortByType = None,
        SortOrder: CodeRepositorySortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCodeRepositoriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories.paginate)
        [Show boto3-stubs documentation](./paginators.md#listcoderepositoriespaginator)
        """

class ListCompilationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)[Show boto3-stubs documentation](./paginators.md#listcompilationjobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: CompilationJobStatusType = None,
        SortBy: ListCompilationJobsSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCompilationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listcompilationjobspaginator)
        """

class ListContextsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts)[Show boto3-stubs documentation](./paginators.md#listcontextspaginator)
    """

    def paginate(
        self,
        SourceUri: str = None,
        ContextType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortContextsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListContextsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts.paginate)
        [Show boto3-stubs documentation](./paginators.md#listcontextspaginator)
        """

class ListDataQualityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions)[Show boto3-stubs documentation](./paginators.md#listdataqualityjobdefinitionspaginator)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDataQualityJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listdataqualityjobdefinitionspaginator)
        """

class ListDeviceFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets)[Show boto3-stubs documentation](./paginators.md#listdevicefleetspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ListDeviceFleetsSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeviceFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets.paginate)
        [Show boto3-stubs documentation](./paginators.md#listdevicefleetspaginator)
        """

class ListDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices)[Show boto3-stubs documentation](./paginators.md#listdevicespaginator)
    """

    def paginate(
        self,
        LatestHeartbeatAfter: datetime = None,
        ModelName: str = None,
        DeviceFleetName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](./paginators.md#listdevicespaginator)
        """

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)[Show boto3-stubs documentation](./paginators.md#listdomainspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](./paginators.md#listdomainspaginator)
        """

class ListEdgePackagingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs)[Show boto3-stubs documentation](./paginators.md#listedgepackagingjobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        ModelNameContains: str = None,
        StatusEquals: EdgePackagingJobStatusType = None,
        SortBy: ListEdgePackagingJobsSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEdgePackagingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listedgepackagingjobspaginator)
        """

class ListEndpointConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)[Show boto3-stubs documentation](./paginators.md#listendpointconfigspaginator)
    """

    def paginate(
        self,
        SortBy: EndpointConfigSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEndpointConfigsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listendpointconfigspaginator)
        """

class ListEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)[Show boto3-stubs documentation](./paginators.md#listendpointspaginator)
    """

    def paginate(
        self,
        SortBy: EndpointSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: EndpointStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEndpointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints.paginate)
        [Show boto3-stubs documentation](./paginators.md#listendpointspaginator)
        """

class ListExperimentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)[Show boto3-stubs documentation](./paginators.md#listexperimentspaginator)
    """

    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortExperimentsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListExperimentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments.paginate)
        [Show boto3-stubs documentation](./paginators.md#listexperimentspaginator)
        """

class ListFeatureGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups)[Show boto3-stubs documentation](./paginators.md#listfeaturegroupspaginator)
    """

    def paginate(
        self,
        NameContains: str = None,
        FeatureGroupStatusEquals: FeatureGroupStatusType = None,
        OfflineStoreStatusEquals: OfflineStoreStatusValueType = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: FeatureGroupSortOrderType = None,
        SortBy: FeatureGroupSortByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFeatureGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#listfeaturegroupspaginator)
        """

class ListFlowDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)[Show boto3-stubs documentation](./paginators.md#listflowdefinitionspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFlowDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listflowdefinitionspaginator)
        """

class ListHumanTaskUisPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)[Show boto3-stubs documentation](./paginators.md#listhumantaskuispaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHumanTaskUisResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis.paginate)
        [Show boto3-stubs documentation](./paginators.md#listhumantaskuispaginator)
        """

class ListHyperParameterTuningJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)[Show boto3-stubs documentation](./paginators.md#listhyperparametertuningjobspaginator)
    """

    def paginate(
        self,
        SortBy: HyperParameterTuningJobSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: HyperParameterTuningJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHyperParameterTuningJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listhyperparametertuningjobspaginator)
        """

class ListImageVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)[Show boto3-stubs documentation](./paginators.md#listimageversionspaginator)
    """

    def paginate(
        self,
        ImageName: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        SortBy: ImageVersionSortByType = None,
        SortOrder: ImageVersionSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImageVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listimageversionspaginator)
        """

class ListImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)[Show boto3-stubs documentation](./paginators.md#listimagespaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ImageSortByType = None,
        SortOrder: ImageSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListImages.paginate)
        [Show boto3-stubs documentation](./paginators.md#listimagespaginator)
        """

class ListLabelingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)[Show boto3-stubs documentation](./paginators.md#listlabelingjobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        StatusEquals: LabelingJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLabelingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listlabelingjobspaginator)
        """

class ListLabelingJobsForWorkteamPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)[Show boto3-stubs documentation](./paginators.md#listlabelingjobsforworkteampaginator)
    """

    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLabelingJobsForWorkteamResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam.paginate)
        [Show boto3-stubs documentation](./paginators.md#listlabelingjobsforworkteampaginator)
        """

class ListModelBiasJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions)[Show boto3-stubs documentation](./paginators.md#listmodelbiasjobdefinitionspaginator)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelBiasJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmodelbiasjobdefinitionspaginator)
        """

class ListModelExplainabilityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions)[Show boto3-stubs documentation](./paginators.md#listmodelexplainabilityjobdefinitionspaginator)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelExplainabilityJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmodelexplainabilityjobdefinitionspaginator)
        """

class ListModelPackageGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups)[Show boto3-stubs documentation](./paginators.md#listmodelpackagegroupspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ModelPackageGroupSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelPackageGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmodelpackagegroupspaginator)
        """

class ListModelPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)[Show boto3-stubs documentation](./paginators.md#listmodelpackagespaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        ModelApprovalStatus: ModelApprovalStatusType = None,
        ModelPackageGroupName: str = None,
        ModelPackageType: ModelPackageTypeType = None,
        SortBy: ModelPackageSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelPackagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmodelpackagespaginator)
        """

class ListModelQualityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions)[Show boto3-stubs documentation](./paginators.md#listmodelqualityjobdefinitionspaginator)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelQualityJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmodelqualityjobdefinitionspaginator)
        """

class ListModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)[Show boto3-stubs documentation](./paginators.md#listmodelspaginator)
    """

    def paginate(
        self,
        SortBy: ModelSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListModels.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmodelspaginator)
        """

class ListMonitoringExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)[Show boto3-stubs documentation](./paginators.md#listmonitoringexecutionspaginator)
    """

    def paginate(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: MonitoringExecutionSortKeyType = None,
        SortOrder: SortOrderType = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: ExecutionStatusType = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMonitoringExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmonitoringexecutionspaginator)
        """

class ListMonitoringSchedulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)[Show boto3-stubs documentation](./paginators.md#listmonitoringschedulespaginator)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringScheduleSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: ScheduleStatusType = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMonitoringSchedulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmonitoringschedulespaginator)
        """

class ListNotebookInstanceLifecycleConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)[Show boto3-stubs documentation](./paginators.md#listnotebookinstancelifecycleconfigspaginator)
    """

    def paginate(
        self,
        SortBy: NotebookInstanceLifecycleConfigSortKeyType = None,
        SortOrder: NotebookInstanceLifecycleConfigSortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookInstanceLifecycleConfigsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listnotebookinstancelifecycleconfigspaginator)
        """

class ListNotebookInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)[Show boto3-stubs documentation](./paginators.md#listnotebookinstancespaginator)
    """

    def paginate(
        self,
        SortBy: NotebookInstanceSortKeyType = None,
        SortOrder: NotebookInstanceSortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: NotebookInstanceStatusType = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances.paginate)
        [Show boto3-stubs documentation](./paginators.md#listnotebookinstancespaginator)
        """

class ListPipelineExecutionStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps)[Show boto3-stubs documentation](./paginators.md#listpipelineexecutionstepspaginator)
    """

    def paginate(
        self,
        PipelineExecutionArn: str = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPipelineExecutionStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps.paginate)
        [Show boto3-stubs documentation](./paginators.md#listpipelineexecutionstepspaginator)
        """

class ListPipelineExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions)[Show boto3-stubs documentation](./paginators.md#listpipelineexecutionspaginator)
    """

    def paginate(
        self,
        PipelineName: str,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortPipelineExecutionsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPipelineExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions.paginate)
        [Show boto3-stubs documentation](./paginators.md#listpipelineexecutionspaginator)
        """

class ListPipelineParametersForExecutionPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution)[Show boto3-stubs documentation](./paginators.md#listpipelineparametersforexecutionpaginator)
    """

    def paginate(
        self, PipelineExecutionArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelineParametersForExecutionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution.paginate)
        [Show boto3-stubs documentation](./paginators.md#listpipelineparametersforexecutionpaginator)
        """

class ListPipelinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines)[Show boto3-stubs documentation](./paginators.md#listpipelinespaginator)
    """

    def paginate(
        self,
        PipelineNamePrefix: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortPipelinesByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPipelinesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines.paginate)
        [Show boto3-stubs documentation](./paginators.md#listpipelinespaginator)
        """

class ListProcessingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)[Show boto3-stubs documentation](./paginators.md#listprocessingjobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: ProcessingJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListProcessingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listprocessingjobspaginator)
        """

class ListSubscribedWorkteamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)[Show boto3-stubs documentation](./paginators.md#listsubscribedworkteamspaginator)
    """

    def paginate(
        self, NameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscribedWorkteamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams.paginate)
        [Show boto3-stubs documentation](./paginators.md#listsubscribedworkteamspaginator)
        """

class ListTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)[Show boto3-stubs documentation](./paginators.md#listtagspaginator)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtagspaginator)
        """

class ListTrainingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)[Show boto3-stubs documentation](./paginators.md#listtrainingjobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: TrainingJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrainingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtrainingjobspaginator)
        """

class ListTrainingJobsForHyperParameterTuningJobPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)[Show boto3-stubs documentation](./paginators.md#listtrainingjobsforhyperparametertuningjobpaginator)
    """

    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: TrainingJobStatusType = None,
        SortBy: TrainingJobSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrainingJobsForHyperParameterTuningJobResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtrainingjobsforhyperparametertuningjobpaginator)
        """

class ListTransformJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)[Show boto3-stubs documentation](./paginators.md#listtransformjobspaginator)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: TransformJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTransformJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtransformjobspaginator)
        """

class ListTrialComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)[Show boto3-stubs documentation](./paginators.md#listtrialcomponentspaginator)
    """

    def paginate(
        self,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortTrialComponentsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrialComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtrialcomponentspaginator)
        """

class ListTrialsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)[Show boto3-stubs documentation](./paginators.md#listtrialspaginator)
    """

    def paginate(
        self,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortTrialsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrialsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials.paginate)
        [Show boto3-stubs documentation](./paginators.md#listtrialspaginator)
        """

class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)[Show boto3-stubs documentation](./paginators.md#listuserprofilespaginator)
    """

    def paginate(
        self,
        SortOrder: SortOrderType = None,
        SortBy: UserProfileSortKeyType = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUserProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles.paginate)
        [Show boto3-stubs documentation](./paginators.md#listuserprofilespaginator)
        """

class ListWorkforcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)[Show boto3-stubs documentation](./paginators.md#listworkforcespaginator)
    """

    def paginate(
        self,
        SortBy: ListWorkforcesSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListWorkforcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces.paginate)
        [Show boto3-stubs documentation](./paginators.md#listworkforcespaginator)
        """

class ListWorkteamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)[Show boto3-stubs documentation](./paginators.md#listworkteamspaginator)
    """

    def paginate(
        self,
        SortBy: ListWorkteamsSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListWorkteamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams.paginate)
        [Show boto3-stubs documentation](./paginators.md#listworkteamspaginator)
        """

class SearchPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.Search)[Show boto3-stubs documentation](./paginators.md#searchpaginator)
    """

    def paginate(
        self,
        Resource: ResourceTypeType,
        SearchExpression: "SearchExpressionTypeDef" = None,
        SortBy: str = None,
        SortOrder: SearchSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Paginator.Search.paginate)
        [Show boto3-stubs documentation](./paginators.md#searchpaginator)
        """
