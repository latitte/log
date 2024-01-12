import re


def get():

    # Spécifiez le nom du fichier d'entrée
    fichier_entree = "./log/controltower_access_reduit.log"

    # Spécifiez le nom du fichier de sortie
    fichier_sortie = "./log/ip.txt"

    # Définissez une expression régulière pour rechercher les adresses IP
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    # Ouvrez le fichier d'entrée en mode lecture
    with open(fichier_entree, 'r') as file_in:
        # Lisez les lignes du fichier d'entrée
        lignes = file_in.readlines()

    # Filtrer les adresses IP au début de chaque ligne
    adresses_ip = [re.search(pattern, ligne).group() for ligne in lignes if re.search(pattern, ligne)]

    # Ouvrez le fichier de sortie en mode écriture
    with open(fichier_sortie, 'w') as file_out:
        # Écrivez les adresses IP dans le fichier de sortie
        file_out.write('\n'.join(adresses_ip))

    print("Les adresses IP ont été extraites avec succès dans", fichier_sortie)
