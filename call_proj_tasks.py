from proj.tasks import add

# llamado de tarea usando delay es un simplificado del metodo apply_async()
add.delay(2, 2)

"""
celery crea su propia cola esta no debe existir previamente y se pueden enviar multiples tareas a una misma cola
"""
add.apply_async((2, 3), queue="celery_queue", countdown=5)
