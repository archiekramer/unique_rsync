
from importlib.resources import path
import unittest, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(os.path.join(os.path.dirname(__file__), '..'))


from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd

class TestComparaisonRepertoire(unittest.TestCase):

    def setUp(self) -> None:
        pass


    def test_ligne_repertoire(self):
        pass

    def test_nature_ligne_repertoire(self):
        pass

    def test_nature_ligne_vide(self):
        pass

    def test_nature_ligne_fichier(self):
        pass

    def test_nature_ligne_size(self):
        pass
