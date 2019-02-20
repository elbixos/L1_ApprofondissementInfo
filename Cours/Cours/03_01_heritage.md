
## Troisième Cours : L'héritage

Tout ceci n'est pas bien compliqué, c'est la mise en oeuvre intelligente de tout
ceci dans des cas réels de programmation qui demande reflexion. Pour vous
expliquer les concepts, je vais prendre des exemples simples.

Cet exemple est complètement pompé sur un cours qui parle de php et disponible à
l'adresse suivante :  
[https://openclassrooms.com/fr/courses/1665806-programmez-en-oriente-objet-en-php](https://openclassrooms.com/fr/courses/1665806-programmez-en-oriente-objet-en-php)

Il s'agit donc de créer un micro jeu d'aventures, de type jeu de rôles, mettant
en jeu des magiciens, des barbares...

Nous avons donc des personnages qui ont des points de vie, qui peuvent attaquer
et prendre des dégâts. Comme nous avons bien compris l'intérêt de la POO pour ce genre de cas, nous allons créer une classe Personnage.

### La classe Personnage

```python
class Personnage():
    def __init__(self, nom):
        self.nom = nom
        self.attaque = 2
        self.hp = 3

    def recevoirDegats(self, degats):
        self.hp -= degats
        if self.hp <=0 :
            print ("Arghhh, c'est la fin pour moi. Souvenez vous de", self.nom)

    def attaquer(self, perso):
        print ("Subit le courroux de", self.nom, "je vais te fumer ", perso.nom)
        perso.recevoirDegats(self.attaque)

    def afficher(self):
        print ("je suis ", self.nom, "il me reste ", self.hp, "points de vie")
```

Nous allons aussi avoir un programme principal qui utilise cette classe :

```python
from Personnage import Personnage

magicMike = Personnage("Mike the Great")

bigBill = Personnage("Bill theBarbarian")

magicMike.afficher()
bigBill.afficher()

magicMike.attaquer(bigBill)

magicMike.afficher()
bigBill.afficher()

bigBill.attaquer(magicMike)
bigBill.attaquer(magicMike)

magicMike.afficher()
bigBill.afficher()
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

```python
class Barbare(Personnage):
  pass
```
Notre programme principal a été a peine modifié.
```python
from Personnage import Personnage
from Barbare import Barbare

magicMike = Personnage("Mike the Great")

bigBill = Barbare("Bill theBarbarian")

magicMike.afficher()
bigBill.afficher()

magicMike.attaquer(bigBill)

magicMike.afficher()
bigBill.afficher()

bigBill.attaquer(magicMike)
bigBill.attaquer(magicMike)

magicMike.afficher()
bigBill.afficher()
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
Executez votre programme principal, et notez que Mike est mort prématurément maintenant.

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
            print ("Subit le courroux de", self.nom, ", boule de feu dans ta face",
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

bigBill = Barbare("Bill theBarbarian")

magicMike.afficher()
bigBill.afficher()

magicMike.bouleDeFeu(bigBill)

magicMike.afficher()
bigBill.afficher()
```
mais c'est dommage d'avoir du modifier le programme principal pour béneficier de la boule de feu.
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
*attaquer*. C'est le Personnage (ici, le magicien) qui choisit une méthode adaptée.
```python
from Personnage import Personnage
from Barbare import Barbare
from Magicien import Magicien

magicMike = Magicien("Mike the Great")

bigBill = Barbare("Bill the Barbarian")

magicMike.afficher()
bigBill.afficher()

magicMike.attaquer(bigBill)

magicMike.afficher()
bigBill.afficher()

bigBill.attaquer(magicMike)
bigBill.attaquer(magicMike)

magicMike.afficher()
bigBill.afficher()
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
