

## Premier TP.

### Premiere partie : Rappels de cours

Ce qui suit est simplement à lire au début du TP en s'assurant que vous
comprenez bien.
Au besoin, demandez a votre encadrant des explications complémentaires.

Il s'agit de reprendre calmement ce que nous avons vu dans le dernier cours :
Transformer le début du petit jeu de balles qui repondissent pour qu'il utilise
des **classes**.

On repart du fichier *tutos.zip* du premier semestre, disponible ici :
[https://elbixos.github.io/L1_OptionInfo/Projets/JeuVideo/Sources/tutos.zip](https://elbixos.github.io/L1_OptionInfo/Projets/JeuVideo/Sources/tutos.zip)


1. on a décompressé le fichier zip dans le repertoire de notre choix
2. on a copié le fichier *06_imageTexte.py* dans un nouveau fichier *monJeu.py*

C'est sur ce fichier *monJeu.py* que nous travaillons maintenant.

### Création d'une proto classe d'objets **ElementGraphique**

Le terme de *proto classe* est juste ici pour signaler que notre classe ne sera
pas, au début, formée de façon très efficace.

Cette classe sera la classe principale de nos éléments graphiques du jeu.
L'ensemble des éléments graphiques est le suivant :
- le personnage du joueur
- la ou les balles
- le fond
- le texte
- les bonus / les vies (si vous en implémentez)

Chaque élément graphique dispose toujours de 2 informations :
- une image qui le représente
- un rectangle qui définit sa position.

Ce seront les **attributs** (les champs) de notre classe.
Quand nous voudrons accéder au champ image d'un élément graphique *el*, nous
utiliserons désormais *el.image* ou *el.rect*.

On souhaitait dans un premier temps créer donc une classe qui, lorsque l'on construit un élément graphique, lui donne une image nulle et un rectangle nul.
**Idéalement, ne regardez pas le code suivant avant d'avoir eu par vous même une
idée assez précise de son contenu.**

```python
class ElementGraphique():
    def __init__(self):
        self.image = 0
        self.rect = 0
```
*Cette classe me fait un peu honte, mais elle va changer plus loin*

Nous voulons ensuite modifiez le code de façon à utiliser cette classe pour le
joueur, la balle et le fond. Notre programme va donc devoir créer 3 éléments graphiques.
Dans cette version, c'est le programme principal qui se charge de donner les bonnes
valeurs à l'image et au rect de chaque élément graphique.
```python
    perso = ElementGraphique()
    perso.image = pygame.image.load("perso.png").convert_alpha()
    perso.rect = perso.image.get_rect()
    perso.rect.x = 240
    perso.rect.y = 300

    fond = ElementGraphique()
    fond.image = pygame.image.load("background.jpg").convert_alpha()
    fond.rect = fond.image.get_rect()

    balle = ElementGraphique()
    balle.image = pygame.image.load("balle.png").convert_alpha()
    balle.rect = balle.image.get_rect()
    balle.rect.x = 140
    balle.rect.x = 270
```

Il faudra également modifier le programme quand on effectue l'affichage de ces
éléments pour avoir

```python
    fenetre.blit(fond.image, fond.rect)
    fenetre.blit(perso.image, perso.rect)
    fenetre.blit(balle.image, balle.rect)
```

### Amélioration du constructeur d'**ElementGraphique**

Vous avez sans doute noté que pour chaque élément graphique, le constructeur
crée l'objet, avec des attributs *image* et *rect*
mal définies, que notre programme modifie ensuite pour leurs donner des valeurs
correctes.
(*parler de constructeur dans ce cas est en fait un abus de langage. Néanmoins, je m'en tiendrais à ce vocabulaire pour le moment*)

Ceci n'est pas du tout dans la philosophie *Objet*. L'idée serait plutôt, quand
on crée un objet, de lui donner son image et de programmer son constructeur pour
que l'objet soit cohérent.

Du coup, nous allons modifier le constructeur pour lui passer en argument l'image
de l'ElementGraphique que l'on veut créer.
Et en bonus, le constructeur va créer le rectangle approprié.

Vous pouvez essayer d'imaginer ce code par vous même avant de regarder ce qui
suit :

```python
class ElementGraphique():
    def __init__(self, img):
        self.image = img
        self.rect = self.image.get_rect()
```

la partie du programme ou l'on crée les éléments graphiques devient :

```python
    image = pygame.image.load("perso.png").convert_alpha()
    perso = ElementGraphique(image)
    perso.rect.x = 240
    perso.rect.y = 300

    image = pygame.image.load("background.jpg").convert_alpha()
    fond = ElementGraphique(image)

    image = pygame.image.load("balle.png").convert_alpha()
    balle = ElementGraphique(image)
    balle.rect.x = 140
    balle.rect.x = 270
```

### Modification du constructeur d'**ElementGraphique**

Nous allons maintenant modifier notre constructeur, de façon à pouvoir,
définir à la fois l'image de l'élément et son rect, mais aussi la position
voulue de l'élément.
*En python, il n'est pas possible de créer deux constructeurs différents.
Nous allons utiliser des parametres optionnels*

Les parametres *x* et *y* peuvent ou pas être passés a la fonction.
Si lors de l'appel de la fonction, on ne les utilise pas, nous leur ferons
prendre la valeur par défaut *0*.

**Important :** J'ai de plus passé au constructeur la fenetre dans laquelle l'element devra s'afficher, ce qui nous simplifiera beaucoup la tache plus tard

Encore une fois, vous pouvez essayer d'imaginer ce code tout seul.
Voici le résultat voulu pour la classe.

```python
class ElementGraphique():
    # Le constructeur basique
    def __init__(self, img, fen, x=0, y=0):
        self.image = img
        self.rect = self.image.get_rect()
        self.fenetre = fen

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y         
```
Cette classe s'utilise maintenant comme suit :
```python
    image = pygame.image.load("perso.png").convert_alpha()
    perso = ElementGraphique(image,fenetre, 240, 300)

    image = pygame.image.load("background.jpg").convert_alpha()
    fond = ElementGraphique(image,fenetre)

    image = pygame.image.load("balle.png").convert_alpha()
    balle = ElementGraphique(image,fenetre,140,70)
```

Ma classe commence a avoir une tête un peu plus jolie, au sens ou elle épargne pas
mal de travail au programme principal.

Nous souhaitons maintenant que les éléments graphiques "sachent" s'afficher
dans leur fenetre (il faudra faire une méthode *afficher* dans la classe ElementGraphique).

Pour bien comprendre comment faire cette méthode, nous allons procéder en 2 étapes
1. d'abord on crée une fonction qui s'occupe de cet affichage. La fonction est externe à la classe.
2. on transforme cette fonction en méthode.

**Remarque :** Quelqu'un qui comprend bien les concepts objets code directement la méthode afficher. Ces 2 étapes n'ont qu'un intérêt purement pédagogiques.


### Création d'une fonction pour l'affichage des **ElementGraphique**
Nous disposons maintenant d'une proto classe qui contient l'**image**, son
**rectangle** et la **fenetre** dans laquelle il doit s'afficher.
Nous pourrions donc créer une fonction d'affichage de tout élément graphique
dans une fenetre donnée.

Une telle fonction s'écrirait comme suit :
```python
def afficher(elGraphique) :
    elGraphique.fenetre.blit(elGraphique.image, elGraphique.rect)  
```
Et le programme principal utiliserait cette fonction à la place des *fenetre.blit*.

Le code d'avant :

```python
    fenetre.blit(fond.image, fond.rect)
    fenetre.blit(perso.image, perso.rect)
    fenetre.blit(balle.image, balle.rect)
```

Le code d'après :

```python
    afficher(fond)
    afficher(perso)
    afficher(balle)
```

### Transformation de cette fonction en méthode d'**ElementGraphique**

Basculons maintenant notre classe en véritable objet :
Un element graphique doit savoir comment s'afficher dans une fenetre
La fonction afficher doit donc devenir une méthode de la classe.

Essayez vous même avant de regarder ce qui suit.
Voici la classe :

```python
class ElementGraphique():
    # Le constructeur basique
    def __init__(self, img, fen, x=0 , y=0):
        self.image = img
        self.rect = self.image.get_rect()
        self.fenetre = fen

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y

    def afficher(self) :
        self.fenetre.blit(self.image, self.rect)  
```

et la partie du programme principal qui affiche les éléments.

```python
    fond.afficher()
    perso.afficher()
    balle.afficher()
```

Le bilan :
- La complexité du programme est déportée dans l'objet **ElementGraphique**, pour un programme beaucoup plus clair.
- Les opérations complexes (création du rectangle, affichage) sont définies une
fois pour toute. La correction de bugs est donc plus simple.

**C'est fini pour les rappels**. Maintenant, vous allez devoir vraiment coder.

### Partie 2 : Implémentation.

#### Question 1.
Commencez par récuperer ce code : [07_Avec_Classes.py](07_Avec_Classes.py)
Testez et vérifiez qu'il fonctionne


Vous allez devoir maintenant modifier le code. Chaque fois que vous faites une modification, testez la pour voir si elle fonctionne.

#### Question 2.
Créez une fonction *deplacer* (externe à la classe ElementGraphique) qui
permettra de déplacer le personage (dans toutes les directions) quand on appuie
sur les touches (sans controle des bords de fenetre)

On devra sans doute lui passer un ElementGraphique (le personnage), ainsi que le
tableau de touches qui permet de savoir quelles touches sont enfoncées.
(*perso étant un objet, la fonction pourra modifier la valeur des attributs du perso, un peu comme si on passait un pointeur sur perso, en C* )

Il faut également, dans le programme principal, appeler cette fonction

### Question 3.
Modifier cette fonction pour que le personnage ne puisse pas déborder de la fenetre de jeu.

**Remarque :**
La hauteur et la largeur de la fenetre sont définies dans le programme
principal. Votre fonction *deplacer* n'y a donc pas accès sauf si vous
les passez comme arguments (ou alors comme variables globales, qui sont a
proscrire).

Or nous voulons également éviter de passer trop d'arguments à nos fonctions,
pour des raisons de simplicité d'usage. C'est la raison pour laquelle j'ai passé
la fenetre au constructeur des ElementsGraphiques.

 La doc pygame m'indique que si l'on souhaite, n'importe ou dans le code
(dans une fonction), connaitre la taille de la fenetre, et que vous disposez
d'une variable qui la représente, on peut faire comme suit :

```python
largeur, hauteur = nom_de_la_fenetre.get_size()
```

Avec mon code, si dans une fonction, je dispose d'un ElementGraphique nommé *el*,
je peux écrire :
```python
largeur, hauteur = el.fenetre.get_size()
```

### Question 4.
Se débrouiller pour que le programme principal permette
à la balle de se déplacer en rebondissant sur les bords de la fenetre.

### Question 5.
Il s'agit maintenant de commencer à préparer le terrain pour passer ceci en
méthode.

Le problème est qu'il faudra déplacer le personnage, mais aussi les balles,
et qu'on ne va pas créer, dans la classe ElementGraphique, une methode
deplacer_perso, une méthode deplacer_balle, et eventuellement deplacer_bonus.

**Il est beaucoup plus efficace d'utiliser des classes spécifiques**.
Nous allons donc créer une classe Perso, une classe Balle, et ainsi de suite.
Ainsi, les classes spécifiques auront leurs méthodes propres (pour se déplacer
notamment)

Toujours dans un souci d'efficacité, **nous allons utiliser la notion
d'héritage**, qui permet de recycler des choses déja faites. Un Perso sera donc
un ElementGraphique spécifique, qui devra disposer des attributs et méthodes
des ElementGraphiques, mais aussi d'attributs propres (ses vies ?) et de
méthodes propres (deplacer).

Creez donc une classe **Perso** qui hérite d'ElementGraphique, et dont le
constructeur appelle celui d'ElementGraphique.
On a vu en cours comment le faire, dans le Battle Royal, en utilisant
*super().__init__*.

Votre programme principal devra également modifier la ligne correspondant à la
création du perso pour créer maintenant un Perso (et non plus un
ElementGraphique)

### Question 6.
Transformez votre fonction *deplacer* en méthode de la classe Perso

Il faudra aussi modifier votre programme principal pour qu'il appelle cette
méthode (et non plus la fonction externe à la classe)

### Question 7.
Creez une classe Balle, héritant de ElementGraphique, qui appelle
le constructeur d'ElementGraphique, et ajoute comme attributs a la balle *dx*
et *dy*, qui représenteront le vecteur de déplacement de la balle, fixé à 3,3
par défaut.

Modifiez votre programme principal pour que la balle soit une Balle (et non plus
un ElementGraphique).

### Question 8.
Ajoutez une méthode déplacer a votre classe Balle, qui permette a la balle de
rebondir.

Appelez cette méthode dans votre programme principal.

### Question 9.
Modifiez votre programme pour que l'on ait 3 balles, réunies dans un tableau,
qui se déplacent à l'écran. Vous pourriez avoir envie de créer trois variables
de type Balle, mais il sera plus efficace de placer ces 3 balles dans un tableau
(une Liste python)

### Minimum requis pour la séance suivante

Cette section décrit ce qu'il faut, **au minimum**, pour pouvoir entamer
sereinement le TP suivant. Evidemment, si vous êtes allé au bout du TP décrit dans
ce document, vous êtes plus loin que cela.

Pour le début du TP2, vous devrez au minimum (pour avoir 10 au TP1) avoir un
programme avec :

- un personnage (ElementGraphique) qui se déplace avec les touches.
- une balle (ElementGraphique) qui se déplace automatiquement et rebondit.
- en cas de collision entre la balle et le personnage, le jeu s'arrete.

### Barême Précis

Puisque la plupart l'ont demandé voici un barême précis. Veuillez noter qu'il est
très délicat de poser un barème précis, puisque :

- si je dis : "Faire telle chose vaut x points", cela sous entends que "faire
telle chose" a été réalisé sans aide exterieure (notamment la mienne). Que cela ne
vous empeche pas de me demander de l'aide, l'idée des TP est surtout de vous faire
progresser.
- si je dis : "Faites une fonction qui....", cela sous entends entre autres que
votre fonction n'utilise aucune variable globale (et donc qu'on lui passe les bons
arguments en parametres, et eventuellement qu'elle retourne les bons arguments)


Pour les PASS, qui ont beaucoup en tête l'idée de concours, vous pouvez aussi vous
détendre un peu, la note de cette UE n'a aucune incidence sur votre parcours
d'origine, ni, en cas de ré-orientation, sur la suite de votre scolarité. On met
plus l'accent sur votre capacité a apprendre, plutôt qu'a obtenir une note précise
(meme si 10 est le minimum à viser)

Bref, voici plus ou moins le barême (sur 20) :

- 2 points : faire tourner le programme initial 07_Avec_Classes.py sur votre machine.
- 1 point : utiliser d'autres images trouvées sur le net.
- 6 points : avoir un programme principal qui
  - (3 points) crée un perso (ElementGraphique) et le gère : Il est controlé par
  les touches du clavier et est coincé par les bords de la fenetre.
  - (3 points) crée une balle (ElementGraphique) et la gère : elle se déplace
  avec une direction initiale de dx=3 pixels, dy =4 pixels à chaque tour de
  boucle. La balle rebondit sur les bords.

Avec ca, qui est vraiment le minimum minimum (sachant que j'ai fourni en cours
le code et  les images d'origine), vous avez 9/20.
vous savez **faire tourner un pg python  utilisant une librairie externe**
(pygame).

- 3 points : faire une fonction *deplacer* qui permette de déplacer le personnage.

Sous réserve que vous fassiez tout cela correctement
(ce que nous avons fait en TP et que vous avez pu voir), vous auriez donc 12.
**Vous aurez appris a faire des fonctions proprement**.

Pour améliorer votre note :
- 2 points : creer une classe Perso, avec sa méthode déplacer()

- 2 points : creer une classe Balle, avec sa méthode déplacer()

Avec ca, vous avez 16, et ca n'est pas volé.
**Vous avez appris a utiliser l'héritage**.

- 2 points :
  - créer 3 balles au début du programme, placées dans un tableau,
  à des positions différentes, et avec les mêmes déplacements initiaux.
  - Utilisez méthode *deplacer* sur chacune de ces balles a l'aide d'une boucle.
  - Affichez ces balles à l'aide d'une boucle.
  - testez la collision entre les balles et le perso a l'aide d'une boucle


Si vous avez bien compris tout ceci, vous savez **ranger vos données dans des structures adaptées a du traitement par boucles** (en gros, des tableaux)...
et vous n'auriez pas volé une note de 18.

Si vous avez crée 3 balles hors tableau, et des variables dx1,dy1, dx2, dy2, dx3, dy3, ca ne sert a rien pour la note, vous restez à 12... (mais vous avez la satisfaction de voir 3 objets bouger à l'écran)

Pour améliorer votre note, on va faire un peu plus d'objet :
(ce qui fera l'objet du TP suivant en fait)

Si vous faites tout ceci, sans problème, sans trop d'aide, et avec un code
nickel, nous voila rendu a une note de 18/20. Vous avez **compris les notions
d'héritage et savez en tirer parti dans un cas pratique**.

Pour avoir plus (cela suppose que tout ce qui précède soit fait)
- codez propre
- ajoutez des fonctionnalités (bonus, menu, son ???)

Pas la peine d'ajouter du son ou un menu si vous n'avez pas un beau tableau de
balles sous forme de classe, c'est du temps perdu.

Voila !
