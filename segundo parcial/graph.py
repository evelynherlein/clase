import heapq
from typing import Any, Dict, List, Optional, Tuple

Arista = Tuple[Any, Any, int]  # (origen, destino, peso)

class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self._info: Dict[Any, Any] = {}            # vértice -> datos extra
        self.adj: Dict[Any, Dict[Any, int]] = {}  # vértice -> {adyacente: peso}

    # estructura
    def insert_vertex(self, value: Any, info: Any = None) -> None:
        if value not in self._adj:
            self._adj[value] = {}
            self._info[value] = info

    def insert_edge(self, origin: Any, destination: Any, weight: int) -> None:
        if origin not in self._adj or destination not in self._adj:
            raise KeyError("Ambos vértices deben existir antes de crear la arista")
        self._adj[origin][destination] = weight
        if not self.directed:
            self._adj[destination][origin] = weight

    def search_vertex(self, value: Any) -> bool:
        return value in self._adj

    def vertex_info(self, value: Any) -> Any:
        return self._info[value]

    def vertices(self) -> List[Any]:
        return list(self._adj)

    def size(self) -> int:
        return len(self._adj)

    def adjacent(self, value: Any) -> Dict[Any, int]:
        return self._adj[value]

    def edges(self) -> List[Arista]:
        """Todas las aristas (en un grafo no dirigido cada una aparece una sola vez)."""
        resultado, vistas = [], set()
        for origen, ady in self._adj.items():
            for destino, peso in ady.items():
                clave = (origen, destino) if self.directed else frozenset((origen, destino))
                if clave not in vistas:
                    vistas.add(clave)
                    resultado.append((origen, destino, peso))
        return resultado

    #Dijkstra
    def dijkstra(self, origin: Any, destination: Any) -> Tuple[Optional[List[Any]], float]:    
        dist = {v: float("inf") for v in self._adj}
        previo: Dict[Any, Any] = {}
        dist[origin] = 0
        cola = [(0, origin)]
        while cola:
            costo, actual = heapq.heappop(cola)
            if costo > dist[actual]:
                continue
            if actual == destination:
                break
            for vecino, peso in sorted(self._adj[actual].items()):
                nuevo = costo + peso
                if nuevo < dist[vecino]:
                    dist[vecino] = nuevo
                    previo[vecino] = actual
                    heapq.heappush(cola, (nuevo, vecino))
        if dist[destination] == float("inf"):
            return None, float("inf")
        camino = [destination]
        while camino[-1] != origin:
            camino.append(previo[camino[-1]])
        return camino[::-1], dist[destination]

    #árbol de expansión
    def prim(self, start: Any) -> Tuple[List[Arista], int]:
        visitados = {start}
        cola = [(peso, start, destino) for destino, peso in self._adj[start].items()]
        heapq.heapify(cola)
        arbol: List[Arista] = []
        total = 0
        while cola and len(visitados) < len(self._adj):
            peso, origen, destino = heapq.heappop(cola)
            if destino in visitados:
                continue
            visitados.add(destino)
            arbol.append((origen, destino, peso))
            total += peso
            for vecino, p in self._adj[destino].items():
                if vecino not in visitados:
                    heapq.heappush(cola, (p, destino, vecino))
        return arbol, total

    def kruskal(self) -> Tuple[List[Arista], int]:
        padre = {v: v for v in self._adj}

        def raiz(v):
            while padre[v] != v:
                padre[v] = padre[padre[v]]
                v = padre[v]
            return v

        arbol: List[Arista] = []
        total = 0
        for origen, destino, peso in sorted(self.edges(), key=lambda a: (a[2], str(a[0]), str(a[1]))):
            ra, rb = raiz(origen), raiz(destino)
            if ra != rb:
                padre[ra] = rb
                arbol.append((origen, destino, peso))
                total += peso
        return arbol, total

    #consultas extra
    def max_weight_edges(self) -> Tuple[int, List[Arista]]:
        """Peso máximo entre las aristas y todas las aristas que lo tienen."""
        aristas = self.edges()
        maximo = max(a[2] for a in aristas)
        return maximo, [a for a in aristas if a[2] == maximo]
