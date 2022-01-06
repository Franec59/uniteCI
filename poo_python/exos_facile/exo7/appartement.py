from exo7.maison import Maison


class Appartement(Maison):
    def __init__(self, porte):
        '''
            via la composition on définit une porte pour notre appartement
            de plus, nous fixons la surperficie à 50 directement dans le constructeur
        '''
        super().__init__(porte, surface=50)
