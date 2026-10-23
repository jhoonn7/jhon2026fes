###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###



# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = input("Introdueix el nom del tecnic:")
nom_xarxa = input("Introdueix el nom de la xarxa:")

printf(f"El tecnic {nom_tecnic} esta instalant la xarxa {nom_xarxa.}.")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud = float(input("Introdueix la longitud de l'enllaç de la fibra:"))
velocitat= float(input("Introdeuix la velocitat de transmisio:"))

segons = 8/velocitat

print(f"Per transmetre 1 GB de dades necesitem {segons}.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores_feina = float(input("Introdueix el numero d'hores de feina"))
preu_hora = float(input("Introdueix el preu per hora"))
preu_material = float(input("Introdeuix el cost del material"))

cost_total = hores_feina * preu_hora + preu_material

print(f"El cost total de la isntalació es {cost_total}$")