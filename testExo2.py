import unittest
from poo_python.exos_facile.exo2 import Somme

# création d'une classe de test

class TestExo2(unittest.TestCase):
    
    def setUp(self):
        self.calcul = Somme(2, 2)
        self.calcul2 = Somme(3, 4)
        self.calcul3 = Somme("m", 4)
        self.calcul4 = Somme(3, "d")
        
    def tearDown(self):
        del self.calcul
        del self.calcul2
        del self.calcul3
        del self.calcul4
    
    def test_surface(self):
        self.assertEqual(self.calcul.somme(), 4)
        # tester si la somme est incorrect
        # self.assertEqual(self.calcul2.somme(), 10)
        with self.assertRaises(Exception) as context:
            self.calcul3.somme()
            self.calcul4.somme()
        self.assertTrue("error" in str(context.exception))
        
# pour lancer le script de test
# if __name__ == '__main__':
#     unittest.main()
