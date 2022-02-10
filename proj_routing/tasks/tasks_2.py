from datetime import date

from config.main import app  # se importa la instacia de celery


# para usar el modo "programada", se debe usar este sender
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        7.0,  # pulso en segundos
        hello.s(),  # nombre de la tarea a ejecutar
        name="task 1",  # un nombre como identificador en el log
    )


@app.task
def hello():
    today = date.today()

    return "ola k ase--->", today.strftime("%d/%m/%Y %H:%M:%S")


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
