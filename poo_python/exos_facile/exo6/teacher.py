from person import Person


class Teacher(Person):
    def __init__(self, age):
        super().__init__(age)

    def explain(self):
        return " l'explication commence "

    def message(self):
        '''
            récupération du message de la classe parente avc ajout du message de la methode explain
        '''
        return super().message() + self.explain()


teacher = Teacher(40)
print(teacher.message())