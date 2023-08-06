from airflow import DAG
from airflow.utils.log.logging_mixin import LoggingMixin
from torch_airflow_sdk.decorators.handle_callback import handle_dag_callback
from torch_airflow_sdk.utils.callback import on_dag_success_callback, on_dag_failure_callback
from torch_airflow_sdk.utils.torch_client import TorchDAGClient


class DAG(DAG, LoggingMixin):

    def __init__(self, pipeline_uid, *args, **kwargs):
        self.pipeline_uid = pipeline_uid
        success_callback_func = on_dag_success_callback
        failure_callback_func = on_dag_failure_callback
        if 'on_failure_callback' in kwargs:
            failure_callback_func = handle_dag_callback(kwargs['on_failure_callback'])
            kwargs.pop('on_failure_callback')
        if 'on_success_callback' in kwargs:
            success_callback_func = handle_dag_callback(kwargs['on_success_callback'])
            kwargs.pop('on_success_callback')
        super(DAG, self).__init__(
            on_failure_callback= failure_callback_func,
            on_success_callback= success_callback_func,
            *args, **kwargs)

    def create_dagrun(self, *args, **kwargs):
        client = TorchDAGClient()
        pipeline_run = client.create_pipeline_run(self.pipeline_uid)
        pipeline_run.create_span(uid= f'{self.pipeline_uid}.span' )
        dagrun = super(DAG, self).create_dagrun(*args, **kwargs)
        return dagrun
