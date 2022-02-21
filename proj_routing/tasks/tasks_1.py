from config.main import app


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        1,
        task_1.s(3, 4),
        name="task_1",
    )


@app.task
def task_1(x, y):
    return x + y

# @app.task
# def mul(x, y):
#     return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)
