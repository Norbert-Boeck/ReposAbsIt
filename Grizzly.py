from Baer import Baer

class Grizzly(Baer):
    def graben(self):
        print("Ich bin ein Grizzlybär und kann toll graben")
    def WSchlaaf(self):
        print("Geht in den Winterschlaaf. ~152 – 213 Tage lang")
beppo = Grizzly(25,235,265)

beppo.schlafen(600)
print(beppo.alter, "Jahre")
beppo.graben()