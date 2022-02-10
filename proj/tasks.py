import random
import time

from .main import app


@app.task
def too_long_task(n):
    t = random.randint(4, 8)
    time.sleep(t)
    return f"task n:{n} long task done"


@app.task
def quick_task(n):
    t = random.randint(0, 3)
    time.sleep(t)
    return f"task n:{n} quick task done"


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def rest(x, y):
    return x - y


@app.task
def n_add(numbers):
    return sum(numbers)
