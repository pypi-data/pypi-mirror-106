from datetime import datetime
from airflow.models.baseoperator import BaseOperator
from torch_airflow_sdk.utils.torch_client import TorchDAGClient


class TorchInitializer(BaseOperator):
    def __init__(self, *, pipeline_uid, **kwargs):
        super().__init__(**kwargs)
        self.pipeline_uid = pipeline_uid

    def execute(self, context):
        client = TorchDAGClient()
        pipeline_res = client.get_pipeline(self.pipeline_uid)
        pipeline_run = pipeline_res.create_pipeline_run()
        pipeline_run.create_span(uid=f'{self.pipeline_uid}.span', context_data={'time': str(datetime.now())})
