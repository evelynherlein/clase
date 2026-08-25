from typing import Any, Optional


class List(list):

    def __init__(self):
        super().__init__()
        self.__criterion_functions = {}

    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__criterion_functions[criterion_key] = criterion_function

    def show(self) -> None:
        for element in self:
            print(element)

    def sort_by_criterion(self, key_criterion=None) -> None:

        sort_criterion = self.__criterion_functions.get(key_criterion)

        if sort_criterion:
            self.sort(key=sort_criterion)

        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()

        elif not self:
            return

        else:
            print("No se puede ordenar la lista: "
                  "no se conoce el criterio.")

    def search(
        self,
        search_value: Any,
        criterion: str = None
    ) -> Optional[int]:

        self.sort_by_criterion(criterion)

        search_criterion = self.__criterion_functions.get(criterion)

        if not self:
            return None

        if (
            search_criterion is None
            and not isinstance(self[0], (bool, int, float, str))
        ):
            print("No se pudo determinar el criterio de búsqueda.")
            return None

        inicio = 0
        fin = len(self) - 1

        while inicio <= fin:

            medio = (inicio + fin) // 2

            if search_criterion:
                valor = search_criterion(self[medio])
            else:
                valor = self[medio]

            if valor == search_value:
                return medio

            elif valor < search_value:
                inicio = medio + 1

            else:
                fin = medio - 1

        return None

    def delete_value(
        self,
        value: Any,
        criterion: str = None
    ) -> Optional[Any]:

        index = self.search(value, criterion)

        if index is not None:
            return self.pop(index)

        return None

    def size(self) -> int:
        return len(self)

    def filter_contain_on_bio(self, values) -> None:

        for element in self:

            for value in values:

                if value.lower() in element.bio.lower():
                    print(element)
                    break

    def filter_start_with(self, values) -> None:

        for element in self:

            if element.name.startswith(values):
                print(element)
