"""
Type annotations for sagemaker service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker import SageMakerClient
    from mypy_boto3_sagemaker.waiter import (
        EndpointDeletedWaiter,
        EndpointInServiceWaiter,
        NotebookInstanceDeletedWaiter,
        NotebookInstanceInServiceWaiter,
        NotebookInstanceStoppedWaiter,
        ProcessingJobCompletedOrStoppedWaiter,
        TrainingJobCompletedOrStoppedWaiter,
        TransformJobCompletedOrStoppedWaiter,
    )

    client: SageMakerClient = boto3.client("sagemaker")

    endpoint_deleted_waiter: EndpointDeletedWaiter = client.get_waiter("endpoint_deleted")
    endpoint_in_service_waiter: EndpointInServiceWaiter = client.get_waiter("endpoint_in_service")
    notebook_instance_deleted_waiter: NotebookInstanceDeletedWaiter = client.get_waiter("notebook_instance_deleted")
    notebook_instance_in_service_waiter: NotebookInstanceInServiceWaiter = client.get_waiter("notebook_instance_in_service")
    notebook_instance_stopped_waiter: NotebookInstanceStoppedWaiter = client.get_waiter("notebook_instance_stopped")
    processing_job_completed_or_stopped_waiter: ProcessingJobCompletedOrStoppedWaiter = client.get_waiter("processing_job_completed_or_stopped")
    training_job_completed_or_stopped_waiter: TrainingJobCompletedOrStoppedWaiter = client.get_waiter("training_job_completed_or_stopped")
    transform_job_completed_or_stopped_waiter: TransformJobCompletedOrStoppedWaiter = client.get_waiter("transform_job_completed_or_stopped")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "EndpointDeletedWaiter",
    "EndpointInServiceWaiter",
    "NotebookInstanceDeletedWaiter",
    "NotebookInstanceInServiceWaiter",
    "NotebookInstanceStoppedWaiter",
    "ProcessingJobCompletedOrStoppedWaiter",
    "TrainingJobCompletedOrStoppedWaiter",
    "TransformJobCompletedOrStoppedWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.endpoint_deleted)[Show boto3-stubs documentation](./waiters.md#endpointdeletedwaiter)
    """

    def wait(self, EndpointName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#endpointdeleted)
        """


class EndpointInServiceWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.endpoint_in_service)[Show boto3-stubs documentation](./waiters.md#endpointinservicewaiter)
    """

    def wait(self, EndpointName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInServiceWaiter)
        [Show boto3-stubs documentation](./waiters.md#endpointinservice)
        """


class NotebookInstanceDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_deleted)[Show boto3-stubs documentation](./waiters.md#notebookinstancedeletedwaiter)
    """

    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeletedWaiter)
        [Show boto3-stubs documentation](./waiters.md#notebookinstancedeleted)
        """


class NotebookInstanceInServiceWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_in_service)[Show boto3-stubs documentation](./waiters.md#notebookinstanceinservicewaiter)
    """

    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInServiceWaiter)
        [Show boto3-stubs documentation](./waiters.md#notebookinstanceinservice)
        """


class NotebookInstanceStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_stopped)[Show boto3-stubs documentation](./waiters.md#notebookinstancestoppedwaiter)
    """

    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStoppedWaiter)
        [Show boto3-stubs documentation](./waiters.md#notebookinstancestopped)
        """


class ProcessingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.processing_job_completed_or_stopped)[Show boto3-stubs documentation](./waiters.md#processingjobcompletedorstoppedwaiter)
    """

    def wait(self, ProcessingJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStoppedWaiter)
        [Show boto3-stubs documentation](./waiters.md#processingjobcompletedorstopped)
        """


class TrainingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.training_job_completed_or_stopped)[Show boto3-stubs documentation](./waiters.md#trainingjobcompletedorstoppedwaiter)
    """

    def wait(self, TrainingJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStoppedWaiter)
        [Show boto3-stubs documentation](./waiters.md#trainingjobcompletedorstopped)
        """


class TransformJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.transform_job_completed_or_stopped)[Show boto3-stubs documentation](./waiters.md#transformjobcompletedorstoppedwaiter)
    """

    def wait(self, TransformJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStoppedWaiter)
        [Show boto3-stubs documentation](./waiters.md#transformjobcompletedorstopped)
        """
