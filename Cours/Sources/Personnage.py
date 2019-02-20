import random

class Personnage():
    def __init__(self, nom):
        self.nom = nom
        self.attaque = 2
        self.hp = 3
        self.alive = True

    def recevoirDegats(self, degats):
        self.hp -= degats
        if self.hp <=0 :
            self.alive = False
            print ("Arghhh, c'est la fin pour moi. Souvenez vous de", self.nom)

    def attaquer(self, perso):
        print ("Subit le courroux de", self.nom, "je vais te fumer ", perso.nom)
        perso.recevoirDegats(self.attaque)

    def afficher(self):
        print ("je suis ", self.nom, "il me reste ", self.hp, "points de vie")

    def isAlive(self):
        return self.alive
