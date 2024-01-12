# Ceci est le fichier qui doit être éxecuter en premier
# Il relie toutes les pages et appelle toutes les fonctions afin de correctement executer le logiciel

# Appel de tous les fichiers du logiciel
import reduct_log
import get_ip
import ip_loca
import map
import gestion_doublons

reduct = 5

# Execution des fonctions
# réduction des logs à 10 lignes
reduct_log.reduction(reduct)

# récupération des ips dans les logs
get_ip.get()

# extraction des ips qui apparaissent plusieurs fois
gestion_doublons.gestion_doublons()

# récupération des coordonées géographique des ips
ip_loca.ip_loca()

# affichage de la map dans l'index.html
map.map()