import random
class BoringParticle:
    def __init__(self, x, y, snelheid):
        self.x = x
        self.y = y
        self.snelheid = snelheid
        self.hoek = random.randint(0, 360)
        self.kleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    def reset(self, x, y):
        self.x = x
        self.y = y
        self.hoek = random.randint(0, 360)
        self.kleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))