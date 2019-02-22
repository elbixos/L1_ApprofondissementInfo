
class Attaque():
    def __init__(self, nom, degats, texte):
        self.nom = nom
        self.degats = degats
        self.texte = texte

    def use(self, user, ennemi, modifier = None):
        if modifier == None :
            modifier = user.force
        if self.isUsable(user) :
            degats = self.degats+modifier
            print (self.texte, ennemi.nom, -(degats), "HP")
            ennemi.recevoirDegats(degats)
            return True
        print ("You cannot use this")
        return False

    def isUsable(self, user):
        return True
