import folium
from folium.plugins import MarkerCluster
import pandas as pd
from geopy.distance import geodesic
from const.name_maps import mapa_i


def message_tooltip(row):
    return (
    f"""
    <div style="font-family:Arial, sans-serif; font-size:13px; padding:5px; line-height:1.5;">
        <div style="text-align:center; font-weight:bold; font-size:14px;">
            Accidentes Ocurridos<br>
            <span style="font-size:16px; color:#d9534f;">{row['total_accidentes']}</span>
        </div>
        <hr style="border-top:1px solid #999; margin:5px 0;">
        <div style="text-align:center; font-weight:bold;">
            Horario Frecuente
        </div>
        <ul style="padding-left:15px; margin:5px 0;">
            <li><b>Madrugada:</b> {row['Hora_moda_madrugada']}</li>
            <li><b>Mañana:</b> {row['Hora_moda_mañana']}</li>
            <li><b>Tarde:</b> {row['Hora_moda_tarde']}</li>
            <li><b>Noche:</b> {row['Hora_moda_noche']}</li>
        </ul>
        <hr style="border-top:1px solid #999; margin:5px 0;">
        <div style="text-align:center; font-weight:bold;">
            Nivel de Afectación
        </div>
        <ul style="padding-left:15px; margin:5px 0;">
            <li><b>Fallecidos:</b> {row['Muertos_sum']}</li>
            <li><b>Graves:</b> {row['Graves_sum']}</li>
            <li><b>Menos Graves:</b> {row['Menos Graves_sum']}</li>
            <li><b>Leves:</b> {row['Leves_sum']}</li>
            <li><b>Ilesos:</b> {row['Ilesos_sum']}</li>

        </ul>
    </div>
    """
        )

# Función que asigna color según total_accidentes
def color_por_accidentes(total):
    if not isinstance(total, str):
        if total <= 10:
            return 'green'         # menor cantidad
        elif total <= 30:
            return 'yellow'        # moderado
        elif total <= 50:
            return 'orange'        # un poco más moderado
        elif total <= 80:
            return '#ff4d4d'       # rojo claro (usar hex para rojo claro)
        else:
            return '#990000'       # rojo oscuro (muchísima concentración)
    else:
        return '#b8b2b2'



def generate_map(df):
    
    lat_center = df['Latitud_mean'].mean()
    lng_center = df['Longitud_mean'].mean()

    m = folium.Map(location=[lat_center-0.2, lng_center-0.1], zoom_start=12)
    marker_cluster = MarkerCluster().add_to(m)

    # Calcular radios de todos los clusters
    radios = []
    for _, row in df.iterrows():
        punto1 = (row['Latitud_min'], row['Longitud_min'])
        punto2 = (row['Latitud_max'], row['Longitud_max'])
        distancia = geodesic(punto1, punto2).meters
        radios.append(distancia / 2)

    RADIUS_MIN = 20
    RADIUS_MAX = 150

    min_radio = min(radios)
    max_radio = max(radios)
    rango_radio = max_radio - min_radio if max_radio != min_radio else 1

    for i, row in df.iterrows():
        radio_real = radios[i]
        radio_escalado = RADIUS_MIN + ((radio_real - min_radio) / rango_radio) * (RADIUS_MAX - RADIUS_MIN)
        if radio_escalado < RADIUS_MIN:
            radio_escalado = RADIUS_MIN

        color = color_por_accidentes(row['total_accidentes'])

        message = message_tooltip(row)

        #popup = folium.Popup(message, max_width=300)

        folium.Circle(
            location=[row['Latitud_mean'], row['Longitud_mean']],
            radius=radio_escalado,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.4,
            tooltip=message,
            # popup=popup
        ).add_to(marker_cluster)

    m.save(f'./mapas/{mapa_i}')
