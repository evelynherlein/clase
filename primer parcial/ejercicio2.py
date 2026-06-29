import json
import os
from collections import deque


def cargar_personajes():
    ruta = os.path.join(os.path.dirname(__file__), "listapersonajes.json")

    with open(ruta, "r", encoding="utf-8") as archivo:
        personajes = json.load(archivo)

    return personajes


def guardar_personajes(personajes):
    ruta = os.path.join(os.path.dirname(__file__), "listapersonajes.json")

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(personajes, archivo, indent=4, ensure_ascii=False)


personajes = cargar_personajes()

# 1 Ordenar por nombre
personajes.sort(key=lambda x: x["name"])

print("PERSONAJES ORDENADOS POR NOMBRE\n")

for p in personajes:
    print(p["name"])

# 2 Posición de The Thing y Rocket Raccoon
print("\nPOSICIONES\n")

for i in range(len(personajes)):

    if personajes[i]["name"] == "The Thing":
        print("The Thing está en la posición", i)

    if personajes[i]["name"] == "Rocket Raccoon":
        print("Rocket Raccoon está en la posición", i)

# 3 Villanos
print("\nVILLANOS\n")

for p in personajes:

    if p["is_villain"]:
        print(p["name"])

# 4 Cola de villanos anteriores a 1980
print("\nVILLANOS ANTES DE 1980\n")

cola = deque()

for p in personajes:

    if p["is_villain"]:
        cola.append(p)

while len(cola) > 0:

    aux = cola.popleft()

    if aux["first_appearance"] < 1980:
        print(aux["name"], "-", aux["first_appearance"])

# 5 Héroes que comienzan con Bl G My W
print("\nSUPERHEROES Bl G My W\n")

for p in personajes:

    if not p["is_villain"]:

        if (p["name"].startswith("Bl") or
                p["name"].startswith("G") or
                p["name"].startswith("My") or
                p["name"].startswith("W")):

            print(p["name"])

# 6 Ordenados por nombre real
personajes.sort(key=lambda x: x["real_name"] if x["real_name"] is not None else "")

print("\nORDENADOS POR NOMBRE REAL\n")

for p in personajes:
    print(p["real_name"], "-", p["name"])

# 7 Superhéroes ordenados por fecha
heroes = []

for p in personajes:

    if not p["is_villain"]:
        heroes.append(p)

heroes.sort(key=lambda x: x["first_appearance"])

print("\nSUPERHEROES POR FECHA\n")

for h in heroes:
    print(h["name"], "-", h["first_appearance"])

# 8 Modificar Ant Man
print("\nMODIFICAR ANT MAN\n")

for p in personajes:

    if p["name"] == "Ant Man":

        print("Antes:", p["real_name"])

        p["real_name"] = "Scott Lang"

        print("Después:", p["real_name"])

guardar_personajes(personajes)

# 9 Buscar time-traveling o suit
print("\nBIOGRAFIAS\n")

for p in personajes:

    bio = p["short_bio"].lower()

    if "time-traveling" in bio or "suit" in bio:
        print(p["name"])

# 10 Eliminar Electro y Baron Zemo
print("\nELIMINAR PERSONAJES\n")

for p in personajes[:]:

    if p["name"] == "Electro" or p["name"] == "Baron Zemo":

        print("Nombre:", p["name"])
        print("Nombre real:", p["real_name"])
        print("Año:", p["first_appearance"])
        print("Biografía:", p["short_bio"])
        print()

        personajes.remove(p)

guardar_personajes(personajes)

print("\nProceso terminado.")