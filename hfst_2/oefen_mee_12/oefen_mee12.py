import json

data = {}
with open("hfst_2\oefen_mee_12\oefen_mee_12.json") as dataFile:
    data = json.load(dataFile)

day = input("Kies een dag: ")
try:
    print(f"Op {input} heb je de volgende activiteiten gepland:")
    for key, value in data.items():
        if key == day:
            if type(value) == list:
                for i in value:
                    print(i)
            else:
                print(value)
            print("")
            edit = input("Wil je deze activiteit wijzigen (j/n)? ")
            if edit == "j":
                new_activity = input("Geef nieuwe activiteit(en) in: ")
                data[day] = new_activity
                print(f"Activiteit op {day} gewijzigd naar {new_activity}")
                with open("hfst_2\oefen_mee_12\oefen_mee_12.json", "w") as file:
                    json.dump(data,file) 
            
except:
    print("Geen geldige dag!")