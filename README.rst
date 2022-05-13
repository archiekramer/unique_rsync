Repertoire rsync_unique.py
========================
Ce projet permet de synchroniser des repertoires.

Contrairement à la commande rsync il ne synchronise qu'une fois chaque fichier.
Le repertoire destination peut donc être vidé et les fichiers qui y ont été synchronisé
ranger dans d'autres emplacement. Sans que le repertoire d'origine n'est besoin d'être vidé également

Tant que le fichier d'origine n'est pas modifié il n'est pas resynchronissé

La connexion s'effectue via SSH pour le transfert de fichier. Il est donc nécessaire de mettre en place
un couple clé privé / publique entre le serveur d'origine et le destinataire.

Le programme est conçut pour tourner sur le serveur destinataire.

---------------

Clé public clé privée doivent être échangé entre les 2 serveurs.
