
## Second Cours : Les Classes

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
appellerait une **structure du données**, et que les langages
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



Passons maintenant a ce qui va permettre de
