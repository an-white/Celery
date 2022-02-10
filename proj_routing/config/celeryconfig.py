# config for  celery
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
task_ignore_result = True
# definir las colas a asignar por archivos de tareas a ejecutar
task_routes = {
    'tasks.tasks_1.*': {'queue': 'queue_1'}, 'tasks.tasks_2.*': {'queue': 'queue_2'}
}
# timezone = 'America/Caracas'
# include = ['proj.tasks']
# Optional configuration, see the application user guide.
# celery_app.conf.task_default_routing
