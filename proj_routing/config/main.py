from celery import Celery

app = Celery("routing_proj")
app.config_from_object("config.celeryconfig")
# app.control.rate_limit("tasks.tasks_1.task_1", "500/m")
# app.conf.task_routes = {'tasks.tasks_2.*': {'queue': 'queue_1'}, 'tasks.tasks_2.*': {'queue': 'queue_2'}}
