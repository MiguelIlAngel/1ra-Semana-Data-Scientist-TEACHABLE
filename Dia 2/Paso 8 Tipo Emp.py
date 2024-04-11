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

# Analisis por VARIABLES

# EDUCACION
temp = df.groupby('educacion').abandono.mean().sort_values(ascending = False) * 100
# Mostrar gráfico
temp.plot.bar()

# ESTADO CIVIL
temp = df.groupby('estado_civil').abandono.mean().sort_values(ascending = False) * 100
# Mostrar gráfico
temp.plot.bar()

# HORAS EXTRA
temp = df.groupby('horas_extra').abandono.mean().sort_values(ascending = False) * 100
# Mostrar gráfico
temp.plot.bar()

# PUESTO
temp = df.groupby('puesto').abandono.mean().sort_values(ascending = False) * 100
# Mostrar gráfico
temp.plot.bar()

# SALARIO
temp = df.groupby('salario_mes').abandono.mean().sort_values(ascending = False) * 100

# GRÁFICOS ADJUNTOS (PARA VERLOS JUNTOS) PASO 8.1

# CONCLUSIONES
# Los empleados con educación de bajo nivel abandonan más
# Los empleados solteros abandonan más
# Los empleados que hacen más horas extra abandonan más
# Los empleados con puesto en ventas abandonan más
# Los empleados con salario bajo abandonan más
# En general, los empleados con mayor nivel de educación, casados, que hacen más horas extra y con mayor nivel de puesto abandonan más

