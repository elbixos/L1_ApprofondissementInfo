
### Les Méthodes

Là ou cela devient vraiment bon, c'est quand les objets peuvent avoir leur propres
fonctions. vous avez déja utilisé cela avec pygame par exemple :
```python
fenetre.blit(myImage,myRect)
```
*fenetre* était bien une variable. On appelait donc une fonction de la variable...
Ces fonctions internes aux objets sont appelées des **méthodes**.
Voyons comment créer une.

#### Création d'une méthode

Reprenons notre fonction d'affichage d'un étudiant et transformons la en méthode.
Nous avons d'une part notre classe qui contient sa fonction *__init__*
(qui entre nous est une méthode) :
```python
class Etudiant():
  def __init___(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom
    self.notes = []
```
D'autre part, nous avons notre fonction *afficher*
```python
def afficher(etudiant):
    print (etudiant.nom, etudiant.prenom, etudiant.notes)
```

Nous allons signaler à la classe que la fonction afficher fait partie de la classe.
Pour cela, nous indentons la partie correspondant à la fonction.

```python
class Etudiant():
    def __init___(self, nom, prenom):
      self.nom = nom
      self.prenom = prenom
      self.notes = []

    def afficher(etudiant):
      print (etudiant.nom, etudiant.prenom, etudiant.notes)
```

Mais il ne s'agit pas pour un objet de type *Etudiant* d'afficher un étudiant qu'on
lui donne, il s'agit pour notre objet de s'afficher lui même.
Nous utilisons encore une fois le mot clef *self* pour désigner l'objet, vu depuis l'objet.
Cela nous donne le code suivant :
```python
class Etudiant():
  def __init___(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom
    self.notes = []

  def afficher(self):
      print (self.nom, self.prenom, self.notes)
```

Recapitulons. Pour créer une méthode dans une classe :
1. on l'indente correctement
2. on lui ajoute **self** comme premier paramètre.

Pour s'en servir, notre programme principal va demander à un etudiant de s'afficher lui même :

```python
etu = Etudiant("Uzumaki","Naruto")
etu.afficher()
```
ou dans un tableau :
```python
promo = []

etu = Etudiant("Uzumaki","Naruto")
promo.append(etu)

etu = Etudiant("Uchiwa","Sazuke")
promo.append(etu)


for e in promo :
  e.afficher()
```
Vous le voyez, à l'appel de la fonction, on ne précise pas **self** ou quoique ce soit.
python va l'ajouter a votre place.


L'intérêt de ces méthodes ne vous saute pas aux yeux ?
c'est normal. L'idée générele est que vous voulez pouvoir utiliser un objet
sans vraiment avoir besoin de savoir ce qui se passe dedans.
En fait, souvent, ce n'est pas la même personne qui code les classes et qui les utilise.

Pour bien s'en rendre compte, déportons notre classe dans un autre fichier.
Nous aurons donc 2 fichiers :
- *etudiant.py*
- *02_03_main.py*

Le fichier *etudiant.py* contient le code de la classe Etudiant.
```python
class Etudiant():
  def __init___(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom
    self.notes = []

  def afficher(self):
      print (self.nom, self.prenom, self.notes)
```
le fichier *02_04_main.py* contiendra le code du programme principal.

```python
from etudiant import Etudiant

promo = []

etu = Etudiant("Uzumaki","Naruto")
promo.append(etu)

etu = Etudiant("Uchiwa","Sazuke")
promo.append(etu)


for e in promo :
  e.afficher()
```
La première ligne dit : "dans le fichier *etudiant.py* (considéré comme un *module*), importe la classe Etudiant".

#### Modification de l'objet *Etudiant*

Nous allons maintenant jouer un peu avec notre objet pour lui ajouter des
fonctionnalités et des attributs. Il sera de votre ressort d'essayer par vous
même. La solution figure en dessous.

1. Ajout d'un attribut *nomComplet*, construit par le constructeur,
sur le modèle suivant : si l'étudiant s'appelle Vincenzo Delapaegas, son nom
complet serait "Mister Vincenzo The Great Delapaegas"

2. Création d'une méthode qui ajoute une note à l'étudiant.

3. Création d'une méthode qui calcule la moyenne de l'étudiant.

4. Création d'une méthode qui permet à un étudiant de se comparer à un autre
(nom de la méthode : *isBetter*, renvoie True si l'étudiant est meilleur que l'etudiant passé en paramètre à la fonction).

Evidemment, pour toutes ces méthodes, il faudra que le programme principal les teste.


```python

class Etudiant():
    def __init__(self, nom, prenom, notes = []):
        self.nom = nom
        self.prenom= prenom
        self.nomComplet = "Mister or Miss "+nom+" The Great "+prenom
        self.notes = notes

    def afficher(self):
        print (self.nom,self.prenom, self.notes)

    def ajouterNote(self, note):
        self.notes.append(note)


    def getMoyenne(self):
        moy = 0.0
        for n in self.notes :
            moy+= n
        if not len(self.notes) == 0:
            moy = moy / len(self.notes)

        return moy

    def isBetter(self,etudiant):
        if (self.getMoyenne() > etudiant.getMoyenne()):
            return True
        return False

```

```python
from etudiant import Etudiant

def afficherPromo(promo):
    for etu in promo :
        etu.afficher()

a = 5
b = a
print (a,b)
a = a+1
print (a,b)


promo = []

e1 = Etudiant("Georges", "Anthony",[15,19])

e1.afficher()

promo.append(e1)

e2 = Etudiant("Valerius","Landry")
e2.ajouterNote(12)
e2.ajouterNote(16)
e2.ajouterNote(14)
promo.append(e2)

afficherPromo(promo)

moy = e1.getMoyenne()
print(moy)

print(e2.getMoyenne())

if e1.isBetter(e2):
    print ("bravo ", e1.nomComplet)
else:
    print ("bravo ", e2.nomComplet)
```
