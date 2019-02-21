from Attaque import Attaque

class AttaqueMagique(Attaque):
    def __init__(self, nom, degats, texte,coutMana):
        Attaque.__init__(self,nom, degats,texte)
        self.coutMana = degats

    def use(self, user, ennemi):
        Attaque.use(self,user, ennemi)
        user.mana -= self.coutMana

    def isUsable(self, perso):
        if perso.mana >= self.coutMana:
            return True
        return False
