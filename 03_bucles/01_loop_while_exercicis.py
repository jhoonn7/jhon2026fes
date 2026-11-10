###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

comptador = 10

while comptador >0:
    print(comptador)
    comptador-=1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
suma = 0
comptador = 0
while comptador<= 20:
    if comptador %2 == 0:
        suma = comptador + suma
    comptador +=1

print(suma)
    



# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

refe = 1
comptador = 1
numero = int(input("Introdueix un nombre enter positiu"))

while comptador <= numero:
    refe = refe * comptador
    comptador +=1
print (f"El Factorial de {numero} és {refe}")
    



# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contra = input("Intodueix una contrasenya")
numero = len(contra)
while numero <8:
    print("La contrasenya ha de tenir un minim de 8 caracters")
    contra = input("Torna a introduir una contrasenya")
    numero = len(contra)

print("Contraenya valida")


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

numero = int(input("Introdeuix la taula que vols saber"))
comptador = 1

while comptador <= 10:
    resultat = numero * comptador
    print(f"{numero}x{comptador} = {resultat}")
    comptador += 1


# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.





# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

numero = int(input("Introdueix numeros sencers"))
suma = 0

while numero != 0:
    suma = suma + numero
    numero = int(input("Introdeuix un altre numero"))

print(f"La suma total és {suma}")



# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

numero = int(input("Introdeuix un nombre sencer positiu"))
comptador = 0 

while numero > 0 :
    numero = numero // 10
    comptador +=1 

print (f"El nombre de xifres es {comptador}")






# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

termes = int(input("Introdueix el nombre de termes que vols veure: "))

a = 0
b = 1
comptador = 0

while comptador < termes:
    print(a)

    seguent = a + b

    a = b
    b = seguent

    comptador += 1






# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

secret = 7

usuari = int(input("Adivina el numero"))

while usuari != secret:
    if usuari > secret:
        print ("El numero secret és mes petit")
    else:
        print("El numero secret es mes gran")
    usuari = int(input("Introdeuix un altre numero"))


print("Felcitats! Has encertat el numero secret")