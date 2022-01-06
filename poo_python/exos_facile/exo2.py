class Somme:
    def __init__(self, nbr1, nbr2):
        self.nbr1 = nbr1
        self.nbr2 = nbr2
        # self.somme()
        # self.message()


    @property
    def nbr1(self):
        return self._nbr1

    @nbr1.setter
    def nbr1(self, nbr):
        self._nbr1 = nbr

    @property
    def nbr2(self):
        return self._nbr2

    @nbr2.setter
    def nbr2(self, nbr2):
        self._nbr2 = nbr2


    def somme(self):
        '''
            calcul de la somme des nombres
        '''
        if type(self.nbr1) is int and type(self.nbr2) is int:
            self.result = self.nbr1 + self.nbr2
            return self.result
        else :
            raise(Exception("error"))
        
        # self.result = self.nbr1 + self.nbr2
        # return self.result

    def message(self):
        '''
            affichage de la somme des nombres
        '''
        print(
            f"la somme de {self.nbr1} et {self.nbr2} est {self.result}")


# somme = Somme(15, 35)

