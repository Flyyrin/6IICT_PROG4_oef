class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa
    
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")
    
    def wijzig_naam(self, naam):
        print(f"{self.naam} heet nu {naam}")
        self.naam = naam
    
    def eten(self, hoeveelheid):
        for i in range(3):
            self.massa += hoeveelheid*(1/3)
            print(f"{self.naam} weegt nu {self.massa}")
        


hond = Hond("Juul", 5)
hond.weegschaal()
hond.eten(0.5)
hond.weegschaal()