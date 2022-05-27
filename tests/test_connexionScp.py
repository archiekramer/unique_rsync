from json.tool import main
import unittest, os, shutil
from test_requirement import INFO_CONNEXION_SCP_TEST
from test_requirement import test_file_destination,test_file_origine
from classes.GetScpConnexion import GetScpConnexion


class TestConnexionSCP(unittest.TestCase):

    def setUp(self) -> None:
        try:
            os.makedirs(test_file_destination)
        except FileExistsError: 
            shutil.rmtree(test_file_destination)
            os.makedirs(test_file_destination)

    def tearDown(self) -> None:
        shutil.rmtree(test_file_destination)

    def test_connexion_scp_ssh(self):
        # Creation connexion SCP de test
        connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP_TEST)

    def test_connexion_scp_list_repertoire(self):
        # Creation connexion SCP de test
        connexion_scp1 = GetScpConnexion(INFO_CONNEXION_SCP_TEST)
        print(test_file_origine)
        print(test_file_destination)
        listing_repertoire = connexion_scp1.get_list_repertoire(test_file_origine)
        self.assertTrue(len(listing_repertoire) > 4)

    def test_telechargement_fichier(self):
        # Creation connexion SCP de test
        connexion_scp2 = GetScpConnexion(INFO_CONNEXION_SCP_TEST)
        listing_repertoire = connexion_scp2.get_list_repertoire(test_file_origine)
        nom_fichier = "/fichier"
        connexion_scp2.get_file_scp(test_file_origine + nom_fichier , test_file_destination)
        emplacement_destination = test_file_destination + nom_fichier
        self.assertTrue(os.path.isfile(emplacement_destination))

    ## Verification retour fonction nature de ligne ##
    def test_telechargement_fichier_echappe(self):
        connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP_TEST)
        nom_fichier = "/Archiekramnom_fichierer - Projet last [mp3-128]/qidsjasqk ['3] (3e copie)/test2#{]@ [-- @ (copie)"
        emplacement_destination = test_file_destination + "/test2#{]@ [-- @ (copie)"
        connexion_scp.get_file_scp(test_file_origine + nom_fichier , test_file_destination)
        self.assertTrue(os.path.isfile(emplacement_destination),"Fichier echappe non telechargable")

if __name__ == "__main__":
    runner = unittest.main()

