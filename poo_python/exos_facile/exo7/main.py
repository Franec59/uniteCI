from maison import Maison
from personne import Personne
from porte import Porte


porte = Porte("bleue")
maison = Maison(porte, 45)
personne = Personne("Fabrice", maison)
personne.affichage()


