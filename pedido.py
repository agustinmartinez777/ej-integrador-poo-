from lista_productos import ListaProductos


class Pedido:
    def __init__(self):
        self.elementos = ListaProductos()

    def agregar(self, producto):
        return self.elementos.agregar(producto)

    def eliminar(self, nombre):
        for comida in self.elementos.comidas:
            if comida.nombre == nombre:
                self.elementos.comidas.remove(comida)
                return True
        for bebida in self.elementos.bebidas:
            if bebida.nombre == nombre:
                self.elementos.bebidas.remove(bebida)
                return True
        print(f"Error: no se encontro '{nombre}' en el pedido.")
        return False

    def mostrar(self):
        print("----- PEDIDO -----")
        for comida in self.elementos.comidas:
            comida.mostrar_informacion()
        for bebida in self.elementos.bebidas:
            bebida.mostrar_informacion()
        print("------------------")

    def calcular_total(self):
        total = 0
        for comida in self.elementos.comidas:
            total += comida.precio
        for bebida in self.elementos.bebidas:
            total += bebida.precio
        return total