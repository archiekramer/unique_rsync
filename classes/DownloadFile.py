import os
from classes.InteractionBdd import InteractionBdd
from config import BASE_NON_REPRISE


class downloadFiles:
    def __init__(self, liste_file, destination, connexion_scp):
        self.destination = destination
        self.liste_file = liste_file
        self.connexion_scp = connexion_scp
        self.interaction_bdd = InteractionBdd()
        for element in liste_file:
            self.get_file(element)
        self.interaction_bdd.deco_bdd()

    def check_parent(self, file):
        parent = file["parent"].replace(BASE_NON_REPRISE, self.destination)
        if not os.path.isdir(parent):
            os.makedirs(parent)
        return parent

    def get_file(self, file):
        element = self.liste_file[file]
        parent_maj = self.check_parent(element)
        path_file_origine = element["parent"] + "/" + file
        path_file_destination = parent_maj + "/" 
        code_retour = self.connexion_scp.get_file_scp(path_file_origine, path_file_destination)
        if code_retour == 0: 
            self.acquittement_bdd(self.liste_file[file])


    def acquittement_bdd(self, element):
        self.interaction_bdd.insertion_bdd(element["size"], element["date"], element["nom"], element["parent"])

