import logging
from classes.InteractionBdd import InteractionBdd
from conf_template import ORIGIN_DIRECTORY


class ComparationRepertoireBdd:
    def __init__(self, liste_fichier_repertoire):
        self.liste_fichier_repertoire = liste_fichier_repertoire
        self.repertoire_parent_actuel = ORIGIN_DIRECTORY
        self.size_position_ligne = 4
        self.date_position_ligne = 5
        self.nom_position_ligne = 7
        self.file_to_sync = {}

    def main(self):
        self.interaction_bdd = InteractionBdd()
        logging.info("Demarrage analyse des lignes du repertoire")
        for line in self.liste_fichier_repertoire:
            self.exploit_line(line.decode("utf-8"))
        logging.info("Fin de l'analyse : {} fichiers a synchroniser".format(len(self.file_to_sync)))
        self.interaction_bdd.deco_bdd()
        return self.file_to_sync

    def exploit_line(self, ligne):
        nature_ligne = self.analyse_ligne_nature(ligne)
        if nature_ligne == "FILE" :
            taille, date, nom = self.ligne_fichier_extract(ligne)
            if self.interaction_bdd.verification_entree_bdd(taille, date,nom, self.repertoire_parent_actuel) is False:
                self.file_to_sync[nom] = {"parent" : self.repertoire_parent_actuel,
                                          "size" : taille,
                                          "date" : date,
                                          "nom": nom}
        elif nature_ligne == "PATH":
            self.repertoire_parent_actuel = self.ligne_repertoire_extract(ligne)
            logging.info("repertoire parent actuel : {}".format(self.repertoire_parent_actuel))

    def ligne_fichier_extract(self, ligne):
        logging.info("Extraction information d'une ligne fichier")
        elts = ligne.strip().split(" ")
        #enlever les element avec double espace qui gène l'extraction suivante
        i = 0
        while i < self.nom_position_ligne:
            if elts[i] == "" : 
                del elts[i]
            else: 
                i+=1
        taille = elts[self.size_position_ligne]
        date = "{} {}".format(elts[self.date_position_ligne],
                                 elts[self.date_position_ligne + 1])
        nom = " ".join(elts[self.nom_position_ligne:])
        logging.info("information extraite {} {} {}".format(taille, date, nom))
        return taille, date, nom

    def analyse_ligne_nature(self, ligne):
        logging.info("recherche de la nature de la ligne")
        try: 
            if ligne[0] == "-":
                return "FILE"
            elif ligne[0] == "d":
                return "DIRECTORY"
            elif "total" in ligne: 
                return "SIZE"
            elif ORIGIN_DIRECTORY in ligne: 
                return "PATH"
        except IndexError: 
            return "EMPTY"
    
    def ligne_repertoire_extract(self, ligne):
        repertoire = ligne.strip()[:-1]
        return repertoire