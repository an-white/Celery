# config for proj celery
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Caracas'
enable_utc = True
include = ['proj.tasks']
task_ignore_result = True
