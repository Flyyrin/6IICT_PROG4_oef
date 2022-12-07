""" Algemeen (gaat over oefening 1 en 2): (  / 2)
Schrijf bij iedere regel code commentaar (  / 1)
Zorg dat de code geen geeft foutmeldingen (  / 1)
    Opgelet! Code in commentaar wordt niet bekeken.
"""

""" OEFENING 1: (  / 5)
oefening1.json bevat info over Warren Buffett.
Dit is een zeer bekende investeerder.
"""

""" STAP 1: (  / 1)
laad oefening1.json in Python. Zet deze dictionary in een variabele.
Gebruik voor beide delen de JSON-module van Python.

Lukt dit niet? Dan mag je de dictionary rechtstreeks in de variabele plakken.
Je krijgt dan wel geen punten voor dit onderdeel.
"""



""" STAP 2: (  / 1)
print volgende zaken van Warren Buffett in een grote f-string:
    - voornaam
    - geboortedatum
    - bedrijf
    - 1 hobby (bvb. deze op index 3)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).

De print kan er als volgt uit zien:
Warren is geboren op 03-08-1930. Hij is de eigenaar van Berkshire Hathaway. Hiernaast speelt hij ook ukelele.
"""



""" STAP 3: (  / 2)
Gebruik code om het minimale en maximale vermogen in de laatste 5 jaar (2017-2021) te bepalen.
Ook als de cijfers van het vermogen zouden wijzigen, moet de code blijven werken.
    Tip: je kan de functies min() en max() toepassen op lijsten. Dit geeft de kleinste/grootste waarde terug.

Lukt dit niet? Dan mag je het minimale en maximale vermogen zelf bepalen.
               Je krijgt dan wel slechts een deel van de punten voor dit onderdeel

Voeg dit minimale en maximale vermogen toe als value aan de hoofddictionary. 
Gebruik hiervoor de keys verm_min en verm_max.
"""

""" STAP 4: (  / 1)
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld oefening1_resultaat.json .
"""

# Stap 1
import json                                                     # Importeer json module
with open("toetsen/07-12-22/oefening1.json", "r") as jsonFile:  # open het json bestand in read modes als jsonFile
    dict = json.load(jsonFile)                                  # variabe dict is jsonFile omgezet naar een dict met json.load

# Stap 2
# \/ print een f-string met waardes uit dict \/
print(f"{dict['voornaam']} is geboren op {dict['geboortedatum']}. Hij is de eigenaar van {dict['bedrijf']}. Hiernaast speelt hij ook {dict['hobbys'][3]}.")

# Stap 3
vermogens = []                                          # maak een lege lijst genaamd vermogens
for vermogen in dict["vermogen_in_miljard"].values():   # voor vermogen in de values van de key "vermogen_in_miljard" in dict
    vermogens.append(vermogen)                          # voeg vermogen toe aan de lijst vermogens

verm_min = min(vermogens)       # verm_min is het minimum van vermogens
verm_max = max(vermogens)       # verm_max is het maximum van vermogens
dict["verm_min"] = verm_min     # key "verm_min" in dict is gelijk aan verm_min
dict["verm_max"] = verm_max     # key "verm_max" in dict is gelijk aan verm_max

# Stap 4
with open("toetsen/07-12-22/oefening1_resultaat.json", "w") as newJsonFile: # open het nieuwe json bestand in write modes als newJsonFile
    json.dump(dict, newJsonFile, indent= 4)                                 # Schrijf dict naar de newJsonFile met json.dump met indents van 4