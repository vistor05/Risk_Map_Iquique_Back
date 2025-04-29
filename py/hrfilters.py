import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import folium
import statistics
import os

# Crear la carpeta de salida si no existe
output_folder = './mapas'
os.makedirs(output_folder, exist_ok=True)

# Definición de archivos y nombres de salida
datasets = {
    "Hr-00-06.csv": "mapa_00-06.html",
    "Hr-06-12.csv": "mapa_06-12.html",
    "Hr-12-19.csv": "mapa_12-19.html",
    "Hr-19-00.csv": "mapa_19-00.html",
}

# Colores y radios de los círculos
circle_styles = [
    (750, "#0078FF"),
    (600, "#00FF3E"),
    (300, "#FFF700"),
    (180, "#FF9300"),
    (100, "#FF0000"),
]

# Texto para los tooltips
tooltip_centro = "Centro de zona con más frecuencia de accidentes"
tooltip_zona = "Zona con más frecuencia de accidentes"

# Procesar cada archivo
for csv_file, output_name in datasets.items():
    url = f"https://raw.githubusercontent.com/Chriiistian/ProyectPART/main/CSV/{csv_file}"
    df = pd.read_csv(url)

    # Extraer coordenadas
    coords = df[['LAT', 'LNG']].dropna().values

    # Clustering
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(coords)
    centers = kmeans.cluster_centers_

    # Centro del mapa
    media_lat = statistics.mean(df['LAT'])
    media_lon = statistics.mean(df['LNG'])
    mapa = folium.Map(location=[media_lat, media_lon], zoom_start=13)

    # Dibujar círculos para cada centro
    for center in centers:
        for radius, color in circle_styles:
            folium.Circle(
                location=[center[0], center[1]],
                radius=radius,
                fill=True,
                color=color,
                tooltip=tooltip_centro if radius <= 300 else tooltip_zona
            ).add_to(mapa)

    # Guardar mapa
    mapa.save(f"{output_folder}/{output_name}")
