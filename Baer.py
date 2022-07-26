import itertools

class Baer:
    #hier entsteht die Klasse Baer
    name = "e"
    nummer = itertools.count()
    alter = 0
    gewicht = 0
    groesse = 0
    def __init__(self, name, alter, gewicht, groesse):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse
        self.IDnummer = next(self.nummer)
    def schlafen(self, dauer):
        print(str(self.name) + " schläft " + str(dauer) + " Minuten.")
    def fressen(self):
        print(str(self.name) + " frisst.")

