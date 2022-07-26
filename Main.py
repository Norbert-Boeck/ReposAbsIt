from Baer import Baer
from BraunBaer import BraunBaer
from Grizzly import Grizzly
from EisBaer import EisBaer
from Panda import Panda




beppo = Grizzly(25,235,265)
beppo.schlafen(600)
print(beppo.alter, " Jahre")
beppo.graben()
beppo.fisch()
print("----")

hippo = BraunBaer(12,120,30)
hippo.klettern()
hippo.schlafen(65)
print(hippo.alter)
print("----")

balu = Panda(28,150,220)
balu.fressen()
balu.rollen()
balu.schlafen(450)
print("----")

lars = EisBaer(40,280,290)
lars.schwimmen()
lars.fressen()
lars.schlafen(600)
lars.setname("max")
print(lars.getname())
