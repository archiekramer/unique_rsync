# TODO Créer un docker et docker-compose pour heberger le tout.

from classes.GetScpConnexion import GetScpConnexion
from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd
from classes.DownloadFile import downloadFiles
from config import INFO_CONNEXION_BDD, INFO_CONNEXION_SCP, DESTINATION_REPERTOIRE, ORIGIN_DIRECTORY


if __name__ == '__main__':
    connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP)
    list_result_directory  = connexion_scp.get_list_repertoire(ORIGIN_DIRECTORY)
    resultat_analyse = ComparationRepertoireBdd(list_result_directory, INFO_CONNEXION_BDD, ORIGIN_DIRECTORY).main()
    downloadFiles(resultat_analyse.file_to_sync, DESTINATION_REPERTOIRE,INFO_CONNEXION_SCP, INFO_CONNEXION_BDD)
    connexion_scp.ssh.close()
