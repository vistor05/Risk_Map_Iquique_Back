import folium
from folium import Element
from folium.plugins import MarkerCluster
import pandas as pd

def create_map_hr(df):


# === Procesar la columna de hora ===
    df['Hora'] = (
        df['Hora']
        .str.replace(r'\s*a\. m\.', 'AM', regex=True)
        .str.replace(r'\s*p\. m\.', 'PM', regex=True)
    )
    df['Hora'] = pd.to_datetime(df['Hora'], format='mixed', errors='coerce').dt.hour

    # === Definir rangos horarios ===
    rango_horas = {
        "00:00-06:00": (0, 6),
        "06:00-12:00": (6, 12),
        "12:00-18:00": (12, 18),
        "18:00-24:00": (18, 24)
    }

    # === Definir colores ===
    colors = [
        'red', 'blue', 'green', 'purple', 'orange', 'darkred',
        'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
        'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
        'gray', 'black', 'lightgray'
    ]

    def get_color(cluster_id):
        if cluster_id == -1:
            return 'gray'  # ruido
        else:
            return colors[cluster_id % len(colors)]

    # === Crear el mapa ===
    lat_center = df['Latitud'].mean()
    lng_center = df['Longitud'].mean()
    m = folium.Map(location=[lat_center, lng_center], zoom_start=12)

    # === Crear capas por rango horario ===
    for label, (inicio, fin) in rango_horas.items():
        df_filtrado = df[(df['Hora'] >= inicio) & (df['Hora'] < fin)].copy()
        if df_filtrado.empty:
            continue

        marker_cluster = MarkerCluster(name=f"{label} hrs").add_to(m)

        for _, row in df_filtrado.iterrows():
            message = (
                f"Hora: {row['Hora']}<br>"
                f"cluster: {row['cluster']}<br>"
                f"Fallecidos: {row['Muertos']}<br>"
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

    # === Leyenda ===
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

    # === Control de capas ===
    folium.LayerControl().add_to(m)

    # Mostrar mapa
    m.save(f"./mapas/Map-Hr.html")