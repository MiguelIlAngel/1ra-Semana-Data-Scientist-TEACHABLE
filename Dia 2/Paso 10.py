import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D')

# ----- PREGUNTAS SEMILLA -----
# Preguntas respecto al impacto del problema

# ¿Cuanto nos ha costado el abandono de empleados este último año?
coste_total =  df.loc[df.abandono == 1].impacto_abandono.sum() # loc = filtrar, 1 = "yes" (los que abandonaron), impacto_abandono = columna con el impacto económico sumados
print(coste_total)
# 2719005.912 euros, es decir, $2.719.005,91 euros es la perdida total por abandono de empleados


# ¿Cuanto nos cuesta que los empleados no estén motivados? (pérdidas en implicación == Baja)
