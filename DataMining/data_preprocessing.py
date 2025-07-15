from datetime import datetime
import pandas as pd


# --- CLASIFICACIÓN DE RANGO HORARIO ---
def clasificar_rango_horario(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M").hour
        if 0 <= hora < 6:
            return 'Madrugada'
        elif 6 <= hora < 12:
            return 'Mañana'
        elif 12 <= hora < 18:
            return 'Tarde'
        else:
            return 'Noche'
    except:
        return None

def moda_por_rango(grupo):
    resultados = {}
    for rango in ['Madrugada', 'Mañana', 'Tarde', 'Noche']:
        horas_rango = grupo[grupo['Rango_Horario'] == rango]['Hora']
        if not horas_rango.empty:
            moda = horas_rango.mode()
            resultados[f'Hora_moda_{rango.lower()}'] = moda.iloc[0] if not moda.empty else None
        else:
            resultados[f'Hora_moda_{rango.lower()}'] = None
    return pd.Series(resultados)


def data_preprocessing(df):
    df['Rango_Horario'] = df['Hora'].apply(clasificar_rango_horario)
    modas_rangos = df.groupby('cluster').apply(moda_por_rango)
    df_resumen = df.groupby('cluster').agg({
    'Muertos': 'sum',
    'Graves': 'sum',
    'Menos Graves': 'sum',
    'Leves': 'sum',
    'Ilesos': 'sum',
    'Latitud': ['mean', 'min', 'max'],
    'Longitud': ['mean', 'min', 'max'],
    }).reset_index()
  
    df_resumen.columns = ['_'.join(col).strip() for col in df_resumen.columns.values]
    df_resumen = df_resumen.rename(columns={'cluster_': 'cluster'})
    conteo_accidentes = df.groupby('cluster').size().reset_index(name='total_accidentes')
    df_resumen = df_resumen.merge(conteo_accidentes, on='cluster', how='left')
    df_resumen = df_resumen.join(modas_rangos)
    df_resumen = df_resumen.fillna("-:-")
    df = df_resumen[df_resumen['cluster'] != -1].copy()
    df_resumen = df.reset_index(drop=True)

    return df_resumen.copy()