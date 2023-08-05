"""
Type annotations for elastictranscoder service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_elastictranscoder import ElasticTranscoderClient

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    ListJobsByPipelinePaginator,
    ListJobsByStatusPaginator,
    ListPipelinesPaginator,
    ListPresetsPaginator,
)
from .type_defs import (
    AudioParametersTypeDef,
    CreateJobOutputTypeDef,
    CreateJobPlaylistTypeDef,
    CreateJobResponseTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresetResponseTypeDef,
    JobInputTypeDef,
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsResponseTypeDef,
    NotificationsTypeDef,
    PipelineOutputConfigTypeDef,
    ReadJobResponseTypeDef,
    ReadPipelineResponseTypeDef,
    ReadPresetResponseTypeDef,
    TestRoleResponseTypeDef,
    ThumbnailsTypeDef,
    UpdatePipelineNotificationsResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdatePipelineStatusResponseTypeDef,
    VideoParametersTypeDef,
)
from .waiter import JobCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ElasticTranscoderClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IncompatibleVersionException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ElasticTranscoderClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """
    def cancel_job(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.cancel_job)
        [Show boto3-stubs documentation](./client.md#cancel_job)
        """
    def create_job(
        self,
        PipelineId: str,
        Input: "JobInputTypeDef" = None,
        Inputs: List["JobInputTypeDef"] = None,
        Output: CreateJobOutputTypeDef = None,
        Outputs: List[CreateJobOutputTypeDef] = None,
        OutputKeyPrefix: str = None,
        Playlists: List[CreateJobPlaylistTypeDef] = None,
        UserMetadata: Dict[str, str] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job)
        [Show boto3-stubs documentation](./client.md#create_job)
        """
    def create_pipeline(
        self,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: "NotificationsTypeDef" = None,
        ContentConfig: "PipelineOutputConfigTypeDef" = None,
        ThumbnailConfig: "PipelineOutputConfigTypeDef" = None,
    ) -> CreatePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_pipeline)
        [Show boto3-stubs documentation](./client.md#create_pipeline)
        """
    def create_preset(
        self,
        Name: str,
        Container: str,
        Description: str = None,
        Video: "VideoParametersTypeDef" = None,
        Audio: "AudioParametersTypeDef" = None,
        Thumbnails: "ThumbnailsTypeDef" = None,
    ) -> CreatePresetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_preset)
        [Show boto3-stubs documentation](./client.md#create_preset)
        """
    def delete_pipeline(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_pipeline)
        [Show boto3-stubs documentation](./client.md#delete_pipeline)
        """
    def delete_preset(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_preset)
        [Show boto3-stubs documentation](./client.md#delete_preset)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """
    def list_jobs_by_pipeline(
        self, PipelineId: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByPipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_pipeline)
        [Show boto3-stubs documentation](./client.md#list_jobs_by_pipeline)
        """
    def list_jobs_by_status(
        self, Status: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_status)
        [Show boto3-stubs documentation](./client.md#list_jobs_by_status)
        """
    def list_pipelines(
        self, Ascending: str = None, PageToken: str = None
    ) -> ListPipelinesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_pipelines)
        [Show boto3-stubs documentation](./client.md#list_pipelines)
        """
    def list_presets(
        self, Ascending: str = None, PageToken: str = None
    ) -> ListPresetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_presets)
        [Show boto3-stubs documentation](./client.md#list_presets)
        """
    def read_job(self, Id: str) -> ReadJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_job)
        [Show boto3-stubs documentation](./client.md#read_job)
        """
    def read_pipeline(self, Id: str) -> ReadPipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_pipeline)
        [Show boto3-stubs documentation](./client.md#read_pipeline)
        """
    def read_preset(self, Id: str) -> ReadPresetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_preset)
        [Show boto3-stubs documentation](./client.md#read_preset)
        """
    def test_role(
        self, Role: str, InputBucket: str, OutputBucket: str, Topics: List[str]
    ) -> TestRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.test_role)
        [Show boto3-stubs documentation](./client.md#test_role)
        """
    def update_pipeline(
        self,
        Id: str,
        Name: str = None,
        InputBucket: str = None,
        Role: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: "NotificationsTypeDef" = None,
        ContentConfig: "PipelineOutputConfigTypeDef" = None,
        ThumbnailConfig: "PipelineOutputConfigTypeDef" = None,
    ) -> UpdatePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline)
        [Show boto3-stubs documentation](./client.md#update_pipeline)
        """
    def update_pipeline_notifications(
        self, Id: str, Notifications: "NotificationsTypeDef"
    ) -> UpdatePipelineNotificationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_notifications)
        [Show boto3-stubs documentation](./client.md#update_pipeline_notifications)
        """
    def update_pipeline_status(self, Id: str, Status: str) -> UpdatePipelineStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_status)
        [Show boto3-stubs documentation](./client.md#update_pipeline_status)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_pipeline"]
    ) -> ListJobsByPipelinePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)[Show boto3-stubs documentation](./paginators.md#listjobsbypipelinepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_status"]
    ) -> ListJobsByStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)[Show boto3-stubs documentation](./paginators.md#listjobsbystatuspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)[Show boto3-stubs documentation](./paginators.md#listpipelinespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_presets"]) -> ListPresetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)[Show boto3-stubs documentation](./paginators.md#listpresetspaginator)
        """
    def get_waiter(self, waiter_name: Literal["job_complete"]) -> JobCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.job_complete)[Show boto3-stubs documentation](./waiters.md#jobcompletewaiter)
        """
