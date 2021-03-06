import logging
from classes.InteractionBdd import InteractionBdd
from datetime import datetime
class ComparationRepertoireBdd:
    def __init__(self, liste_fichier_repertoire, repertoire_origine):
        self.liste_fichier_repertoire = liste_fichier_repertoire
        self.repertoire_parent_actuel = repertoire_origine
        self.origin_directory = repertoire_origine
        self.size_position_ligne = 4
        self.date_position_ligne = 5
        self.nom_position_ligne = 7
        self.file_to_sync = {}
        self.interaction_bdd = None

    def main(self,  info_bdd):
        self.init_co(info_bdd)
        logging.info("Demarrage analyse des lignes du repertoire")
        for line in self.liste_fichier_repertoire:
            self.exploit_line(line.decode("utf-8"))
        logging.info("Fin de l'analyse : {} fichiers a synchroniser".format(len(self.file_to_sync)))
        self.close_co()
        return self.file_to_sync

    def init_co(self, info_connexion = None):
        if info_connexion is None: 
            self.interaction_bdd = InteractionBdd()
        else: 
            self.interaction_bdd = InteractionBdd(information_connexion_bdd=info_connexion)

    def close_co(self):
        self.interaction_bdd.deco_bdd()

    def exploit_line(self, ligne):
        nature_ligne = self.analyse_ligne_nature(ligne, base_directory = self.origin_directory)
        if nature_ligne == "FILE" :
            taille, date, nom = self.ligne_fichier_extract(ligne)
            if self.interaction_bdd.verification_entree_bdd(taille, date,nom, self.repertoire_parent_actuel) is False:
                #verifier si pas un fichier temporaire qui s'est ajouté
                if "~{}".format(datetime.strftime(datetime.now(),"%Y")) not in nom:
                    self.file_to_sync[self.repertoire_parent_actuel + nom] = {"parent" : self.repertoire_parent_actuel,
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

    def analyse_ligne_nature(self, ligne, base_directory):
        logging.info("recherche de la nature de la ligne")
        try: 
            if ligne[0] == "-":
                return "FILE"
            elif ligne[0] == "d":
                return "DIRECTORY"
            elif "total" in ligne: 
                return "SIZE"
            elif base_directory in ligne: 
                return "PATH"
        except IndexError: 
            return "EMPTY"
     
    def ligne_repertoire_extract(self, ligne):
        repertoire = ligne.strip()[:-1]
        return repertoire