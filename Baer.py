from xmlrpc.client import GzipDecodedResponse


class Baer:
    alter = 0
    gewicht = 0
    groesse = 0
    #self? nutzlos?
    # def = Metode
    def schlafen(self, dauer):
        print("Schlafe " +str(dauer) + " Minuten")
    def fressen(self):
        print("fressen")
    def __init__(self, alter, gewicht, groesse):
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse

bruno = Baer(20,180,210)
bruno.schlafen(20)
print(bruno.alter, "Jahre")
print(bruno.gewicht, "Kg")
print(bruno.groesse, "cm")

balu = Baer(22,190,230)
print(balu.alter, "Jahre")
print(balu.gewicht, "Kg")
print(balu.groesse, "cm")

