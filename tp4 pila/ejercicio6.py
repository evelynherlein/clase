"""

La lista de superhéroes es una lista de estos diccionarios.
"""

# ------------------------------------------------------------------
# Datos iniciales
# ------------------------------------------------------------------
superheroes = [
    {"nombre": "Linterna Verde", "anio": 1940, "casa": "DC",
     "biografia": "Hal Jordan recibe un anillo de poder que crea constructos de energía."},
    {"nombre": "Wolverine", "anio": 1974, "casa": "Marvel",
     "biografia": "Mutante con garras de adamantium y factor de curación acelerado."},
    {"nombre": "Dr. Strange", "anio": 1963, "casa": "Otro",
     "biografia": "Ex-cirujano convertido en el Hechicero Supremo, usa una capa mágica."},
    {"nombre": "Capitana Marvel", "anio": 1968, "casa": "Marvel",
     "biografia": "Carol Danvers obtiene poderes cósmicos y viste un traje que absorbe energía."},
    {"nombre": "Mujer Maravilla", "anio": 1941, "casa": "DC",
     "biografia": "Princesa amazona que lucha con el lazo de la verdad y su armadura dorada."},
    {"nombre": "Flash", "anio": 1940, "casa": "DC",
     "biografia": "Barry Allen obtiene supervelocidad tras un accidente de laboratorio."},
    {"nombre": "Star-Lord", "anio": 1976, "casa": "Marvel",
     "biografia": "Peter Quill lidera a los Guardianes de la Galaxia con su traje y máscara."},
    {"nombre": "Batman", "anio": 1939, "casa": "DC",
     "biografia": "Bruce Wayne combate el crimen en Gotham sin superpoderes, con gran armadura."},
    {"nombre": "Moon Knight", "anio": 1975, "casa": "Marvel",
     "biografia": "Marc Spector recibe poderes del dios egipcio Khonshu y usa un traje blanco."},
    {"nombre": "Superman", "anio": 1938, "casa": "DC",
     "biografia": "Kryptoniano criado en la Tierra con poderes casi ilimitados."},
]


# a. Eliminar el nodo que contiene la información de Linterna Verde
def eliminar_superheroe(lista, nombre):
    for h in lista:
        if h["nombre"] == nombre:
            lista.remove(h)
            return True
    return False


# b. Mostrar el año de aparición de Wolverine

def anio_aparicion(lista, nombre):
    for h in lista:
        if h["nombre"] == nombre:
            return h["anio"]
    return None


# c. Cambiar la casa de Dr. Strange a Marvel
def cambiar_casa(lista, nombre, nueva_casa):
    for h in lista:
        if h["nombre"] == nombre:
            h["casa"] = nueva_casa
            return True
    return False


# d. Mostrar el nombre de los superhéroes cuya biografía menciona
#    "traje" o "armadura"
def con_traje_o_armadura(lista):
    resultado = []
    for h in lista:
        bio = h["biografia"].lower()
        if "traje" in bio or "armadura" in bio:
            resultado.append(h["nombre"])
    return resultado


# e. Mostrar nombre y casa de los superhéroes con fecha de aparición
#    anterior a 1963
def anteriores_a_1963(lista):
    return [(h["nombre"], h["casa"]) for h in lista if h["anio"] < 1963]


# f. Mostrar la casa a la que pertenece un superhéroe puntual
#    (usada para Capitana Marvel y Mujer Maravilla)
def casa_de(lista, nombre):
    for h in lista:
        if h["nombre"] == nombre:
            return h["casa"]
    return None


# g. Mostrar toda la información de un superhéroe puntual
#    (usada para Flash y Star-Lord)
def info_completa(lista, nombre):
    for h in lista:
        if h["nombre"] == nombre:
            return h
    return None


# h. Listar los superhéroes que comienzan con la letra B, M o S
def comienzan_con(lista, letras=("B", "M", "S")):
    return [h["nombre"] for h in lista if h["nombre"].upper().startswith(tuple(letras))]


# i. Determinar cuántos superhéroes hay de cada casa de comic
def contar_por_casa(lista):
    conteo = {}
    for h in lista:
        conteo[h["casa"]] = conteo.get(h["casa"], 0) + 1
    return conteo



# Demostración de uso
if __name__ == "__main__":

    print("a. Eliminar a Linterna Verde")
    eliminar_superheroe(superheroes, "Linterna Verde")
    print([h["nombre"] for h in superheroes], "\n")

    print("b. Año de aparición de Wolverine")
    print(anio_aparicion(superheroes, "Wolverine"), "\n")

    print("c. Cambiar la casa de Dr. Strange a Marvel")
    cambiar_casa(superheroes, "Dr. Strange", "Marvel")
    print(casa_de(superheroes, "Dr. Strange"), "\n")

    print('d. Superhéroes cuya biografía menciona "traje" o "armadura"')
    print(con_traje_o_armadura(superheroes), "\n")

    print("e. Superhéroes con año de aparición anterior a 1963 (nombre, casa)")
    print(anteriores_a_1963(superheroes), "\n")

    print("f. Casa de Capitana Marvel y Mujer Maravilla")
    print("Capitana Marvel ->", casa_de(superheroes, "Capitana Marvel"))
    print("Mujer Maravilla ->", casa_de(superheroes, "Mujer Maravilla"), "\n")

    print("g. Información completa de Flash y Star-Lord")
    print(info_completa(superheroes, "Flash"))
    print(info_completa(superheroes, "Star-Lord"), "\n")

    print("h. Superhéroes que comienzan con B, M o S")
    print(comienzan_con(superheroes), "\n")

    print("i. Cantidad de superhéroes por casa")
    print(contar_por_casa(superheroes))