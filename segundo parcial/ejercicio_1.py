import json
import unicodedata
from pathlib import Path

from tree import BinaryTree


def normalizar(texto: str) -> str:
    sin_acentos = unicodedata.normalize("NFD", texto)
    sin_acentos = "".join(c for c in sin_acentos if unicodedata.category(c) != "Mn")
    return sin_acentos.lower().strip()

#carga
def cargar_pokemons(ruta: Path) -> list:
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


def construir_arboles(pokemons: list):
    arbol_nombre = BinaryTree()   # clave: nombre normalizado
    arbol_numero = BinaryTree()   # clave: número de Pokédex
    arbol_tipo = BinaryTree()     # clave: tipo normalizado (un nodo agrupa a todos sus Pokémon)

    for p in pokemons:                                   # se cargan en el orden (aleatorio) del JSON
        arbol_nombre.insert_node(normalizar(p["nombre"]), p)
        arbol_numero.insert_node(p["numero"], p)
        for tipo in p["tipos"]:
            clave = normalizar(tipo)
            nodo = arbol_tipo.search(clave)
            if nodo is None:
                arbol_tipo.insert_node(clave, {"tipo": tipo, "pokemons": [p]})
            else:
                nodo.other_values["pokemons"].append(p)
    return arbol_nombre, arbol_numero, arbol_tipo


def mostrar_pokemon(p: dict) -> None:
    print(f"  N° {p['numero']:>4} | {p['nombre']}")
    print(f"    Tipo/s: {', '.join(p['tipos'])}")
    print(f"    Débil frente a: {', '.join(p['debilidades'])}")
    print(f"    Megaevolución: {'Sí' if p['mega_evolucion'] else 'No'} | "
          f"Gigamax: {'Sí' if p['gigamax'] else 'No'}")


def buscar_por_numero(arbol_numero: BinaryTree, numero: int) -> None:
    print(f"\nBúsqueda por número: {numero}")
    nodo = arbol_numero.search(numero)
    if nodo is None:
        print("  No se encontró ningún Pokémon con ese número.")
    else:
        mostrar_pokemon(nodo.other_values)


def buscar_por_nombre(arbol_nombre: BinaryTree, texto: str) -> None:
    print(f"\nBúsqueda por nombre (proximidad): '{texto}'")
    nodos = arbol_nombre.proximity_search(normalizar(texto))
    if not nodos:
        print("  Sin coincidencias.")
    for nodo in nodos:
        mostrar_pokemon(nodo.other_values)


def nombres_por_tipo(arbol_tipo: BinaryTree, tipo: str) -> None:
    nodo = arbol_tipo.search(normalizar(tipo))
    if nodo is None:
        print(f"\nTipo {tipo}: no hay Pokémon de ese tipo.")
        return
    nombres = sorted(p["nombre"] for p in nodo.other_values["pokemons"])
    print(f"\nPokémon de tipo {nodo.other_values['tipo']} ({len(nombres)}):")
    print("  " + ", ".join(nombres))


def listado_por_numero(arbol_numero: BinaryTree) -> None:
    print("\nListado ascendente por número:")
    for nodo in arbol_numero.inorden():
        print(f"  {nodo.other_values['numero']:>4} - {nodo.other_values['nombre']}")


def listado_por_nombre(arbol_nombre: BinaryTree) -> None:
    print("\nListado ascendente por nombre:")
    for nodo in arbol_nombre.inorden():
        print(f"  {nodo.other_values['nombre']}")


def listado_por_nivel(arbol_nombre: BinaryTree) -> None:
    print("\nListado por nivel (árbol de nombres):")
    nivel_actual = -1
    for nivel, nodo in arbol_nombre.by_level():
        if nivel != nivel_actual:
            nivel_actual = nivel
            print(f"  Nivel {nivel}:")
        print(f"    {nodo.other_values['nombre']}")


def debiles_frente_a(arbol_nombre: BinaryTree, nombre_atacante: str) -> None:
    """Pokémon cuya lista de debilidades incluye algún tipo del Pokémon atacante."""
    nodo = arbol_nombre.search(normalizar(nombre_atacante))
    if nodo is None:
        print(f"\n{nombre_atacante} no está cargado.")
        return
    tipos_atacante = nodo.other_values["tipos"]
    afectados = [
        n.other_values["nombre"]
        for n in arbol_nombre.inorden()
        if set(n.other_values["debilidades"]) & set(tipos_atacante)
    ]
    print(f"\nPokémon débiles frente a {nodo.other_values['nombre']} "
          f"({'/'.join(tipos_atacante)}) - {len(afectados)}:")
    print("  " + ", ".join(afectados))


def tipos_y_cantidades(arbol_tipo: BinaryTree) -> None:
    print("\nTipos de Pokémon y cuántos hay de cada uno:")
    for nodo in arbol_tipo.inorden():
        print(f"  {nodo.other_values['tipo']:<10} {len(nodo.other_values['pokemons'])}")


def contar(arbol_numero: BinaryTree, campo: str) -> int:
    return sum(1 for n in arbol_numero.inorden() if n.other_values[campo])

def pausa() -> None:
    input("\n--- Presioná Enter para volver al menú ---")

def pedir_numero(mensaje: str):
    try:
        return int(input(mensaje).strip())
    except ValueError:
        print("  Ingresá un número entero válido.")
        return None

MENU = """
================ POKÉDEX (árboles AVL) ================
 1. Mostrar datos de un Pokémon por número
 2. Mostrar datos de un Pokémon por nombre (proximidad)
 3. Nombres de los Pokémon de un tipo
 4. Listado ascendente por número
 5. Listado ascendente por nombre
 6. Listado por nivel (por nombre)
 7. Débiles frente a Jolteon, Lycanroc y Tyrantrum
 8. Tipos de Pokémon y cuántos hay de cada uno
 9. Cantidad de Pokémon con megaevolución
10. Cantidad de Pokémon con forma Gigamax
 0. Salir
========================================================"""


def main() -> None:
    pokemons = cargar_pokemons(Path(__file__).with_name("pokemons.json"))
    arbol_nombre, arbol_numero, arbol_tipo = construir_arboles(pokemons)
    print(f"Pokémon cargados: {len(pokemons)}")

    while True:
        print(MENU)
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            numero = pedir_numero("Número de Pokémon: ")
            if numero is not None:
                buscar_por_numero(arbol_numero, numero)
        elif opcion == "2":
            buscar_por_nombre(arbol_nombre, input("Nombre (o parte del nombre): "))
        elif opcion == "3":
            tipo = input("Tipo (ej. fantasma, fuego, acero, eléctrico): ")
            nombres_por_tipo(arbol_tipo, tipo)
        elif opcion == "4":
            listado_por_numero(arbol_numero)
        elif opcion == "5":
            listado_por_nombre(arbol_nombre)
        elif opcion == "6":
            listado_por_nivel(arbol_nombre)
        elif opcion == "7":
            for atacante in ("Jolteon", "Lycanroc", "Tyrantrum"):
                debiles_frente_a(arbol_nombre, atacante)
        elif opcion == "8":
            tipos_y_cantidades(arbol_tipo)
        elif opcion == "9":
            print(f"\nPokémon con megaevolución: {contar(arbol_numero, 'mega_evolucion')}")
        elif opcion == "10":
            print(f"\nPokémon con forma Gigamax: {contar(arbol_numero, 'gigamax')}")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
        pausa()


if __name__ == "__main__":
    main()