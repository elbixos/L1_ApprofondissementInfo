import random
from Attaque import Attaque

class Personnage():
    def __init__(self, nom):
        self.nom = nom
        self.force = 0
        self.hp = 4
        self.alive = True
        self.attaques=[]
        self.attaques.append(Attaque("baffe", 1,"baffe dans ton nez"))
        self.attaques.append(Attaque("kick", 1,"coup de genou dans le bidou"))

    def recevoirDegats(self, degats):
        self.hp -= degats
        if self.hp <=0 :
            self.alive = False
            print ("Arghhh, c'est la fin pour moi. Souvenez vous de", self.nom)

    def attaquer(self, perso):
        print ("Fear",self.nom)

        canUseAttack = False
        while canUseAttack == False :
            at = random.choice(self.attaques)
            canUseAttack = at.isUsable(self)

        at.use(self, perso)

    def afficher(self):
        print ("je suis ", self.nom, "il me reste ", self.hp, "points de vie")

    def isAlive(self):
        return self.alive
