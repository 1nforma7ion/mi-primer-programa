numero_inicial = 10
print(numero_inicial)
if numero_inicial % 2 == 0:
    print("este numero es par")
else:
    print("este numero es impar")
while numero_inicial > 0:
    numero_inicial -= 1
    print(numero_inicial)
    if numero_inicial % 2 == 0:
        print("este numero es par")
    else:
        print("este numero es impar")

print("he terminado")
