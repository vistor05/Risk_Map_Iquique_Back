## Importación de librerías
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import pandas as pd
from data_preprocessing import data_preprocessing
from generate_map import generate_map
#Función principal
def execute_script():
    print('ejecutando...')
    # Carga de datos
    url = 'https://github.com/KrisMoshiro/risk-map-iquique-data/raw/refs/heads/main/acc_2010_2023_V4.3.csv'
    df = pd.read_csv(url)
    features = ['Latitud', 'Longitud']#, 'Muertos', 'Graves', 'Menos Graves', 'Leves','Ilesos']
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



# os.system('cls')
# print('¿Cual desea ejecutar?\n')
# print('1) Básico\n2) Hora\n3) Afectación\n4) Todos')
# option = int(input('Ingrese opcion: '))
# print('ejecutando...')
# if(option == 1):
#     execute_script('basic')    
# elif(option == 2):
#     execute_script('hr')
# elif(option == 3):
#     execute_script('affectation')
# else:
#     execute_script('hr')
#     execute_script('basic')
#     execute_script('affectation')
# print('proceso finalizado')