import pandas as pd
import numpy as np
def calcular_nulos (df_limpio):
  numero_nulos=df_limpio.isnull().sum()
  porcentaje_nulos=(df_limpio.isnull().sum()/df_limpio.shape[0])*100
  return numero_nulos, porcentaje_nulos
def analisis_general_categoricas(df_limpio):
  col_cat=df_limpio.select_dtypes(include= "O").columns
  if len(col_cat)==0:
    print("No hay columnas categóricas")
  else:
    for col in col_cat:
      print(f"Esta columna tiene {len(df_limpio[col].unique())} valores únicos")
      print(df_limpio[col].value_counts(normalize=True))
      print("-------------------------")
      print(df_limpio[col].describe())
      print("-------------------------")