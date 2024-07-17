# from celery import Celery  # type: ignore
# from kombu.utils.url import safequote  # type: ignore
# from flou_server import config

# settings = config.get_settings()

# broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
#     aws_access_key=safequote(settings.aws_access_key_id),
#     aws_secret_key=safequote(settings.aws_secret_access_key),
# )

# celery_app = Celery(
#     "flou_server_workers",
#     broker_url=broker_url,
#     result_backend=None,
#     task_default_queue="[queue-name].fifo",
#     include=["flou_server.background_tasks"],
#     broker_transport_options={
#         "predefined_queues": {
#             "[queue-name].fifo": {
#                 "url": "https://sqs.us-east-1.amazonaws.com/[account_id]/[queue-name].fifo",
#                 "access_key_id": settings.aws_access_key_id,
#                 "secret_access_key": settings.aws_secret_access_key,
#             }
#         }
#     },
# )
