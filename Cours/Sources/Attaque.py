
class Attaque():
    def __init__(self, nom, degats, texte):
        self.nom = nom
        self.degats = degats
        self.texte = texte

    def use(self, user, ennemi):
        if self.isUsable(user) :
            print (self.texte, ennemi.nom, -(self.degats+user.force), "HP")
            ennemi.recevoirDegats(self.degats+user.force)
            return True
        print ("You cannot use this")
        return False

    def isUsable(self, user):
        return True
