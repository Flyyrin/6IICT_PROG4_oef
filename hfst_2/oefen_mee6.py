import csv

film_kritieken = [
    {"FILM": "Monty Python and the Holy Grail", "SCORE": 8},
    {"FILM": "Monty Python's Life of Brian", "SCORE": 8.5},
    {"FILM": "Monty Python's Meaning of Life", "SCORE": 7}
]
film_header = ["FILM", "SCORE"]

fp = open( "kritieken_to_csv.csv", "w", newline="" )
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=film_header)

csv_writer.writeheader()
for rij in film_kritieken:
    csv_writer.writerow(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar
