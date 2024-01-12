def gestion_doublons():
    def remove_duplicate_ips(input_file, output_file):
        # Dictionnaire pour stocker le nombre d'occurrences de chaque IP
        ip_counts = {}

        # Liste pour stocker les lignes uniques
        unique_lines = []

        # Lecture des informations depuis le fichier ip.txt
        with open(input_file, "r") as file:
            for line in file:
                # Séparation des données en une liste
                data = line.strip().split(',')

                # Extraction de l'IP
                ip = data[0]

                # Mise à jour du dictionnaire des occurrences de l'IP
                ip_counts[ip] = ip_counts.get(ip, 0) + 1

                # Ajout de la ligne à la liste des lignes uniques si l'occurrence est de 1
                if ip_counts[ip] == 1:
                    unique_lines.append(line)

        # Écriture des lignes uniques dans le fichier de sortie
        with open(output_file, "w") as output_file:
            output_file.writelines(unique_lines)

    # Utilisation du script pour retirer les IPs dupliquées dans le fichier ip.txt
    remove_duplicate_ips("./log/ip.txt", "./log/ip.txt")
