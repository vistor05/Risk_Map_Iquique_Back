## Importación de librerías
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import pandas as pd
from dataMining.data_preprocessing import data_preprocessing
from dataMining.generate_map import generate_map

#Función principal donde executa el mapa
def execute_script():
    print('ejecutando...')
    # Carga de datos
    url = 'https://github.com/KrisMoshiro/risk-map-iquique-data/raw/refs/heads/main/acc_2010_2023_V4.3.csv'
    df = pd.read_csv(url)
    features = ['Latitud', 'Longitud']
    X = df[features].copy()
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)
    db = DBSCAN(eps=0.00001, min_samples=10)
    df['cluster'] = db.fit_predict(X_scaled)
    n_clusters = len(set(df['cluster'])) - (1 if -1 in df['cluster'].values else 0)
    print(f"Se encontró {n_clusters} clústeres.")
    df_clustered = data_preprocessing(df)
    
    generate_map(df_clustered)


execute_script()