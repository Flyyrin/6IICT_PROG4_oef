""" Niveau 1: los sommatie recursief op """

# def sommatie(getal):
#     waarde = 0
#     while getal >= 1:
#         waarde = waarde + getal
#         getal = getal - 1
#     return waarde

def sommatie(n):
    if n == 1:
        return 1
    
    vorige_faculteit = sommatie( n-1 )
    return n + vorige_faculteit

print( sommatie(1) )   # 1
print( sommatie(2) )   # 3
print( sommatie(3) )   # 6
print( sommatie(4) )   # 10
print( sommatie(5) )   # 15
print( sommatie(100) ) # 5050


""" Niveau 2: los sommatie met while-loops op """