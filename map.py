# installer la librairie follium (pip install folium)
#appel de la librairie
import folium

def map():
    def create_map():
        # Crée une carte centrée sur une position de départ
        m = folium.Map(location=(43.39342927483907, -1.0394325269186133), zoom_start=5)

        # Lecture des informations depuis le fichier ip_loca.txt
        with open("./log/ip_loca.txt", "r") as file:
            for line in file:
                # Séparation des données en une liste
                data = line.strip().split(',')

                # Extraction des informations
                ip = data[0]
                latitude = float(data[1])
                longitude = float(data[2])

                # Ajout d'un marqueur pour chaque ensemble d'informations
                folium.Marker(
                    location=[latitude, longitude],
                    tooltip=ip,
                    popup=f"IP: {ip}<br>Latitude: {latitude}<br>Longitude: {longitude}",
                    icon=folium.Icon(icon="home"),
                ).add_to(m)

        # Enregistre la carte au format HTML
        m.save("index.html")

    # Appelle la fonction pour créer la carte
    create_map()
