from itertools import combinations
from graph import Graph

# Episodios en los que aparece cada personaje (película numerada de la saga principal).
APARICIONES = {
    "Luke Skywalker": {4, 5, 6, 7, 8, 9},
    "Darth Vader":    {3, 4, 5, 6},
    "Yoda":           {1, 2, 3, 5, 6, 8},
    "Boba Fett":      {2, 5, 6},
    "C-3PO":          {1, 2, 3, 4, 5, 6, 7, 8, 9},
    "Leia":           {4, 5, 6, 7, 8, 9},
    "Rey":            {7, 8, 9},
    "Kylo Ren":       {7, 8, 9},
    "Chewbacca":      {3, 4, 5, 6, 7, 8, 9},
    "Han Solo":       {4, 5, 6, 7, 9},
    "R2-D2":          {1, 2, 3, 4, 5, 6, 7, 8, 9},
    "BB-8":           {7, 8, 9},
}
TOTAL_EPISODIOS = 9


def construir_grafo() -> Graph:
    grafo = Graph(directed=False)
    for nombre, episodios in APARICIONES.items():
        grafo.insert_vertex(nombre, episodios)
    for a, b in combinations(APARICIONES, 2):
        en_comun = len(grafo.vertex_info(a) & grafo.vertex_info(b))
        if en_comun > 0:                       # sin episodios en común no hay arista
            grafo.insert_edge(a, b, en_comun)
    return grafo


def mostrar_arbol(titulo, arbol, total):
    print(f"\n{titulo}")
    for origen, destino, peso in arbol:
        print(f"  {origen} -- {destino}  (episodios: {peso})")
    print(f"  Peso total: {total}")


def mostrar_camino(grafo, origen, destino):
    camino, costo = grafo.dijkstra(origen, destino)
    print(f"\nCamino más corto de {origen} a {destino}:")
    if camino is None:
        print("  No existe camino.")
        return
    print("  " + " -> ".join(camino))
    print(f"  Peso total: {costo}")


if __name__ == "__main__":
    grafo = construir_grafo()
    print(f"Vértices: {grafo.size()} | Aristas: {len(grafo.edges())}")

    # a) árbol de expansión mínimo desde C-3PO, Yoda y Leia (Prim)
    for inicio in ("C-3PO", "Yoda", "Leia"):
        arbol, total = grafo.prim(inicio)
        mostrar_arbol(f"Árbol de expansión mínimo desde {inicio} (Prim):", arbol, total)
    _, total_kruskal = grafo.kruskal()
    print(f"\nControl con Kruskal: peso total del árbol = {total_kruskal}")

    # b) máximo de episodios compartidos y todos los pares que lo alcanzan
    maximo, pares = grafo.max_weight_edges()
    print(f"\nMáximo de episodios compartidos por dos personajes: {maximo}")
    for a, b, _ in pares:
        print(f"  {a} y {b}")

    # c) caminos más cortos
    mostrar_camino(grafo, "C-3PO", "R2-D2")
    mostrar_camino(grafo, "Yoda", "Darth Vader")

    # d) personajes que aparecieron en los nueve episodios
    en_todos = [n for n in grafo.vertices() if len(grafo.vertex_info(n)) == TOTAL_EPISODIOS]
    print(f"\nPersonajes que aparecieron en los {TOTAL_EPISODIOS} episodios: {', '.join(en_todos)}")
