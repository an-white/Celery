import random
import time

from config.main import app


@app.task
def video(name):
    t = random.randint(1, 10)
    time.sleep(t)
    return f"video: {name} convertido"


@app.task
def image(name):
    t = random.randint(1, 10)
    time.sleep(t)
    return f"imagen: {name} enviada"
