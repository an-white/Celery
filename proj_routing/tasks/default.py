import random
import time

from config.main import app


@app.task
def default():
    t = random.randint(1, 10)
    time.sleep(t)
    return f"tarea por defecto ejecutada"
