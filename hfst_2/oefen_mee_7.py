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
    dict = {}
    try:
        if eruption[1] != "Year":
            dict["Year"] = int(eruption[1])
            dict["Name"] = eruption[4]
            list.append(dict)
    except:
        pass

header = ["Year", "Name"]

fp = open( "vulcanenLD.csv", "w", newline="" )
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=header)
csv_writer.writeheader()
for rij in list:
    csv_writer.writerow(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar


fp = open( "vulcanenLL.csv", "w", newline="")

list = []
list = []
for eruption in eruptions_ll:
    try:
        if eruption[1] != "Year":
            list.append([int(eruption[1]),eruption[4]])
        else:
            list.append([eruption[1],eruption[4]])
    except:
        pass

csv_writer = csv.writer( fp , delimiter=";")
for listi in list:
    csv_writer.writerow( [listi[0],listi[1]] )

fp.close()