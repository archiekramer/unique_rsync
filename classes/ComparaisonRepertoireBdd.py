from classes.InteractionBdd import InteractionBdd


class ComparationRepertoireBdd:
    def __init__(self, liste_fichier_repertoire, origin_directory):
        self.nature_unique_equivalent = {
            "-" : "FILE", 
            "d" : "DIRECTORY"
        }
        self.nature_text_equivalent = {
            origin_directory : "PATH", 
            "total" : "SIZE",
        }
        self.liste_fichier_repertoire = liste_fichier_repertoire
        self.repertoire_parent_actuel = origin_directory
        self.size_position_ligne = 4
        self.date_position_ligne = 5
        self.nom_position_ligne = 7
        self.file_to_sync = {}

    def main(self):
        self.interaction_bdd = InteractionBdd()
        for line in self.liste_fichier_repertoire:
            self.exploit_line(line.decode("utf-8"))
        self.interaction_bdd.deco_bdd()
        return self.file_to_sync

    def exploit_line(self, ligne):
        nature_ligne = self.analyse_ligne_nature(ligne)
        if nature_ligne is "FILE" :
            taille, date, nom = self.ligne_fichier_extract(ligne)
            if self.interaction_bdd.verification_entree_bdd(taille, date,nom, self.repertoire_parent_actuel) is False:
                self.file_to_sync[nom] = {"parent" : self.repertoire_parent_actuel,
                                          "size" : taille,
                                          "date" : date,
                                          "nom": nom}
        elif nature_ligne is "PATH":
            self.repertoire_parent_actuel = self.ligne_repertoire_extract(ligne)

    def ligne_fichier_extract(self, ligne):
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
        return taille, date, nom

    def analyse_ligne_nature(self, ligne):
        for key, value in self.nature_unique_equivalent.items():
            try:
                if ligne[0] == key:
                    return value
            except IndexError: 
                return "EMPTY"
        for key, value in self.nature_text_equivalent.items():
            if key in ligne :
                return value

    def ligne_repertoire_extract(self, ligne):
        repertoire = ligne.strip()[:-1]
        return repertoire