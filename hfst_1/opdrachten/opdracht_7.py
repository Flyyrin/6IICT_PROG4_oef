from cProfile import label
import random

land_hoofdstad = { # 10 paren
    "belgie": "brussel",
    "frankrijk": "parijs",
    "nederland": "amsterdam",
    "duitsland": "berlijn",
    "engeland": "londen",
    "spanje": "barcelona",
    "portugal": "lisabon",
    "italie": "rome",
    "luxemburg": "luxemburg",
    "polen": "warschau"
}

score = 0
testing = True

while testing:
    hoeveel = int(input(f"Hoveel vragen wil je max {len(land_hoofdstad)}? "))
    if hoeveel <= len(land_hoofdstad):
        testing = False

for key in random.sample(sorted(land_hoofdstad),k=hoeveel):
    if input(f"Wat is de hoofdstad van {key}? ") == land_hoofdstad[key]:
        score += 1
        print("Goed geantwoord")
    else:
        print("Fout antwoord")

print(f"Je had er {score}/{hoeveel} goed")