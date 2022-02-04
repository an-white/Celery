from tasks import add

if __name__ == '__main__':
    result = add.delay(5, 4)

    """
    ready() returns if the task has finished or not
    """
    result.ready()

    """
    get() espera a que se complete la tarea
    get hara un raise exception en caso de ocurrir un except pero puede ser desactivado
    con
    get(propagate=False)
    """

    """
    si la tarea lenvanta un except puede obtenerse acceso al traceback original con
    result.traceback
    """
