quiere_helado = input("¿quieres helado? (si/no): ").upper()
tienes_dinero = input("¿tienes dinero? (si/no): ").upper()
vendedor = input("¿esta el vendedor? (si/no): ").upper()
tu_tia = input("¿estas con tu tia? (si/no): ").upper()

te_apetece_helado = quiere_helado == "SI"
puedes_pagarlo = tienes_dinero == "SI" or tu_tia == "SI"
esta_el_vendedor = vendedor == "SI"



if te_apetece_helado and puedes_pagarlo and esta_el_vendedor:
    print("comete un helado")
else:
    print("pues no comas el helado")