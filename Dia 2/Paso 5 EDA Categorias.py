# ANALISIS EXPLORATORIO DE DATOS (EDA) - PASO 5 "CATEGORIAS"

# ALTERAMOS VALORES SEGUN CONCLUSIONES DE PASO 4

import pandas as pd # Pandas, librería para manipulación de datos
import numpy as np # Numpy, librería para cálculos matemáticos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook (SOLO SE USA EN Jupyter Notebook)

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'


# CONCLUSIONES VSTAS A TRAVES DE LOS GRÁFICOS

# mayor_edad, solo tiene UN valor, por lo que no aporta información --> eliminarla
df.drop(columns = 'mayor_edad', inplace = True) # Eliminar columna "mayor_edad" porque solo tiene un valor

# Imputaciion de valores nulos (reemplazar valores nulos)

# educacion tiene 101 valores nulos, la mayoría de los empleados tienen educación universitaria, por lo que imputaremos "Universitario", osea que reemplazaremos los valores nulos por "Universitario"
df['educacion'] = df['educacion'].fillna('Universitaria') # df['educacion'] -> Serie, df['educacion'].fillna('Universitaria') -> Reemplazar valores nulos por "Universitaria"

# satisfaccion_trabajo tiene 76 valores nulos, la mayoría de los empleados tienen satisfacción "Alta", por lo que imputaremos "Alta", osea que reemplazaremos los valores nulos por "Alta"
df['satisfaccion_trabajo'] = df['satisfaccion_trabajo'].fillna('Alta') # df['satisfaccion_trabajo'] -> Serie, df['satisfaccion_trabajo'].fillna('Alta') -> Reemplazar valores nulos por "Alta"

# implicacion tiene 18 valores nulos, la mayoría de los empleados tienen implicación "Media", por lo que imputaremos "Media", osea que reemplazaremos los valores nulos por "Media"
df['implicacion'] = df['implicacion'].fillna('Media') # df['implicacion'] -> Serie, df['implicacion'].fillna('Media') -> Reemplazar valores nulos por "Media"




