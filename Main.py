from Baer import Baer
from BrownBaer import BrownBear
from Grizzly import Grizzly
from Panda import Panda
from EisBaer import EisBaer

pepo = Grizzly(25, 400, 300)

pepo.graben()
pepo.schlafen(1000)
pepo.fressen()
pepo.pilzeEssen()
print(pepo.alter, " Jahre")
print(pepo.gewicht, " kg")
print(pepo.groesse, " cm")

hippo = BrownBear(12,120,195)
hippo.klettern()
hippo.schlafen(65)
print(hippo.alter, " Jahre")

peter = Panda (20, 300, 150)
peter.rollen()
peter.schlafen(2000)
print(peter.alter, " Jahre")

lars = EisBaer(30, 400, 300)
lars.schwimmen()
lars.schlafen(60)
print(lars.alter, " Jahre")