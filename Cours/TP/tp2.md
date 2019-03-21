
## TP 2.

Normalement, à ce stade, vous devriez avoir fini le TP 1,
et donc avoir une balle qui rebondit, un joueur qui se déplace.
Idéalement, vous détectez les contacts entre le joueur et la balle pour arrêter
le jeu.

MAIS : vos variables de déplacement de la balle sont externes à la balle
et manipulées par le programme principal qui effectue le déplacement de la balle.

Pour simplifier tout cela, nous allons créer une nouvelle classe qui sera une
variété spécifique d'**ElementGraphique** et qui aura la capacité de se déplacer
tout seul en ligne droite.

Créons donc une classe **Balle** qui hérite d'**ElementGraphique**

### Création des objets qui se déplacent seuls...

Dans un fichier *Balle.py*, vous allez donc avoir ceci :

```python
class Balle (ElementGraphique):
    def __init__(self,img):
        ElementGraphique.__init__(self, img)
```

Pour déclarer notre balle, dans notre programme principal,
nous allons maintenant déclarer la création de la balle comme suit :

```python
image = pygame.image.load("balle.png").convert_alpha()
balle = Balle(image)
balle.rect.x = 140
balle.rect.y = 270
```

Pour le moment, ce que nous avons fait n'a servi à rien, sauf que *balle*
est maintenant une instance de *Balle* qui **hérite** de *ElementGraphique*.

Ce que nous voulons, c'est que chaque balle ait une direction spécifique qui sera
modifiée lors des rebonds.
Pour cela, nous allons ajouter des champs **deltaX** et **deltaY** à nos objets
*Balle*. Le fichier *Balle.py* devient alors

```python
class Balle (ElementGraphique):
    def __init__(self,img):
        ElementGraphique.__init__(self, img)
        self.deltaX = 3
        self.deltaY = -4
```

Maintenant, la balle transporte avec elle son vecteur de déplacement.
Vous pouvez modifier votre programme votre programme principal pour qu'il
utilise ces nouvelles variables.
Vous aurez sans doute quelque chose comme ce qui suit au sein de votre boucle
*while* :

```python
  balle.rect.x += balle.deltaX
  balle.rect.y += balle.deltaY
```
Ceci fonction mais n'est pas très objet.

Créez donc une méthode de la classe *Balle* qui effectue le déplacement.
Cette méthode s'appelera **deplacer** :

```python
    def deplacer(self):
        self.rect.x += self.deltaX
        self.rect.y += self.deltaY
```

et votre programme principal aura alors la ligne suivante dans la boucle *while* :
```python
  balle.deplacer()
```

Notez bien qu'on ne prend ici pas en compte les rebonds.
Pour cela, il faut impérativement que la fonction déplacer ait accès à la fenêtre.
Soit vous ajouter ce paramètre à la méthode *deplacer*, soit, lorsque l'on crée
un *ElementGraphique*, celui ci doit savoir à quelle fenetre il est attaché.
La seconde solution sera plus pratique sur le long terme, mais c'est à vous de voir.

Débrouillez vous pour faire fonctionner les rebonds.

### Gestion des collisions à la sauce objet :
Tant que vous y êtes, créez une méthode dans *ElementGraphique* qui dit si un
*ElementGraphique* en touche un autre. Cette méthode aurait la forme suivante :
```python
    def collide(self, other):
        if self.rect.collide_rect(other.rect)
            return True
        return False
```

Utilisez cette méthode pour gérer le contact entre votre balle et votre joueur.

#### Qu'avons nous gagné ?
C'est facile a voir :

1. Au lieu de manipuler une balle, construisez un tableau de 3 ou 4 balles. Constatez que la manipulation des multiples balles est beaucoup plus facile car chaque balle se gère plus ou moins toute seule.

2. Vous pouvez maintenant vous débrouiller pour que le jeu commence avec une seule balle et qu'une balle soit ajoutée tous les 100 tours de boucles (idéalement toutes les 5 secondes)

3. Débrouillez vous pour que lorsqu'une balle est créee, sa direction soit tirée au hasard.

### Gestion du joueur

Ce que nous avons fait pour la balle, nous allons le faire pour un joueur.

1. Créez une classe **Joueur** qui hérite de *ElementGraphique*.
Vous pouvez par exemple ajouter un champ **vies** à votre joueur si vous voulez,
initialisé à 3.

Votre joueur devrait être initialisé comme suit :
```python
image = pygame.image.load("perso.png").convert_alpha()
joueur = Joueur(image)
```

2. Ajoutez une méthode *deplacer* qui prend comme argument le tableau de touches
et qui modifie la position du joueur en fonction de ce tableau.
Votre programme principal appelera cette méthode comme suit :
```python
    joueur.deplacer(touches)
```

3. En cas de collision, le joueur doit perdre une vie et le programme
doit s'arreter si le joueur n'a plus de vies.

### Minimum requis pour la séance suivante

Cette section décrit ce qu'il faut, **au minimum**, pour pouvoir entamer sereinement le TP suivant. Evidemment, si vous êtes allé au bout du TP décrit dans ce document, vous êtes plus loin que cela.

Pour le début du TP3, vous devrez au minimum (pour avoir 10 au TP1) avoir un programme avec :

- un personnage (Joueur) qui se déplace grace à la méthode *deplacer* de la classe Joueur.
- Un tableau de balles (Balle) qui se déplacent automatiquement et rebondissent grace à la méthode *deplacer* de la classe Balle.
- en cas de collision entre une balle et le personnage, le jeu s'arrête.
- Le jeu commence avec une seule balle.
- Une balle est ajoutée tous les 100 tours de boucle.
