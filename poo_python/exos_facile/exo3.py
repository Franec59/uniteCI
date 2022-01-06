class Student:
    def __init__(self):
        '''
            initialisation d'un tableau vide
        '''
        self._tableau = []

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def note(self):
        pass
    
    @note.setter    
    def note(self, note):
        '''
            remplissage du tableau avec les notes
        '''
        self.tableau = note

    @property
    def tableau(self):
        return self._tableau

    @tableau.setter
    def tableau(self, note):
        self._tableau.append(note)
            
    def moyenne(self):
        '''
            parcours du tableau de note et calcul de la moyenne
        '''
        self.result = 0
        for i, val in enumerate(self.tableau):
            self.result += val

        self.result = self.result / len(self.tableau)
        return self.result
        self.message()
        
        # test *******************
        # return 5
        

    def message(self):
        '''
            affichage de la moyenne
        '''
        print(f"la moyenne des notes est de {self.result}")

    def addNote(self):
        i = 0
        taille = input("nombre de note : ")
        if type(taille) is int:
            while i < int(taille):
                nbr = input("veuillez renseigner un nombre : ")
                self.note = int(nbr)
                i = i + 1
            
            self.moyenne()
        else :
            raise(Exception("error"))
        

        # TEST ************************************************
        # return 5
        # return int(taille)
        # return int(nbr)
    
student = Student().addNote()
