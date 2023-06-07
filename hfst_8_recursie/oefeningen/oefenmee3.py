""" Bepaal de faculteit van een getal met behulp van een while-loop. """

def faculteit(getal):
    waarde = 1
    while getal >= 1:
        waarde = waarde * getal
        getal = getal - 1
    print(waarde)

faculteit(5)