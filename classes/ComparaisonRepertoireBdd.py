from classes.InteractionBdd import InteractionBdd

BASE_HOME = "/home/archiekramer/"


class ComparationRepertoireBdd:
    def __init__(self, liste_fichier_repertoire, INFO_CO_BDD):
        self.ligne_vide = "VIDE"
        self.ligne_path = "PATH"
        self.ligne_size = "SIZE"
        self.ligne_fichier = "Fichier"
        self.ligne_repertoire = "REPERTOIRE"
        self.repertoire_parent_actuel = str()
        self.size_position_ligne = 4
        self.date_position_ligne = 5
        self.nom_position_ligne = 8
        self.file_to_sync = {}
        self.interaction_bdd = InteractionBdd(username_bdd = INFO_CO_BDD["username"], mdp_bdd = INFO_CO_BDD["mdp"], database = INFO_CO_BDD["database"])
        for line in liste_fichier_repertoire:
            self.exploit_line(line.decode("utf-8").replace("  ", " "))
        self.interaction_bdd.deco_bdd()

    def exploit_line(self, ligne):
        nature_ligne = self.analyse_ligne_nature(ligne)
        if nature_ligne is self.ligne_fichier :
            taille, date, nom = self.ligne_fichier_extract(ligne)
            if self.interaction_bdd.verification_entree_bdd(taille, date,nom, self.repertoire_parent_actuel) is False:
                self.file_to_sync[nom] = {"parent" : self.repertoire_parent_actuel,
                                          "size" : taille,
                                          "date" : date,
                                          "nom": nom}
        elif nature_ligne is self.ligne_path:
            self.repertoire_parent_actuel = self.ligne_repertoire_extract(ligne)

    def ligne_fichier_extract(self, ligne):
        elts = ligne.strip().split(" ")
        taille = elts[self.size_position_ligne]
        date = "{} {} {}".format(elts[self.date_position_ligne],
                                 elts[self.date_position_ligne + 1],
                                 elts[self.date_position_ligne + 2])
        nom = " ".join(elts[self.nom_position_ligne:])
        if nom == "":
            print("pause")
        return taille, date, nom

    def analyse_ligne_nature(self, ligne):
        if ligne == "" :
            return self.ligne_vide
        elif ligne[0] == "d":
            return self.ligne_repertoire
        elif ligne[0] == "-":
            return self.ligne_fichier
        elif BASE_HOME in ligne:
            return self.ligne_path
        elif "total " in ligne:
            return self.ligne_size

    def ligne_repertoire_extract(self, ligne):
        repertoire = ligne.strip()[:-1]
        return repertoire