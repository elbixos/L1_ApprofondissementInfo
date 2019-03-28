import toutBiten

## Initialisation de la fenetre et crÃ©ation
pygame.init()
#creation de la fenetre

largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

# lecture des images, bien rangées dans un dictionnaire
# ===============================
images["fond"] = pygame.image.load("background.jpg").convert()
images["joueur"] = pygame.image.load("perso.png").convert_alpha()
images["balle"] = pygame.image.load("balle.png").convert_alpha()
#       le texte
font = pygame.font.Font(None, 34)
image["text"] = font.render('<Escape> pour quitter', True, (255, 255, 255))



# creation des objets du jeu
# ===============================
# le fond
fond = ElementGraphique(images["fond"],0,0, fen= fenetre)

# le texte
texte = ElementGraphique(images["texte"],10,20, fen= fenetre)

# creation du tableau de balles
# et ajout d'une balle au début du jeu
balles=[]
balles.append(Balle(images["balle"],fen=fenetre))

# le joueur
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

    # on ajoute des balles si c'est le moment.
    ajouterBalles(balles, time,fps)

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
