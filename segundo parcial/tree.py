from collections import deque
from typing import Any, List, Optional, Tuple


class Node:
    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.other_values = other_values
        self.height = 0

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None
        self._size = 0

    def size(self) -> int:
        return self._size

    # balanceo AVL
    def height(self, root: Optional[Node]) -> int:
        return -1 if root is None else root.height

    def update_height(self, root: Optional[Node]) -> None:
        if root is not None:
            root.height = max(self.height(root.left), self.height(root.right)) + 1

    def simple_rotation(self, root: Node, control: bool) -> Node:
        if control:  # rotación hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:        # rotación hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        return aux

    def double_rotation(self, root: Node, control: bool) -> Node:
        if control:  # doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            return self.simple_rotation(root, True)
        root.right = self.simple_rotation(root.right, True)  # doble a la izquierda
        return self.simple_rotation(root, False)

    def auto_balance(self, root: Optional[Node]) -> Optional[Node]:
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    # operaciones
    def insert_node(self, value: Any, other_value: Any = None) -> None:
        def _insert(root: Optional[Node]) -> Node:
            if root is None:
                return Node(value, other_value)
            if value < root.value:
                root.left = _insert(root.left)
            else:
                root.right = _insert(root.right)
            root = self.auto_balance(root)
            self.update_height(root)
            return root

        self.root = _insert(self.root)
        self._size += 1

    def search(self, value: Any) -> Optional[Node]:
        root = self.root
        while root is not None:
            if value == root.value:
                return root
            root = root.left if value < root.value else root.right
        return None

    #recorridos
    def inorden(self) -> List[Node]:
        """Orden ascendente por clave."""
        resultado: List[Node] = []

        def _inorden(root):
            if root is not None:
                _inorden(root.left)
                resultado.append(root)
                _inorden(root.right)

        _inorden(self.root)
        return resultado

    def preorden(self) -> List[Node]:
        resultado: List[Node] = []

        def _preorden(root):
            if root is not None:
                resultado.append(root)
                _preorden(root.left)
                _preorden(root.right)

        _preorden(self.root)
        return resultado

    def postorden(self) -> List[Node]:
        resultado: List[Node] = []

        def _postorden(root):
            if root is not None:
                _postorden(root.left)
                _postorden(root.right)
                resultado.append(root)

        _postorden(self.root)
        return resultado

    def by_level(self) -> List[Tuple[int, Node]]:
        resultado: List[Tuple[int, Node]] = []
        if self.root is not None:
            pendientes = deque([(0, self.root)])
            while pendientes:
                nivel, nodo = pendientes.popleft()
                resultado.append((nivel, nodo))
                if nodo.left is not None:
                    pendientes.append((nivel + 1, nodo.left))
                if nodo.right is not None:
                    pendientes.append((nivel + 1, nodo.right))
        return resultado

    def proximity_search(self, texto: str) -> List[Node]:
        return [n for n in self.inorden() if texto in n.value]
