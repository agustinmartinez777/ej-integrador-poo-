from comida import Comida
from bebida import Bebida


class ListaProductos:
    def __init__(self):
        self.comidas = []
        self.bebidas = []

    def agregar(self, producto):
        if isinstance(producto, Comida):
            self.comidas.append(producto)
            return True
        if isinstance(producto, Bebida):
            self.bebidas.append(producto)
            return True
        print("Error: solo se pueden agregar comidas o bebidas.")
        return False