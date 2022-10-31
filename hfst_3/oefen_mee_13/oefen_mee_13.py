import json

data = []
with open("hfst_3\oefen_mee_13\oefen_mee_13.json") as dataFile:
    data = json.load(dataFile)

for index, report in enumerate(data):
    datum = report["Date"]
    aantal_vandaag = report["Cases"]
    if index:
        nieuwe_besmettingen = data[index]["Cases"] - data[index-1]["Cases"]
    else:
        nieuwe_besmettingen = 0
    print(f'{datum} waren er {nieuwe_besmettingen} nieuwe coronagevallen')
    data[index]["New Cases"] = nieuwe_besmettingen

print(data)

with open("hfst_3\oefen_mee_13\oefen_mee_13_2.json", "w") as file:
    json.dump(data,file)

