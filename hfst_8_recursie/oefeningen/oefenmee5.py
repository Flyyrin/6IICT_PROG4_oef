""" Niveau 1: los omdraaien van woord recursief op """

def draaiom(woord):
    if woord == "":
        return woord
    else:
        return woord[-1] + draaiom(woord[:-1])

print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI

""" Niveau 2: los omdraaien van woord met while-loops op """

# schrijf een while loop om een woord om te draaien