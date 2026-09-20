import numpy as np

def calcular_estatisticas(df, coluna):

    moda_val = df[coluna].mode()
    return {
        "Média": df[coluna].mean(),
        "Mediana": df[coluna].median(),
        "Moda": moda_val.iloc[0] if not moda_val.empty else np.nan,
        "Desvio padrão": df[coluna].std(),
    }