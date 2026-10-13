
from collections import deque


# CREAR NODO
class Nodo:
    def __init__(self, nombre, derrotado_por):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = ""
        self.capturada = ""
        self.izq = None
        self.der = None


# INSERTAR EN EL ARBOL
def insertar(raiz, nombre, derrotado_por):
    if raiz is None:
        return Nodo(nombre, derrotado_por)

    if nombre < raiz.nombre:
        raiz.izq = insertar(raiz.izq, nombre, derrotado_por)
    elif nombre > raiz.nombre:
        raiz.der = insertar(raiz.der, nombre, derrotado_por)

    return raiz


# BUSCAR UNA CRIATURA
def buscar(raiz, nombre):
    if raiz is None:
        return None

    if raiz.nombre == nombre:
        return raiz

    if nombre < raiz.nombre:
        return buscar(raiz.izq, nombre)
    else:
        return buscar(raiz.der, nombre)


# A) LISTADO INORDEN
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)

        print(raiz.nombre, "- Derrotado por:",
              raiz.derrotado_por or "Nadie")

        inorden(raiz.der)


# B) CARGAR DESCRIPCION
def cargar_descripcion(raiz, nombre, descripcion):
    nodo = buscar(raiz, nombre)

    if nodo is not None:
        nodo.descripcion = descripcion
        print("Descripcion guardada")
    else:
        print("Criatura no encontrada")


# C) MOSTRAR TODA LA INFORMACION
def mostrar_criatura(raiz, nombre):
    nodo = buscar(raiz, nombre)

    if nodo is not None:
        print("Nombre:", nodo.nombre)
        print("Derrotado por:", nodo.derrotado_por or "Nadie")
        print("Descripcion:", nodo.descripcion or "Sin descripcion")
        print("Capturada por:", nodo.capturada or "Nadie")
    else:
        print("Criatura no encontrada")


# D) TRES HEROES CON MAS VICTORIAS
def contar_derrotas(raiz, conteo):
    if raiz is not None:
        contar_derrotas(raiz.izq, conteo)

        if raiz.derrotado_por:
            heroe = raiz.derrotado_por
            conteo[heroe] = conteo.get(heroe, 0) + 1

        contar_derrotas(raiz.der, conteo)


def top_tres(raiz):
    conteo = {}
    contar_derrotas(raiz, conteo)

    ordenados = sorted(
        conteo.items(),
        key=lambda x: (-x[1], x[0])
    )

    for heroe, cantidad in ordenados[:3]:
        print(heroe, ":", cantidad)


# E) CRIATURAS DERROTADAS POR HERACLES
def derrotadas_heracles(raiz):
    if raiz is not None:
        derrotadas_heracles(raiz.izq)

        if raiz.derrotado_por == "Heracles":
            print(raiz.nombre)

        derrotadas_heracles(raiz.der)


# F) CRIATURAS NO DERROTADAS
def no_derrotadas(raiz):
    if raiz is not None:
        no_derrotadas(raiz.izq)

        if raiz.derrotado_por == "":
            print(raiz.nombre)

        no_derrotadas(raiz.der)


# G Y H) REGISTRAR CAPTURA
def capturar(raiz, nombre, heroe):
    nodo = buscar(raiz, nombre)

    if nodo is not None:
        nodo.capturada = heroe
        print(nombre, "capturada por", heroe)
    else:
        print("Criatura no encontrada")


# I) BUSQUEDA POR COINCIDENCIA
def buscar_coincidencia(raiz, texto):
    if raiz is not None:
        buscar_coincidencia(raiz.izq, texto)

        if texto.lower() in raiz.nombre.lower():
            print(raiz.nombre)

        buscar_coincidencia(raiz.der, texto)


# J) ELIMINAR CRIATURA
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
        raiz.derrotado_por = aux.derrotado_por
        raiz.descripcion = aux.descripcion
        raiz.capturada = aux.capturada

        raiz.der = eliminar(raiz.der, aux.nombre)

    return raiz


# K) MODIFICAR AVES DEL ESTINFALO
def modificar_aves(raiz):
    nodo = buscar(raiz, "Aves del Estínfalo")

    if nodo is not None:
        nodo.derrotado_por = "Heracles"
        nodo.descripcion = "Heracles derroto a varias aves"
        print("Aves del Estinfalo modificadas")


# L) CAMBIAR NOMBRE
def cambiar_nombre(raiz, viejo, nuevo):
    nodo = buscar(raiz, viejo)

    if nodo is not None:
        derrotado = nodo.derrotado_por
        descripcion = nodo.descripcion
        capturada = nodo.capturada

        raiz = eliminar(raiz, viejo)
        raiz = insertar(raiz, nuevo, derrotado)

        nuevo_nodo = buscar(raiz, nuevo)
        nuevo_nodo.descripcion = descripcion
        nuevo_nodo.capturada = capturada

        print("Nombre modificado")
    else:
        print("Criatura no encontrada")

    return raiz


# M) LISTADO POR NIVEL
def por_nivel(raiz):
    if raiz is None:
        return

    cola = deque([raiz])

    while cola:
        nodo = cola.popleft()
        print(nodo.nombre)

        if nodo.izq is not None:
            cola.append(nodo.izq)

        if nodo.der is not None:
            cola.append(nodo.der)


# N) CAPTURADAS POR HERACLES
def capturadas_heracles(raiz):
    if raiz is not None:
        capturadas_heracles(raiz.izq)

        if raiz.capturada == "Heracles":
            print(raiz.nombre)

        capturadas_heracles(raiz.der)


# DATOS DE LA TABLA
criaturas = [
    ("Ceto", ""),
    ("Tifón", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", ""),
    ("Pefredo", ""),
    ("Enio", ""),
    ("Escila", ""),
    ("Caribdis", ""),
    ("Euríale", ""),
    ("Esteno", ""),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", ""),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", ""),
    ("Cerbero", ""),
    ("Cerda de Cromión", "Teseo"),
    ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", ""),
    ("Gerión", "Heracles"),
    ("Cloto", ""),
    ("Láquesis", ""),
    ("Átropos", ""),
    ("Minotauro de Creta", "Teseo"),
    ("Harpías", ""),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", ""),
    ("Talos", "Medea"),
    ("Sirenas", ""),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", ""),
    ("Basilisco", ""),
    ("Jabalí de Erimanto", "")
]


# CARGAR ARBOL
arbol = None

for nombre, derrotado in criaturas:
    arbol = insertar(arbol, nombre, derrotado)


# MENU PRINCIPAL
opcion = -1

while opcion != 0:
    print("\n===== MENU CRIATURAS MITOLOGICAS =====")
    print("1. Listado inorden")
    print("2. Cargar descripcion")
    print("3. Mostrar informacion de Talos")
    print("4. Top 3 heroes")
    print("5. Derrotadas por Heracles")
    print("6. Criaturas no derrotadas")
    print("7. Registrar capturas de Heracles")
    print("8. Buscar por coincidencia")
    print("9. Eliminar Basilisco y Sirenas")
    print("10. Modificar Aves del Estinfalo")
    print("11. Cambiar Ladon por Dragon Ladon")
    print("12. Listado por nivel")
    print("13. Capturadas por Heracles")
    print("0. Salir")

    try:
        opcion = int(input("Ingrese opcion: "))
    except ValueError:
        print("Ingrese un numero valido")
        continue

    if opcion == 1:
        inorden(arbol)

    elif opcion == 2:
        nombre = input("Nombre de criatura: ")
        descripcion = input("Descripcion: ")
        cargar_descripcion(arbol, nombre, descripcion)

    elif opcion == 3:
        mostrar_criatura(arbol, "Talos")

    elif opcion == 4:
        top_tres(arbol)

    elif opcion == 5:
        derrotadas_heracles(arbol)

    elif opcion == 6:
        no_derrotadas(arbol)

    elif opcion == 7:
        nombres = [
            "Cerbero",
            "Toro de Creta",
            "Cierva de Cerinea",
            "Jabalí de Erimanto"
        ]

        for nombre in nombres:
            capturar(arbol, nombre, "Heracles")

    elif opcion == 8:
        texto = input("Ingrese coincidencia: ")
        buscar_coincidencia(arbol, texto)

    elif opcion == 9:
        arbol = eliminar(arbol, "Basilisco")
        arbol = eliminar(arbol, "Sirenas")
        print("Criaturas eliminadas")

    elif opcion == 10:
        modificar_aves(arbol)

    elif opcion == 11:
        arbol = cambiar_nombre(
            arbol, "Ladón", "Dragón Ladón"
        )

    elif opcion == 12:
        por_nivel(arbol)

    elif opcion == 13:
        capturadas_heracles(arbol)

    elif opcion == 0:
        print("Fin del programa")

    else:
        print("Opcion incorrecta")
