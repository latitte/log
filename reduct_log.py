# Script permettant de reduire le fichier controltower_access.log


def reduction(reduct):
    # Spécifier le nom du fichier d'entrée
    fichier_entree = "./log/controltower_access.log"

    # Spécifier le nom du fichier de sortie
    fichier_sortie = "./log/controltower_access_reduit.log"

    # Ouvrez le fichier d'entrée en mde lecture
    with open(fichier_entree, 'r') as file_in:
        # Lisez les 10 premières lignes du fichiers d'entrée
        lignes = file_in.readlines()[:reduct]

    # Ouvrez le fichier de sortie en mode écritire
    with open(fichier_sortie, 'w') as file_out:
        # Ecrivez les lignes lues dans le fichier de sortie
        file_out.writelines(lignes)

    print("Les ", reduct, " premières lignes ont été extraites avec succeès dans", fichier_sortie)