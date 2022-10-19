import csv 

fp = open( "volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.reader( fp , delimiter=";")

for rij in csv_reader:
    print(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar