import random

class Perso:
    def __init__(self,name):
        self.adjectives =  ["l'alcoolique", "le maigrichon", "le petit"]
        #["the Great", "le fourbe", "le sournois", "le guerrier"]
        self.name = name + " " + random.choice(self.adjectives)
        self.hp = 8 + random.randint(0,2)
        self.attack = 5 +random.randint(0,2)
        self.defense = 5 +random.randint(0,2)
        self.degats = 2 + random.randint(0,1)

    def afficher(self):
        print("==========")
        print("voici :", self.name )
        print("points de vie",self.hp)
        print("attaque :",self.attack)
        print("défense :",self.defense)
        print("degats :",self.degats)

    def get_attack_score(self):
        return self.attack + random.randint(1,6)

    def get_defense_score(self):
        return self.defense + random.randint(1,6)

    def receive_damages(self, degats):
        self.hp -= degats
        print(self.name, "a pris ", degats, "degats et a encore", self.hp, "point de vie")


    def attaquer(self,victime):
        print("ATTAQUE ", "de" ,self.name, "sur", victime.name)
        score_attaque = self.get_attack_score()
        score_defense = victime.get_defense_score()

        if score_attaque > score_defense :
            print("l'attaque de", self.name,"passe")
            victime.receive_damages(self.degats)

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
        self.degats += 2
        self.adjectives =  ["le barbare", "le terrible", "le destructeur"]
        self.name = name + " " + random.choice(self.adjectives)
