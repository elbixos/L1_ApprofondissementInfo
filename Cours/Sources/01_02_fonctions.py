
def helloWorld(langue):
    if langue == "francais":
        trad = "bonjour"
    else:
        if langue == "anglais":
            trad = "hello"

    print (trad)

def afficherTab(tableau, message):
    # la petite ligne
    for i in range(10) :
        print '-',
    print

    # le message
    print "Affichage de", message


    # la petite ligne
    for i in range(10) :
        print '-',
    print

    print ' | ',
    for i in range(len(tableau)):
        print tableau[i],' | ',
    print 

    calcul = sommeTableau(tableau)


    print ("Somme : ", calcul)




def additionnerBidon(nombre1, nombre2, resu):
    resu = nombre1 + nombre2
    print (resu)

def additionner(nombre1, nombre2):
    resu = nombre1 + nombre2

    return resu

def sommeTableau(tab):
    resu = 0
    for case in tab:
        resu = resu + case
    return resu



tab = [1,3,-5.5, 6, 13, 3]

tab2 = []
tab2.append(-4)

afficherTab(tab, "tableau 1")

afficherTab(tab2, "tableau 2")

r = 0
additionnerBidon(5,2,r)
print ("premier resultat ", r )

toto = additionner(3,14)
print ("second resultat ", toto )

maSomme = sommeTableau(tab)
print(maSomme)

print( sommeTableau(tab2))

helloWorld("anglais")
