boodschappen_lijst = ["appel","doerian","banaan","doerian","appel","kers",
"kers","mango","appel","appel","kers","doerian","banaan",
"appel","appel","appel","appel","banaan","appel"]

"""
Oplossing:
boodschappen_dict = {'appel': 9, 'doerian': 3, 'banaan': 3, 'kers': 3, 'mango': 1}

"""

boodschappen_dict = {}
enkel_lijst = []

for item in boodschappen_lijst:
    if item not in enkel_lijst:
        enkel_lijst.append(item)
    
for item in enkel_lijst:
    boodschappen_dict[item] = (boodschappen_lijst.count(item))

print(boodschappen_dict)
