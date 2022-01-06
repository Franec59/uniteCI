class Add:
    def __init__(self):
        '''
            creation d'un attribut stockant la somme des nombres
        '''
        self.nbr = 0

    def calc(self, param):
        '''
            addition de nbr et de la nouvelle valeur
        '''
        self.nbr += param

    def message(self):
        '''
            affichage de la somme des nombres
        '''

        print(f"la somme des nombres est égale à {self.nbr}")
