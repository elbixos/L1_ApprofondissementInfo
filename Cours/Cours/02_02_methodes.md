
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
le fichier *02_03_main.py* contiendra le code du programme principal.




Améliorons notre exemple un petit peu pour mieux comprendre.
