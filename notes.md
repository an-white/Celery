cuando se levanta celery se puede ver la configuracion esta contiene

broker la url specifica argumentada en

concurrency por defecto es el numero de nucleos de la cpu del computador

**monitorear el projecto desde Flower con celery -A proj flower**

apply_async metodo en el cual puedo definir la cola de ejecucion (debe tener un worker asignado para que se ejecute)
y el tiempo de espera para ejecutar la tarea

add.apply_async((2, 2), queue='lopri', countdown=10)

uso de signatures para pasar la firma de la invocacion de una tarea a otro proceso o como argumento de otra funcion
add.signature((2, 2), countdown=10).delay()

**primitivas de celery**

**group**
llama a una lista de tareas en paralelo y retorna una instancia que nos permite inspeccionar esos resultados como un
grupo

**chain**
se pueden vincular tareas de tal forma que al una dar un retorno la siguiente es llamada

chain(add.s(4, 4) | mul.s(8))().get()

**chord**
es un grupo con un callback, un grupo vinculado a otra tarea se convertira automaticamente en un chord
(group(add.s(i, i) for i in range(10)) | xsum.s())().get()

map starmap chunks