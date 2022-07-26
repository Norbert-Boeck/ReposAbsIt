from Baer import Baer
class BrillenBaer(Baer):
    def schnueffeln(self):
        print("der Brillenbär schnüffelt")
        
#alles folgende gehört in die Main.py
klaus = BrillenBaer(12,120,120)
klaus.schnueffeln()