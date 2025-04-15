import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def graficar_categoricas(df_limpio):
    """
    Genera una visualización en subplots para todas las variables categóricas de un DataFrame.
    Parámetros:
    df : pandas.DataFrame
        El DataFrame a analizar.
    Salida:
    Muestra un conjunto de gráficos tipo countplot para las columnas categóricas.
    """
    # Detectar columnas categóricas (tipo object o string)
    col_cat = df_limpio.select_dtypes(include="O").columns
    num_cols = len(col_cat)
    if num_cols == 0:
        print("No hay columnas categóricas para graficar.")
        return
    # Calcular número de filas (3 columnas por fila)
    num_filas = (num_cols + 2) // 3
    # Crear subplots
    fig, axes = plt.subplots(num_filas, 3, figsize=(15, num_filas * 4))
    axes = axes.flatten()
    # Graficar cada variable categórica
    for i, col in enumerate(col_cat):
        sns.countplot(data=df_limpio, x=col, ax=axes[i], hue=col, legend=False)
        axes[i].set_title(f"Distribución de {col}")
        axes[i].tick_params(axis='x', rotation=45)
    # Eliminar ejes sobrantes (si los hay)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()