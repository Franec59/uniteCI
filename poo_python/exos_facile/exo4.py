class Imaginaire:
    def __init__(self):
        '''
            création de deux tableaux à vide regroupant les réels et les imaginaires
        '''
        self._tableau_reel = []
        self._tableau_imaginaire = []

    @property
    def tableau_imaginaire(self):
        return self._tableau_imaginaire

    @tableau_imaginaire.setter
    def tableau_imaginaire(self, param):
        '''
            remplissage du tableau imaginaire
        '''
        self.tableau_imaginaire.append(param)

    @property
    def tableau_reel(self):
        return self._tableau_reel

    @tableau_reel.setter
    def tableau_reel(self, param):
        '''
            remplissage du tableau réel
        '''
        self._tableau_reel.append(param)
 

    def calcul_imaginaire(self):
        '''
            calcul de la somme des imaginaires
        '''
        ima = 0
        for i, val in enumerate(self.tableau_imaginaire):
            ima += val
        return ima

    def calc_reel(self):
        '''
            calcul de la somme des réels
        '''
        re = 0
        for i, val in enumerate(self.tableau_reel):
            re += val
        return re

    def message(self):

        self.calc_reel()
        self.calcul_imaginaire()
        '''
            affichage de la somme des reels et imaginaires
        '''
        print(
            f"les reels sont {self.calc_reel()} et les imaginaires sont {self.calcul_imaginaire()}i ")

    def question(self):
        nbr_round = input("veuillez renseigner le nombre d'imaginaire et d'entier : ")

        nbr = 0
        while nbr < int(nbr_round):
            reel = input("veuillez renseigner un reel : ")
            im = input("veuillez renseigner un imaginaire : ")

            self.tableau_reel = int(reel)
            self.tableau_imaginaire = int(im)
            nbr += 1

        self.message()


imaginaire = Imaginaire().question()