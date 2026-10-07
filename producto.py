class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        if precio < 0:
            print("Error: el precio no puede ser negativo. Se asigna 0.")
            self.precio = 0
        else:
            self.precio = precio

    def mostrar_informacion(self):
        print(f"{self.nombre} - ${self.precio}")