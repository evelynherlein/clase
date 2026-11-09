
class nodoArista(object):
    """Clase nodo arista."""

    def __init__(self, info, destino):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.sig = None


class Arista(object):
    """Clase lista de aristas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacía."""
        self.inicio = None
        self.tamanio = 0


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacío."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


# ---------------------------------------------------------------- operaciones base
def insertar_vertice(grafo, dato):
    """Inserta un vértice al grafo (ordenado)."""
    nodo = nodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def agregar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino (ordenada por destino)."""
    nodo = nodoArista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregar_arista(destino.adyacentes, dato, origen.info)


def buscar_vertice(grafo, buscado):
    """Devuelve la dirección del vértice buscado."""
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux


# ---------------------------------------------------------------- EJERCICIO 5
def eliminar_arista(vertice, destino):
    """Elimina una arista del vértice y la devuelve si la encuentra.

    'vertice' es la lista de aristas (vertice.adyacentes).
    Devuelve la info (peso) de la arista eliminada, o None si no existe
    una arista con ese destino. Elimina la primera que coincida.
    """
    x = None
    if vertice.inicio is None:          # vértice sin aristas
        return x
    if vertice.inicio.destino == destino:
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while act is not None and act.destino != destino:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x


# ---------------------------------------------------------------- pruebas
if __name__ == "__main__":
    g = Grafo(dirigido=True)
    for v in "ABCD":
        insertar_vertice(g, v)
    for o, d, peso in [("A", "B", 4), ("A", "D", 7), ("B", "C", 2)]:
        insertar_arista(g, peso, buscar_vertice(g, o), buscar_vertice(g, d))

    a = buscar_vertice(g, "A")
    print("Elimino A->B, peso devuelto:", eliminar_arista(a.adyacentes, "B"))
    print("Elimino A->B otra vez:", eliminar_arista(a.adyacentes, "B"))
    print("Elimino A->Z (no existe):", eliminar_arista(a.adyacentes, "Z"))
    print("Aristas que quedan en A:", a.adyacentes.tamanio)