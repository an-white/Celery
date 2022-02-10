import random

from proj.tasks import *

"""
antes de ejecutar el script tener corriendo el worker con
celery -A proj.main worker -l info -c 5

donde
celery -A <directorio.de.la.app.main> worker -l info -c <numero_de_workers>
"""

if __name__ == '__main__':
    campaigns = random.randint(3, 10)
    for n in range(campaigns):
        if n % 2 == 0:
            """
            apply_async recibe los parametros en forma de tupla si no los recibe de esta forma dara errores
            """
            too_long_task.apply_async((n,), countdown=random.randint(2, 10))
        else:
            quick_task.apply_async((n,), countdown=random.randint(2, 10))
