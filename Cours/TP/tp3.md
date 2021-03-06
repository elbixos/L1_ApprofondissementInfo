
## TP 3.


Normalement, à ce stade, vous devriez avoir fini le TP 2,
et donc avoir un joueur qui se déplace,
et des balles qui s'ajoutent toutes seules régulièrement.

### La petite pause reflexion

Prenons quelques instants pour examiner l'intérêt de notre façon de coder...
voici ce a quoi devrait ressembler plus ou moins votre programme principal

```python
import toutBiten

def lireImages():
  images = {}
  images["fond"] = pygame.image.load("background.jpg").convert()
  images["perso"] = pygame.image.load("perso.png").convert_alpha()
  images["balle"] = pygame.image.load("perso.png").convert_alpha()

  # Choix de la police pour le texte
  font = pygame.font.Font(None, 34)
  images["texte"] = font.render('<Escape> pour quitter', True, (255, 255, 255))

  return images

def ajouterBalles(balles, compteur, fps, duree):
  if compteur/fps == duree:
    balles.append(Balle(images["balle"],largeur/2, hauteur/2, fen=fenetre))

## Initialisation de la fenetre et crÃ©ation
pygame.init()
#creation de la fenetre

largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

# lecture des images, bien rangées dans un dictionnaire
# on trouvera ainsi l'image du joueur dans :
# images["joueur"], et ainsi de suite
# ===============================
images = lireImages()

# creation des objets du jeu
# ===============================
fond = ElementGraphique(images["fond"],0,0, fen= fenetre)

texte = ElementGraphique(images["texte"],10,20, fen= fenetre)

# creation du tableau de balles avec une balle dedans
b = Balle(images["balle"],largeur/2, hauteur/2, fen=fenetre)
balles=[b]

joueur = Joueur(images["joueur"], 20, 50, fen = fenetre)

horloge = pygame.time.Clock()

# En avant !
fps = 30
continuer = True
time = 0
while continuer == True :
    horloge.tick(fps)
    time+=1

    # Recuperation de l'etat du clavier et des evenements de souris
    touches = pygame.key.get_pressed();
    evenements = pygame.event.get()

    # on ajoute des balles toutes les 5 secondes.
    ajouterBalles(balles, time, fps, 5)

    # deplacement du joueur
    joueur.deplacer(touches)

    # déplacement des balles
    for b in balles:
        b.deplacer()

    # Detection des collisions joueur / balles :
    for b in balles :
        if joueur.collide(b):
            joueur.toucher()
            if joueur.estMort():
                continuer = False

    # Affichage des elements
    fond.afficher()
    joueur.afficher()
    texte.afficher()

    for b in balles:
        b.afficher()

    # raffraichissement de l'ecran
    pygame.display.flip()


    # On vide la pile d'evenements et on verifie certains evenements
    for event in evenements:   # parcours de la liste des evenements recus
        if event.type == QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle

```

#### Coder proprement, pourquoi ?

Normalement, vous devriez trouver ce code beaucoup plus lisible
que ce que vous aviez fait au premier semestre.

En fait, le programme principal est maintenant le chef d'orchestre du programme,
et :
1. toutes les difficultés algorithmique sont déportées dans les fonctions/ classes.
2. la logique du programme apparait clairement.

Quel est l'intérêt de tout ceci ?
Aucun si votre objectif est de programmer des choses très simple
en un temps très court. Néanmoins, à terme, vous devrez programmer des choses
très complexes, à plusieurs. Dans ce cas, il est impératif que votre programme
soit aussi facile à comprendre que possible.

1. Imaginez que vous repreniez votre programme du premier
semestre dans 6 mois, un an ou que vous le donniez a l'un de vos amis et que l'objectif soit d'ajouter une fonctionnalité, j'aurais tendance a penser que ce serait compliqué car vous aurez oublié toute la logique que vous aviez en tête à l'époque.
2. Imaginez maintenant que l'on vous fournisse toutes les classes (Balle,
  Joueur,...) avec juste une petite documentation :
    - pour créer un joueur, utiliser le code
    ```python
    joueur = Joueur(image, x,y, fenetre)
    ```
    - pour déplacer un joueur, utiliser le code
    ```python
    joueur.deplacer()
    ```
    Il serait maintenant très facile pour vous de faire le programme principal
    **sans même savoir comment ces objets sont codés**.


A terme, dans la plupart de vos programmes, **vous utiliserez des librairies externes
de fonctions ou de classes, que vous combinerez pour faire des programmes**.
Parfois, vous **créerez des librairies qui seront utilisées par d'autres**

Cette capacité à recycler le code des autres est ce qui a rendu l'informatique
aussi efficace (et omniprésente dans notre vie quotidienne). Négliger ceci
ferait de vous un piêtre programmeur.

#### Coder proprement, comment ?
On l'a vu :
- l'utilisation de fonctions permet de déporter les problèmes et d'éviter de
dupliquer du code.
- l'utilisation de classes permet de bien ranger les variables et par l'héritage, d'améliorer la lisibilité.

Mais il vous faut aussi quelques règles simples pour bien concevoir vos
classes. On pourrait résumer en : **Un objet doit savoir faire TOUT ce qui releve de lui, et rien de plus**. Demandez vous toujours qui doit gérer un problème.

Par exemple : mes balles sont rassemblées dans un tableau (*balles*). Qui gère ce tableau ? Une balle ne doit pas décider d'ajouter une balle au tableau.
Ici, c'est le programme principal qui va s'en charger.

C'est ainsi qu'on se retrouve avec deux fonctions associées au programme
principal :
- *lireImages*
- *ajouterBalles*
car ces actions ne doivent pas être attachée à une classe existante.

Toutes les autres actions sont bien placées dans les objets qui doivent s'en
occuper.

### A faire ce TP ci

Pour ce TP, je vais vous simplement vous donner les consignes et vous allez essayer de créer les classes necessaires ou recycler les classes existantes.

il faudra donc que votre programme :
- ajoute de temps à autres des **Bonus**
- il y aura au minimum 2 sortes de Bonus :
  - un qui ajoute une vie
  - un qui augmente la vitesse du joueur
- Fonctionnement des bonus :
  - ils apparaissent en haut de l'écran
  - ils descendent verticalement
  - il peut y en avoir plusieurs en même temps
  - ils sont détruits quand ils sortent de l'écran.
  - si le joueur touche un bonus, il bénéficie de l'effet du bonus.

Les petits plus possibles :
- le bonus de vitesse n'a qu'une durée d'effet limité sur le joueur.
- inventer d'autres sortes de bonus
- faire des trajectoires plus jolies pour les bonus (l'ellipse descendante serait parfait)
- faire évoluer le score en fonction du temps et du nombre de balles.

### Minimum requis pour la séance suivante

Cette section décrit ce qu'il faut, **au minimum**, pour pouvoir entamer sereinement le TP suivant. Evidemment, si vous êtes allé au bout du TP décrit dans ce document, vous êtes plus loin que cela.

Pour le début du TP4, vous devrez au minimum (pour avoir 10 au TP3) avoir un programme avec :
- des bonus qui ajoutent une vie au joueur s'il les touche
