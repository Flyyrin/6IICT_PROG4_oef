""" Niveau 1 & 2
Wat gaat hier mis?
IndexError omdat de gegeven index niet betaat in de lijst
"""
fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]

def addFruit():
    fruit = input("Element aan lijst toevoegen: ")
        
    if fruit == "":
        return # Loop stopt wanneer gebruiker een lege string ingeeft.
    else:
        fruit_lijst.append(fruit)
        return

while True:
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )
    for i in range(getal):
        try:
            fruit = fruit_lijst[i]
            print(fruit)
        except:
            pass
    addFruit()