para correr el worker celery -A <nombre_del_archivo_de_la_task> worker --loglevel=INFO

**añadir conf app**

app.conf.task_serializer = "json"

**añadir varias configuraciones a la app**

app.conf.update(
task_serializer='json', accept_content=['json'], # Ignore other content result_serializer='json', timezone='Europe/Oslo'
, enable_utc=True,
)

chequear el archivo de configuraciones python -m celeryconfig