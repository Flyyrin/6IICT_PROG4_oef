import requests, json

client_id = "7511999c73b54ce4a2f90026229c7991"
client_secret = "c090f5c5d2d34e0185f09c8fdc2c8feb"

# Herinner je dat een API gewoon een speciale URL is...
# Via deze URL kunnen we ons inlogtoken aanvragen.
url = 'https://accounts.spotify.com/api/token'

# Deze zaken moeten we de API geven om een inlogtoken te genereren.
inloggegevens = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# requests het inlogtoken, haal de tekst uit deze request en zet in cred_response
cred_resp = requests.post(url, inloggegevens).text
# Opgelet! Onderstaande regel is BELANGRIJK. 
cred_resp = json.loads(cred_resp)

print(cred_resp)

""" Oefen mee 2: 
zet de dictionary cred_resp in JSON-bestand met de naam certificatie.json

"""