from Personnage import Personnage

class Magicien(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.mana = 5
        self.attaqueBdF = 8

    def bouleDeFeu(self, perso):
        if self.mana >= 5 :
            print ("boule de feu dans ta face", perso.nom)
            perso.recevoirDegats(self.attaqueBdF)
            self.mana -= 4
        else :
            print("Heu, non rien")

    def attaquer(self, perso):
        if self.mana >= 5 :
            self.bouleDeFeu(perso)
        else :
            Personnage.attaquer(self,perso)
