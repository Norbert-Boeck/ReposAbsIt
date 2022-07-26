from operator import ge
from ssl import AlertDescription


class Baer:
    #alter = 20
    #gewicht = 680
    #groesse = 250
    def __init__(self, alter, gewicht, groesse):
        self.alter = alter
        self.gewicht = gewicht
        self.groesse = groesse
    def schlafen (self, dauer):
        print ("Schlafe " + str(dauer) + " Minuten")

    def fressen (self):
        print ("fressen")



