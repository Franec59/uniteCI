class Personne:
    def __init__(self, nom, maison):
        self.nom = nom
        self.maison = maison

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, param):
        self._nom = param


    def affichage(self):
        '''
            affichage des données de l'utilisateur + de sa maison via la méthode get_surface + de la porte de sa maison via la méthode get_couleur appartenant à l'objet porte et étant récupéré via la méthode get_porte
        '''
        print(f"{self.nom} possède une maison de {self.maison.surface} m², cette maison a une porte de couleur {self.maison._porte.couleur}")
