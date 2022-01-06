from abc import ABC


class Person(ABC):
    '''
        création d'une classe abstraite, classe qui ne sera pas instanciée 
    '''
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age


    def message(self):
        return "hello"
