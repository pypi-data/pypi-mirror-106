from airflow import DAG
from airflow.utils.log.logging_mixin import LoggingMixin
from torch_airflow_sdk.decorators.handle_callback import handle_dag_callback
from torch_airflow_sdk.utils.callback import on_dag_success_callback, on_dag_failure_callback
from torch_airflow_sdk.utils.torch_client import TorchDAGClient


class TorchDAG(DAG, LoggingMixin):

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
        super(TorchDAG, self).__init__(
            on_failure_callback= failure_callback_func,
            on_success_callback= success_callback_func,
            *args, **kwargs)

    def create_dagrun(self, *args, **kwargs):
        client = TorchDAGClient()
        pipeline_run = client.create_pipeline_run(self.pipeline_uid)
        pipeline_run.create_span(uid= f'{self.pipeline_uid}.span' )
        dagrun = super(TorchDAG, self).create_dagrun(*args, **kwargs)
        return dagrun

# class TorchDAG(DAG, LoggingMixin):
#
#     def __init__(self, pipeline_uid, *args, **kwargs):
#         self.pipeline_uid = pipeline_uid
#         super().__init__(
#             on_failure_callback= on_dag_failure_callback,
#             on_success_callback= on_dag_success_callback,
#             *args, **kwargs)
#
#     # add task to dag
#     def add_task(self, task):
#         task_id = task.task_id
#         span_task_id = task_id
#         span_task_uid = self._generate_span_uid(task_id)
#
#         span_task = SpanOperator(
#             task_id= span_task_id,
#             operator=task,
#             span_uid= span_task_uid,
#             on_failure_callback = self._send_failure_event,
#             on_success_callback = self._send_success_event,
#             pipeline_uid=self.pipeline_uid
#         )
#         super().add_task(span_task)
#         task = span_task
#         return task
#
#     # used to setup dependancy b/w tasks in a dag
#     def set_dependency(self, upstream_task, downstream_task):
#         upstream_task_id = upstream_task.task_id
#         downstream_task_id = downstream_task.task_id
#         super().set_dependency(upstream_task_id, downstream_task_id)
#
#     # generate span uid for span task
#     def _generate_span_uid(self, task_id):
#         uid = task_id + '_span_task'
#         return uid
#
#     # trigger function when span operator succeed
#     def _send_success_event(self, context):
#         pass
#
#     # trigger function when span operator fails
#     def _send_failure_event(self, context):
#         pass
#
#     # trigger function when you trigger dag manually or automatically
#     def create_dagrun(self, *args, **kwargs):
#         # create_pipeline_run(self.pipeline_uid)
#         client = TorchDAGClient()
#         client.create_pipeline_run(self.pipeline_uid)
#         dagrun = super(TorchDAG, self).create_dagrun(*args, **kwargs)
#         return dagrun
#
#     # handle call back
#     def handle_callback(self, *args, **kwargs):
#         super().handle_callback(*args, **kwargs )