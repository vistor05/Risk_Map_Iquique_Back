## Importación de librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import folium
import statistics

def crear_mapa(X, pesos, latitudes, longitudes, nombre_archivo, tooltip_centro, tooltip_zona):
    """Función que entrena KMeans y genera el mapa"""
    clusters = 2
    kmeans = KMeans(n_clusters=clusters, random_state=42)
    kmeans.fit(X, sample_weight=pesos)

    media_lat = statistics.mean(latitudes)
    media_lon = statistics.mean(longitudes)

    mapa = folium.Map(location=[media_lat, media_lon], zoom_start=13)

    # Colores y radios para los círculos
    radios_colores = [
        (750, "#0078FF", tooltip_zona),
        (600, "#00FF3E", tooltip_zona),
        (300, "#FFF700", tooltip_centro),
        (180, "#FF9300", tooltip_centro),
        (100, "#FF0000", tooltip_centro),
    ]

    for center in kmeans.cluster_centers_:
        for radio, color, tooltip in radios_colores:
            folium.Circle(
                location=[center[0], center[1]],
                tooltip=tooltip,
                radius=radio,
                fill=True,
                color=color
            ).add_to(mapa)

    mapa.save(f"./mapas/{nombre_archivo}")

def execute_scripts():
    """Función principal"""
    # Carga de datos
    url = 'https://raw.githubusercontent.com/Chriiistian/ProyectPART/Pagina_Web(J)/CSV/Data%20frame%20final.csv'
    dbf = pd.read_csv(url)
    dbf = dbf.drop(columns=['Unnamed: 0'])

    # Variables de interés
    latitudes = dbf['LAT']
    longitudes = dbf['LNG']
    X = np.column_stack((latitudes, longitudes))  # Más eficiente que tu anterior bucle

    # Definición de los mapas a generar
    mapas_info = [
        {
            "pesos": dbf['Count_acc'],
            "nombre": "Map1.html",
            "tooltip_centro": "Centro con más frecuencia de accidentes",
            "tooltip_zona": "Zona con más frecuencia de accidentes"
        },
        {
            "pesos": dbf['Fallecidos'],
            "nombre": "Map2.html",
            "tooltip_centro": "Centro de zona con más frecuencia de fallecidos",
            "tooltip_zona": "Zona con más frecuencia de fallecidos"
        },
        {
            "pesos": dbf['Graves'],
            "nombre": "Map3.html",
            "tooltip_centro": "Centro de zona con más frecuencia de lesionados graves",
            "tooltip_zona": "Zona con más frecuencia de lesionados graves"
        },
        {
            "pesos": dbf['Menos_Grav'],
            "nombre": "Map4.html",
            "tooltip_centro": "Centro de zona con más frecuencia de lesionados menos graves",
            "tooltip_zona": "Zona con más frecuencia de lesionados menos graves"
        },
        {
            "pesos": dbf['Leves'],
            "nombre": "Map5.html",
            "tooltip_centro": "Centro de zona con más frecuencia de lesionados leves",
            "tooltip_zona": "Zona con más frecuencia de lesionados leves"
        },
    ]

    # Generar cada mapa
    for mapa in mapas_info:
        crear_mapa(
            X=X,
            pesos=mapa["pesos"],
            latitudes=latitudes,
            longitudes=longitudes,
            nombre_archivo=mapa["nombre"],
            tooltip_centro=mapa["tooltip_centro"],
            tooltip_zona=mapa["tooltip_zona"]
        )

