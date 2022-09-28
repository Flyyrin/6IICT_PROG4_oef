# niveau 1:
puntenlijst = [
    ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], # 1 punt
    ["D", "G"],                                         # 2 punten
    ["B", "C", "M", "P"],                               # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    ["K"],                                              # 5 punten
    ["J", "X"],                                         # 6 punten
    ["Q","Z"]                                           # 7 punten
]

dict = {}
dict2 = {}
for list in puntenlijst:
    dict[puntenlijst.index(list)+1] = list

for waarde, lijst in dict.items():
    for letter in lijst:
        dict2[letter] = waarde

print(dict2)


# niveau 2:
puntenlijst_en = [
    ["A", "E", "I", "O", "U", "L", "N", "S", "T"],      # 1 punt
    ["D", "G", "K"],                                    # 2 punten
    ["B", "M", "P", "Q", "R"],                          # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    [],                                                 # 5 punten
    ["J", "X"],                                         # 6 punten
    ["C","Z"]                                           # 7 punten
]

dict = {}
dict2 = {}
for list in puntenlijst:
    dict[puntenlijst.index(list)+1] = list

for waarde, lijst in dict.items():
    for letter in lijst:
        dict2[letter] = waarde

print(dict2)

# niveau 3:
input = input("Geef Letter: ")

try:
    print(dict2[input])
except:
    print("Ongeldige waarde")