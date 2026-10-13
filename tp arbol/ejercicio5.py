
# A) CREAR EL NODO DEL ARBOL

class Nodo:
    def __init__(self, nombre, heroe):
        self.nombre = nombre
        self.heroe = heroe
        self.izq = None
        self.der = None


# INSERTAR PERSONAJES EN EL ARBOL

def insertar(raiz, nombre, heroe):
    if raiz is None:
        return Nodo(nombre, heroe)

    if nombre < raiz.nombre:
        raiz.izq = insertar(raiz.izq, nombre, heroe)
    elif nombre > raiz.nombre:
        raiz.der = insertar(raiz.der, nombre, heroe)

    return raiz


# B) LISTAR VILLANOS ALFABETICAMENTE

def listar_villanos(raiz):
    if raiz is not None:
        listar_villanos(raiz.izq)

        if raiz.heroe == False:
            print(raiz.nombre)

        listar_villanos(raiz.der)


# C) MOSTRAR HEROES QUE EMPIEZAN CON C

def heroes_con_c(raiz):
    if raiz is not None:
        heroes_con_c(raiz.izq)

        if raiz.heroe == True and raiz.nombre.startswith("C"):
            print(raiz.nombre)

        heroes_con_c(raiz.der)


# D) CONTAR CANTIDAD DE SUPERHEROES

def contar_heroes(raiz):
    if raiz is None:
        return 0

    cantidad = contar_heroes(raiz.izq)
    cantidad += contar_heroes(raiz.der)

    if raiz.heroe == True:
        cantidad += 1

    return cantidad


# E) BUSQUEDA POR PROXIMIDAD

def buscar_proximidad(raiz, texto):
    if raiz is not None:
        buscar_proximidad(raiz.izq, texto)

        if texto.lower() in raiz.nombre.lower():
            print("Encontrado:", raiz.nombre)

        buscar_proximidad(raiz.der)


# ELIMINAR UN NODO DEL ARBOL

def eliminar(raiz, nombre):
    if raiz is None:
        return None

    if nombre < raiz.nombre:
        raiz.izq = eliminar(raiz.izq, nombre)

    elif nombre > raiz.nombre:
        raiz.der = eliminar(raiz.der, nombre)

    else:
        if raiz.izq is None:
            return raiz.der

        if raiz.der is None:
            return raiz.izq

        aux = raiz.der

        while aux.izq is not None:
            aux = aux.izq

        raiz.nombre = aux.nombre
        raiz.heroe = aux.heroe
        raiz.der = eliminar(raiz.der, aux.nombre)

    return raiz


# MODIFICAR NOMBRE DEL PERSONAJE

def modificar_nombre(raiz, viejo, nuevo):
    actual = raiz

    while actual is not None and actual.nombre != viejo:
        if viejo < actual.nombre:
            actual = actual.izq
        else:
            actual = actual.der

    if actual is not None:
        heroe = actual.heroe
        raiz = eliminar(raiz, viejo)
        raiz = insertar(raiz, nuevo, heroe)
        print("Nombre modificado correctamente")
    else:
        print("Personaje no encontrado")

    return raiz


# F) LISTAR HEROES EN ORDEN DESCENDENTE

def heroes_descendente(raiz):
    if raiz is not None:
        heroes_descendente(raiz.der)

        if raiz.heroe == True:
            print(raiz.nombre)

        heroes_descendente(raiz.izq)


# G) GENERAR UN BOSQUE

def generar_bosque(raiz, arbol_heroes, arbol_villanos):
    if raiz is not None:

        arbol_heroes, arbol_villanos = generar_bosque(
            raiz.izq, arbol_heroes, arbol_villanos
        )

        if raiz.heroe == True:
            arbol_heroes = insertar(
                arbol_heroes, raiz.nombre, True
            )
        else:
            arbol_villanos = insertar(
                arbol_villanos, raiz.nombre, False
            )

        arbol_heroes, arbol_villanos = generar_bosque(
            raiz.der, arbol_heroes, arbol_villanos
        )

    return arbol_heroes, arbol_villanos


# G.I) CONTAR NODOS DE CADA ARBOL

def contar_nodos(raiz):
    if raiz is None:
        return 0

    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)


# G.II) BARRIDO ALFABETICO

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.nombre)
        inorden(raiz.der)


# PROGRAMA PRINCIPAL

arbol = None

personajes = [
    ("Iron Man", True),
    ("Thanos", False),
    ("Captain America", True),
    ("Loki", False),
    ("Thor", True),
    ("Hulk", True),
    ("Black Widow", True),
    ("Ultron", False),
    ("Captain Marvel", True),
    ("Spider-Man", True),
    ("Red Skull", False),
    ("Doctor Strang", True),
    ("Hela", False),
    ("Hawkeye", True),
    ("Crossbones", False)
]

for nombre, heroe in personajes:
    arbol = insertar(arbol, nombre, heroe)


print("\nB) VILLANOS ORDENADOS ALFABETICAMENTE")
listar_villanos(arbol)


print("\nC) SUPERHEROES QUE EMPIEZAN CON C")
heroes_con_c(arbol)


print("\nD) CANTIDAD DE SUPERHEROES")
print(contar_heroes(arbol))


print("\nE) BUSQUEDA POR PROXIMIDAD")
buscar_proximidad(arbol, "Strang")

arbol = modificar_nombre(
    arbol, "Doctor Strang", "Doctor Strange"
)


print("\nF) SUPERHEROES EN ORDEN DESCENDENTE")
heroes_descendente(arbol)


print("\nG) GENERAR BOSQUE")

arbol_heroes = None
arbol_villanos = None

arbol_heroes, arbol_villanos = generar_bosque(
    arbol, arbol_heroes, arbol_villanos
)


print("\nG.I) CANTIDAD DE NODOS")

print("Heroes:", contar_nodos(arbol_heroes))
print("Villanos:", contar_nodos(arbol_villanos))


print("\nG.II) HEROES ORDENADOS ALFABETICAMENTE")
inorden(arbol_heroes)

print("\nG.II) VILLANOS ORDENADOS ALFABETICAMENTE")
inorden(arbol_villanos)
