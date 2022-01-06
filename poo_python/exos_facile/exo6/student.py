from person import Person


class Student(Person):
    def __init__(self, age):
        super().__init__(age)

    def GoToClasses(self):
        return " je vais en cours "

    def display_age(self):
        return (f" j'ai {self.age} ans ")

    def message(self):
        '''
            récupération du message de la classe parente, on y ajoute les messages de la classe actuelle
        '''
        return super().message() + self.GoToClasses() + self.display_age()


student = Student(15)
print(student.message())