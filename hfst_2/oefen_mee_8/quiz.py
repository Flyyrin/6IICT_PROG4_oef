import json

data = {}
with open("hfst_2\oefen_mee_8\quiz.json") as dataFile:
    data = json.load(dataFile)

print(data)

for vak, vragen in data["quiz"].items():
    print(f"Vak: {vak}")
    for vraag, vraaginhoud in vragen.items():
        print(vraaginhoud["vraag"])
        print(vraaginhoud["opties"])
        antwoord = input("Antwoord: ")
        if antwoord == vraaginhoud["antwoord"]:
            print(f"{antwoord} is correct!")
        else:
            print(f'{antwoord} is niet correct. Het correcte antwoord is {vraaginhoud["antwoord"]}')
        print("")