from producto import Producto

class Comida(Producto):
    def __init__(self, nombre, precio, tipo_comida):
        super().__init__(nombre, precio)
        self.tipo_comida = tipo_comida

    def mostrar_informacion(self):
        print(f"[Comida] {self.nombre} ({self.tipo_comida}) - ${self.precio}")