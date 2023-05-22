class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa
    
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")

hond = Hond("Juul", 5)
hond.weegschaal()