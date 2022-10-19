import json

data = {}
with open("hfst_2\oefen_mee_8\oefen_mee_8.json") as dataFile:
    data = json.load(dataFile)

input = input("Kies een dag: ")
try:
    print(f"Op {input} heb je de volgende activiteiten gepland:")
    for key, value in data.items():
        if key == input:
            if type(value) == list:
                for i in value:
                    print(i)
            else:
                print(value)
except:
    print("Dag niet in agenda!")