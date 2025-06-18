import pandas as pd
import folium
from folium import Element
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def create_basic_map(df):
    # Elegimos un punto central del mapa (promedio de coordenadas)
    lat_center = df['Latitud'].mean()
    lng_center = df['Longitud'].mean()

    # Crear el mapa centrado
    m = folium.Map(location=[lat_center, lng_center], zoom_start=12)

    # Crear grupos de marcadores para clústeres
    marker_cluster = MarkerCluster().add_to(m)

    # Asignar colores por clúster
    colors = [
        'red', 'blue', 'green', 'purple', 'orange', 'darkred',
        'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
        'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
        'gray', 'black', 'lightgray'
    ]

    # Función para obtener color por clúster
    def get_color(cluster_id):
        if cluster_id == -1:
            return 'gray'  # ruido
        else:
            return colors[cluster_id % len(colors)]

    #'Fallecidos', 'Graves', 'Menos_Grav', 'Leves'

    # Agregar puntos al mapa
    for _, row in df.iterrows():
        message = f"Fallecidos: {row['Muertos']}<br>Graves: {row['Graves']}<br>Menos Graves: {row['Menos Graves']}<br>Leves: {row['Leves']}<br>Ilesos: {row['Ilesos']}"
        folium.CircleMarker(
            location=[row['Latitud'], row['Longitud']],
            radius=4,
            color=get_color(row['cluster']),
            fill=True,
            fill_opacity=0.6,
            tooltip= message, # hover sobre punto, se mostrará la info.
            popup=message #f"Fallecidos: {row['Muertos']}<br>Graves: {row['Graves']}<br>Menos Graves: {row['Menos Graves']}<br>Leves: {row['Leves']}", # hover sobre punto, se mostrará la info.


        ).add_to(marker_cluster)



        # Mostrar mapa
    m.save(f"./mapas/Map-Basic.html")

    # === Guardar los datos como GeoJSON ===
    # Crear GeoDataFrame con geometría
    gdf = gpd.GeoDataFrame(df.copy(), geometry=gpd.points_from_xy(df.Longitud, df.Latitud))
    gdf.set_crs(epsg=4326, inplace=True)  # Asegurar que esté en WGS84 (lat/lon)
    gdf.to_file("./mapas/Map-Basic.geojson", driver='GeoJSON')