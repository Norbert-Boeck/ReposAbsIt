
from BraunBaer import BraunBaer
from EisBaer import EisBaer
from Grizzly import Grizzly
from Panda import Panda
from EisBaer import EisBaer

beppo = Grizzly(25,235,265)
beppo.schlafen(600)
print(beppo.alter, "Jahre")
beppo.graben()
print("-------")

hippo = BraunBaer(12,120,195)
hippo.klettern()
hippo.schlafen(65)
print(hippo.alter, "Jahre")
print("----")

balu = Panda(28,150,220)
balu.fressen()
balu.rollen()
balu.schlafen(450)
print("-------")

lars = EisBaer(14,280,290)
lars.schwimmen()
lars.fressen()
lars.schlafen(600)
lars.setname("max")
print(lars.getname())
