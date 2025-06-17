import folium
from folium import Element
from folium.plugins import MarkerCluster


def create_map_affectation(df):

    # === Crear el mapa centrado ===
    lat_center = df['Latitud'].mean()
    lng_center = df['Longitud'].mean()
    m = folium.Map(location=[lat_center, lng_center], zoom_start=12)

    # === Colores para clústeres ===
    colors = [
        'red', 'blue', 'green', 'purple', 'orange', 'darkred',
        'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
        'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
        'gray', 'black', 'lightgray'
    ]

    def get_color(cluster_id):
        return 'gray' if cluster_id == -1 else colors[cluster_id % len(colors)]

    # === Tipos de lesiones a filtrar ===
    tipos_lesion = ['Muertos', 'Graves', 'Menos Graves', 'Leves', 'Ilesos']

    # === Crear un grupo por cada tipo de lesión ===
    for tipo in tipos_lesion:
        grupo = folium.FeatureGroup(name=f"{tipo}", show=True).add_to(m)
        marker_cluster = MarkerCluster().add_to(grupo)

        df_filtrado = df[df[tipo] > 0]  # Mostrar solo si hay al menos 1 en esa categoría
#f"Cluster: {row['cluster']}<br>"
        for _, row in df_filtrado.iterrows():
            message = (
                f"Hora: {row['Hora']}:00<br>"
                f"Muertos: {row['Muertos']}<br>"
                f"Graves: {row['Graves']}<br>"
                f"Menos Graves: {row['Menos Graves']}<br>"
                f"Leves: {row['Leves']}<br>"
                f"Ilesos: {row['Ilesos']}"
            )

            folium.CircleMarker(
                location=[row['Latitud'], row['Longitud']],
                radius=4,
                color=get_color(row['cluster']),
                fill=True,
                fill_opacity=0.6,
                tooltip=message,
                popup=message
            ).add_to(marker_cluster)



    # === Control de capas ===
    folium.LayerControl().add_to(m)


    # === Mostrar mapa ===
    m.save(f"./mapas/Map-Affectation.html")
