## Importación de librerías
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import pandas as pd
from basic_map import create_basic_map
from hr_map import create_map_hr
from affectation_map import create_map_affectation
import os


def execute_script(type_map:str):
    """Función principal"""
    # Carga de datos
    url = 'https://github.com/KrisMoshiro/risk-map-iquique-data/raw/refs/heads/main/acc_2010_2023_V2.csv'
    df = pd.read_csv(url)
    features = ['Latitud', 'Longitud', 'Muertos', 'Graves', 'Menos Graves', 'Leves','Ilesos']
    X = df[features].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    db = DBSCAN(eps=0.5, min_samples=10)
    df['cluster'] = db.fit_predict(X_scaled)
    n_clusters = len(set(df['cluster'])) - (1 if -1 in df['cluster'].values else 0)
    # print(f"DBSCAN encontró {n_clusters} clústeres.")
    if(type_map == 'basic'):
        create_basic_map(df)

    if(type_map == 'hr'):
        create_map_hr(df)

    if(type_map == 'affectation'):
        create_map_affectation(df)


os.system('cls')
print('¿Cual desea ejecutar?\n')
print('1) Básico\n2) Hora\n3) Afectación\n4) Todos')
option = int(input('Ingrese opcion: '))
print('ejecutando...')
if(option == 1):
    execute_script('basic')    
elif(option == 2):
    execute_script('hr')
elif(option == 3):
    execute_script('affectation')
else:
    execute_script('hr')
    execute_script('basic')
    execute_script('affectation')
print('proceso finalizado')