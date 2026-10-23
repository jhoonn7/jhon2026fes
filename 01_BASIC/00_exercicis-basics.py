###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Jhon Pinzon \nGranollers")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print("a;",type(a))
print("b;",type(b))
print("c;",type(c))
print("d;",type(d))
print("e;",type(e))

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

numero = "12345"
numero_enter = int(numero)
print(numero_enter)
numero_float = float(numero_enter)
print(numero_float)
num = 3.99
num_sencer = int(num)
print(num_sencer)

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí

nom = "Jhon"
edat = 19
altura = 195

print(f"Em dic {nom}, tinc {edat}anys i faig {altura} metres")



print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

resultat = int(round(3.1416)/2)
print("",resultat)



print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temperatura = float(input("Introdueix la temperatura en graus Celsius."))
farenhait=(temperatura*9/5)+32
print(f"La temperatura en celsius es {temperatura}ºC y en fareinhait es {farenhait}F")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

compte = float(input("Introdueix l'import del compte:"))
percentatge = float(input("Introdueix el porcentatge de propina:"))

propina = compte * percentatge / 100
compte_tot = compte + propina
print(f"L'import de la propina es {propina:.2f} euros")
printf(f"L'import total que s'ha de pagar es de {compte_tot:.2f} euros")


print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

contra = input("Introdueix la contranenya desitjada:")
if len(contra)>=8:
    print("Contrasenya valida")

else :
    print("Contrasenya invalida")


