import numpy as np # Numpy, librería para cálculos matemáticos
import pandas as pd # Pandas, librería para manipulación de datos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'
#print(df) # Mostrar DataFrame COMPLETO

print(df.head()) # Mostrar las primeras 5 filas del DataFrame


