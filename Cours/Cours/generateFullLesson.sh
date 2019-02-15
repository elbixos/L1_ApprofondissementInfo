#!/bin/bash

FILE=cours.md
if [ -f $FILE ]; then
    \rm $FILE
fi

# generation des chapitres independants
source generateChapter.sh 1
source generateChapter.sh 2

## generation du fichier complet.
LISTE=$(ls 000_title.md 00_intro.md 0*_[0-9]*.md)
echo "---------------"
echo "Liste des fichiers du cours complet"
echo ""
echo $LISTE
cat $LISTE > cours.md
echo "---------------"
