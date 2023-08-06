from torch_sdk.torch_client import TorchClient
import functools
from torch_airflow_sdk.initialiser import torch_credentials


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class TorchDAGClient:

    def __init__(self) -> None:
        self.torchClient = TorchClient(**torch_credentials)
        self.latest_pipeline_run = None

    def __repr__(self) -> str:
        pass

    def get_pipeline(self, pipeline_uid):
        pipeline = self.torchClient.get_pipeline(pipeline_uid)
        return pipeline

    def get_parent_span(self, pipeline_uid, parent_span_uid):
        pipeline = self.torchClient.get_pipeline(pipeline_uid)
        pipeline_run = pipeline.get_latest_pipeline_run()
        span_context = pipeline_run.get_span(span_uid=parent_span_uid)
        return span_context

    def create_pipeline_run(self, pipeline_uid):
        pipeline = self.torchClient.get_pipeline(pipeline_uid)
        pipeline_run = pipeline.create_pipeline_run()
        self.latest_pipeline_run = pipeline_run
        return pipeline_run

    def get_latest_pipeline_run(self, pipeline_uid):
        pipeline = self.torchClient.get_pipeline(pipeline_uid)
        pipeline_run = pipeline.get_latest_pipeline_run()
        return pipeline_run
