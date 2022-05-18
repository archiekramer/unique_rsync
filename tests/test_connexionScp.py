import unittest, os
from test_requirement import *
from classes.GetScpConnexion import GetScpConnexion


class TestComparaisonRepertoire(unittest.TestCase):

    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    ## Verification retour fonction nature de ligne ##
    def test_telechargement_fichier_echappe(self):
        connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP)
        remote_path_file = "/home/archiekramer/test"
        remote_path_file = "/home/archiekramer/test 123"
        remote_path_file = "/home/archiekramer/test 123 [123]"
        remote_path_file = "/home/archiekramer/test 123 [12 3]"
        remote_path_file = "/home/archiekramer/Mediacentre/Divers/Angel Arekin - Retour aux sources - Le Porteur de Mort 6  [mp3-64]/01 - Cycle 49 - Chapitre 1.mp3"
        local_path_file = "file.mp3"
        connexion_scp.get_file_scp( remote_path_file, local_path_file)
        self.assertTrue(os.path.isfile(local_path_file))
