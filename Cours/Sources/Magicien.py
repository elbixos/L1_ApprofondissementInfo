from Personnage import Personnage
from AttaqueMagique import AttaqueMagique

class Magicien(Personnage):
    Personnage.allAttacks.append(AttaqueMagique("Boule de feu", 5,"Burn, yes you're gonna burn",4,"magicien"))
    Personnage.allAttacks.append(AttaqueMagique("Eclair", 3,"Zap",3,"magicien"))

    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.mana = 5
        self.magie = 1
        self.type = "magicien"

        self.getMyAttacks()
