class Etudiant():
  def __init__(self):
    self.nom = ""
    self.prenom = ""
    self.notes = []

etu1 = Etudiant()

etu1.nom = "Uzumaki"
etu1.prenom = "Naruto"
etu1.notes.append(14.5)

etu2 = Etudiant()

etu2.nom = "Uchiwa"
etu2.prenom = "Sazuke"
etu2.notes.append(15)

print (etu2.nom, etu2.notes)

promo = []
etu = Etudiant()

etu.nom = "Uzumaki"
etu.prenom = "Naruto"
etu.notes.append(14.5)
promo.append(etu)

etu = Etudiant()

etu.nom = "Uchiwa"
etu.prenom = "Sazuke"
etu.notes.append(15)
promo.append(etu)


for e in promo :
  print (e.nom, e.prenom, e.notes)
  print(type(e))
