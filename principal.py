from comida import Comida
from bebida import Bebida
from pedido import Pedido

pizza = Comida("Pizza muzzarella", 5000, "Pizza")
milanesa = Comida("Milanesa con papas", 6500, "Plato principal")
gaseosa = Bebida("Gaseosa", 1500, 500)
agua = Bebida("Agua mineral", 1000, 500)

print("=== Menu ===")
pizza.mostrar_informacion()
milanesa.mostrar_informacion()
gaseosa.mostrar_informacion()
agua.mostrar_informacion()


print()
print("=== Prueba de precio negativo ===")
flan = Comida("Flan", -800, "Postre")
flan.mostrar_informacion()


print()
pedido = Pedido()
print("Pedido creado.")


pedido.agregar(pizza)
pedido.agregar(milanesa)
pedido.agregar(gaseosa)
pedido.agregar(agua)

pedido.mostrar()

print("Eliminando: Agua mineral")
pedido.eliminar("Agua mineral")
pedido.mostrar()

print(f"Total a pagar: ${pedido.calcular_total()}")