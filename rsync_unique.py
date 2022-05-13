# TODO Créer un docker et docker-compose pour heberger le tout.

from classes.GetScpConnexion import GetScpConnexion
from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd
from classes.DownloadFile import downloadFiles
from config import INFO_CONNEXION_BDD, INFO_CONNEXION_SCP, DESTINATION_REPERTOIRE


if __name__ == '__main__':
    connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP)
    liste_repertoire_complet  = connexion_scp.get_list_repertoire("/home/archiekramer/Mediacentre/Divers")
    resultat_analyse = ComparationRepertoireBdd(liste_repertoire_complet, INFO_CONNEXION_BDD)
    downloadFiles(resultat_analyse.file_to_sync, DESTINATION_REPERTOIRE,INFO_CONNEXION_SCP, INFO_CONNEXION_BDD)
    connexion_scp.ssh.close()
