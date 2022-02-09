from proj.tasks import add

# llamado de tarea usando delay es un simplificado del metodo apply_async()
add.delay(2, 2)

add.apply_async((2, 3), queue="lopri", countdown=10)
