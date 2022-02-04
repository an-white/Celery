broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Caracas'
enable_utc = True

"""
añadir prioridad de ciertas tareas
task_routes = {
    'tasks.add': 'low-priority',
}
"""

"""
añadir cantidad de veces que puede ser procesada
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}
"""
