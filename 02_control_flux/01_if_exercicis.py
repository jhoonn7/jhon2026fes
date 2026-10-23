###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

n1 = int(input("Introdueix el primer nombre"))
n2 = int(input("Introdueix el segon nombre"))

if n1 > n2:
   print(f"{n1} es més gran que {n2}")
elif n1 == n2:
   print(f"{n1} i {n2} son iguals")
else: 
   print(f"{n1} és més petit que {n2}")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

n1 = int(input("Introdueix el Primer nombre"))
n2 = int(input("Introdeuix el segon nombre"))
operació = input("Introdueix l'operació")


if operació == '+':
   resultat = n1+n2
   print(f"El resultat de l'operació es {resultat}.")

elif operació == '-':
   resultat = n1-n2
   print(f"El resultat de l'operació es {resultat}.")

elif operació == '*':
   resultat = n1*n2
   print(f"El resultat de l'operació es {resultat}.")


elif operació == '/' :
   if n2!=0:
      resultat = n1/n2
      print(f"El resultat de l'operació es {resultat}.")

   else:
      print("No es pot dividir entre zero")
else:
   print("OPeració no valida")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any_cl = input("Introdueix l'any que vols q estudiem")

if any % 400 == 0:
   print("es de traspas")
elif any % 100 == 0:
   print("No es de traspas")
elif  any % 4 ==0:
   print("Es un any de traspas")
else:
   printf("No és un any de traspas")

   
# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Intodueix una edat"))
if edat < 0:
   print("Edat no valida")
elif edat>=0 and edat<3:
   print("Es un bebe")
elif edat > 2 and edat < 13:
   print("Es un menol")
elif edat > 12 and edat < 18:
   print("Es un adolescent")
elif edat > 17 and edat < 65:
   print("ES un adult")
else:
   print("Es una persona gran")



# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble



# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
pot_op = float(input("Introdeuix la potencia optica en dBm"))

if pot_op < -27:
   print("Nivell baix")
elif pot_op > -8:
   print("Nivell alt")
else:
   print("Nivell aceptable")


# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.


consum = float(input("Introdeuix el consum de dades"))
if consum < 0:
   print("Dada no valida")
elif consum < = 20:
   print(f"Has consumit {consum} Gb")
else:
   consum_ad = consum - 20
   print(f"Has consumit {consum} gb i {consum_ad} gb adicionals")







# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("Introdueix l'estas de l'indicador LOS (s/n): ").strip() .lower()

indicadorinternet = input("Introdueix l'estas de l'indicador Internet (s/n):").strip() .lower()

if los == "s":
   print("Cal revisar el cable de la fibra")
elif indicadorinternet != "s":
   print("Cal comprobar el servei del proveidor")
else:
   printf("FUnciona correctament")


# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = int(input("Introdeuix el percentatge de bateria"))
if bateria>100 or bateria <0:
   print("ERROR")
elif bateria <20:
   print("Nivell Crític")
elif bateria >=20 and bateria<50:
   print("Nivell baix")
else:
   print("Suficient")




# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte_actiu = input("El compte esta actiu? (s/n): ").strip() .lower()
contra = input("Contrasenya correcte? (s/n): ").strip() .lower()
if compte_actiu != "s":
   print("Accès denegat, compte inactiu")
elif contra != "s":
   print("COntrasenya Incorrecta")
else:
   codi = input("El codi de verificació es correcte? (s/n)").strip() .lower()
   if codi !="s":
      print("Codi Incorrecte")
   else:
      print("Accés permes")
   

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
