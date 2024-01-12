import urllib.request
import json
import time

#################################################################################
#               Extrait la liste des adresses ip à partir d'un fichier log
#               Entrée de la fonction : le fichier log (file)
#               Sortie de la fonction : la liste des adresses ip (listip)
##################################################################################

def ip_loca():
    def gene_listip(file) :
        f = open(file, "r")
        listip=[]
        for ligne in f :
            a=ligne.split("\n")
            listip.append(a[0])
        return listip

    #################################################################################
    #               calcule la latitude et la longitude en fonction de l'ip
    #               Entrée de la fonction : la liste des adresses ip (liste)
    #               Sortie de la fonction : un tableau (tab)
    #                   1er champ   : l'ip
    #                   2ème champs : latitide
    #                   3ème champs : longitude
    ##################################################################################
    def gene_lat_lon(liste) :
        tab=[]
        url = "http://ip-api.com/json/"
        for ip in liste:
            time.sleep(0.01)
            response = urllib.request.urlopen (url + ip)
            data = response.read()
            values = json.loads(data)
            lati=values['lat']
            longi=values['lon']
            #ip = ip[:-2]
            tab.append([ip,lati,longi])
            #print([ip, lati, longi])
        return(tab)

    #################################################################################
    #               Programme principal
    ##################################################################################

    listip=gene_listip("./log/ip.txt")
    tab = gene_lat_lon(listip)
    print(tab)

    # Ouvrez le fichier de sortie en mode écritire
    with open('./log/ip_loca.txt', 'w') as file_out:
        for item in tab:
            line =','.join(map(str, item)).rstrip()+'\n'
            file_out.write(line)
