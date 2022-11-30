fruit_lijst = ["Appel", "Banaan", "Kers"]

getal = input( "Geef een getal: " )
if "." in getal:
    getal = float( getal )
else:
    getal = int( getal )
try:
    print( fruit_lijst[getal] )
except IndexError:
    print("Niet in lijst")

print("Programma klaar")  
