###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Encaminador casa"
Ubicacio = "Granollers"
Num_de_ports= 10
estat_encaminador = True

print(f"{nom_encaminador},{Ubicacio},{Num_de_ports}, {estat_encaminador}")



# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.


GB_Inclosos = 100
Gb_consumits =75.9

gb_restants= GB_Inclosos - Gb_consumits

print(f"Dades restants: {gb_restants:.2f} GB")

Gb_consumits = 5
gb_restants= GB_Inclosos - Gb_consumits

print(f"Dades restants depsres de actualitzar : {gb_restants:.2f}GB")