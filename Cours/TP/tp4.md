## TP4

Bon, votre jeu commence a ressembler à un vrai jeu,
il est temps d'ajouter ... **des animations** ...

Parce qu'un personnage, quand il bouge, il bouge...

Dans un premier temps, le personnage ne sera pas directionnel.
il sera juste animé dans le temps, indépendamment de sa direction.

Pour trouver des graphismes de qualité, je vous conseille vivement d'aller voir
à vos heures perdues le site suivant
[https://opengameart.org/](https://opengameart.org/).

En particulier, les images que nous allons utiliser ont été créees par :
**Stephen Challener (Redshrike)** for the original sprites.

### Récupération des images.

Nous allons donc animer les balles...
Oubliez les gifs animés. Quand on programme des jeux, on anime des images les
unes après les autres. Et nous allons le faire nous même (pas avec la classe
*Sprites*)

Vous trouverez les différentes images dans le fichier suivant :
[spritesheets/anim.zip](spritesheets/anim.zip)

Dézippez ceci.

### Concept de l'animation :
Nos balles n'auront plus une seule image, mais plusieurs.
Il s'agira, régulièrement, de changer l'image affichée par le jeu.

Les questions à se poser :
- Comment stockeriez vous toutes ces images ?
- Comment se souvenir quelle image doit on afficher à un moment donné ?
- Comment savoir quand on doit changer d'image ?

En programmation orientée objet, il faudra vraisemblablement
dériver la classe **Balle** en une classe **BalleAnimee**
(plus intelligemment, l'**ElementGraphique** serait dérivé en **ElementGraphiqueAnime** et la balle hériterait de ce dernier).
De plus :
- le constructeur d'une balle devra maintenant prendre en compte l'ensemble des images.
- la méthode afficher va gérer le changement d'images.

Et hop, on a des objets animés.
