from celery import Celery

"""
se necesita una instancia de celery
"""
# app = Celery("tasks", broker="pyamqp://guest@localhost//")

"""
guardar resultados
"""

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

"""
para correr el worker
celery -A <nombre_del_archivo_de_la_task> worker --loglevel=INFO
"""


@app.task
def add(x, y):
    return x + y


"""
añadir conf app
"""
app.conf.task_serializer = "json"

"""añadir un archivo de configuraciones"""
app.config_from_object("celeryconfig")
