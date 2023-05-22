class Hond:
    def weeg(self, massa):
        self.massa = massa
    
    def benoem(self, naam):
        self.naam = naam
    
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg")

hond = Hond()
hond.benoem("Juul")
hond.weeg(5)
hond.weegschaal()