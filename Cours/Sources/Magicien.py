from Personnage import Personnage
from AttaqueMagique import AttaqueMagique

class Magicien(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.mana = 5
        self.magie = 1
        self.attaques.append(AttaqueMagique("Boule de feu", 5,"Burn, yes you're gonna burn",4))
        self.attaques.append(AttaqueMagique("Eclair", 3,"Zap",3))
