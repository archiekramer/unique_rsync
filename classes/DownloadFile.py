import logging
import os
from classes.InteractionBdd import InteractionBdd


class downloadFiles:
    def __init__(self, liste_file, destination, connexion_scp):
        self.destination = destination
        self.liste_file = liste_file
        self.connexion_scp = connexion_scp
    
    def download_files(self, base_directory_origine):
        self.interaction_bdd = InteractionBdd()
        for element in self.liste_file:
            self.get_file(element, base_directory_origine)
        self.interaction_bdd.deco_bdd()

    def check_parent(self, file, base_non_reprise):
        logging.debug("verification presence parent")
        parent = file["parent"].replace(base_non_reprise, self.destination)
        if not os.path.isdir(parent):
            os.makedirs(parent)
            logging.debug("Creation du repertoire {}".format(parent))
        return parent

    def get_file(self, file, base_directory_origin):
        element = self.liste_file[file]
        parent_maj = self.check_parent(element, base_directory_origin)
        path_file_origine = element["parent"] + "/" + file

        path_file_destination = parent_maj + "/" 
        logging.info("Demarrage telechargement de fichier")
        logging.info("origine : {}".format(path_file_origine))
        logging.info("destination : {}".format(path_file_destination))
        code_retour = self.connexion_scp.get_file_scp(path_file_origine, path_file_destination)
        if code_retour == 0: 
            logging.info("telechargement fichier ok, acquittement en BDD")
            self.acquittement_bdd(self.liste_file[file])

    def acquittement_bdd(self, element):
        self.interaction_bdd.insertion_bdd(element["size"], element["date"], element["nom"], element["parent"])

