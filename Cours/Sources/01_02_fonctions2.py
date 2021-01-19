def afficher(tableau):
    print("===============")
    for e in tableau :
        print(e) # un commentaire en bout de ligne
        # un commentaire
        # sur une autre ligne
    print("===============")

def calculer_somme(tableau):
    resu = 0
    for e in tableau:
        resu+=e

    return resu

def relou(a,b,c):
    resu = a + b**c
    return resu

tab1 = [1,4,-12,5,9]

tab2 = ["toto","bill","truc"]

afficher(tab1)

afficher(tab2)

somme = calculer_somme(tab1)
print("hors de la fonction", somme)
print(resu)
print (relou(1,2,3))
