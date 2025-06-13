import pandas as pd
import folium
from folium import Element
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np

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
        message = f"cluster: {row['cluster']}<br>Fallecidos: {row['Muertos']}<br>Graves: {row['Graves']}<br>Menos Graves: {row['Menos Graves']}<br>Leves: {row['Leves']}<br>Ilesos: {row['Ilesos']}"
        folium.CircleMarker(
            location=[row['Latitud'], row['Longitud']],
            radius=4,
            color=get_color(row['cluster']),
            fill=True,
            fill_opacity=0.6,
            tooltip= message, # hover sobre punto, se mostrará la info.
            popup=message #f"Fallecidos: {row['Muertos']}<br>Graves: {row['Graves']}<br>Menos Graves: {row['Menos Graves']}<br>Leves: {row['Leves']}", # hover sobre punto, se mostrará la info.


        ).add_to(marker_cluster)

    # === Agregar leyenda al mapa ===
    legend_html = """
    <div style="
        position: fixed;
        bottom: 50px;
        left: 50px;
        width: 220px;
        height: auto;
        background-color: white;
        border:2px solid grey;
        z-index:9999;
        font-size:14px;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    ">
    <b>Leyenda de Concentración de Accidentes</b><br>
    <span style="color:orange;">&#9679;</span>mayor<br>
    <span style="color:yellow;">&#9679;</span>media<br>
    <span style="color:green;">&#9679;</span>baja<br>
    </div>
    """
    m.get_root().html.add_child(Element(legend_html))

    # === Agregar control de capas ===
    folium.LayerControl().add_to(m)

    # Mostrar mapa
    m.save(f"./mapas/Map-Basic.html")