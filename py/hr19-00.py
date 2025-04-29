import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import datetime
from datetime import time
import folium
import statistics
from folium.plugins import HeatMap
from datetime import date, time, datetime

url=('https://raw.githubusercontent.com/Chriiistian/ProyectPART/main/CSV/Hr-19-00.csv')
dbhr=pd.read_csv(url)
dbhr

Lat= dbhr['LAT']
Lon = dbhr['LNG']

X = []
for i in range(len(dbhr['LAT'])):
    X.append(Lat[i])
    X.append(Lon[i])

X = np.array(X)

X = X.reshape(-1, 2,)

clusters = 2
KMean = KMeans(n_clusters=clusters)
KMean_g = KMean.fit_predict(X)
KMean.fit(X)

mediaLong = statistics.mean(Lon)
mediaLat = statistics.mean(Lat)


mapa = folium.Map(location=[mediaLat, mediaLong], zoom_start = 13)

tooltip = 'Centro de zona con mas frecuencia de accidentes en la mañana'
tooltip1 = 'Zona con mas frecuencia de accidentes en la mañana'
folium.Circle([KMean.cluster_centers_[0][0], KMean.cluster_centers_[0][1]], tooltip = tooltip1, radius= 750, fill = True,color = "#0078FF" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[1][0], KMean.cluster_centers_[1][1]], tooltip = tooltip1, radius= 750, fill = True,color = "#0078FF" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[0][0], KMean.cluster_centers_[0][1]], tooltip = tooltip1, radius= 600, fill = True,color = "#00FF3E" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[1][0], KMean.cluster_centers_[1][1]], tooltip = tooltip1, radius= 600, fill = True,color = "#00FF3E" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[0][0], KMean.cluster_centers_[0][1]], tooltip = tooltip, radius= 300, fill = True,color = "#FFF700" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[1][0], KMean.cluster_centers_[1][1]], tooltip = tooltip, radius= 300, fill = True,color = "#FFF700" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[0][0], KMean.cluster_centers_[0][1]], tooltip = tooltip, radius= 180, fill = True,color = "#FF9300" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[1][0], KMean.cluster_centers_[1][1]], tooltip = tooltip, radius= 180, fill = True,color = "#FF9300" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[0][0], KMean.cluster_centers_[0][1]], tooltip = tooltip, radius= 100, fill = True,color = "#FF0000" ).add_to(mapa)
folium.Circle([KMean.cluster_centers_[1][0], KMean.cluster_centers_[1][1]], tooltip = tooltip, radius= 100, fill = True,color = "#FF0000" ).add_to(mapa)
mapa.save('mapas/Map9.html')