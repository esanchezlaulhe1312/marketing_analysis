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
    
def subplot_col_num_hist (dataframe,col):
    num_graph=len(col)
    num_rows= (num_graph +2)//3
    fig,axes=plt.subplots(num_rows,3, figsize=(15, num_rows*5))
    axes = axes.flatten()
    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax=axes[i], bins=200)
        axes[i].text(0.8, 0.9, f'Media:{round(dataframe[col].mean(),4)}', horizontalalignment='center', verticalalignment='center', transform=axes[i].transAxes)
        axes[i].text(0.8, 0.8, f'Mediana:{dataframe[col].median()}', horizontalalignment='center', verticalalignment='center', transform=axes[i].transAxes)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_ylabel('Frecuencia')
        # borrar los dos últimos gráficos que no tienen datos
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()


def subplot_col_num_boxplot (dataframe,col):
    num_graph=len(col)
    num_rows= (num_graph +2)//3
    fig,axes=plt.subplots(num_rows,3, figsize=(15, num_rows*5))
    axes = axes.flatten()
    for i, col in enumerate(col):
        sns.boxplot(data=dataframe, x=col, ax=axes[i])
        axes[i].set_title(f'Boxplot de {col}')
    # borrar los dos últimos gráficos que no tienen datos
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
plt.tight_layout()
plt.show()

def subplot_col_num_2 (dataframe,col):
    num_graph=len(col)
    num_rows= (num_graph +2)//2
    
    fig,axes=plt.subplots(num_graph,2, figsize=(15, num_rows*5), constrained_layout=True)
    
    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax=axes[i,0], bins=200)
        axes[i,0].set_title(f'Distribución de {col}')
        axes[i,0].set_ylabel('Frecuencia')
        
        sns.boxplot(data=dataframe, x=col, ax=axes[i,1])
        axes[i,1].set_title(f'Boxplot de {col}')
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
plt.tight_layout()
plt.show()

def analyze_ctr(dataframe, outliers=False):
  if outliers==True:
   ctr_by_campaign=dataframe.groupby('campaign_type')['CTR'].mean().sort_values(ascending=False)
   ctr_by_channel=dataframe.groupby('channel_used')['CTR'].mean().sort_values(ascending=False)
  else:
   ctr_by_campaign=dataframe.groupby('campaign_type')['CTR'].median().sort_values(ascending=False)
   ctr_by_channel=dataframe.groupby('channel_used')['CTR'].median().sort_values(ascending=False)  
  print('CTR promedio por tipo de campaña:')
  print(ctr_by_campaign, '\n')
  print('CTR promedio por canal utilizado:')
  print(ctr_by_channel, '\n')

  fig, axes=plt.subplots(1,2,figsize=(16,6))

  sns.barplot(x=ctr_by_campaign.index, y=ctr_by_campaign.values,palette='coolwarm',hue=ctr_by_campaign.index,ax=axes[0])
  axes[0].set_title('CTR por tipo de campaña')
  axes[0].set_xticklabels(ctr_by_campaign.index, rotation=45)
  axes[0].tick_params(axis='x',labelsize=10)
  axes[0].tick_params(axis='y',labelsize=10)
  
  sns.barplot(x=ctr_by_channel.index, y=ctr_by_channel.values,palette='viridis',hue=ctr_by_channel.index,ax=axes[1])
  axes[1].set_title('CTR por canal utilizado')
  axes[1].set_xticklabels(ctr_by_channel.index, rotation=45)
  axes[1].tick_params(axis='x',labelsize=10)
  axes[1].tick_params(axis='y',labelsize=10)
  plt.tight_layout()
  
def analyze_conversion(dataframe, outliers=False):
    metrics=['conversion_cost','conversion_value']
    if outliers==True:
     for metric in metrics:
        metric_by_channel=dataframe.groupby('channel_used')[metric].mean().sort_values(ascending=False)
        metric_by_segment=dataframe.groupby('customer_segment')[metric].mean().sort_values(ascending=False)
    else:
        metric_by_channel=dataframe.groupby('channel_used')[metric].median().sort_values(ascending=False)
        metric_by_segment=dataframe.groupby('customer_segment')[metric].median().sort_values(ascending=False)  
    print('conversion rate promedio por canal utilizado')
    print(metric_by_channel, '\n')
    print('conversion rate promedio por segmento de cliente:')
    print(metric_by_segment, '\n')
    
    fig, axes=plt.subplots(1,2,figsize=(16,6))
    sns.barplot(x=metric_by_channel.index, y=metric_by_channel.values,palette='coolwarm',hue=metric_by_channel.index,ax=axes[0])
    axes[0].set_title('conversion rate por canal utilizado')
    axes[0].set_xticklabels(metric_by_channel.index, rotation=45)
    axes[0].tick_params(axis='x',labelsize=10)
    axes[0].tick_params(axis='y',labelsize=10)
    
    sns.barplot(x=metric_by_segment.index, y=metric_by_segment.values,palette='viridis',hue=metric_by_segment.index,ax=axes[1])
    axes[1].set_title('conversion rate por segmento de cliente')
    axes[1].set_xticklabels(metric_by_segment.index, rotation=45)
    axes[1].tick_params(axis='x',labelsize=10)
    axes[1].tick_params(axis='y',labelsize=10)
    plt.tight_layout()