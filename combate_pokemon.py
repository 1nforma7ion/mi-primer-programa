pokemon_elegido = input("¿contra que pokemon quieres pelear? (squirtle / charmander / bulbasaur):  ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

#pokemon a elegir
if pokemon_elegido == "squirtle":
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "bulbasaur"
    ataque_pokemon = 10

#elegimos el ataque
while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("que ataques quieres usar? (chispaso / bola voltio):  ")

    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "bola voltio":
        vida_enemigo -= 12

    print("la vida del {} es de {}".format(pokemon_elegido, vida_enemigo))

#enemigo ataca
    print("{} te hace un ataque de {}".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("la vida de pikachu es de {}".format(vida_pikachu))

#resultado
if vida_pikachu <= 0:
    print("has perdido!")
elif vida_enemigo <= 0:
    print("has ganado!")




print("el combate ha termiando")

