from Perso import *

arene = []

p = Perso("Ra's al Ghul")
arene.append(p)

p = Perso("Ragnar")
arene.append(p)

p = Perso("Link")
arene.append(p)

# Affichage initial
for unGars in arene:
    unGars.afficher()

print ("Bienvenue dans le Thunder Dome")
while len(arene) > 1 :
    print("===========")
    attaquant = random.choice(arene)

    victime = random.choice(arene)
    while victime==attaquant :
        victime = random.choice(arene)

    attaquant.attaquer(victime)

    if not victime.is_alive():
        print("..........")
        print("Arghhhhh, honorez la memoire de ",victime.name)
        arene.remove(victime)

print("======================")
print ("Le vainqueur du trophée des champions est ", arene[0].name)
