# para añadir definir el nombre del nodo al cual pertenece un worker de la misma instancia de celery

`celery -A tasks.tasks_1 worker -l info -Q queue_1 -n worker1.%h`

donde:
celery -A <direccion.de.tarea.archivo_tareas> worker -l info -Q <nombre_de_la_cola> -n <nombre_del_worker.%h>

**necesario para cuando se tiene 2 o mas workers en la misma instancia para ejecutar diferentes tareas**

**ejecutar un beat**

`celery -A tasks.tasks_1 beat -l info`