from porte import Porte


class Maison:
    def __init__(self, porte: Porte, surface):
        '''
            via la composition, on définit une porte pour notre maison
        '''
        self.surface = surface
        self.porte = porte

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, param):
        self._surface = param

    @property
    def porte(self):
        return self._porte
    
    @porte.setter
    def porte(self, porte):
        self._porte = porte

    def affichage(self):
        return (f"la maison fait {self.surface} m²")
