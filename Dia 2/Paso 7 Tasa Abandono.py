import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D')

# ----- PRRGUNTAS SEMILLA -----

# Cuantificación del problema
# ¿Cuál es la tasa de abandono?

# Creamos la variable (tasa_abandono) para el posterior print
tasa_abandono = df.abandono.value_counts(normalize = True) * 100
# -> Conteo de valores de la columna "abandono" normalizado

# Mostramos la tasa de abandono
print(tasa_abandono)

