from Baer import Baer

class EisBaer(Baer):
    bearname = ""
    def schwimmen(self):
        print("Ich bin EisBaer und ich kann schwimmen")
    def setname(self, name):
        self.bearname = name
    def getname(self):
        return self.bearname