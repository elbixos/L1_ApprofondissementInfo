from etudiant import Etudiant

promo = []

etu = Etudiant("Uzumaki","Naruto")
promo.append(etu)

etu = Etudiant("Uchiwa","Sazuke")
promo.append(etu)


for e in promo :
  e.afficher()
