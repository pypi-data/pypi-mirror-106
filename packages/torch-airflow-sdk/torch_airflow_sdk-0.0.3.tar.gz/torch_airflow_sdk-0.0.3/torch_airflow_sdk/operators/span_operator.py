from datetime import datetime
from airflow.models.baseoperator import BaseOperator
from torch_airflow_sdk.utils.torch_client import TorchDAGClient
from torch_sdk.events.generic_event import GenericEvent

import logging
LOGGER = logging.getLogger("airflow.task")


class SpanOperator(BaseOperator):
    def __init__(self, *, operator: BaseOperator, pipeline_uid=None, span_uid: str = None, **kwargs):
        if kwargs.get("provide_context"):
            kwargs.pop('provide_context', None)
        super().__init__(**kwargs)
        self.operator = operator
        self.pipeline_uid = pipeline_uid
        self.span_uid = span_uid
        self.pipeline_run = None

    def execute(self, context):
        try:
            LOGGER.info("Send span start event")
            client = TorchDAGClient()
            self.pipeline_run = client.get_parent_span(pipeline_uid=self.pipeline_uid,
                                                       parent_span_uid=f'{self.pipeline_uid}.span')
            self.span_context = self.pipeline_run.create_child_span(uid=self.span_uid,
                                                                    context_data={'time': str(datetime.now())})
            context['span_context_parent'] = self.span_context
            try:
                self.operator.prepare_for_execution().execute(context)
            except:
                try:
                    self.operator.execute(context)
                except:
                    raise Exception(f'Could not able to execute task of {self.operator} for span {self.span_uid}')
        except Exception as e:
            LOGGER.error("Send span end failure event")
            exception = e.__dict__
            LOGGER.error(exception)
            self.span_context.send_event(
                GenericEvent(context_data={'status': 'error', 'error_data': str(e), 'time': str(datetime.now()),
                                           'exception_type': str(type(e).__name__)},
                             event_uid=f'{self.span_uid}.error.event'))
            self.span_context.abort(
                context_data={'status': 'error', 'time': str(datetime.now())})
            raise e
        else:
            LOGGER.info("Send span end success event")
            self.span_context.end(context_data={'status': 'success', 'time': str(datetime.now())})

    def set_downstream(self, task_or_task_list) -> None:
        super().set_downstream(task_or_task_list)

    def set_upstream(self, task_or_task_list) -> None:
        super().set_upstream(task_or_task_list)

# class SpanOperator(BaseOperator):
#     def __init__(self, *, operator: BaseOperator, pipeline_uid=None, span_uid: str = None, **kwargs):
#         super().__init__(**kwargs)
#         self.operator = operator
#         self.pipeline_uid = pipeline_uid
#         self.span_uid = span_uid
#         self.pipeline_run = None
#
#     def set_pipeline_run(self, pipeline_run):
#         self.pipeline_run = pipeline_run
#
#     def execute(self, context):
#         try:
#             print("Send span start event")
#             client = TorchDAGClient()
#             self.pipeline_run = client.get_latest_pipeline_run(self.pipeline_uid)
#             # self.pipeline_run = get_latest_pipeline_run(self.pipeline_uid)
#             print('pipeline run is : ' , self.pipeline_run)
#             self.span_context = self.pipeline_run.create_span(uid= self.span_uid, context_data= { 'time': str(datetime.datetime.now()) } )
#             self.operator.execute(context)
#             context['ti'].xcom_push(key=self.span_uid, value=str(context['ti']))
#         except Exception as e:
#             print("Sending Span End Event With Status Failure")
#             exception = e.__dict__
#             print(exception)
#             self.span_context.end(
#                 context_data={'status': 'error', 'error_data': str(e), 'time': str(datetime.datetime.now()),
#                               'exception_type': str(type(e).__name__)})
#             raise e
#         else:
#             print("Sending Span End Event With Status Success")
#             self.span_context.end(context_data={'status': 'success', 'time': str(datetime.datetime.now())})
#
#     def set_downstream(self, task_or_task_list) -> None:
#         super().set_downstream(task_or_task_list)
#
#     def set_upstream(self, task_or_task_list) -> None:
#         super().set_upstream(task_or_task_list)
