numero_1 = float(input("ingrese el primer numero: "))
operacion = input("¿que operacion quiere realizar? (multiplicacion/divicion/suma/resta): ").upper()
numero_2 = float(input("ingrese el segundo numero: "))

if operacion == "SUMA":
    resultado = numero_1+numero_2
    print("el resultaddo es {}".format(resultado))
elif operacion == "RESTA":
    resultado = numero_1-numero_2
    print("el resultaddo es {}".format(resultado))
elif operacion == "MULTIPLICACION":
    resultado = numero_1*numero_2
    print("el resultaddo es {}".format(resultado))
else:
    resultado = numero_1/numero_2
    print("el resultaddo es {}".format(resultado))


