import pandas as pd
import numpy as np
# Desarrollo de función que integra todos los métodos utilizados para realizar una primera exploración de los datos. Esta función se puede reutilizar. 
# Una vez terminada la función, se han borrado todas las celdas posteriores y que contenían cada uno de los métodos ahora metidos en una sola función ejecutable
# Utilizamos display en vez de print porque queremos que nos devuelva un dataframe
def eda_preliminar (df_cleaning):
  df_cleaning.sample(5)
  print('------------------------')
  print('INFO')
  df_cleaning.info()
  print('------------------------')
  # % de nulos por columna
  print('NULOS')
  round(df_cleaning.isnull().sum()/df_cleaning.shape[0]*100,2)
  print('------------------------')
  # Número de registros duplicados en el dataframe
  print('DUPLICADOS')
  # Aquí podemos utilizar directamente el print porque el output no es un dataframe si no la suma de los registros que hay duplicados en el df
  print(df_cleaning.duplicated().sum())
  print('------------------------')
  print('FRECUENCIA DE TIPOS DE DATOS POR COLUMNAS')
  # select_dtypes(include='O') quiere decir que seleccione los tipos de datos clasificados como 'O' o lo que es lo mismo:"Objects"
  # value_counts() sirve para obtener la frecuencia de las categorías de datos. 
  for col in df_cleaning.select_dtypes(include='O').columns:
    print(df_cleaning[col].value_counts())
    print('********************')
# Función para convertir todos los registros string en minúsculas
def valores_minus (df_cleaning):
  for col in df_cleaning.select_dtypes(include='O').columns:
    df_cleaning[col]=df_cleaning[col].str.lower()

# Función para quita las comas de los campos acquisition cost y total ($)
dolar=['acquisition_cost','total($)']

def dolares (df_cleaning,lista_col):
  for col in lista_col:
    df_cleaning[col] = df_cleaning [col].str.replace('$','').str.replace(',','')
    
def comas (df_cleaning,lista_col):
  for col in lista_col:
  	df_cleaning[col]=df_cleaning[col].str.replace(',','.')

# función para Convertir a float las columnas 
def convertir_columnas (df_cleaning,formato_fecha):
  for col in df_cleaning.columns:
    for dtype in [float,int]:
      try:
        df_cleaning[col] = df_cleaning[col].astype(dtype)
      except:
        pass
    try:
      df_cleaning[col]=pd.to_datetime(df_cleaning[col], format=formato_fecha)
    except:
      pass

def quitar_espacios (df_cleaning):
  for col in df_cleaning.columns:
    try:
      df_cleaning[col] = df_cleaning[col].str.replace(' ','_')
    except:
      pass