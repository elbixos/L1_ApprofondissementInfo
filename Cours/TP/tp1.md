

## Premier TP.

On repart du fichier *tutos.zip* du premier semestre, disponible ici :
[https://elbixos.github.io/L1_OptionInfo/Projets/JeuVideo/Sources/tutos.zip](https://elbixos.github.io/L1_OptionInfo/Projets/JeuVideo/Sources/tutos.zip)

1. décompressez le dans le repertoire de votre choix
2. copiez le fichier *06_imageTexte.py* dans un nouveau fichier *monJeu.py*

C'est sur ce fichier *monJeu.py* que nous travaillerons maintenant.

Nous allons faire plusieurs choses dans ce TP :

### Création d'une proto classe d'objets **ElementGraphique**

Le terme de *proto classe* est juste ici pour signaler que notre classe ne sera pas,
au début, formée de façon très efficace.

Cette classe sera la classe principale de nos éléments graphiques du jeu.
L'ensemble des éléments graphiques est la suivante :
- le joueur
- la ou les balles
- le fond

Chaque élément graphique dispose toujours de 2 informations :
- une image qui le représente
- un rectangle qui définit sa position.

Ce seront les **propriétés** (les champs) de notre classe.
Quand nous voudrons accéder au champ image d'un élément graphique *el*, nous
utiliserons désormais *el.image* ou *el.rect*.

Créez donc une classe qui, lorsque l'on construit un élément graphique
lui donne une image nulle et un rectangle nul.
Idéalement, ne regardez pas le code suivant et essayez par vous même.
Si cela coince, regardez le code suivant :

```python
class ElementGraphique():
    def __init__(self):
        self.image = 0
        self.rect = 0
```
*Cette classe me fait un peu honte, mais elle va changer plus loin*

Modifiez le code de façon a utiliser cette classe pour le joueur,
la balle et le fond :
votre programme va donc créer 3 éléments graphiques :
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
(*ceci est en fait un abus de langage. je m'en tiendrais à ce vocabulaire néanmoins*)
crée l'objet, avec des propriétés *image* et *rect* mal définies,
que notre programme modifie ensuite pour leurs donner des valeurs correctes.

Ceci n'est pas du tout dans la philosophie *Objet*. L'idée serait plutôt, quand
on crée un objet, de lui donner son image et de programmer son constructeur pour
que l'objet soit cohérent.

Du coup, nous allons modifier le constructeur pour lui passer en argument l'image
de l'ElementGraphique que l'on veut créer. Et en bonus, le constructeur va créer le rectangle
approprié.

Vous pouvez essayer tout seul, mais pouvez aussi regarder ce qui suit :

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

### Deuxième amélioration du constructeur d'**ElementGraphique**

Nous allons maintenant ajouter un second constructeur, qui, si on l'utilise,
permet de définir à la fois l'image de l'élément et son rect, mais aussi la position
voulue de l'élément.

Encore une fois, vous pouvez essayer tout seul. Voici le résultat voulu pour la classe.

```python
class ElementGraphique():
    # Le constructeur basique
    def __init__(self, img):
        self.image = img
        self.rect = self.image.get_rect()

    # Constructeur qui positionne
    def __init__(self, img, x , y):
        # tout d'abord on appelle le constructeur précédent.
        ElementGraphique.__init__(self,img)

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y         
```
Cette classe s'utilise maintenant comme suit :
```python
    image = pygame.image.load("perso.png").convert_alpha()
    perso = ElementGraphique(image,240, 300)

    image = pygame.image.load("background.jpg").convert_alpha()
    fond = ElementGraphique(image,0,0)

    image = pygame.image.load("balle.png").convert_alpha()
    balle = ElementGraphique(image,140,70)
```

Ma classe commence a avoir une tête un peu plus jolie, au sens ou elle épargne pas
mal de travail au programme principal.


### Création d'une fonction pour l'affichage des **ElementGraphique**
Nous disposons maintenant d'une proto classe qui contient l'image et son rectangle.
Nous pouvons donc créer une fonction d'affichage de tout élément graphique dans une fenetre
donnée

Une telle fonction s'écrirait comme suit :
```python
def afficher(elGraphique, window) :
    window.blit(elGraphique.image, elGraphique.rect)  
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
    afficher(fond,fenetre)
    afficher(perso,fenetre)
    afficher(balle,fenetre)
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
    def __init__(self, img):
        self.image = img
        self.rect = self.image.get_rect()

    # Constructeur qui positionne
    def __init__(self, img, x , y):
        # tout d'abord on appelle le constructeur précédent.
        ElementGraphique.__init__(self,img)

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y

    def afficher(self, window) :
        window.blit(self.image, self.rect)  
```

et la partie du programme principal qui affiche les éléments.

```python
    fond.afficher((fenetre)
    perso.afficher((fenetre)
    balle.afficher((fenetre)
```

Le bilan :
- La complexité du programme est déportée dans l'objet **ElementGraphique**, pour un programme beaucoup plus clair.
- Les opérations complexes (création du rectangle, affichage) sont définies une fois pour toute. La correction de bugs est donc plus simple.

### Les choses a faire maintenant
Vous pouvez maintenant faire quelques manipulations qui serviront de
base pour le prochain TP.

- créer la fonction qui déplace le perso. Passez lui tous les arguments dont elle a besoin. (*perso étant un objet, la fonction peut modifier la valeur de ses propriétés* )

- créer la fonction qui déplace la balle. Passez lui tous les arguments dont elle a besoin. (*balle étant un objet, la fonction peut modifier la valeur de ses propriétés* )

- Modifiez votre programme pour que l'on ait 3 balles, réunies dans un tableau, qui se déplacent à l'écran.
