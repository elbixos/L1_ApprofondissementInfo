from Personnage import Personnage
from Barbare import Barbare
from Magicien import Magicien
import random

def nettoyer(listePerso):
    newList = []
    for p in listePerso:
        if p.isAlive():
            newList.append(p)

    return(newList)

def afficher(listePerso, turn):
    print ("======Tour ",turn, "===========")
    for p in listePerso:
        p.afficher()
    print()

assemblee = []

p = Personnage("Popaul the farmer")
assemblee.append(p)
p = Magicien("Mandrix the Great")
assemblee.append(p)
p = Barbare("Cohen the Barbarian")
assemblee.append(p)

turn = 0


while (len(assemblee) > 1):
    turn +=1
    afficher(assemblee, turn)
    # Selection de 2 joueurs au hasard.
    twoGuys = random.sample(assemblee,2)

    # Le premier attaque le second.
    twoGuys[0].attaquer(twoGuys[1])
    assemblee = nettoyer(assemblee)

print()
print ("================")
print ("Vainqueur : ", assemblee[0].nom)
