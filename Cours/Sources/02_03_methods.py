class Etudiant():
  def __init__(self,nom, prenom):
    self.nom = nom
    self.prenom = prenom
    self.notes = []

  def afficher(self):
    print (self.nom, self.prenom, self.notes)

promo = []

etu = Etudiant("Uzumaki","Naruto")
promo.append(etu)

etu = Etudiant("Uchiwa","Sazuke")
promo.append(etu)


for e in promo :
  e.afficher()
