
## Second Cours : Les Classes

### Mais d'abord : pour les étudiants de Pass

Nous avons vu la fin du tutoriel sur le jeu vidéo.
Vous auriez déja du récupérer les sources et les images de ce tuto.
Voici le code de ce que l'on a fait en cours. Regardez le cours d'option info
des L1 informatique si certains points vous paraissent nébuleux...

- [code fait en cours](../Sources/02_00_tuto_jeu_video.py)

Placez ce code dans le repertoire ou vous avez décompressé le zip du tuto pour
pouvoir le lancer (les images doivent se trouver dans le meme répertoire)

### Ok, les Classes...


Il s'agit ici de vous présenter un peu de programmation Objet par l'exemple.
Dans un premier temps, nous allons voir les objets comme la réunion de plusieurs
variables décrivant l'objet qui nous intéresse.


### Création d'un objet
Prenons un exemple :
Si je souhaite créer un étudiant, je voudrais stocker :
- son nom (String)
- son prénom (String)
- ses notes (un tableau de float)

Ces informations seront les **attributs** de l'objet.
Vu du programme principal, l'objectif est de créer un étudiant et tenter d'accéder
à ces **attributs**. On leur donne aussi le nom de **champs**

```python
etu = Etudiant()

etu.nom = "Uzumaki"
etu.prenom = "Naruto"
print(etu.notes)
print(type(etu))
```

Vu de l'extérieur de l'objet, le programme voit un objet nommé *etu* de type Etudiant,
et accède à l'attribut nom en utilisant *etu.nom*

Encore faut il expliquer à python ce qu'est cet Etudiant.
C'est un nouveau type de variables. Dans le cas présent, c'est ce que le C
appellerait une **structure de donnée**, et que les langages
objets appellent une **classe**.

Pour la créer et l'utiliser, on aurait le programme complet suivant (les explications
  viendront en dessous) :

```python
class Etudiant():
  def __init___(self):
    self.nom = ""
    self.prenom = ""
    self.notes = []


etu = Etudiant()

etu.nom = "Uzumaki"
etu.prenom = "Naruto"
print(etu.notes)
```

La première ligne déclare la classe Etudiant (un nouveau type d'objets).
On n'oublie pas les *:* qui signalent le début d'un bloc d'instruction.
Tout ce qui fait partie de l'objet doit être indenté.

Qu'est ce qui fait partie de l'objet ?
Dans notre cas, une seule chose : la fonction *__init__*.

#### La fonction *__init__*

Son nom est imposé et c'est la fonction qui sera appelée lorsque qu'on créera un
objet de type *Etudiant*. Les langages objets parlent de
de **constructeur** de la classe *Etudiant* (*en python, c'est un léger abus
de langage*). Reste à expliquer ce qu'est ce paramètre **self**, passé à la fonction.

**self** est l'objet lui même (celui qu'on essaye de créer).
C'est Python qui se charge de le passer à la fonction *__init__*
lorsqu'elle est appelée par cette ligne :
```python
etu = Etudiant()
```

Je recommence :
Lorsqu'on demande la création d'un *Etudiant*, on écrit *etu = Etudiant()*.
A ce moment, python va appeler la fonction *__init__* de la classe *Etudiant*.
Comme cette fonction a pour objectif de créer un objet avec des propriétés spécifique,
il faut bien nommer cet objet. La solution en python est de passer un argument à la fonction.
Cet argument peut avoir n'importe quel nom quand vous écrivez la fonction, mais
**il serait très malvenu de l'appeler autrement que self**. Tout le monde utilise ce nom,
y compris des IDE et des générateurs de documentation.

Le code de la fonction est relativement simple :
```python
self.nom = ""
self.prenom = ""
self.notes = []
```
Ici, nous créeons successivement les champs
- nom
- prenom
- notes

en les initialisant avec une valeur utile pour la suite.

#### Utilisation des objets

Revenons dans le programme principal pour jouer avec nos nouveaux objets.
La classe *Etudiant* existe. On peut créer des variables de type étudiant.

```python
etu1 = Etudiant()

etu1.nom = "Uzumaki"
etu1.prenom = "Naruto"
etu1.notes.append(14.5)

etu2 = Etudiant()

etu2.nom = "Uchiwa"
etu2.prenom = "Sazuke"
etu2.notes.append(15)
```

Cela devient vraiment utile quand on peut faire un tableau d'*Etudiants*...

```python
promo = []
etu = Etudiant()

etu.nom = "Uzumaki"
etu.prenom = "Naruto"
etu.notes.append(14.5)
promo.append(etu)

etu = Etudiant()

etu.nom = "Uchiwa"
etu.prenom = "Sazuke"
etu.notes.append(15)

for e in promo :
  print (e.nom, e.prenom, e.notes)
```

#### Passage de paramètres au *__init__*

Pour le moment, quand je crée un étudiant, son nom est *""*.
Cette façon de procéder n'est pas très pratique. Je voudrais pouvoir créer
des étudiants en définissant leur nom et leur prénom.

Pour cela, il suffit de modifier la fonction *__init__* en lui ajoutant les
paramètres qui m'intéressent :

```python
class Etudiant():
  def __init___(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom
    self.notes = []
```

Et quand je crée un étudiant, je doit maintenant spécifier son nom et son prénom.
(notez que le tableau des notes reste vide)
```python
promo = []

etu = Etudiant("Uzumaki","Naruto")
promo.append(etu)

etu = Etudiant("Uchiwa","Sazuke")
promo.append(etu)


for e in promo :
  print (e.nom, e.prenom, e.notes)
```

### Intérêt de ce qui précède.

Déja, cela va permettre de ranger un peu les variables de nos programmes.
Si vous essayez de faire ce qui précède sans classes, vous utiliserez vraisemblablement
3 tableaux :
- un tableau pour stocker les noms.
- un tableau pour stocker les prenoms.
- un tableau 2D pour stocker les notes.

Les informations sur un étudiant sont donc disséminées, et si vous voulez
afficher toutes les informations d'un étudiant, il faudra passer à la fonction chacun
des tableaux.

Dans notre cas, un étudiant est bien une entité unique qui contient plusieurs informations.
Et ca c'est cool.

Imaginons que l'on fasse une fonction qui affiche les informations d'un étudiant,
c'est facile :

```python
def afficher(etudiant):
    print (etudiant.nom, etudiant.prenom, etudiant.notes)
```
Notre programme principal devient
```python
promo = []

etu = Etudiant("Uzumaki","Naruto")
promo.append(etu)

etu = Etudiant("Uchiwa","Sazuke")
promo.append(etu)


for e in promo :
  afficher(e)
```

C'est beau, c'est propre.

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

Ok. Normalement, tout ceci ne vous a pas posé trop de problèmes. Voyons donc ce qui rend tout ceci vraiment classieux : la notion d'héritage.


### les fichiers

Les sources de tout ce que nous avons fait dans ce cours sont dans le répertoire [Sources](../Sources/index.md).
On y trouvera en particulier
les exemples sur les fonctions dans les fichiers dont le nom commence par **02_0** dans le répertoire [Sources](../Sources/index.md)

___

Vous pouvez repartir vers le [Sommaire](99_sommaire.md)

___
