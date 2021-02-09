from Perso import *

def virer_morts(arene):
    new_arene = []
    for p in arene :
        if not p.is_alive():
            print("..........")
            print("Arghhhhh, honorez la memoire de ",p.name)
        else :
            new_arene.append(p)

    return new_arene

arene = []

p = Barbare("Ra's al Ghul")
arene.append(p)

p = Perso("Ragnar")
arene.append(p)

p = Chevalier("Link")
arene.append(p)

p = Magicien("Merlin")
arene.append(p)

p = Magicien("Dumbledore")
arene.append(p)

p = Barbare("Dar Umbra")
arene.append(p)

# Affichage initial
for unGars in arene:
    unGars.afficher()

print("\n===========")
print("===========")
print ("Bienvenue dans le Thunder Dome")

while len(arene) > 1 :
    print("===========")
    attaquant = random.choice(arene)

    victime = random.choice(arene)
    while victime==attaquant :
        victime = random.choice(arene)

    attaquant.attaquer(victime)

    arene = virer_morts(arene)

print("======================")
print ("Le vainqueur du trophée des champions est :")
arene[0].afficher()
