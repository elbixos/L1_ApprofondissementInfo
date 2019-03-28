
## TP 3.

Normalement, à ce stade, vous devriez avoir fini le TP 2,
et donc avoir un joueur qui se déplace,
et des balles qui s'ajoutent toutes seules régulièrement.

Prenons quelques instants pour examiner l'intérêt de notre façon de coder...
voici ce a quoi devrait ressembler plus ou moins votre programme principal

```python
import toutBiten

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
continuer = False
time = 0
while continuer == True :
    horloge.tick(fps)
    time+=1

    # Recuperation de l'etat du clavier et des evenements de souris
    touches = pygame.key.get_pressed();
    evenements = pygame.event.get()

    # on ajoute des balles si c'est le moment.
    if time/fps == 5: # ca fait 5s !
      balles.append(Balle(images["balle"],largeur/2, hauteur/2, fen=fenetre))

    # deplacement du joueur
    joueur.deplacer(touches)

    # Detection des collisions joueur / balles :
    for b in balles :
        if joueur.collide(b):
            joueur.toucher()
            if joueur.estMort():
                continuer = False

    # déplacement des balles
    for b in balles:
        b.deplacer()

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
Normalement, vous devriez trouver ce code beaucoup plus lisible
que ce que vous aviez fait au premier semestre.

En fait, le programme principal est maintenant le chef d'orchestre du programme,
et :
1. toutes les difficultés algorithmique sont déportées dans les fonctions/ classes.
2. la logique du programme apparait clairement.

Quel est l'intérêt de tout ceci ?
Aucun si votre objectif est de programmer des choses très simple en un temps
très court. Néanmoins, a terme, vous devrez programmer des choses très complexes.
