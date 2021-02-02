import random

class Perso:
    def __init__(self,name):
        self.adjectives =  ["l'alcoolique", "le maigrichon", "le petit"]
        #["the Great", "le fourbe", "le sournois", "le guerrier"]
        self.name = name + " " + random.choice(self.adjectives)
        self.hp = 8 + random.randint(0,2)
        self.attack = 5 +random.randint(0,2)
        self.defense = 5 +random.randint(0,2)
        self.classe = "Perso de base"

        self.liste_attaques = []
        attaque = Attaque("Pal a viré", 2+ random.randint(0,1))
        self.liste_attaques.append(attaque)
        attaque = Attaque("lowkick", 3+ random.randint(0,1))
        self.liste_attaques.append(attaque)

    def afficher(self):
        print("==========")
        print("voici :", self.name )
        print("classe :",self.classe)
        print("points de vie",self.hp)
        print("attaque :",self.attack)
        print("défense :",self.defense)

        print("je sais faire :")
        for a in self.liste_attaques:
            a.afficher()


    def get_attack_score(self):
        return self.attack + random.randint(1,6)

    def get_defense_score(self):
        return self.defense + random.randint(1,6)

    def receive_damages(self, degats):
        self.hp -= degats
        if self.hp <0 :
            self.hp = 0
        print(self.name, "a pris ", degats, "degats et a encore", self.hp, "point de vie")


    def attaquer(self,victime):
        attaque = random.choice(self.liste_attaques)
        print("Tentative de",attaque.nom, "de" ,self.name, "sur", victime.name)

        score_attaque = self.get_attack_score()
        score_defense = victime.get_defense_score()

        if score_attaque > score_defense :
            print("l'attaque de", self.name,"passe")
            victime.receive_damages(attaque.degats)

        else:
            print("belle esquive de ", victime.name)

    def is_alive(self):
        if self.hp <= 0:
            return False
        return True

class Barbare(Perso):

    def __init__(self,name):
        ## Construire un Perso
        super().__init__(name)

        self.hp += 2
        self.adjectives =  ["le barbare", "le terrible", "le destructeur"]
        self.name = name + " " + random.choice(self.adjectives)
        self.classe = "Barbare"

        self.liste_attaques = []
        attaque = Attaque("Coup d'boule')", 4+ random.randint(0,1))
        self.liste_attaques.append(attaque)
        attaque = Attaque("highkick", 5+ random.randint(0,1))
        self.liste_attaques.append(attaque)


class Chevalier(Perso):
    def __init__(self,name):
        ## Construire un Perso
        super().__init__(name)
        self.adjectives =  ["le cuirassé", "le loyal", "le régicide"]
        self.name = name + " " + random.choice(self.adjectives)
        self.armure = 2
        self.classe = "Chevalier"

    def receive_damages(self, degats):
        if self.armure >0 :
            self.armure-=1
            degats_pares = int(degats/2)
            degats_encaisses = degats-degats_pares
            print("l'armure de",self.name,"encaisse",degats_encaisses,"degats")
        else :
            print("plus d'armure, tout dans sa musette")
            degats_encaisses = degats

        super().receive_damages(degats_encaisses)

    def afficher(self):
        super().afficher()
        print("armure :",self.armure)


class Attaque:
    def __init__(self,nom, degats):
        self.nom = nom
        self.degats = degats

    def afficher(self):
        print(self.nom, " degats :",self.degats)
