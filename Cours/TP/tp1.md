

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

Ce seront les **attributs** (les champs) de notre classe.
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

Vous avez sans doute noté que pour chaque élément graphique, le constructeur crée l'objet, avec des attributs *image* et *rect*
mal définies, que notre programme modifie ensuite pour leurs donner des valeurs correctes. (*parler de constructeur dans ce cas est en fait un abus de langage. Néanmoins, je m'en tiendrais à ce vocabulaire pour le moment*)

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

### Modification du constructeur d'**ElementGraphique**

Nous allons maintenant modifier notre constructeur, de façon à pouvoir,
définir à la fois l'image de l'élément et son rect, mais aussi la position
voulue de l'élément.
*En python, il n'est pas possible de créer deux constructeurs différents.
Nous allons utiliser des parametres optionnels*

les parametres $x$ et $y$ peuvent ou pas être passés a la fonction. Si lors de
l'appel de la fonction, on ne les utilise pas, nous leur ferons prendre la
valeur par défaut $0$.

Encore une fois, vous pouvez essayer tout seul. Voici le résultat voulu pour la classe.

```python
class ElementGraphique():
    # Le constructeur basique
    def __init__(self, img, x=0, y=0):
        self.image = img
        self.rect = self.image.get_rect()

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y         
```
Cette classe s'utilise maintenant comme suit :
```python
    image = pygame.image.load("perso.png").convert_alpha()
    perso = ElementGraphique(image,240, 300)

    image = pygame.image.load("background.jpg").convert_alpha()
    fond = ElementGraphique(image)

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
    def __init__(self, img, x , y):
        self.image = img
        self.rect = self.image.get_rect()

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y

    def afficher(self, window) :
        window.blit(self.image, self.rect)  
```

et la partie du programme principal qui affiche les éléments.

```python
    fond.afficher(fenetre)
    perso.afficher(fenetre)
    balle.afficher(fenetre)
```

Le bilan :
- La complexité du programme est déportée dans l'objet **ElementGraphique**, pour un programme beaucoup plus clair.
- Les opérations complexes (création du rectangle, affichage) sont définies une fois pour toute. La correction de bugs est donc plus simple.

### Les choses a faire maintenant
Vous pouvez maintenant faire quelques manipulations qui serviront de
base pour le prochain TP.

- créer la fonction qui déplace le perso. Passez lui tous les arguments dont elle a besoin. (*perso étant un objet, la fonction peut modifier la valeur de ses attributs* )

- créer la fonction qui déplace la balle. Passez lui tous les arguments dont elle a besoin. (*balle étant un objet, la fonction peut modifier la valeur de ses attributs* )

- Modifiez votre programme pour que l'on ait 3 balles, réunies dans un tableau, qui se déplacent à l'écran.


### Minimum requis pour la séance suivante

Cette section décrit ce qu'il faut, **au minimum**, pour pouvoir entamer sereinement le TP suivant. Evidemment, si vous êtes allé au bout du TP décrit dans ce document, vous êtes plus loin que cela.

Pour le début du TP2, vous devrez au minimum (pour avoir 10 au TP1) avoir un programme avec :

- un personnage (ElementGraphique) qui se déplace avec les touches.
- une balle (ElementGraphique) qui se déplace automatiquement et rebondit.
- en cas de collision entre la balle et le personnage, le jeu s'arrete.

### Barême Précis

Puisque la plupart l'ont demandé voici un barême précis. Veuillez noter qu'il est très délicat de poser un barème précis, puisque :

- si je dis : "Faire telle chose vaut x points", cela sous entends que "faire telle chose" a été réalisé sans aide exterieure (notamment la mienne). Que cela ne vous empeche pas de me demander de l'aide, l'idée des TP est surtout de vous faire progresser.
- si je dis : "Faites une fonction qui....", cela sous entends entre autres que votre fonction n'utilise aucune variable globale (et donc qu'on lui passe les bons arguments en parametres, et eventuellement qu'elle retourne les bons arguments)


Pour les PASS, qui ont beaucoup en tête l'idée de concours, vous pouvez aussi vous détendre un peu, la note de cette UE n'a aucune incidence sur votre parcours d'origine, ni, en cas de ré-orientation, sur la suite de votre scolarité. On met plus l'accent sur votre capacité a apprendre, plutôt qu'a obtenir une note précise (meme si 10 est le minimum à viser)

Bref, voici plus ou moins le barême (sur 20) :

- 2 points : faire tourner le programme initial 07_Avec_Classes.py sur votre machine.
- 1 point : utiliser d'autres images trouvées sur le net.
- 3 points : avoir un programme principal :
  - crée un perso et le gère : Il est controlé par les touches du clavier et est coincé par les bords de la fenetre.
  - crée une balle et le gère : elle se déplace avec une direction initiale de dx=3 pixels, dy =4 pixels à chaque tour de boucle. La balle rebondit sur les bords.

Avec ca, qui est vraiment le minimum minimum (sachant que j'ai fourni le code et les images d'origine), vous avez 6/20. vous savez **faire tourner un pg python utilisant une librairie externe** (pygame).

- 3 points : faire une fonction *deplacer_perso* qui permette de déplacer le personnage.
- 3 points : faire une fonction *deplacer_balle* qui permette de déplacer la balle.

Sous réserve que vous fassiez tout cela correctement
(ce que nous avons fait en TP et que vous avez pu voir), vous auriez donc 12.
**Vous aurez appris a faire des fonctions proprement**.


Pour améliorer votre note :

- 3 points :
  - créer 3 balles au début du programme, placées dans un tableau,
à des positions différentes, et avec les mêmes déplacements initiaux.
  - Utilisez la fonction *deplacer_balle* sur chacune de ces balles a l'aide d'une boucle.
  - Affichez ces balles à l'aide d'une boucle.
  - testez la collision entre les balles et le perso a l'aide d'une boucle

Ceci vous posera sans doute un problème : le stockage des directions de déplacement de chacune des balles (chacun a le sien, puisque la direction de chacune des balles peut changer a des moments différents). Une idée pourrait être
de stocker les dx des balles dans un tableau, les dy des balles dans un autre tableau.

Pour vous donner une idée du problème, voici ce à quoi pourrait ressembler la partie du pg principal qui effectue le déplacement des balles sous réserve que :
- mes dx soient dans un tableau *DX*
- mes dy soient dans un tableau *DY*
- mes balles soient des ElementGraphique dans un tableau *balles*

```python
for i in range(len(balles)):
  DX[i], DY[i] = deplacer_balle(balles[i], DX[i], DY[i])
```

Si vous avez bien compris tout ceci, vous savez **ranger vos données dans des structures adaptées a du traitement par boucles** (en gros, des tableaux)...
et vous n'auriez pas volé une note de 15.

Si vous avez crée 3 balles hors tableau, et des variables dx1,dy1, dx2, dy2, dx3, dy3, ca ne sert a rien pour la note, vous restez à 12... (mais vous avez la satisfaction de voir 3 objets bouger à l'écran)

Pour améliorer votre note, on va faire un peu plus d'objet :
(ce qui fera l'objet du TP suivant en fait)

- 3 points :
  - creez une classe Balle :
    - héritant de ElementGraphique
    - avec comme propriétés supplémentaires *dx*, *dy*  
    - avec une méthode deplacer (sans autre argument que self)
  - creez une classe Perso :
      - héritant de ElementGraphique
      - avec comme propriétés supplémentaires *vitesse*  
      - avec une méthode deplacer (sans comme argument *touches*)
  - votre programme principal devra créer 3 balles dans un tableau, les deplacer
  et tester la collision avec le personnage à l'aide d'une boucle.


Si vous voulez tenter cette partie après avoir fait tout ce qui précède, vous pouvez rendre 2 fichiers python...

Si jamais vous avez directement tenté cette solution et qu'elle fonctionne, les points précédents sont plus ou moins acquis... (avec des bémols en fonction de la façon dont c'est codé) et vous pouvez ne rendre qu'un seul fichier python.

Si vous faites tout ceci, sans problème, sans aide, et avec un code nickel, nous voila rendu a une note de 18/20. Vous avez **compris les notions d'héritage et savez en tirer parti dans un cas pratique**.

Pour avoir plus (cela suppose que tout ce qui précède soit fait)
- codez propre
- ajoutez des fonctionnalités (bonus, menu, son ???)

Pas la peine d'ajouter du son ou un menu si vous n'avez pas un beau tableau de balles sous forme de classe, c'est du temps perdu.

Voila !
