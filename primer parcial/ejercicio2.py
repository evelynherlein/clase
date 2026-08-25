from collections import deque

from lista import List
from super_heroes_data import superheroes


class Personaje:

    def __init__(
        self,
        name,
        alias,
        real_name,
        bio,
        first_appearance,
        is_villain
    ):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):

        tipo = "Villano" if self.is_villain else "Héroe"

        return (
            f"{self.name} | "
            f"real: {self.real_name} | "
            f"{self.first_appearance} | "
            f"{tipo}"
        )


def by_name(personaje):
    return personaje.name


def by_real_name(personaje):
    return personaje.real_name or ""


def by_first_appearance(personaje):
    return personaje.first_appearance


def separador(titulo):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


lista = List()

lista.add_criterion("name", by_name)
lista.add_criterion("real_name", by_real_name)
lista.add_criterion(
    "first_appearance",
    by_first_appearance
)

for hero in superheroes:

    personaje = Personaje(
        hero["name"],
        hero["alias"],
        hero["real_name"],
        hero["short_bio"],
        hero["first_appearance"],
        hero["is_villain"]
    )

    lista.append(personaje)



if __name__ == "__main__":

    print(
        f"Cantidad total de personajes: {lista.size()}"
    )

    separador(
        "1) Listado ordenado ascendente por NOMBRE"
    )

    lista.sort_by_criterion("name")
    lista.show()

    separador(
        "2) Posición de The Thing y Rocket Raccoon"
    )

    posicion_thing = lista.search(
        "The Thing",
        "name"
    )

    posicion_rocket = lista.search(
        "Rocket Raccoon",
        "name"
    )

    print(
        f"The Thing está en la posición: "
        f"{posicion_thing}"
    )

    print(
        f"Rocket Raccoon está en la posición: "
        f"{posicion_rocket}"
    )


    separador(
        "3) Listado de todos los villanos"
    )

    villanos = List()

    for personaje in lista:

        if personaje.is_villain:
            villanos.append(personaje)

    villanos.show()

    print(
        f"\nTotal de villanos: {villanos.size()}"
    )

    separador(
        "4) Villanos que aparecieron antes de 1980"
    )

    cola_villanos = deque()

    for villano in villanos:
        cola_villanos.append(villano)

    print("Villanos anteriores a 1980:")

    while cola_villanos:

        villano = cola_villanos.popleft()

        if villano.first_appearance < 1980:
            print(villano)

    separador(
        "5) Superhéroes que comienzan con Bl, G, My y W"
    )

    lista.filter_start_with(
        ("Bl", "G", "My", "W")
    )

    separador(
        "6) Listado ordenado ascendente por NOMBRE REAL"
    )

    lista.sort_by_criterion("real_name")
    lista.show()

    separador(
        "7) Listado ordenado por FECHA DE APARICIÓN"
    )

    lista.sort_by_criterion(
        "first_appearance"
    )

    lista.show()

    separador(
        "8) Modificar nombre real de Ant Man"
    )

    posicion_ant_man = lista.search(
        "Ant Man",
        "name"
    )

    if posicion_ant_man is not None:

        personaje = lista[posicion_ant_man]

        print(
            f"Nombre real ANTES: "
            f"{personaje.real_name}"
        )

        personaje.real_name = "Scott Lang"

        print(
            f"Nombre real DESPUÉS: "
            f"{personaje.real_name}"
        )

    else:

        print(
            "No se encontró 'Ant Man' en la lista."
        )

    separador(
        "9) Personajes con 'time-traveling' o 'suit'"
    )

    lista.filter_contain_on_bio(
        ["time-traveling", "suit"]
    )

    separador(
        "10) Eliminar Electro y Baron Zemo"
    )

    nombres_a_eliminar = [
        "Electro",
        "Baron Zemo"
    ]

    for nombre in nombres_a_eliminar:

        eliminado = lista.delete_value(
            nombre,
            "name"
        )

        if eliminado is not None:

            print(
                f"Eliminado -> {eliminado}"
            )

        else:

            print(
                f"'{nombre}' no estaba en la lista."
            )

    print(
        f"\nCantidad total de personajes "
        f"después de eliminar: {lista.size()}"
    )
