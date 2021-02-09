
## Quatrième cours : dictionnaires et autres choses
Dans ce cours un peu fourre tout, je vais reprendre différentes notions vu avant,
approfondir certains concepts et en voir des nouvelles.

1. Dans ce cours, je vais revenir sur la fin d'implémentation des attaques du mini jeu
vu dans le cours 3. Ses problèmes, sa solution.

2. Une des solutions passe par l'utilisation de variables de classes.

3. les dictionnaires.

### Les dictionnaires Python

Bon, on va reprendre ce qui se dit sur le net :

- Le dictionnaire est aussi un objet conteneur (comme une liste ou un tuple)

- Il ne tient pas en compte la notion d'ordre d'insertion, à la différence des listes.

- Pour accéder aux objets contenus dans le dictionnaire, on n'utilise pas
nécessairement des indices mais des **clefs** qui peuvent être de bien des types distincts.

Dit autrement, un dictionnaire stocke des associations entre une **clef** et une **valeur**

Le plus simple est de faire un exemple. Mettons donc en oeuvre un ... dictionnaire ...
Dans un dictionnaire, on cherche à associer à un mot une définition.
Ce qui permet d'accéder à la définition est le mot.
donc : le mot est la clef, la valeur est la définition.

```python
mondico = []
mondico["arbre"]="souvent un truc vert avec un tronc marron"

mondico["chat"]="sale petite bête sournoise avec des grands yeux"

mondico["guitare"]="le plus bel instrument de musique au monde"

print (mondico)
```


### Le code de début de TP

Avec un minijeu vidéo et ses classes : [07_Avec_Classes.py](../TP/07_Avec_Classes.py)
