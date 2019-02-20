from Personnage import Personnage

class Barbare(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.hp = 5
        self.attaque = 4
