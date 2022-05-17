import sys, unittest, os, mysql
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import INFO_CONNEXION_BDD_TEST

connection = mysql.connector.connect (host='localhost',
                                        database=INFO_CONNEXION_BDD_TEST['database'],
                                        user= INFO_CONNEXION_BDD_TEST["username"],
                                        password=INFO_CONNEXION_BDD_TEST["mdp"])
cursor = connection.cursor()

firt_try = """
drop database %s;
create database %s CHARACTER SET 'utf8';
use %s;

CREATE TABLE historique_download (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nom VARCHAR(1000) NOT NULL,
    date_last_change VARCHAR(50) NOT NULL,
    size varchar(50) NOT NULL,
    parent_directory VARCHAR(1000) NOT NULL,
    sync BOOLEAN,
    PRIMARY KEY (id),
    key (nom(20)),
    Index (date_last_change) ,
    Index (size),
    Index (parent_directory)
)
ENGINE=INNODB;

ALTER TABLE historique_download ADD CONSTRAINT history_parent_directory FOREIGN KEY (parent_directory) REFERENCES historique_download(id);
"""


cursor.execute(request,(taille, date, nom, parent, True))
cursor.close()
connection.commit()
