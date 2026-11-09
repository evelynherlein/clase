
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


def marcar_no_visitado(grafo):
    """Marca todos los vértices como no visitados."""
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


# ---------------------------------------------------------------- EJERCICIO 14
def existe_paso(grafo, origen, destino):
    """Devuelve True si se puede ir del vértice origen al vértice destino.

    Usa barrido en profundidad. Antes de llamarla conviene hacer
    marcar_no_visitado(grafo).
    """
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


# ---------------------------------------------------------------- pruebas
if __name__ == "__main__":
    g = Grafo(dirigido=True)
    for v in "ABCDEF":
        insertar_vertice(g, v)
    for o, d, peso in [("A", "B", 4), ("B", "C", 2), ("A", "D", 7), ("E", "A", 1)]:
        insertar_arista(g, peso, buscar_vertice(g, o), buscar_vertice(g, d))

    for o, d in [("A", "C"), ("A", "E"), ("E", "C"), ("C", "A"), ("A", "F")]:
        marcar_no_visitado(g)
        r = existe_paso(g, buscar_vertice(g, o), buscar_vertice(g, d))
        print(f"{o} -> {d}: {r}")