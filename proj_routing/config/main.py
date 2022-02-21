from celery import Celery
from kombu import Queue, Exchange

app = Celery("routing_proj")
app.config_from_object("config.celeryconfig")
# app.control.rate_limit("tasks.tasks_1.task_1", "500/m")
# app.conf.task_routes = {'tasks.tasks_2.*': {'queue': 'queue_1'}, 'tasks.tasks_2.*': {'queue': 'queue_2'}}

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='tasks.default'),
    Queue('videos', Exchange('media'), routing_key='tasks.media.video'),
    Queue('images', Exchange('media'), routing_key='tasks.media.image'),
)

app.conf.task_default_queue = 'default'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'default'
