import random
from Attaque import Attaque

class Personnage():
    allAttacks = []
    allAttacks.append(Attaque("baffe", 1,"baffe dans ton nez","all"))
    allAttacks.append(Attaque("kick", 1,"coup de genou dans le bidou","all"))


    def __init__(self, nom):
        self.nom = nom
        self.force = 0
        self.magie = 0
        self.hp = 4
        self.alive = True
        self.type = "paysan"
        self.attaques=[]
        self.getMyAttacks()



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


    def fullPresentation(self):
        print ('=================')
        self.afficher()
        print ("-----------------")
        print ("mes attaques :")
        for at in self.attaques :
            print (at)
        print ("-----------------")

    def isAlive(self):
        return self.alive

    def getMyAttacks(self) :
        self.attaques=[]
        for at in Personnage.allAttacks:
            if at.isForMe(self):
                self.attaques.append(at)
