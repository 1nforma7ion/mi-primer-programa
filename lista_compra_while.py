mi_lista = []
input_usuario = input("¿que necesitas comprar (escribe FIN para salir): ").upper()

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("¿que necesitas comprar (escribe FIN para salir): ").upper()

for item in mi_lista:
    print("tengo que comprar {}".format(item))

print("esta es la lista de compra")
