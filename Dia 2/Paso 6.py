# ANALISIS EXPLORATORIO DE DATOS (EDA) - PASO 6 "NUMERICAS"

import pandas as pd # Pandas, librería para manipulación de datos
import numpy as np # Numpy, librería para cálculos matemáticos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook (SOLO SE USA EN Jupyter Notebook)

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'

# Definimos gráficos para variables numéricas
def estadisticos_cont(num):
    #Calculamos describe
    estadisticos = num.describe().T
    #Añadimos la mediana
    estadisticos['median'] = num.median()
    #Reordenamos para que la mediana esté al lado de la media
    estadisticos = estadisticos.iloc[:,[0,1,8,2,3,4,5,6,7]]
    #Lo devolvemos
    return(estadisticos)

# Llamamos y mostramos a la función para calcular estadísticos de las variables numéricas
print(estadisticos_cont(df.select_dtypes(np.number)))


