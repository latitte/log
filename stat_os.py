import re

def get():

    # Spécifiez le nom du fichier d'entrée
    fichier_entree = "./log/controltower_access_reduit.log"

    # Spécifiez le nom du fichier de sortie
    fichier_sortie = "./log/os.txt"

    # Définissez une expression régulière pour rechercher les systèmes d'exploitation
    os_patterns = {
        'Windows': re.compile(r'Windows', re.IGNORECASE),
        'Linux': re.compile(r'Linux', re.IGNORECASE),
        'Mac OS': re.compile(r'Mac OS|Macintosh', re.IGNORECASE),
        'iOS': re.compile(r'iPhone|iPad|iPod|iOS', re.IGNORECASE),
        'Android': re.compile(r'Android', re.IGNORECASE),
    }

    # Ouvrez le fichier d'entrée en mode lecture
    with open(fichier_entree, 'r') as file_in:
        # Lisez les lignes du fichier d'entrée
        lignes = file_in.readlines()

    # Filtrer les systèmes d'exploitation au début de chaque ligne
    os_detected = [get_os_from_user_agent(ligne, os_patterns) for ligne in lignes]

    # Ouvrez le fichier de sortie en mode écriture
    with open(fichier_sortie, 'w') as file_out:
        # Écrivez les systèmes d'exploitation dans le fichier de sortie
        file_out.write('\n'.join(os_detected))

    print("Les systèmes d'exploitation ont été extraits avec succès dans", fichier_sortie)

def get_os_from_user_agent(user_agent, os_patterns):
    for os, pattern in os_patterns.items():
        if pattern.search(user_agent):
            return os
    return 'Inconnu'

get()
