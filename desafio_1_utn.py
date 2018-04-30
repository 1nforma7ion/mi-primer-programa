#ejercicio 1-------------------------------------------------------------------

numero_usuario = int(input("ingrese el numero que quiera convertir en unidad de tiempo: "))

horas = int(numero_usuario / 3600)
minutos = int((numero_usuario - horas * 3600 ) / 60)
segundos = numero_usuario - ((horas * 3600) + (minutos * 60))

print("el timpo transcurrido es de {}:{}:{}".format(horas, minutos, segundos))

#ejericio 2------------------------------------------------------------------

tiempo_horas = int(input("ingrese horas: "))
tiempo_minutos = int(input("ingrese minutos: "))
tiempo_segundos = int(input("ingrese segundos: "))

total_segundos = (tiempo_horas * 3600) + (tiempo_minutos * 60) + tiempo_segundos
print("el total de segundos es {}".format(total_segundos))







