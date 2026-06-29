def buscar_capitan(lista, i=0):
    if i >= len(lista):
        return False

    if lista[i] == "Capitan America":
        return True

    return buscar_capitan(lista, i + 1)


def listar_superheroes(lista, i=0):
    if i >= len(lista):
        return

    print(lista[i])
    listar_superheroes(lista, i + 1)


superheroes = [
    "Iron Man",
    "Hulk",
    "Thor",
    "Black Widow",
    "Hawkeye",
    "Capitan America",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Scarlet Witch",
    "Ant-Man",
    "Wolverine",
    "Deadpool",
    "Captain Marvel",
    "Storm"
]

if buscar_capitan(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")

print("\nLista de superheroes:")
listar_superheroes(superheroes)