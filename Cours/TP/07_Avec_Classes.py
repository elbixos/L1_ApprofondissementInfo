import pygame

def lire_images():
    # Lecture des images
    images = {}

    # lecture de l'image du perso
    image = pygame.image.load("perso.png").convert_alpha()
    images["perso"]=image
    image = pygame.image.load("background.jpg").convert()
    images["fond"]=image
    image = pygame.image.load("balle.png").convert_alpha()
    images["balle"]=image

    # Choix de la police pour le texte
    font = pygame.font.Font(None, 34)
    image = font.render('<Escape> pour quitter', True, (255, 255, 255))
    images["texte1"]=image

    return images


class ElementGraphique:
    def __init__(self,image,fenetre,x=0, y=0):
        self.image=image
        self.fenetre = fenetre
        self.rect = image.get_rect()
        self.rect.x=x
        self.rect.y=y


    def afficher(self):
        self.fenetre.blit(self.image, self.rect)


# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

images = lire_images()


perso = ElementGraphique(images["perso"],fenetre,x=60,y=80)

# lecture de l'image du fond
fond = ElementGraphique(images["fond"],fenetre)

balle = ElementGraphique(images["balle"],fenetre,x=400,y=300)

texte1 = ElementGraphique(images["texte1"],fenetre,x=10,y=10)

# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=1;
continuer=True
while continuer == True:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)

    i=i+1
    print (i)

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=False

    # Affichage du fond
    fond.afficher()

    # Affichage Perso
    perso.afficher()

    if touches[pygame.K_LEFT] :
        perso.rect.x-=3
    if touches[pygame.K_RIGHT] :
        perso.rect.x+=3



    balle.afficher()

    balle.rect.x += 3

    # Affichage du Texte
    texte1.afficher()

    # rafraichissement
    pygame.display.flip()

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = False	   # On arrete la boucle

# fin du programme principal...
pygame.quit()
