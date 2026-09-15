"""
Ejercicio: Entrenadores Pokémon con Lista de Lista
----------------------------------------------------
Estructura de datos:

Pokémon    -> [nombre, nivel, tipo, subtipo]
Entrenador -> [nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, [pokemons]]
Lista      -> [entrenador1, entrenador2, ...]

Índices de un ENTRENADOR:
  0 -> nombre
  1 -> torneos_ganados
  2 -> batallas_perdidas
  3 -> batallas_ganadas
  4 -> lista de pokemons

Índices de un POKEMON:
  0 -> nombre
  1 -> nivel
  2 -> tipo
  3 -> subtipo
"""


# =========================================================
# DATOS DE EJEMPLO
# =========================================================
def cargar_datos():
    entrenadores = [
        ["Ash", 5, 10, 40,
         [["Pikachu", 35, "electrico", "ninguno"],
          ["Charizard", 50, "fuego", "volador"],
          ["Bulbasaur", 20, "planta", "veneno"]]],

        ["Misty", 2, 15, 30,
         [["Starmie", 40, "agua", "psiquico"],
          ["Gyarados", 45, "agua", "volador"]]],

        ["Brock", 4, 8, 45,
         [["Onix", 38, "roca", "tierra"],
          ["Geodude", 25, "roca", "tierra"]]],

        ["Gary", 6, 5, 60,
         [["Blastoise", 55, "agua", "ninguno"],
          ["Arcanine", 48, "fuego", "ninguno"],
          ["Wingull", 15, "agua", "volador"]]],

        ["May", 1, 20, 20,
         [["Torchic", 18, "fuego", "ninguno"],
          ["Tyrantrum", 60, "roca", "dragon"],
          ["Tyrantrum", 42, "roca", "dragon"]]],  # pokemon repetido a propósito

        ["Dawn", 4, 3, 47,
         [["Terrakion", 55, "roca", "lucha"],
          ["Piplup", 22, "agua", "ninguno"]]],
    ]
    return entrenadores


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def buscar_entrenador(entrenadores, nombre):
    """Devuelve la lista del entrenador (o None si no existe)."""
    for e in entrenadores:
        if e[0].lower() == nombre.lower():
            return e
    return None


def mostrar_pokemon(p):
    print(f"    - {p[0]} | Nivel: {p[1]} | Tipo: {p[2]} | Subtipo: {p[3]}")


# =========================================================
# a. Cantidad de Pokémon de un determinado entrenador
# =========================================================
def cantidad_pokemons(entrenadores, nombre_entrenador):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None:
        return -1  # no existe
    return len(e[4])


# =========================================================
# b. Entrenadores que ganaron más de 3 torneos
# =========================================================
def entrenadores_mas_de_3_torneos(entrenadores):
    resultado = []
    for e in entrenadores:
        if e[1] > 3:
            resultado.append(e[0])
    return resultado


# =========================================================
# c. Pokémon de mayor nivel del entrenador con más torneos ganados
# =========================================================
def pokemon_top_del_mejor_entrenador(entrenadores):
    if not entrenadores:
        return None

    # Buscar entrenador con más torneos ganados
    mejor_entrenador = entrenadores[0]
    for e in entrenadores:
        if e[1] > mejor_entrenador[1]:
            mejor_entrenador = e

    if not mejor_entrenador[4]:
        return mejor_entrenador[0], None

    # Buscar su pokemon de mayor nivel
    mejor_pokemon = mejor_entrenador[4][0]
    for p in mejor_entrenador[4]:
        if p[1] > mejor_pokemon[1]:
            mejor_pokemon = p

    return mejor_entrenador[0], mejor_pokemon


# =========================================================
# d. Mostrar todos los datos de un entrenador y sus Pokémon
# =========================================================
def mostrar_datos_entrenador(entrenadores, nombre_entrenador):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None:
        print(f"El entrenador '{nombre_entrenador}' no existe.")
        return

    print(f"Entrenador: {e[0]}")
    print(f"  Torneos ganados: {e[1]}")
    print(f"  Batallas perdidas: {e[2]}")
    print(f"  Batallas ganadas: {e[3]}")
    print("  Pokémons:")
    if not e[4]:
        print("    (no tiene pokemons)")
    for p in e[4]:
        mostrar_pokemon(p)


# =========================================================
# e. Entrenadores con porcentaje de batallas ganadas > 79%
# =========================================================
def entrenadores_mas_79_porciento(entrenadores):
    resultado = []
    for e in entrenadores:
        total = e[2] + e[3]  # perdidas + ganadas
        if total > 0:
            porcentaje = (e[3] / total) * 100
            if porcentaje > 79:
                resultado.append((e[0], round(porcentaje, 2)))
    return resultado


# =========================================================
# f. Entrenadores con Pokémon tipo fuego y planta, o agua/volador
#    (tipo y subtipo)
# =========================================================
def entrenadores_fuego_planta_o_agua_volador(entrenadores):
    resultado = []
    for e in entrenadores:
        tiene_fuego = False
        tiene_planta = False
        tiene_agua_volador = False

        for p in e[4]:
            tipo = p[2].lower()
            subtipo = p[3].lower()
            if tipo == "fuego":
                tiene_fuego = True
            if tipo == "planta":
                tiene_planta = True
            if tipo == "agua" and subtipo == "volador":
                tiene_agua_volador = True

        if (tiene_fuego and tiene_planta) or tiene_agua_volador:
            resultado.append(e[0])
    return resultado


# =========================================================
# g. Promedio de nivel de los Pokémon de un entrenador
# =========================================================
def promedio_nivel(entrenadores, nombre_entrenador):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None or not e[4]:
        return 0

    suma = 0
    for p in e[4]:
        suma += p[1]
    return suma / len(e[4])


# =========================================================
# h. Cuántos entrenadores tienen a un determinado Pokémon
# =========================================================
def cuantos_entrenadores_tienen_pokemon(entrenadores, nombre_pokemon):
    contador = 0
    for e in entrenadores:
        for p in e[4]:
            if p[0].lower() == nombre_pokemon.lower():
                contador += 1
                break  # no contar dos veces al mismo entrenador
    return contador


# =========================================================
# i. Entrenadores que tienen Pokémon repetidos
# =========================================================
def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for e in entrenadores:
        nombres = []
        for p in e[4]:
            nombres.append(p[0].lower())

        tiene_repetidos = False
        for n in nombres:
            if nombres.count(n) > 1:
                tiene_repetidos = True
                break

        if tiene_repetidos:
            resultado.append(e[0])
    return resultado


# =========================================================
# j. Entrenadores que tengan Tyrantrum, Terrakion o Wingull
# =========================================================
def entrenadores_con_pokemons_especiales(entrenadores):
    buscados = ["tyrantrum", "terrakion", "wingull"]
    resultado = []
    for e in entrenadores:
        for p in e[4]:
            if p[0].lower() in buscados:
                resultado.append(e[0])
                break
    return resultado


# =========================================================
# k. Determinar si entrenador "X" tiene al Pokémon "Y"
# =========================================================
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    e = buscar_entrenador(entrenadores, nombre_entrenador)
    if e is None:
        print(f"El entrenador '{nombre_entrenador}' no existe.")
        return False

    for p in e[4]:
        if p[0].lower() == nombre_pokemon.lower():
            print(f"Sí, {e[0]} tiene a {p[0]}.\n")
            print("Datos del entrenador:")
            print(f"  Nombre: {e[0]}")
            print(f"  Torneos ganados: {e[1]}")
            print(f"  Batallas perdidas: {e[2]}")
            print(f"  Batallas ganadas: {e[3]}")
            print("Datos del Pokémon:")
            mostrar_pokemon(p)
            return True

    print(f"No, {e[0]} no tiene a {nombre_pokemon}.")
    return False


# =========================================================
# PROGRAMA PRINCIPAL (para probar todas las funciones)
# =========================================================
def main():
    entrenadores = cargar_datos()

    print("=" * 60)
    print("a) Cantidad de pokemons de 'Ash':")
    print(cantidad_pokemons(entrenadores, "Ash"))

    print("=" * 60)
    print("b) Entrenadores con más de 3 torneos ganados:")
    print(entrenadores_mas_de_3_torneos(entrenadores))

    print("=" * 60)
    print("c) Pokémon de mayor nivel del entrenador con más torneos:")
    nombre_e, pokemon = pokemon_top_del_mejor_entrenador(entrenadores)
    print(f"Entrenador: {nombre_e}")
    if pokemon:
        mostrar_pokemon(pokemon)

    print("=" * 60)
    print("d) Datos completos de 'Brock':")
    mostrar_datos_entrenador(entrenadores, "Brock")

    print("=" * 60)
    print("e) Entrenadores con más del 79% de batallas ganadas:")
    print(entrenadores_mas_79_porciento(entrenadores))

    print("=" * 60)
    print("f) Entrenadores con fuego+planta o agua/volador:")
    print(entrenadores_fuego_planta_o_agua_volador(entrenadores))

    print("=" * 60)
    print("g) Promedio de nivel de pokemons de 'Gary':")
    print(promedio_nivel(entrenadores, "Gary"))

    print("=" * 60)
    print("h) Cuántos entrenadores tienen a 'Tyrantrum':")
    print(cuantos_entrenadores_tienen_pokemon(entrenadores, "Tyrantrum"))

    print("=" * 60)
    print("i) Entrenadores con pokemons repetidos:")
    print(entrenadores_con_pokemons_repetidos(entrenadores))

    print("=" * 60)
    print("j) Entrenadores con Tyrantrum, Terrakion o Wingull:")
    print(entrenadores_con_pokemons_especiales(entrenadores))

    print("=" * 60)
    print("k) ¿'Dawn' tiene a 'Terrakion'?")
    entrenador_tiene_pokemon(entrenadores, "Dawn", "Terrakion")

    print("=" * 60)
    print("k) ¿'Ash' tiene a 'Squirtle'?")
    entrenador_tiene_pokemon(entrenadores, "Ash", "Squirtle")


if __name__ == "__main__":
    main()