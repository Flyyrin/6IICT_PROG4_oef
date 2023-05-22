import pygame
from particle import BoringParticle
import random
import math

# Constantes.
breedte, hoogte = 600,600
fps = 120
aantal_particles = 200
snelheid = 0.2
dikte = 5

# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((breedte,hoogte))
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.
particles = []  
""" Vul lijst aan... """
for i in range(aantal_particles):
    particles.append(BoringParticle(breedte/2, hoogte/2, snelheid))

running = True
while running:
    # Maak scherm schoon.
    scherm.fill((0,0,0))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(fps)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).
    for particle in particles:
        """ 1. Beweeg particle """
        particle.x = particle.x + (particle.snelheid * interval * math.cos(particle.hoek))
        particle.y = particle.y + (particle.snelheid * interval * math.sin(particle.hoek))

        """ 2. Reset particle """
        if (particle.x - dikte - 10) > breedte or (particle.x + dikte - 10)  < 0 or (particle.y - dikte - 10) > hoogte or (particle.y + dikte - 10)  < 0:
            particle.reset(breedte/2, hoogte/2)
        pygame.draw.circle(scherm, particle.kleur, (particle.x, particle.y), dikte)

    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()