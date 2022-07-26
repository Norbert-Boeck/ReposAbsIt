from Baer import Baer


class EisBaer(Baer):
    bearname = ""
    def schwimmen(self):
        print("der Baer schwimmt")
    def setname(self,name):
        self.bearname = name   
    def getname(self):
        return self.bearname    