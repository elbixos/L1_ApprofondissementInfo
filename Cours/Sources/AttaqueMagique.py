from Attaque import Attaque

class AttaqueMagique(Attaque):
    def __init__(self, nom, degats, texte,coutMana,userType="magicien"):
        Attaque.__init__(self,nom, degats,texte,userType)
        self.coutMana = degats

    def use(self, user, ennemi):
        if Attaque.use(self,user, ennemi, modifier = user.magie) :
          user.mana -= self.coutMana


    def isUsable(self, perso):
        if Attaque.isUsable(self,perso) :
            if perso.mana >= self.coutMana:
                return True
        return False
