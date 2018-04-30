import random

#DATOS:
nombre_jugador = input('Ingrese su nombre: ')

posiciones = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 50)
segmentos = ('Triples', 'Dobles', 'Simples')

#PRIMER TIRADA:

tiro_uno = random.choice(posiciones)

print('Has realizado tu primer tiro')

if tiro_uno != 25 and  tiro_uno != 50 and tiro_uno != 0:
    print('{}, tu dardo ha obtenido {} puntos para tu primer tiro'.format(nombre_jugador, tiro_uno))
    segmento_uno = random.choice(segmentos)
    if segmento_uno == 'Triples':
        tiro_uno = tiro_uno * 3
        print('Tu dardo ha caido en el segmento "{}", por lo que se multiplicara por 3'. format(segmento_uno))
        print('Tu tiro ahora vale {} puntos'.format(tiro_uno))
    elif segmento_uno == 'Dobles':
        tiro_uno = tiro_uno * 2
        print('Tu dardo ha caido en el segmento "{}", por lo que se multiplicara por 2'. format(segmento_uno))
        print('Tu tiro ahora vale {} puntos'.format(tiro_uno))
    else:
        print('Tu dardo ha caido en el segmento "{}", por lo que tu puntaje no cambia'.format(segmento_uno))

elif tiro_uno == 50 or tiro_uno == 25 or tiro_uno == 0:
    if tiro_uno == 50:
        print('Tu dardo ha caido en el centro de la diana, tu puntaje es de {} en tu 1er tiro'.format(tiro_uno))
    elif tiro_uno == 25:
        print('Tu dardo ha caido en el aro interno de la diana, tu puntaje es de {} en tu 1er tiro'.format(tiro_uno))
    else:
        print('Tu dardo no ha dado en el tablero, tu puntaje es de {} en tu 1er tiro'.format(tiro_uno))

#SEGUNDA TIRADA:

tiro_dos = random.choice(posiciones)

print('Has realizado tu segundo tiro')


if tiro_dos != 25 and tiro_dos != 50 and tiro_dos != 0:
    print('{}, tu dardo ha obtenido {} puntos para tu segundo tiro'.format(nombre_jugador, tiro_dos))
    segmento_dos = random.choice(segmentos)
    if segmento_dos == 'Triples':
        tiro_dos = tiro_dos * 3
        print('Tu dardo ha caido en el segmento "{}", por lo que se multiplicara por 3'.format(segmento_dos))
        print('Tu tiro ahora vale {} puntos'.format(tiro_dos))
    elif segmento_dos == 'Dobles':
        tiro_dos = tiro_dos * 2
        print('Tu dardo ha caido en el segmento "{}", por lo que se multiplicara por 2'.format(segmento_dos))
        print('Tu tiro ahora vale {} puntos'.format(tiro_dos))
    else:
        print('Tu dardo ha caido en el segmento "{}", por lo que tu puntaje no cambia'.format(segmento_dos))

elif tiro_dos == 50 or tiro_dos == 25 or tiro_dos == 0:
    if tiro_dos == 50:
        print('Tu dardo ha caido en el centro de la diana, tu puntaje es de {} en tu 2do tiro'.format(tiro_dos))
    elif tiro_dos == 25:
        print('Tu dardo ha caido en el aro interno de la diana, tu puntaje es de {} en tu 2do tiro'.format(tiro_dos))
    else:
        print('Tu dardo no ha dado en el tablero, tu puntaje es de {} en tu 2do tiro'.format(tiro_dos))

#TERCER TIRADA:

tiro_tres = random.choice(posiciones)

print('Has realizado tu tercer tiro')


if tiro_tres != 25 and tiro_tres != 50 and tiro_tres != 0:
    print('{}, tu dardo ha obtenido {} puntos para tu tercer tiro'.format(nombre_jugador, tiro_tres))
    segmento_tres = random.choice(segmentos)
    if segmento_tres == 'Triples':
        tiro_tres = tiro_tres * 3
        print('Tu dardo ha caido en el segmento "{}", por lo que se multiplicara por 3'.format(segmento_tres))
        print('Tu tiro ahora vale {} puntos'.format(tiro_tres))
    elif segmento_tres == 'Dobles':
        tiro_tres = tiro_tres * 2
        print('Tu dardo ha caido en el segmento "{}", por lo que se multiplicara por 2'.format(segmento_tres))
        print('Tu tiro ahora vale {} puntos'.format(tiro_tres))
    else:
        print('Tu dardo ha caido en el segmento "{}", por lo que tu puntaje no cambia'.format(segmento_tres))

elif tiro_tres == 50 or tiro_tres == 25 or tiro_tres == 0:
    if tiro_tres == 50:
        print('Tu dardo ha caido en el centro de la diana, tu puntaje es de {} en tu 3er tiro'.format(tiro_tres))
    elif tiro_tres == 25:
        print('Tu dardo ha caido en el aro interno de la diana, tu puntaje es de {} en tu 3er tiro'.format(tiro_tres))
    else:
        print('Tu dardo no ha dado en el tablero, tu puntaje es de {} en tu 3er tiro'.format(tiro_tres))

#SUMA DE PUNTOS Y RESULTADOS:

suma_puntos = tiro_uno + tiro_dos + tiro_tres
print('Tu puntaje total es de {}'.format(suma_puntos))

if tiro_uno > tiro_dos and tiro_uno > tiro_tres:
    if tiro_dos > tiro_tres:
        mid = tiro_dos
        menor = tiro_tres
    else:
        mid = tiro_tres
        menor = tiro_dos
    may = tiro_uno
    print('Tu mejor tiro fue el numero uno, con un puntaje de {} , tu segundo mejor tiro fue con {} puntos y tu tiro con menor puntje fue {} puntos'.format(may, mid, menor))

elif tiro_dos > tiro_tres:
    if tiro_tres > tiro_uno:
        mid = tiro_tres
        menor = tiro_uno
    else:
        mid = tiro_uno
        menor = tiro_tres
    may = tiro_dos
    print('Tu mejor tiro fue el numero uno, con un puntaje de {} , tu segundo mejor tiro fue con {} puntos y tu tiro con menor puntje fue {} puntos'.format(may, mid, menor))
else:
    if tiro_dos > tiro_uno:
        mid = tiro_dos
        menor = tiro_uno
    else:
        mid = tiro_uno
        menor = tiro_dos
    may = tiro_tres
    print('Tu mejor tiro fue el numero uno, con un puntaje de {} , tu segundo mejor tiro fue con {} puntos y tu tiro con menor puntje fue {} puntos'.format(may, mid, menor))

if suma_puntos <= 10:
    print('{}, mejor dedicate a otra cosa'.format(nombre_jugador))
elif (suma_puntos > 10) and (suma_puntos < 50):
    print('{}, sigue practicando'.format(nombre_jugador))
elif (suma_puntos >= 50) and (suma_puntos < 100):
    print('{}, vas por buen camino'.format(nombre_jugador))
else:
    print('{}, eres un genio!'.format(nombre_jugador))

#FIN DEL PROGRAMA

