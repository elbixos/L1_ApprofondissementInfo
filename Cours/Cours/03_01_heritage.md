
## Troisième Cours : L'héritage

Tout ceci n'est pas bien compliqué, c'est la mise en oeuvre intelligente de tout
ceci dans des cas réels de programmation qui demande reflexion. Pour vous
expliquer les concepts, je vais prendre des exemples simples.

Il s'agit ici de créer un micro jeu d'aventures, de type jeu de rôles, mettant
en jeu des magiciens, des barbares...

Nous avons donc des personnages qui ont des points de vie, qui peuvent attaquer
et prendre des dégâts. Comme nous avons bien compris l'intérêt de la POO pour ce genre de cas, nous allons créer une classe Personnage.

Dans le cours, j'ai repris tout ce qui suit avec des petites modifs.
Le code final est disponible ici :
- le fichier des classes : [Perso.py](../Sources/Perso.py)
- le programme principal : [AreneV2.py](../Sources/AreneV2.py)

Ce qui suit est une explication détaillée du principe, les fichiers ci-dessus
font un peu plus, ou un peu différemment.

### La classe Personnage

```python
class Personnage():
    def __init__(self, nom):
        self.nom = nom
        self.attaque = 2
        self.hp = 3
        self.alive = True

    def recevoirDegats(self, degats):
        self.hp -= degats
        if self.hp <=0 :
            self.alive = False
            print ("Arghhh, c'est la fin pour moi. Souvenez vous de", self.nom)

    def attaquer(self, perso):
        print ("Subit le courroux de", self.nom, "je vais te fumer ", perso.nom)
        perso.recevoirDegats(self.attaque)

    def afficher(self):
        print ("je suis ", self.nom, "il me reste ", self.hp, "points de vie")

    def isAlive(self):
        return self.alive
```

Nous allons aussi avoir un programme principal qui utilise cette classe :
1. le programme crée un tableau de personnages.
2. Tant qu'il reste plus d'un personnage en piste :
  1. on affiche les joueurs en lice.
  2. on en tire 2 au sort.
  3. le premier attaque le second.
  4. on vire les morts.
3. on affiche le vainqueur

```python
import random

def nettoyer(listePerso):
    newList = []
    for p in listePerso:
        if p.isAlive():
            newList.append(p)

    return(newList)

def afficher(listePerso, turn):
    print ("======Tour ",turn, "===========")
    for p in listePerso:
        p.afficher()
    print()

assemblee = []

p = Personnage("Popaul the farmer")
assemblee.append(p)
p = Personnage("Mandrix the Great")
assemblee.append(p)
p = Personnage("Cohen the Barbarian")
assemblee.append(p)

turn = 0


while (len(assemblee) > 1):
    turn +=1
    afficher(assemblee, turn)
    # Selection de 2 joueurs au hasard.
    twoGuys = random.sample(assemblee,2)

    # Le premier attaque le second.
    twoGuys[0].attaquer(twoGuys[1])
    assemblee = nettoyer(assemblee)

print()
print ("================")
print ("Vainqueur : ", assemblee[0].nom)
```

### Le Barbare
Nous souhaiterions maintenant ajouter des types de personnages.
Par exemple, un personnage pourrait être, soit un magicien, soit un barbare.
Le barbare est un personnage un peu plus costaud.

Nous aimerions conserver tout ce qui a été fait pour les personnages, en modifiant
ce dont nous avons besoin.

La classe Barbare va hériter de la classe Personnage : un objet de type Barbare
aura automatiquement les mêmes attributs et méthodes que la classe Personnage.
Gardez ceci en tête : on peut vouloir que Barbare hérite de Personnage car un
Barbare est un Personnage. En revanche, un Personnage n'est pas un Barbare.

La classe dérivée est une version spécialisée de la classe **Parente**.

Créons donc un fichier *Barbare.py* contenant les lignes suivantes :

```python
class Barbare(Personnage):
  pass
```

Notre programme principal a été a peine modifié :
Nous avons ajouté cette ligne en haut
```python
from Barbare import Barbare
```

Nous avons modifié la création du personnage de *Cohen*.
```python
p = Personnage("Cohen the Barbarian")
```


Que s'est il passé ? Quand je demande la création d'un Barbare, comme la classe Barbare ne propose pas de constructeur, Python appelle automatiquement la méthode *__init__* de la classe parente

Bon, mais si l'on veut améliorer un peu notre barbare, nous allons lui créer son propre constructeur.

```python
from Personnage import Personnage

class Barbare(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.hp = 5
        self.attaque = 4
```
Executez votre programme principal, et notez que le barbare est plus costaud qu'avant.

Explications :
- Quand on crée un Barbare, python cherche une méthode *__init__*.
Comme il en trouve une dans la classe Barbare, il l'applique.
- Comme nous voulons en fait créer un Personnage, nous appelons explicitement le
constructeur de cette classe. Notez bien comment j'apppelle le constructeur de
la classe Personnage en lui passant *self*.
- Nous modifions les paramètres qui nous intéressent


### Le Magicien

Nous voulons créer un magicien qui est aussi un personnage.
Nous voudrions qu'un magicien dispose d'une réserve de magie (mana).
Si cette réserve est suffisamment grande, il peut lancer une boule de feu.
Ici, notre nouvelle classe va donc avoir un nouvel attribut par rapport
à la classe Personnage.

Nous allons également lui créer une méthode bouleDeFeu.
```python
from Personnage import Personnage

class Magicien(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.mana = 5
        self.attaqueBdF = 8

    def bouleDeFeu(self, perso):
        if self.mana >= 5 :
            print ("boule de feu dans ta face ",
            perso.nom)
            perso.recevoirDegats(self.attaqueBdF)
            self.mana -= 4
        else :
            print("Heu, non rien")
```
je pourrais utiliser cela comme suit :
```python
from Personnage import Personnage
from Barbare import Barbare
from Magicien import Magicien

magicMike = Magicien("Mike the Great")
bill = Personnage("Bill the not so great")

magicMike.bouleDeFeu(bigBill)
```
mais c'est délicat de modifier le programme principal précédent pour bénéficier de la boule de feu.
Nous allons donc **redéfinir** la méthode *attaquer* de la classe *Personnage*
dans la classe *Magicien*.

```python
from Personnage import Personnage

class Magicien(Personnage):
    def __init__(self,nom):
        # je crée un personnage
        Personnage.__init__(self,nom)

        # je modifie ce qui m'intéresse
        self.mana = 5
        self.attaqueBdF = 8

    def bouleDeFeu(self, perso):
        if self.mana >= 5 :
            print ("boule de feu dans ta face", perso.nom)
            perso.recevoirDegats(self.attaqueBdF)
            self.mana -= 4
        else :
            print("Heu, non rien")

    def attaquer(self, perso):
        if self.mana >= 5 :
            self.bouleDeFeu(perso)
        else :
            Personnage.attaquer(self,perso)

```
Du coup, notre programme principal n'a plus besoin que d'utiliser la fonction
*attaquer*. C'est le Personnage (ici, le magicien) qui choisit une méthode adaptée. Nous conservons donc le programme initial à ceci prêt que *Mandrix The Great* est maintenant officiellement un magicien.


```python
```python
import random

def nettoyer(listePerso):
    newList = []
    for p in listePerso:
        if p.isAlive():
            newList.append(p)

    return(newList)

def afficher(listePerso, turn):
    print ("======Tour ",turn, "===========")
    for p in listePerso:
        p.afficher()
    print()

assemblee = []

p = Personnage("Popaul the farmer")
assemblee.append(p)
p = Personnage("Mandrix the Great")
assemblee.append(p)
p = Personnage("Cohen the Barbarian")
assemblee.append(p)

turn = 0


while (len(assemblee) > 1):
    turn +=1
    afficher(assemblee, turn)
    # Selection de 2 joueurs au hasard.
    twoGuys = random.sample(assemblee,2)

    # Le premier attaque le second.
    twoGuys[0].attaquer(twoGuys[1])
    assemblee = nettoyer(assemblee)

print()
print ("================")
print ("Vainqueur : ", assemblee[0].nom)
```


Cette notion de **redéfinition** est primordiale en POO. Que fait python à l'appel de la fonction attaquer ? Il cherche dans la classe la plus en bas de l'arbre d'héritage (le plus près de l'objet) si elle propose une méthode *attaquer*. Si oui, il l'applique. Sinon, il regarde si son parent le plus proche en propose une. Si oui, il l'applique. Et ainsi de suite.

De la même façon que les fonctions avaient souvent pour objectif de déplacer
la difficulté hors du programme principal, avec les objets, nous pouvons
déplacer la difficulté dans les classes. Le mécanisme de redéfinition permet
d'adapter nos fonctions à nos objets de façon très précise.

Le programmeur qui utilise nos classes n'a souvent aucune idée de la façon dont
les choses sont implémentées. Il n'a besoin que de documentation sur l'utilisation des objets.

### Les héritages multiples

En voulant aller plus loin, nous pourrions avoir envie d'avoir différentes races
(Humains, Orcs, Trolls, ...). On pourrait alors créer une classe Orc,
et une classe MagicienOrc qui est à la fois un Magicien et un Orc.

On parle alors d'héritage multiple. Mon conseil sera simple :
pour le moment évitez ça.
- beaucoup de langages ne tolèrent pas l'héritage multiple
- Si vous en avez besoin, c'est souvent car votre design est mal conçu.
- Cela va peut être poser des problèmes que vous ne maitrisez pas encore.

Ca viendra.
