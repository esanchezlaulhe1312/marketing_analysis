def count_outliers(dataframe,columns):
  outliers_count={}
  outliers_percent={}
  for col in columns:
    Q1=dataframe[col].quantile(0.25)
    Q3=dataframe[col].quantile(0.75)
    IQR=Q3-Q1
    lower_bound=Q1-1.5*IQR
    upper_bound=Q3+1.5*IQR
    outliers=dataframe[(dataframe[col]<lower_bound) | (dataframe[col]>upper_bound)]
    outliers_count[col]=outliers.shape[0]
    outliers_percent[col]=round(outliers.shape[0]/dataframe.shape[0],3)
  return outliers_count, outliers_percent

def filter_no_outliers(dataframe,lista_columnas):
  data_filtered=dataframe.copy()
  for col in lista_columnas:
    Q1=dataframe[col].quantile(0.25)
    Q3=dataframe[col].quantile(0.75)
    IQR=Q3-Q1
    lower_bound=Q1-1.5*IQR
    upper_bound=Q3+1.5*IQR
    data_filtered=data_filtered[(data_filtered[col]>=lower_bound)&(data_filtered[col]<=upper_bound)]
  return data_filtered