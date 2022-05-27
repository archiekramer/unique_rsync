create database {database} CHARACTER SET 'utf8';
use {database};

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