from math import *


class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, param):
        self._x = param

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, param):
        self._y = param

    @staticmethod
    def mesure(p1, p2):
        '''
            calcul de la distance entre les deux points via le module math de python
        '''
        calc = sqrt(pow((p2.x - p1.x),2) + pow((p2.y - p1.y),2))

        Point.message(calc)

    @staticmethod
    def message(param):
        '''
            affichage de la distance
        '''
        print(f"la distance entre ces deux points est de {param}")

    @staticmethod
    def question():
        x = input("veuillez renseigner la position x du premier point : ")
        y = input("veuillez renseigner la position y du premier point : ")
        p1 = Point(int(x), int(y))

        x = input("veuillez renseigner la position x du second point : ")
        y = input("veuillez renseigner la position y du second point : ")
        p2 = Point(int(x),int(y))
        Point.mesure(p1, p2)

Point.question()




