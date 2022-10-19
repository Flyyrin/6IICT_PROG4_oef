import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") 
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []
for rij in csv_reader:
    eruptions_ll.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

list = []
for eruption in eruptions_ll:
    try:
        list.append([eruption[1],eruption[4]])
    except:
        pass

print(list)

# Niveau 2
list = []
for eruption in eruptions_ll:
    try:
        if eruption[1] != "Year":
            list.append([int(eruption[1]),eruption[4]])
        else:
            list.append([eruption[1],eruption[4]])
    except:
        pass