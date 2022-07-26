class Baer:
    alter = 0
    gewicht = 0
    groesse = 0

    def schlafen(self,dauer):
        print("Außerdem schlafe ich " + str(dauer) + " Tage lang ")
    def fressen(self):
        print("fressen")
    def __init__(self, alter, gewicht, groesse):
        print("Ich bin " +str(alter) + " Jahre alt")
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse