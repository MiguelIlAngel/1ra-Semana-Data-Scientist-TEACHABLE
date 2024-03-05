import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D')

# ----- PREGUNTAS SEMILLA -----
# ¿Cuál es el tipo de empleado que abandona más?

# Transformar abandonos en 0 y 1
df['abandono'] = df['abandono'].map({'No': 0, 'Yes': 1})
# df['abandono'] -> Serie, df['abandono'].map({'No': 0, 'Yes': 1}) -> Reemplazar "No" por 0 y "Yes" por 1

# Analisis por educacion
temp = df.groupby('educacion').abandono.mean().sort_values(ascending = False) * 100
# Mostrar gráfico
temp.plot.bar()