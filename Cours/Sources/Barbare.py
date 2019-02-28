from Personnage import Personnage
from Attaque import Attaque


class Barbare(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.hp = 6
        self.force = 2

        self.attaques.append(Attaque("Grosse taloche", 2,"Grosse taloche sur eut' bouche"))
        self.attaques.append(Attaque("Coup de boule", 3,"Coup de boule in ze face"))
