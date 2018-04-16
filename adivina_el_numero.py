numero_ganador = int(input("ingrese el numero que su amigo debe adivinar: "))
respuesta = 0

while numero_ganador != respuesta :
    respuesta = int(input("adivina el numero: "))
    if numero_ganador != respuesta:
        print("incorrecto")

print("has ganado!!!")
