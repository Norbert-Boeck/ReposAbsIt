from socketserver import BaseRequestHandler


class Baer:
    alter = 0 
    gewicht = 0
    groesse = 0
    def schlafen(self,dauer):
        print("Schlafe " + str(dauer) + " Minuten")
    def fressen(self):
        print("fressen")
    def __init__(self, alter, gewicht, groesse):
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse
balu = Baer(30,650,200)
bruno = Baer(10,450,500)
balu = bruno

