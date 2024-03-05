# Como vimos en el PASO 2, vamos a eliminar las variables "años en puesto" y "conciliación" porque tienen demasiados nulos

import pandas as pd # Pandas, librería para manipulación de datos
import numpy as np # Numpy, librería para cálculos matemáticos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'

# df = df.drop(columns = ['anos_en_puesto', 'conciliacion']) # La diferencia con la línea de abajo es que la eliminacion es temporal
df.drop(columns = ['anos_en_puesto', 'conciliacion'], inplace = True) # Eliminar columnas con demasiados nulos, inplace = True para que sea permanente

# Para ver si se eliminaron las columnas
print(df.isna().sum().sort_values(ascending=False)) # df.isna() -> DataFrame con valores faltantes, df.isna().sum() -> Suma de valores faltantes por columna, df.isna().sum().sort_values(ascending=False) -> Ordenar de mayor a menor


