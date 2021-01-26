import pygame

# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

imageFond = pygame.image.load("background.jpg")
rectFond = imageFond.get_rect()

# lecture de l'image du perso
imagePerso = pygame.image.load("perso.png").convert_alpha()

# creation d'un rectangle pour positioner l'image du personnage
rectPerso = imagePerso.get_rect()
print(rectPerso)
rectPerso.x = 100
rectPerso.y = 200
print (rectPerso)
print (rectPerso.w , rectPerso.h)

vitesse = 10

imageBalle = pygame.image.load("balle.png").convert_alpha()
rectBalle = imageBalle.get_rect()
rectBalle.x = 360
rectBalle.y = 200

dy = -5
dx = 3

rectBalle2 = imageBalle.get_rect()
rectBalle2.x = 160
rectBalle2.y = 400

dy2 = 5
dx2 = -3

score = 0
font = pygame.font.Font(None, 34)

imageScore = font.render('Score : '+ str(score) , True, (255, 0, 255))
rectScore = imageScore.get_rect()


# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=1;
continuer=1
while continuer:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)

    i=i+1
    score += 1
    imageScore = font.render('Score : '+ str(score) , True, (255, 0, 255))
    print (i)

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0

    rectBalle.x += dx
    rectBalle.y += dy

    if rectBalle.y <= 0 or rectBalle.y + rectBalle.h > hauteur :
        dy = -dy

    if rectBalle.x <= 0 or rectBalle.x + rectBalle.w > largeur :
        dx = -dx

    rectBalle2.x += dx2
    rectBalle2.y += dy2

    if rectBalle2.y <= 0 or rectBalle2.y + rectBalle2.h > hauteur :
        dy2 = -dy2

    if rectBalle2.x <= 0 or rectBalle2.x + rectBalle2.w > largeur :
        dx2 = -dx2


    if touches[pygame.K_RIGHT] :
        rectPerso.x += vitesse

    if touches[pygame.K_LEFT] :
        rectPerso.x += -vitesse

    if touches[pygame.K_DOWN] :
        rectPerso.y += vitesse

    if touches[pygame.K_UP] :
        rectPerso.y += -vitesse

    if rectPerso.x < 0 :
        rectPerso.x = 0

    if rectPerso.x + rectPerso.w > largeur :
        rectPerso.x = largeur - rectPerso.w

    if rectBalle.colliderect(rectPerso) :
        continuer = False


    fenetre.blit(imageFond, rectFond)

    # Affichage Perso
    fenetre.blit(imagePerso, rectPerso)

    fenetre.blit(imageBalle, rectBalle)
    fenetre.blit(imageBalle, rectBalle2)

    fenetre.blit(imageScore, rectScore)

    # rafraichissement
    pygame.display.flip()

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle

# fin du programme principal...
pygame.quit()
