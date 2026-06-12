#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
#F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from collections import deque

cola = deque([
    {"personaje": "Tony Stark", "heroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "heroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "heroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "heroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "heroe": "Ant-Man", "genero": "M"}
])

aux = deque()

while cola:
    dato = cola.popleft()

    # A) 
    if dato["heroe"] == "Capitana Marvel":
        print("a) Personaje de Capitana Marvel:", dato["personaje"])

    # B) 
    if dato["genero"] == "F":
        print("b) Superheroe femenino:", dato["heroe"])

    # C) 
    if dato["genero"] == "M":
        print("c) Personaje masculino:", dato["personaje"])

    # D) 
    if dato["personaje"] == "Scott Lang":
        print("d) Superheroe de Scott Lang:", dato["heroe"])

    # E)
    if (dato["personaje"][0] == "S" or
        dato["heroe"][0] == "S"):
        print("e)", dato)

    # F) Buscar Carol Danvers
    if dato["personaje"] == "Carol Danvers":
        print("f) Carol Danvers si esta. Su superheroe es:",
              dato["heroe"])

    aux.append(dato)

while aux:
    cola.append(aux.popleft())