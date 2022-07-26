from Baer import Baer
from BraunBaer import BraunBaer
from EisBaer import EisBaer
from Panda import Panda

bruno = Baer(20,180,210)
bruno.schlafen(25)

print("Der Bär Bruno ist",bruno.alter,"Jahre alt")
print(bruno.gewicht,"kg")
print(bruno.groesse,"cm")

balu = Baer(22,190,230)
bruno.schlafen(30)

print("Der Bär Balu ist",balu.alter,"Jahre alt")
print(balu.gewicht,"kg")
print(balu.groesse,"cm")

lars = EisBaer(100,230,43)
lars.schwimmen()

gisela = Panda(110,20,143)
gisela.rollen()

print("Der Bär Bruno ist",bruno.alter,"Jahre alt")
print(bruno.gewicht,"kg")
print(bruno.groesse,"cm")

balu.alter=33
print(balu.alter)

hiphop = BraunBaer(12,120,195)
hiphop.klettern()
hiphop.schlafen(65)
hiphop.honigessen()