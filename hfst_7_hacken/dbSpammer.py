import requests
import random

URL = "http://172.16.1.37:8888/register_query.php" 
id = 0

funny_names = ["Sjaak Pindakaas", "Truusje Knalpot", "Henk Flapdrol", "Annie Pannekoek", "Johan Kwijlstra", "Greetje Giechel", "Bertje Bezemsteel", "Miepje Kolderkat", "Keesje Klungel", "Lotte Scheetjes"]
funny_last_names = ["De Boef", "Knots", "Slingerbeen", "Giechelkont", "Brokkenpap", "Floddergans", "Kolderneus", "Bonzelijn", "Pannekoek", "Spring-in-'t-veld"]
funny_numbers = [42, 1337, 8675309, 80085, 123456789, 7777777, 911, 24601, 1234, 9999]
while True:
    id += 1
    data = {
        "employee_id": f"{random.choice(funny_names)}.{random.choice(funny_last_names)}",
        "password": "-",
        "firstname": random.choice(funny_names),
        "lastname": random.choice(funny_last_names),
        "phone_nr": random.choice(funny_numbers),
        "register": ""
    }

    response = requests.post(URL, data=data)
    if "Successfully" in response.text:
        print(f"Succes {id}")
    else:
        print("Error")