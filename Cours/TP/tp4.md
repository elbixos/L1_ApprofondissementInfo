## TP4 et autres

Bon, votre jeu commence a ressembler à un vrai jeu,
il est temps d'ajouter ... ce que vous voudrez !

En gros, si vous avez déja un jeu dans lequel vous avez des balles qui
apparaissent, un personnage avec des vies et un bonus de vie, vous auriez deja
la moyenne (disons ~12, en fonction de la qualité du code, et de la jouabilité)

Voici quelques pistes pour améliorer votre note, sachant qu'ici, je ne vais pas
vous donner d'indications de code directement, mais seulement vous expliquer le
principe. Il vous reviendra d'essayer de mettre ceci sous forme de code.

Je vous indique dans le titre une idée du nombre de points supplémentaires
qu'on pourrait obtenir en implémentant cette fonctionnalité. A vous de voir
quel temps vous voulez/pouvez consacrer à cette matière.

**Je vous conseille vivement de sauvegarder différentes versions de votre code
pour toujours être capable de rendre un projet fonctionnel, meme si vous n'avez
pas réussi a faire fonctionner quelque chose !**

### des bonus divers (~2 pts)

Je vous laisse les inventer, sachant par exemple qu'un bonus dont l'effet
est limité dans le temps est plus difficile a mettre en oeuvre qu'un bonus qui
ajoute une vie (ou qu'un malus qui retire une vie)

Ce sera 2 pts, quel que soit le nombre de bonus additionnels, pas 2pts par bonus !

### de la musique et des effets sonores (~1 pts)
c'est facile, mais ca rend bien. Ce n'est pas cher payé, mais votre petit frère
sera fier de vous...

### Une page d'intro / une pause / une page Game Over (2 pts)

Le concept est simple :
- au début du jeu, on a une page qui présente le nom du jeu, eventuellement une
ou plusieurs images. Si le joueur appuie sur <Enter>, le jeu débute.
- pendant le jeu, si le joueur appuie sur <P>, on met le jeu en pause
(avec un affichage qui dit "Pause").
Quand on est en pause, si on appuie sur <U>, le jeu reprend
- Lorsque le joueur a perdu, on affiche un message / une image signalant
"Game Over". Si le joueur appuie sur <Enter>, le programme s'arrête.

Pour faire tout cela, il nous faut simplement une variable **etat** qui signale
dans lequel de ces cas on est. Par exemple, lorsque le programme débute, on sera
dans l'état correspondant à l'intro....

Ensuite, dans notre boucle while, il suffit de regarder quelle est la valeur
de cette variable, et en fonction, de faire les choses qui correspondent à cet
état. Si on est dans l'etat jeu, et que le joueur appuie sur P, on modifie
notre variable d'état pour que lors du prochain tour de boucle, on soit en pause.

Notez que certaines choses doivent être faites quel que soit l'état (le réglage
du tick d'horloge, la récupération des touches enfoncées, la gestion des
evenements QUIT). Elles peuvent donc être faites hors des tests permettant
de traiter chaque état.

### Des Animations (3 voir 5 points)

Parce qu'un personnage, quand il bouge, il bouge...

Dans un premier temps, le personnage ne sera pas directionnel.
il sera juste animé dans le temps, indépendamment de sa direction.

Pour trouver des graphismes de qualité, je vous conseille vivement d'aller voir
à vos heures perdues le site suivant
[https://opengameart.org/](https://opengameart.org/).

En particulier, les images que nous allons utiliser ont été créees par :
**Stephen Challener (Redshrike)** for the original sprites.

#### Récupération des images.

Nous allons donc animer les balles...
Oubliez les gifs animés. Quand on programme des jeux, on anime des images les
unes après les autres. Et nous allons le faire nous même (pas avec la classe
*Sprites*)

Vous trouverez les différentes images dans le fichier suivant :
[spritesheets/anim.zip](spritesheets/anim.zip)

Dézippez ceci.

#### Concept de l'animation :
Nos balles n'auront plus une seule image, mais plusieurs.
Il s'agira, régulièrement, de changer l'image affichée par le jeu.
Si vous voulez faire cela, je conseille très vivement que toutes les images
représentant un objet aient la même taille (ca simplifie beaucoup les choses).

Les questions à se poser :
- Comment stockeriez vous toutes ces images ? -> un tableau
- Comment se souvenir quelle image doit on afficher à un moment donné ? -> un entier
- Comment savoir quand on doit changer d'image ? -> on compte le temps qui passe.

En programmation orientée objet, il faudra vraisemblablement
dériver la classe **Balle** en une classe **BalleAnimee**
(plus intelligemment, l'**ElementGraphique** serait dérivé en **ElementGraphiqueAnime** et la balle hériterait de ce dernier).
De plus :
- le constructeur d'une balle devra maintenant prendre en compte l'ensemble des images.
- la méthode afficher va gérer le changement d'images.

pour un peu plus de détails :
- le constructeur d'ElementGraphiqueAnime va recevoir non pas une image, mais
une liste d'images. Il pourra appeler le constructeur d'ElementGraphique
en lui donnant la premiere image du tableau.
- Une seule de ces images sera l'image courante (celle d'un ElementsGraphique
normal).
- Un ElementGraphiqueAnime aura donc un champ correspondant au numéro d'image
actuellement utilisée. Cette image sera alors placée dans le champ image "normal"
- tous les xxx affichages, on changera le numéro d'image et le champ image "normal"
avant d'afficher comme d'habitude.

Si votre classe ElementGraphiqueAnime est prete, il suffit de :
1. déclarer votre classe Balle comme héritant de la classe ElementGraphiqueAnime.
2. dans votre main, quand on crée une balle, on lui donne le tableau des images
représentant une balle.

Tout le reste est normalement déja pris en compte
Ceci vous permettra d'avoir des balles animées (ca vaudrait dans les 3 points)

#### Des personnages directionnels (3 points supp)

Eventuellement, si vous avez vraiment du temps ou vraiment envie, vous pourriez
avoir un personnage dont les images changent en fonction de sa direction :
il marche (avec une animation), mais de plus la série d'images utilisées dépend
de sa direction (il marche vers la gauche ou vers la droite ou...)

Ici, un personnage n'aura pas seulement une liste d'image pour le représenter,
mais 4 ! une quand il va a gauche, une quand il va a droite...
et il faudra savoir quand on change de direction, pour changer de paquet d'images
a afficher. S'il conserve la meme direction, on changera juste d'image dans l'animation
en cours.

Le plus simple serait :
- de stocker toutes ces listes d'images dans un dictionnaire, dont les clefs sont
les directions ("gauche", "droite"...)
- créer une classe ElementGraphiqueAnimeDirectionel qui herite d'ElementGraphiqueAnime
et dont le constructeur prend ce dictionnaire. La direction par défaut est "droite",
par exemple, et permet d'appeler le constructeur d'ElementGraphiqueAnime.
- un ElementGraphiqueAnimeDirectionel doit connaitre sa direction actuelle, ainsi
que sa précedente direction.
- sa méthode déplacer stocke sa direction et sa direction précédente avant de
faire un déplacement normal
- sa méthode afficher regarde sa direction et sa direction précédente. Si les
deux sont égales, on affiche normalement la suite de l'animation en cours.
Si elles sont différentes, on change la liste d'images utilisées pour qu'elle
corresponde à la nouvelle direction.

Ceci est assez délicat à mettre en oeuvre. Rien d'insurmontable, mais cela peut
prendre du temps.
Et hop, on a des objets animés.
