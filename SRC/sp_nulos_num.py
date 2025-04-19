import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
def calcular_solo_col_null(dataframe,umbral=10):
  columns_with_nulls=dataframe.columns[dataframe.isnull().any()]
  null_columns_info=pd.DataFrame(
    {"Column":columns_with_nulls,
     "DataType":[dataframe[col].dtype for col in columns_with_nulls],
     "NullCount":[dataframe[col].isnull().sum() for col in columns_with_nulls],
     "Null%":[((dataframe[col].isnull().sum()/dataframe.shape[0])*100) for col in columns_with_nulls]}
  )
  display(null_columns_info)
  low_null_cols=null_columns_info[null_columns_info['Null%']>umbral]['Column'].tolist()
  high_null_cols=null_columns_info[null_columns_info['Null%']<=umbral]['Column'].tolist()
  return high_null_cols,low_null_cols

def imputar_iterative(dataframe,lista_columnas):
  iter_imputer=IterativeImputer(max_iter=50,
                              random_state=42)
  data_imputed=iter_imputer.fit_transform(dataframe[lista_columnas])
  new_col=[col for col in lista_columnas]
  dataframe[new_col]=data_imputed
  display(dataframe[new_col].describe().T)
  return dataframe,new_col