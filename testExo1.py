import unittest
from poo_python.exos_facile.exo1 import Rectangle

# création d'une classe de test

class TestExo1(unittest.TestCase):
    
    def setUp(self):
        self.calcul = Rectangle(5, 10)
        self.calcul2 = Rectangle(3, 4)
        self.calcul3 = Rectangle("m", 4)
        
    def tearDown(self):
        del self.calcul
        del self.calcul2
        del self.calcul3
    
    def test_surface(self):
        self.assertEqual(self.calcul.surface(), 50)
        self.assertEqual(self.calcul2.surface(), 12)
        with self.assertRaises(Exception) as context:
            self.calcul3.surface()
        self.assertTrue("error" in str(context.exception))
        
# pour lancer le script de test
# if __name__ == '__main__':
#     unittest.main()
