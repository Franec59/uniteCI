class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        # self.surface()
        # self.message()

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, largeur):
        self._largeur = largeur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, hauteur):
        self._hauteur = hauteur

    def surface(self):
        '''
            calcul de la surface du rectangle
        '''
        if type(self.hauteur) is int and type(self.largeur) is int:
            self.result = self.hauteur * self.largeur
            return self.result
        else :
            raise(Exception("error"))
        
        # self.result = self.hauteur * self.largeur
        # return self.result

    def message(self):
        '''
            affichage de la surface du rectangle
        '''
        print(f"la surface du rectangle est de : {self.result} cm^2")


# rectangle = Rectangle(5, 10)
