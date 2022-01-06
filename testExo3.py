import unittest
from poo_python.exos_facile.exo3 import Student

# création d'une classe de test

class TestExo3(unittest.TestCase):
    
    def setUp(self):
        self.student = Student()
        self.tab = [ 2, 3]
        
        
    def tearDown(self):
        del self.student
        
    
    def test_addNote(self):
        # tester que la fonction addNote return bien quelque chose
        # self.assertEqual(self.student.addNote(), 5)
        
        # tester que la fonction addNote return taille
        # self.assertEqual(self.student.addNote(), 2)
        
        # tester que la fonction addNote return nbr ( 1 seule note)
        # self.assertEqual(self.student.addNote(), 2)
        
        # tester que la fonction addNote return le tableau de notes ( toutes les notes )
        # self.assertEqual(self.student.addNote(), self.tab)
        
        # tester la fonction moyenne() ******************
        
        # tester que moyenne return quelque chose
        self.assertEqual(self.student.moyenne(), 5)
        
        
        
        
# pour lancer le script de test
if __name__ == '__main__':
    unittest.main()
