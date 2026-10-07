from producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen):
        super().__init__(nombre, precio)
        self.volumen = volumen

    def mostrar_informacion(self):
        print(f"[Bebida] {self.nombre} ({self.volumen} ml) - ${self.precio}")