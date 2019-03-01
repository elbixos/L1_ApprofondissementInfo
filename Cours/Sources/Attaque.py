
class Attaque():
    def __init__(self, nom, degats, texte,userType= "all"):
        self.nom = nom
        self.degats = degats
        self.texte = texte
        self.userTypes = [userType]

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
        if self.isForMe(user):
            return True
        return False

    def isForMe(self, user):
        if ("all" in self.userTypes) or (user.type in self.userTypes):
            return True
        return False

    def __str__(self):
        return self.nom + " utilisable par " + str(self.userTypes) + " degats : " +str(self.degats)
