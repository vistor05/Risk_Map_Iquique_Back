##Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import datetime
from datetime import time
import folium
import statistics
from folium.plugins import HeatMap
##Carga y asignacion del dataset

def execute_scripts():
    url='https://raw.githubusercontent.com/Chriiistian/ProyectPART/Pagina_Web(J)/CSV/Data%20frame%20final.csv'
    dbf=pd.read_csv(url)
    dbf=dbf.drop(['Unnamed: 0'], axis=1)

    ##definicion de variables
    Lat= dbf['LAT']
    Lon = dbf['LNG']
    fc = dbf['Fallecidos']
    gv = dbf['Graves']
    mgv = dbf['Menos_Grav']
    lv= dbf['Leves']
    ct = dbf['Count_acc']
    ##creacion y asignacion del algoritmo
    X = []
    for i in range(len(dbf['LAT'])):
        X.append(Lat[i])
        X.append(Lon[i])

    X = np.array(X)

    X = X.reshape(-1, 2,)

    clusters = 2
    KMean = KMeans(n_clusters=clusters)
    KMean_g = KMean.fit_predict(X)
    KMean.fit(X, sample_weight=ct)

    KMean.cluster_centers_

    ## MAPA 1 Cantidad de Accidentes

    mediaLong = statistics.mean(Lon)
    mediaLat = statistics.mean(Lat)

    mapa = folium.Map(location=[mediaLat, mediaLong], zoom_start = 13)


    tooltip = 'Centro con mas frecuencia de accidentes'  
    tooltip1 = 'Zona con mas frecuencia de accidentes'   
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

    mapa.save("./mapas/Map1.html")

    ##MAPA 2 CAntidad de Fallecidos

    clusters = 2
    KMean = KMeans(n_clusters=clusters)
    KMean_g = KMean.fit_predict(X)
    KMean.fit(X, sample_weight=fc)

    mediaLong = statistics.mean(Lon)
    mediaLat = statistics.mean(Lat)

    mapa = folium.Map(location=[mediaLat, mediaLong], zoom_start = 13)

    tooltip = 'Centro de zona con mas frecuencia de fallecidos'
    tooltip1 = 'Zona con mas frecuencia de fallecidos' 
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

    mapa.save("./mapas/Map2.html")

    ##MAPA 3 CAntidad de Lesionados Grave

    clusters = 2
    KMean = KMeans(n_clusters=clusters)
    KMean_g = KMean.fit_predict(X)
    KMean.fit(X, sample_weight=gv)

    mediaLong = statistics.mean(Lon)
    mediaLat = statistics.mean(Lat)

    mapa = folium.Map(location=[mediaLat, mediaLong], zoom_start = 13)

    tooltip = 'Centro de zona con mas frecuencia de lesionados graves'
    tooltip1 = 'Zona con mas frecuencia de lesionados graves'
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

    mapa.save("./mapas/Map3.html")

    ##MAPA 4 CAntidad de Lesionados Menos Graves

    clusters = 2
    KMean = KMeans(n_clusters=clusters)
    KMean_g = KMean.fit_predict(X)
    KMean.fit(X, sample_weight=mgv)

    mediaLong = statistics.mean(Lon)
    mediaLat = statistics.mean(Lat)

    mapa = folium.Map(location=[mediaLat, mediaLong], zoom_start = 13)

    tooltip = 'Centro de zona con mas frecuencia de lesionados menos graves'
    tooltip1 = 'Zona con mas frecuencia de lesionados menos graves'
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

    mapa.save("./mapas/Map4.html")

    ##MAPA 5 CAntidad de Lesionados Leves

    clusters = 2
    KMean = KMeans(n_clusters=clusters)
    KMean_g = KMean.fit_predict(X)
    KMean.fit(X, sample_weight=lv)

    mediaLong = statistics.mean(Lon)
    mediaLat = statistics.mean(Lat)

    mapa = folium.Map(location=[mediaLat, mediaLong], zoom_start = 13)


    tooltip = 'Centro de zona con mas frecuencia de lesionados leves'
    tooltip1 = 'Zona con mas frecuencia de lesionados leves'
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

    mapa.save("./mapas/Map5.html")