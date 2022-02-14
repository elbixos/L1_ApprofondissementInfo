
## TP 2.

Normalement, à ce stade, a minima, vous devriez avoir :
- une balle (ElementGraphique) qui rebondit,
- un joueur (ElementGraphique) qui se déplace.
- Vous détectez les contacts entre le joueur et la balle pour arrêter le jeu.

Dans le meilleur des cas, vous avez déja :
- une classe Balle (qui possede une méthode deplacer)
- une classe Perso (qui possede une méthode déplacer)
- votre programme principal génère un tableau de 3 objets de type Balle et les
fait se déplacer, calcule les collisions avec le perso et arrete le jeu.

### Si vous n'etes pas dans le meilleur des cas (ce qui se comprendrait)

#### Question 1 :
Rattrapez votre retard : créez une classe Perso, avec sa méthode déplacer,
qui dépend des touches.

#### Question 2 :
Rattrapez votre retard : créez une classe Balle, avec sa méthode déplacer,
qui permet de rebondir.

#### Question 3 :
Rattrapez votre retard : votre programme principal doit créer un tableau de 3
balles, qui se déplacent toutes seules.

#### Question 4 :
Rattrapez votre retard : votre programme doit tester la collision avec chacune
des balles et arreter le programme en cas de collision.

### Si vous avez fait tout ce qui précède

#### Question 5
Si ce n'est pas déja fait, créez une méthode dans *ElementGraphique* qui dit si un
*ElementGraphique* en touche un autre. Cette méthode aurait la forme suivante :
```python
    def collide(self, other):
        if self.rect.collide_rect(other.rect)
            return True
        return False
```
Par héritage, les objets de type Balle ou Perso pourront utiliser cette méthode.

Utilisez donc cette méthode pour gérer le contact entre les balles et le joueur.
Ca simplifiera beaucoup le code du programme principal.

#### Question 6
Ajoutez de l'aléatoire : modifiez le constructeur d'une Balle pour que sa position
soit tirée au hasard (dans la fenetre). Vous pouvez aussi tirer au sort son
déplacement initial (dans la mesure du raisonnable)

#### Question 7
Debrouillez vous pour que le jeu commence avec une seule balle,
puis crée une nouvelle balle toutes les 3 secondes.

#### Question 8 (difficile)
Ajoutez des vies a votre personnage. Il commence avec 3 vies.
Il en perd une a chaque collision. lorsqu'il n'a plus de vies, le jeu s'arrête.

*Remarque* : lorsque le personnage est touché, il va sans doute falloir
désactiver le test de collisions pour un moment (sinon, il touche la meme balle
30 fois par seconde et perd toutes ses vies d'un coup)

Une belle façon de faire cela est de preparer un attribut invulnerable dans la
classe Perso, ainsi qu'un compteur de temps.
1. Quand le personnage est touché invulnérable passe a True, et le compteur à
zéro.
2. Lorsqu'on déplace le personnage, s'il est invulnerable, on incrémente le
compteur. Si le compteur est supérieur à 30 (soit une seconde), il cesse d'être
invulnerable (invulnerable passe a False)

Pour gérer les collisions :
1. on crée une méthode *appliquer_degats* dans la classe Perso, qui sera appelée
dès qu'une collision balle / perso est détectée.
2. si le perso est n'est pas invulnerable, cette méthode lui retire une vie.
Sinon, elle ne fait rien.

#### Question 9
Commencez a penser a des bonus.
il nous faudrait
- un bonus qui ajoute une vie
- un bonus qui donne une survitesse pendant 5s.



### Minimum requis pour la séance suivante

Cette section décrit ce qu'il faut, **au minimum**, pour pouvoir entamer sereinement le TP suivant. Evidemment, si vous êtes allé au bout du TP décrit dans ce document, vous êtes plus loin que cela.

Pour le début du TP3, vous devrez au minimum (pour avoir 10 au TP1) avoir un programme avec :

- un personnage (Joueur) qui se déplace grace à la méthode *deplacer* de la classe Joueur.
- Un tableau de balles (Balle) qui se déplacent automatiquement et rebondissent grace à la méthode *deplacer* de la classe Balle.
- en cas de collision entre une balle et le personnage, le jeu s'arrête.
- Le jeu commence avec 3 balles.


### Les points en plus.
En gros :

- les questions 5 et 6 vous amenent à 12
- la question 7 vous amene à 14
- la question 8 vous amene à 17
- au dela, vous avez mis des bonus, mais ca fait longtemps que vous ne codez
plus pour la note, mais parce que c'est cool.
