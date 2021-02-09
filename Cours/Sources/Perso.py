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
        tirage = random.randint(1,6)
        score  = self.attack + tirage
        statut = "standard"

        if tirage == 1:
            statut = "fail"

        if tirage == 6:
            statut = "success"

        return score, statut

    def get_defense_score(self):
        return self.defense + random.randint(1,6)

    def receive_damages(self, degats):
        self.hp -= degats
        if self.hp <0 :
            self.hp = 0
        print(self.name, "a pris ", degats, "degats et a encore", self.hp, "point de vie")


    def attaquer(self,victime):

        # Choix d'une attaqie
        attaque = random.choice(self.liste_attaques)
        while not self.is_attack_possible(attaque):
            #print("ATTAQUE IMPOSSIBLE", attaque.nom)
            attaque = random.choice(self.liste_attaques)

        print("Tentative de",attaque.nom, "de" ,self.name, "sur", victime.name)

        score_attaque,statut = self.get_attack_score()

        if statut == "fail":
            print("ECHEC CRITIQUE")
            self.receive_damages(attaque.degats)

        elif statut == "success":
            print("SUCCES CRITIQUE")
            victime.receive_damages(2*attaque.degats)


        else :
            score_defense = victime.get_defense_score()

            if score_attaque > score_defense :
                print("l'attaque de", self.name,"passe")
                victime.receive_damages(attaque.degats)

            else:
                print("belle esquive de ", victime.name)

        # On applique les effets de l'attaque a l'agresseur
        self.apply_effects_on_attacker(attaque)

    def is_alive(self):
        if self.hp <= 0:
            return False
        return True

    def is_attack_possible(self, attaque):
        if attaque.type == "standard":
            return True
        return False

    def apply_effects_on_attacker(self,attaque):
        if attaque.type == "standard":
            pass

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

        attaque = Attaque("coup d'Excalibur", 4+ random.randint(0,1))
        self.liste_attaques.append(attaque)

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

class Magicien(Perso):
    def __init__(self,name):
        super().__init__(name)
        self.adjectives =  ["le Grand", "le Nécromancien"]
        self.name = name + " " + random.choice(self.adjectives)
        self.classe = "Mago"
        self.hp-=2
        self.attack-=1
        self.defense-=1
        self.mana = 8

        attaque = AttaqueMagique("Boule de Feu",7, 6)
        self.liste_attaques.append(attaque)

        attaque = AttaqueMagique("Eclairs de Zardoz",4, 4)
        self.liste_attaques.append(attaque)

    def afficher(self):
        super().afficher()
        print("mana :",self.mana)

    def is_attack_possible(self, attaque):
        #attaque.afficher()

        if attaque.type == "standard":
            return True

        if attaque.type == "magique":
            if self.mana >= attaque.mana :
                return True

        #print("Autres cas")
        return False

    def apply_effects_on_attacker(self,attaque):
        if attaque.type == "magique":
            self.mana -= attaque.mana
            print("Soustraction des points de mana")
            print("reste",self.mana, "pour ",self.name)


class Attaque:
    def __init__(self,nom, degats):
        self.nom = nom
        self.degats = degats
        self.type = "standard"

    def afficher(self):
        print(self.nom, "type :",self.type, "degats :",self.degats)

class AttaqueMagique(Attaque):
    def __init__(self,nom, degats,mana):
        super().__init__(nom,degats)
        self.type = "magique"
        self.mana = mana

    def afficher(self):
        print(self.nom, "type :",self.type, "degats :",self.degats, "cout en mana", self.mana)
