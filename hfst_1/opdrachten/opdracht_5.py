poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

for persoon in poll_talen:
    if favorite_languages.get(persoon):
        print(f"Bedankt voor je deelname {persoon}")
    else:
        print("Gelieven deel te nemen")