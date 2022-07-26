from EisBaer import EisBaer
from Panda import Panda
from BraunBaer import BraunBaer
from Grizzly import Grizzly
from BrillenBaer import BrillenBaer





beppo = Grizzly(25,235,265)
beppo.schlafen(600)
print(beppo.alter, "Jahre")
beppo.graben()
print("-----")



hippo = BraunBaer(12,120,195)
hippo.klettern()
hippo.schlafen(65)
print(hippo.alter)


po = Panda(4,200,210)
po.rollen()



lars = EisBaer(15,320,300)
lars.schwimmen()


