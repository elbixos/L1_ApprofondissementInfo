from Personnage import Personnage
from Barbare import Barbare
from Magicien import Magicien

magicMike = Magicien("Mike the Great")

bigBill = Barbare("Bill the Barbarian")

magicMike.afficher()
bigBill.afficher()

magicMike.attaquer(bigBill)

magicMike.afficher()
bigBill.afficher()

bigBill.attaquer(magicMike)
bigBill.attaquer(magicMike)

magicMike.afficher()
bigBill.afficher()
