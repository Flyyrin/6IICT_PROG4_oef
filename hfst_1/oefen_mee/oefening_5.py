""" 
Voorbeeld:

>>> input() = "Dit is een zin"
>>> Dict    = {"Dit": "tiD", "is": "si", "een": "nee", "zin": "niz"}

Tip: je hebt al in de reeksen gezien hoe een woord om te keren.
"""

zin = input("Geef een zin op: ").split(" ")
dict = {}

for woord in zin:
    dict[woord] = woord[::-1]

print(dict)