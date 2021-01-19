c = 13.5
d= 3


c = c+d
print(c)

print("entrez un truc")
val = "truc bidon"
print("Vous avez entré")
print(val)


print(type(c))
print(type(val))

if c < 15:
    print("Je suis comme kirikou")
    print("petit mais vaillant")
else :
    print("grand, très grand")

print("hors du if")

tab1 = []
print(tab1)
tab1.append(12.5)
tab1.append(-2)
tab1.append(True)
tab1.append("dotBiten")
print(tab1)

tab2 = [1,4,5,12,-5]
print(tab2)

somme = 0
for some_stuff in tab2:
    somme += some_stuff**2

print (somme)

for elt in tab2 :
    if elt < 4.5 :
        print (elt)
        elt = -12

print (tab2)

tab2[0] = -200
print (tab2)

for i in [0,1,2,3]:
    if tab2[i] < 4.5 :
        tab2[i] = -12

print(tab2)

for i in range(4):
    if tab2[i] < 4.5 :
        tab2[i] = -16

print(tab2)
print(len(tab2))

for i in range(len(tab2)):
    if tab2[i] < 4.5 :
        tab2[i] = -16
    print("nouvelle case")

print(tab2)

print("welcome nouvel editeur avec Terminal")
