from Baer import Baer

class Grizzly(Baer):
    def graben(self):
        print("Grizzly gräbt")

beppo = Grizzly(25,235,265)
beppo.schlafen(600)
print(beppo.alter, "Jahre")
beppo.graben()