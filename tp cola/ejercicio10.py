#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#resolver las siguientes actividades:
#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#11:43 y las 15:57, y determinar cuántas son.

from collections import deque

cola = deque([
    {"hora": "10:30", "app": "Facebook", "mensaje": "Nuevo comentario"},
    {"hora": "12:00", "app": "Twitter", "mensaje": " noticia de Python"},
    {"hora": "13:20", "app": "Instagram", "mensaje": "stories"},
    {"hora": "14:00", "app": "Twitter", "mensaje": "Curso de Python"},
    {"hora": "16:10", "app": "Facebook", "mensaje": "Nueva notificacion"}
])

# A)
def eliminar_facebook(cola):
    aux = deque()

    while cola:
        notificacion = cola.popleft()

        if notificacion["app"] != "Facebook":
            aux.append(notificacion)

    return aux


# B) 
def mostrar_twitter_python(cola):
    aux = deque()

    while cola:
        notificacion = cola.popleft()

        if (notificacion["app"] == "Twitter" and
            "Python" in notificacion["mensaje"]):
            print(notificacion)

        aux.append(notificacion)

    # devolver todo a la cola original
    while aux:
        cola.append(aux.popleft())


# C) 
# entre las 11:43 y 15:57
def contar_notificaciones(cola):
    pila = []
    aux = deque()

    inicio = "11:43"
    fin = "15:57"

    while cola:
        notificacion = cola.popleft()

        if inicio <= notificacion["hora"] <= fin:
            pila.append(notificacion)

        aux.append(notificacion)

    # reconstruir la cola
    while aux:
        cola.append(aux.popleft())

    print("Cantidad de notificaciones:", len(pila))


cola = eliminar_facebook(cola)

print("Notificaciones de Twitter con Python:")
mostrar_twitter_python(cola)

contar_notificaciones(cola)