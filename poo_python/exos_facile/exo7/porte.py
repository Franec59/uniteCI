class Porte:
    def __init__(self, couleur):
        self.couleur = couleur
    
    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, param):
        self._couleur = param


    def affichage(self):
        return "je suis une porte, ma couleur est {self.couleur}"
